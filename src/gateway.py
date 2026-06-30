import asyncio
import logging
import time
from contextlib import asynccontextmanager
from typing import Any
import httpx
import websockets
from fastapi import FastAPI, Request, BackgroundTasks, WebSocket
from fastapi.websockets import WebSocketState
from starlette.websockets import WebSocketDisconnect
from websockets import ClientConnection
import uvicorn
import ujson
from converters import (
    ACTION_MAP,
    failed,
    get_params,
    ok,
    transform_action_response,
    transform_event_async,
)


class ColorFormatter(logging.Formatter):
    COLORS = {
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


handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(ColorFormatter("%(asctime)s [%(levelname)s] %(message)s"))

logging.basicConfig(level=logging.INFO, handlers=[handler])


CONFIG = {
    "HOST": "127.0.0.1",
    "PORT": 8000,
    # Milky 支持: "WEBSOCKET", "SSE", "WEBHOOK"
    "MILKY_TYPE": "WEBSOCKET",
    "MILKY_HOST": "127.0.0.1",
    "MILKY_PORT": 3000,
    "MILKY_ACCESS_TOKEN": "",
    # OneBot 支持: "WS_CLIENT", "WS_SERVER"
    "ONEBOT_TYPE": "WS_CLIENT",
    "ONEBOT_HOST": "127.0.0.1",
    "ONEBOT_PORT": 8080,
    "ONEBOT_ACCESS_TOKEN": "",
    "ONEBOT_HEARTBEAT_INTERVAL": 5,
    "MILKY_HEARTBEAT_ENABLED": False,
    "MILKY_HEARTBEAT_INTERVAL": 30,
}


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
    HTTP_CLIENT = httpx.AsyncClient(timeout=10.0)
    onebot_client_ws: UnifiedWebSocket | None = None
    onebot_server_wss: set[UnifiedWebSocket] = set()
    milky_ready: asyncio.Event | None = None
    self_id: int | None = None

    @classmethod
    def milky_auth_headers(cls) -> dict[str, str]:
        token = CONFIG["MILKY_ACCESS_TOKEN"]
        return {"Authorization": f"Bearer {token}"} if token else {}

    @classmethod
    def onebot_header(cls) -> dict[str, str]:
        headers = {}
        token = CONFIG["ONEBOT_ACCESS_TOKEN"]
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
            f"http://{CONFIG['MILKY_HOST']}:{CONFIG['MILKY_PORT']}/api/{action}",
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
            "interval": int(CONFIG["ONEBOT_HEARTBEAT_INTERVAL"] * 1000),
        }

    @classmethod
    async def send_to_onebot(cls, message: dict[str, Any]) -> None:
        ob_type = CONFIG["ONEBOT_TYPE"]
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
            logging.info(f"忽略暂未映射的 Milky 事件: {message.get('event_type')}")
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


async def source_ws_client_loop():
    ws_url = f"ws://{CONFIG['MILKY_HOST']}:{CONFIG['MILKY_PORT']}/event"
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
                async for message in ws:
                    msg_str = (
                        message if isinstance(message, str) else message.decode("utf-8")
                    )
                    await GatewayHub.dispatch_to_onebot(msg_str)
        except Exception as e:
            if GatewayHub.milky_ready is not None:
                GatewayHub.milky_ready.clear()
            logging.warning(f"[Milky Ws_Client] Milky Websocket 断开, 5秒后重连: {e}")
            await asyncio.sleep(5)


async def onebot_ws_client_loop():
    ws_url = f"ws://{CONFIG['ONEBOT_HOST']}:{CONFIG['ONEBOT_PORT']}/onebot/v11/ws"
    while True:
        if GatewayHub.milky_ready is not None:
            await GatewayHub.milky_ready.wait()
        await GatewayHub.refresh_self_id()
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
                        (
                            message
                            if isinstance(message, str)
                            else message.decode("utf-8")
                        )
                    )
                    asyncio.create_task(
                        GatewayHub.handle_onebot_event_flow(
                            msg, reply_channel=GatewayHub.onebot_client_ws
                        )
                    )
        except Exception as e:
            GatewayHub.onebot_client_ws = None
            logging.warning(f"[Onebot Ws_Client] Onebot Websocket 断开, 5秒后重连: {e}")
            await asyncio.sleep(5)


async def onebot_heartbeat_loop():
    while True:
        try:
            await asyncio.sleep(CONFIG["ONEBOT_HEARTBEAT_INTERVAL"])
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
            await asyncio.sleep(CONFIG["MILKY_HEARTBEAT_INTERVAL"])
            if GatewayHub.milky_ready is not None:
                await GatewayHub.milky_ready.wait()
            logging.error("[Milky Heartbeat] ? 这个为什么会运行")
        except asyncio.CancelledError:
            raise
        except Exception as e:
            logging.warning(f"[Milky Heartbeat] 心跳循环异常: {e}")


async def source_sse_loop():
    """从 Milky SSE 读取事件并转发给 OneBot"""
    sse_url = f"http://{CONFIG['MILKY_HOST']}:{CONFIG['MILKY_PORT']}/event"
    while True:
        try:
            logging.info(f"[Milky SSE] 正在连接 Milky SSE {sse_url}...")
            async with GatewayHub.HTTP_CLIENT.stream(
                "GET", sse_url, headers=GatewayHub.milky_auth_headers()
            ) as response:
                logging.info("[Milky SSE] 连接 SSE 成功..")
                if GatewayHub.milky_ready is not None:
                    GatewayHub.milky_ready.set()

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
            await asyncio.sleep(5)


async def endpoint_source_webhook(request: Request, background_tasks: BackgroundTasks):
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
            asyncio.create_task(
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

    if CONFIG["MILKY_TYPE"] == "WEBSOCKET":
        bg_tasks.append(asyncio.create_task(source_ws_client_loop()))
    elif CONFIG["MILKY_TYPE"] == "SSE":
        bg_tasks.append(asyncio.create_task(source_sse_loop()))
    else:
        GatewayHub.milky_ready.set()

    if CONFIG["ONEBOT_TYPE"] == "WS_CLIENT":
        bg_tasks.append(asyncio.create_task(onebot_ws_client_loop()))
    bg_tasks.append(asyncio.create_task(onebot_heartbeat_loop()))
    if CONFIG["MILKY_HEARTBEAT_ENABLED"]:
        bg_tasks.append(asyncio.create_task(milky_heartbeat_loop()))

    logging.info("Started..")
    yield
    for task in bg_tasks:
        task.cancel()
    await GatewayHub.HTTP_CLIENT.aclose()


app = FastAPI(
    lifespan=lifespan, title="Milky强兼器", host=CONFIG["HOST"], port=CONFIG["PORT"]
)

if CONFIG["MILKY_TYPE"] == "WEBHOOK":
    logging.info(
        f"[Milky Webhook] 服务地址 http://{CONFIG['HOST']}:{CONFIG['PORT']}/milky/webhook"
    )
    app.add_api_route("/milky/webhook", endpoint_source_webhook, methods=["POST"])

if CONFIG["ONEBOT_TYPE"] == "WS_SERVER":
    logging.info(
        f"[Onebot Ws_Client] 服务地址 http://{CONFIG['HOST']}:{CONFIG['PORT']}/onebot/v11/ws"
    )
    app.add_api_websocket_route("/onebot/v11/ws", endpoint_onebot_reverse_ws)


@app.get("/health")
async def health():
    return {"status": "running"}


if __name__ == "__main__":
    uvicorn.run(app)
