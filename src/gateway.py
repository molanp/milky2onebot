import asyncio
from collections.abc import Coroutine
from contextlib import asynccontextmanager
import logging
import time
from typing import Any, ClassVar

from fastapi import BackgroundTasks, FastAPI, Request, WebSocket
from fastapi.websockets import WebSocketState
import httpx
from starlette.websockets import WebSocketDisconnect
import ujson
import uvicorn
import websockets
from websockets import ClientConnection

from .config import load_config
from .converters import (
    ACTION_MAP,
    failed,
    get_params,
    ok,
    transform_action_response,
    transform_event_async,
)

SETTINGS = load_config()


class ColorFormatter(logging.Formatter):
    COLORS: ClassVar[dict[str, str]] = {
        "DEBUG": "\033[36m",  # 青色
        "INFO": "\033[32m",  # 绿色
        "WARNING": "\033[33m",  # 黄色
        "ERROR": "\033[31m",  # 红色
        "CRITICAL": "\033[41m",  # 红底
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        level_name = record.levelname
        color = self.COLORS.get(level_name, "")
        record.levelname = f"{color}{level_name}{self.RESET}"
        record.msg = f"\033[37m{record.msg}{self.RESET}"
        return super().format(record)


def setup_logging() -> None:
    handler = logging.StreamHandler()
    level = getattr(logging, SETTINGS.logging.level.upper(), logging.INFO)
    handler.setLevel(level)
    formatter_cls = ColorFormatter if SETTINGS.logging.color else logging.Formatter
    handler.setFormatter(formatter_cls("%(asctime)s [%(levelname)s] %(message)s"))
    logging.basicConfig(level=level, handlers=[handler], force=True)


setup_logging()


class UnifiedWebSocket:
    def __init__(self, raw_ws: ClientConnection | WebSocket):
        self.raw_ws = raw_ws

    async def send(self, text: str):
        if isinstance(self.raw_ws, ClientConnection):
            await self.raw_ws.send(text)
        elif self.raw_ws.client_state == WebSocketState.CONNECTED:
            await self.raw_ws.send_text(text)

    async def send_json(self, json: dict[str, Any]):
        await self.send(ujson.dumps(json))


class GatewayHub:
    HTTP_CLIENT = httpx.AsyncClient(timeout=SETTINGS.performance.http_timeout)
    onebot_client_ws: UnifiedWebSocket | None = None
    onebot_server_wss: ClassVar[set[UnifiedWebSocket]] = set()
    pending_tasks: ClassVar[set[asyncio.Task[Any]]] = set()
    milky_ready: asyncio.Event | None = None
    self_id: int | None = None

    @classmethod
    def create_task(cls, coro: Coroutine[Any, Any, Any]) -> asyncio.Task[Any]:
        task = asyncio.create_task(coro)
        cls.pending_tasks.add(task)
        task.add_done_callback(cls._drop_task)
        return task

    @classmethod
    def _drop_task(cls, task: asyncio.Task[Any]) -> None:
        cls.pending_tasks.discard(task)
        if task.cancelled():
            return
        try:
            task.result()
        except Exception as e:
            logging.exception(f"后台任务异常: {e}")

    @classmethod
    def milky_auth_headers(cls) -> dict[str, str]:
        token = SETTINGS.milky.access_token
        return {"Authorization": f"Bearer {token}"} if token else {}

    @classmethod
    def onebot_header(cls) -> dict[str, str]:
        headers = {}
        token = SETTINGS.onebot.access_token
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if cls.self_id is not None:
            headers["X-Self-ID"] = str(cls.self_id)
        return headers

    @classmethod
    async def call_milky_api(
        cls, action: str, payload: dict[str, Any]
    ) -> dict[str, Any]:
        response = await cls.HTTP_CLIENT.post(
            f"{SETTINGS.milky.api_base_url}/{action}",
            json=payload,
            headers=cls.milky_auth_headers(),
        )
        response.raise_for_status()
        return response.json()

    @classmethod
    async def refresh_self_id(cls) -> int | None:
        try:
            response = await cls.call_milky_api("get_login_info", {})
        except Exception as e:
            logging.warning(f"获取 Milky 登录信息失败，暂无法设置 X-Self-ID: {e}")
            return cls.self_id
        if response.get("status") == "ok" and response.get("retcode") == 0:
            cls.self_id = int(response["data"]["uin"])
            logging.info(f"已获取 X-Self-ID: {cls.self_id}")
        else:
            logging.warning(f"获取 Milky 登录信息失败: {response}")
        return cls.self_id

    @classmethod
    async def resolve_file_url(
        cls, scene: str, peer_id: int, file_data: dict[str, Any]
    ):
        try:
            if scene == "group":
                response = await cls.call_milky_api(
                    "get_group_file_download_url",
                    {"group_id": peer_id, "file_id": file_data["file_id"]},
                )
            elif file_data.get("file_hash"):
                response = await cls.call_milky_api(
                    "get_private_file_download_url",
                    {
                        "user_id": peer_id,
                        "file_id": file_data["file_id"],
                        "file_hash": file_data["file_hash"],
                    },
                )
            else:
                return None
            if response.get("status") == "ok" and response.get("retcode") == 0:
                return response.get("data", {}).get("download_url")
            logging.warning(f"获取文件下载链接失败: {response}")
        except Exception as e:
            logging.warning(f"获取文件下载链接异常: {e}")
        return None

    @classmethod
    def build_onebot_heartbeat(cls) -> dict[str, Any]:
        return {
            "time": int(time.time()),
            "self_id": cls.self_id or 0,
            "post_type": "meta_event",
            "meta_event_type": "heartbeat",
            "status": {
                "online": cls.milky_ready.is_set() if cls.milky_ready else True,
                "good": cls.milky_ready.is_set() if cls.milky_ready else True,
            },
            "interval": int(SETTINGS.heartbeat.onebot_interval * 1000),
        }

    @classmethod
    async def send_to_onebot(cls, message: dict[str, Any]) -> None:
        ob_type = SETTINGS.onebot.mode
        if ob_type == "WS_CLIENT" and cls.onebot_client_ws:
            await cls.onebot_client_ws.send_json(message)
        elif ob_type == "WS_SERVER" and cls.onebot_server_wss:
            if tasks := [ws.send_json(message) for ws in cls.onebot_server_wss]:
                await asyncio.gather(*tasks, return_exceptions=True)

    @classmethod
    async def dispatch_to_onebot(cls, raw_message: dict[str, Any] | str):
        if isinstance(raw_message, str):
            try:
                message = ujson.loads(raw_message)
            except Exception as e:
                return failed(str(e), retcode=-500)
        else:
            message = raw_message

        try:
            converted = await transform_event_async(
                message, file_url_resolver=cls.resolve_file_url
            )
        except Exception as e:
            logging.exception(f"Milky 事件转换失败: {e}")
            return failed(str(e), retcode=-500)

        if converted is None:
            logging.warning(f"未知的的 Milky 事件: {message.get('event_type')}")
            return None

        message = converted

        await cls.send_to_onebot(message)

    @classmethod
    async def handle_onebot_event_flow(
        cls, onebot_message: dict, reply_channel: UnifiedWebSocket
    ) -> None:
        echo = onebot_message.get("echo")
        try:
            route_result = cls.transform_onebot_router(onebot_message)
            if not isinstance(route_result, tuple):
                await reply_channel.send_json(route_result)
                return
            milky_router, milky_params, mapping, source_params = route_result
            if mapping.local_response is not None:
                await reply_channel.send_json(
                    ok(mapping.local_response(source_params), echo=echo)
                )
                return
            try:
                milky_response = await cls.call_milky_api(milky_router, milky_params)
            except Exception:
                await reply_channel.send_json(
                    failed(
                        "Milky API request failed",
                        retcode=-502,
                        echo=echo,
                    )
                )
                return
            onebot_response = transform_action_response(
                milky_response, mapping, source_params, echo=echo
            )
            await reply_channel.send_json(onebot_response)
        except Exception as e:
            logging.exception(f"中转 OneBot API 调用失败: {e}")
            await reply_channel.send_json(failed(str(e), retcode=-500, echo=echo))
            return

    @classmethod
    def transform_onebot_router(cls, onebot_message: dict):
        if not (action := onebot_message.get("action")):
            return failed(
                "No action specified", retcode=-400, echo=onebot_message.get("echo")
            )
        mapping = ACTION_MAP.get(action)
        if mapping is None:
            return failed(
                f"Router not found: {action}",
                retcode=-404,
                echo=onebot_message.get("echo"),
            )
        try:
            source_params = get_params(onebot_message)
            milky_params = mapping.params(source_params)
            return (
                mapping.resolve_action(source_params),
                milky_params,
                mapping,
                source_params,
            )
        except Exception as e:
            return failed(str(e), retcode=-400, echo=onebot_message.get("echo"))


async def milky_ws_client_loop():
    ws_url = SETTINGS.milky.ws_event_url
    while True:
        try:
            logging.info(f"[Milky Ws_Client] Trying to connect {ws_url}..")
            async with websockets.connect(
                ws_url,
                ping_interval=20,
                additional_headers=GatewayHub.milky_auth_headers(),
            ) as ws:
                logging.info("[Milky Ws_Client] Connected to Milky Websocket Server..")
                if GatewayHub.milky_ready is not None:
                    GatewayHub.milky_ready.set()
                await GatewayHub.refresh_self_id()
                async for message in ws:
                    msg_str = (
                        message if isinstance(message, str) else message.decode("utf-8")
                    )
                    await GatewayHub.dispatch_to_onebot(msg_str)
        except Exception as e:
            if GatewayHub.milky_ready is not None:
                GatewayHub.milky_ready.clear()
            logging.warning(f"[Milky Ws_Client] Milky Websocket 断开, 5秒后重连: {e}")
            await asyncio.sleep(SETTINGS.milky.reconnect_interval)


async def onebot_ws_client_loop():
    ws_url = SETTINGS.onebot.ws_url
    while True:
        if GatewayHub.milky_ready is not None:
            await GatewayHub.milky_ready.wait()
        try:
            logging.info(f"[Onebot Ws_Client] Trying to connect {ws_url}..")
            async with websockets.connect(
                ws_url,
                ping_interval=20,
                additional_headers=GatewayHub.onebot_header(),
            ) as ws:
                GatewayHub.onebot_client_ws = UnifiedWebSocket(ws)
                logging.info(
                    "[Onebot Ws_Client] Connected to Onebot Websocket Server.."
                )
                async for message in ws:
                    msg = ujson.loads(
                        message if isinstance(message, str) else message.decode("utf-8")
                    )
                    GatewayHub.create_task(
                        GatewayHub.handle_onebot_event_flow(
                            msg, reply_channel=GatewayHub.onebot_client_ws
                        )
                    )
        except Exception as e:
            GatewayHub.onebot_client_ws = None
            logging.warning(f"[Onebot Ws_Client] Onebot Websocket 断开, 5秒后重连: {e}")
            await asyncio.sleep(SETTINGS.onebot.reconnect_interval)


async def onebot_heartbeat_loop():
    while True:
        try:
            await asyncio.sleep(SETTINGS.heartbeat.onebot_interval)
            if GatewayHub.milky_ready is not None:
                await GatewayHub.milky_ready.wait()
            await GatewayHub.send_to_onebot(GatewayHub.build_onebot_heartbeat())
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logging.warning(f"[Onebot Heartbeat] 心跳发送失败: {e}")


async def milky_heartbeat_loop():
    while True:
        try:
            await asyncio.sleep(SETTINGS.heartbeat.milky_interval)
            if GatewayHub.milky_ready is not None:
                await GatewayHub.milky_ready.wait()
            logging.debug("[Milky Heartbeat] ?!谁让你启动 Milky 心跳的!?")
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logging.warning(f"[Milky Heartbeat] 心跳发送失败: {e}")


async def milky_sse_loop():
    """从 Milky SSE 读取事件并转发给 OneBot"""
    sse_url = SETTINGS.milky.sse_event_url
    while True:
        try:
            logging.info(f"[Milky SSE] 正在连接 Milky SSE {sse_url}...")
            async with GatewayHub.HTTP_CLIENT.stream(
                "GET", sse_url, headers=GatewayHub.milky_auth_headers()
            ) as response:
                logging.info("[Milky SSE] 连接 SSE 成功..")
                if GatewayHub.milky_ready is not None:
                    GatewayHub.milky_ready.set()
                await GatewayHub.refresh_self_id()

                event_name: str | None = None
                data_lines: list[str] = []

                async for raw_line in response.aiter_lines():
                    if raw_line is None:
                        continue

                    line = raw_line.rstrip("\n")

                    if line == "":
                        if data_lines:
                            data_str = "\n".join(data_lines)
                            logging.info(f"[Milky SSE] Received event: {event_name}")
                            await GatewayHub.dispatch_to_onebot(data_str)
                        event_name = None
                        data_lines = []
                        continue
                    if line.startswith("event:"):
                        event_name = line[len("event:") :].strip()
                        continue
                    if line.startswith("data:"):
                        data_line = line[len("data:") :].lstrip()
                        data_lines.append(data_line)
                        continue

        except Exception as e:
            if GatewayHub.milky_ready is not None:
                GatewayHub.milky_ready.clear()
            logging.error(f"[Milky SSE] SSE 流中断, 5秒后重连: {e}")
            await asyncio.sleep(SETTINGS.milky.reconnect_interval)


async def endpoint_milky_webhook(request: Request, background_tasks: BackgroundTasks):
    body = await request.body()
    background_tasks.add_task(GatewayHub.dispatch_to_onebot, body.decode("utf-8"))
    return {"status": "accepted"}


async def endpoint_onebot_reverse_ws(websocket: WebSocket):
    await websocket.accept()
    adapted_ws = UnifiedWebSocket(websocket)
    GatewayHub.onebot_server_wss.add(adapted_ws)
    try:
        while True:
            message = await websocket.receive_json()
            GatewayHub.create_task(
                GatewayHub.handle_onebot_event_flow(message, reply_channel=adapted_ws)
            )
    except WebSocketDisconnect:
        pass
    finally:
        GatewayHub.onebot_server_wss.remove(adapted_ws)


@asynccontextmanager
async def lifespan(app: FastAPI):
    bg_tasks = []
    GatewayHub.milky_ready = asyncio.Event()

    if SETTINGS.milky.mode == "WEBSOCKET":
        bg_tasks.append(asyncio.create_task(milky_ws_client_loop()))
    elif SETTINGS.milky.mode == "SSE":
        bg_tasks.append(asyncio.create_task(milky_sse_loop()))
    else:
        GatewayHub.milky_ready.set()

    if SETTINGS.onebot.mode == "WS_CLIENT":
        bg_tasks.append(asyncio.create_task(onebot_ws_client_loop()))
    if SETTINGS.heartbeat.onebot_enabled:
        bg_tasks.append(asyncio.create_task(onebot_heartbeat_loop()))
    if SETTINGS.heartbeat.milky_enabled:
        bg_tasks.append(asyncio.create_task(milky_heartbeat_loop()))

    logging.info("Started..")
    yield
    for task in bg_tasks:
        task.cancel()
    await GatewayHub.HTTP_CLIENT.aclose()


app = FastAPI(
    lifespan=lifespan,
    title="Milky强兼器",
    host=SETTINGS.server.host,
    port=SETTINGS.server.port,
)

if SETTINGS.milky.mode == "WEBHOOK":
    logging.info(
        f"[Milky Webhook] 服务地址 http://{SETTINGS.server.host}:{SETTINGS.server.port}/milky/webhook"
    )
    app.add_api_route("/milky/webhook", endpoint_milky_webhook, methods=["POST"])

if SETTINGS.onebot.mode == "WS_SERVER":
    logging.info(
        f"[Onebot Ws_Client] 服务地址 http://{SETTINGS.server.host}:{SETTINGS.server.port}/onebot/v11/ws"
    )
    app.add_api_websocket_route("/onebot/v11/ws", endpoint_onebot_reverse_ws)


@app.get("/health")
async def health():
    return {"status": "running"}


if __name__ == "__main__":
    uvicorn.run(app, host=SETTINGS.server.host, port=SETTINGS.server.port)
