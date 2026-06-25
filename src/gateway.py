import asyncio
import logging
from contextlib import asynccontextmanager
import httpx
import websockets
from fastapi import FastAPI, Request, BackgroundTasks, WebSocket
from fastapi.websockets import WebSocketState
from starlette.websockets import WebSocketDisconnect
from websockets import ClientConnection

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


CONFIG = {
    # Milky 支持: "WS_CLIENT", "SSE", "WEBHOOK"
    "MILKY_TYPE": "WS_CLIENT",
    "MILKY_WS_URL": "ws://milky.ntqqrev.org/event",
    "MILKY_SSE_URL": "http://milky.ntqqrev.org/sse",
    "MILKY_HTTP_POST_URL": "http://milky.ntqqrev.org/api",
    # OneBot 支持: "WS_CLIENT", "WS_SERVER"
    "ONEBOT_TYPE": "WS_CLIENT",
    "ONEBOT_WS_URL": "ws://127.0.0.1:8080/onebot/v11/ws",
}


class UnifiedWebSocket:
    def __init__(self, raw_ws: ClientConnection | WebSocket):
        self.raw_ws = raw_ws

    async def send(self, text: str):
        if isinstance(self.raw_ws, ClientConnection):
            await self.raw_ws.send(text)
        elif self.raw_ws.client_state == WebSocketState.CONNECTED:
            await self.raw_ws.send_text(text)


class GatewayHub:
    HTTP_CLIENT = httpx.AsyncClient(timeout=10.0)
    onebot_client_ws: UnifiedWebSocket | None = None
    onebot_server_wss: set[UnifiedWebSocket] = set()

    @classmethod
    async def dispatch_to_onebot(cls, raw_message: str):
        ob_type = CONFIG["ONEBOT_TYPE"]

        if ob_type == "WS_CLIENT" and cls.onebot_client_ws:
            await cls.onebot_client_ws.send(raw_message)

        elif ob_type == "WS_SERVER" and cls.onebot_server_wss:
            if tasks := [ws.send(raw_message) for ws in cls.onebot_server_wss]:
                await asyncio.gather(*tasks, return_exceptions=True)

    @classmethod
    async def handle_onebot_event_flow(
        cls, onebot_message: str, reply_channel: UnifiedWebSocket
    ) -> None:
        try:
            response = await cls.HTTP_CLIENT.post(
                CONFIG["MILKY_HTTP_POST_URL"], json={"raw": onebot_message}
            )
            response_text = response.text
            # TODO: 处理格式到ob
            await reply_channel.send(response_text)
        except Exception as e:
            logging.error(f"中转 OneBot 事件失败: {e}")
            return


async def source_ws_client_loop():
    while True:
        try:
            async with websockets.connect(
                CONFIG["MILKY_WS_URL"], ping_interval=20
            ) as ws:
                logging.info("已建立与 Milky 的 Websocket 连接..")
                async for message in ws:
                    msg_str = (
                        message if isinstance(message, str) else message.decode("utf-8")
                    )
                    await GatewayHub.dispatch_to_onebot(msg_str)
        except Exception as e:
            logging.warning(f"Milky Websocket 断开 ({e}), 5秒后重连...")
            await asyncio.sleep(5)


async def onebot_ws_client_loop():
    while True:
        try:
            async with websockets.connect(CONFIG["ONEBOT_WS_URL"]) as ws:
                GatewayHub.onebot_client_ws = UnifiedWebSocket(ws)
                logging.info("已主动建立与 OneBot 正向 WS 的连接..")
                async for message in ws:
                    msg_str = (
                        message if isinstance(message, str) else message.decode("utf-8")
                    )
                    asyncio.create_task(
                        GatewayHub.handle_onebot_event_flow(
                            msg_str, reply_channel=GatewayHub.onebot_client_ws
                        )
                    )
        except Exception as e:
            GatewayHub.onebot_client_ws = None
            logging.warning(f"OneBot 正向 WS 断开 ({e!r}), 5秒后重连...")
            await asyncio.sleep(5)


async def source_sse_loop():
    while True:
        try:
            async with GatewayHub.HTTP_CLIENT.stream(
                "GET", CONFIG["MILKY_SSE_URL"]
            ) as response:
                logging.info("连接 SSE 成功..")
                async for line in response.aiter_lines():
                    if line.startswith("data:"):
                        await GatewayHub.dispatch_to_onebot(line[5:].strip())
        except Exception as e:
            logging.error(f"SSE 流中断 ({e!r}), 5秒后重连...")
            await asyncio.sleep(5)


async def endpoint_source_webhook(request: Request, background_tasks: BackgroundTasks):
    body = await request.body()
    background_tasks.add_task(GatewayHub.dispatch_to_onebot, body.decode("utf-8"))
    return {"status": "accepted"}


async def endpoint_onebot_reverse_ws(websocket: WebSocket):
    await websocket.accept()
    # 丢进适配器，统一管理
    adapted_ws = UnifiedWebSocket(websocket)
    GatewayHub.onebot_server_wss.add(adapted_ws)
    try:
        while True:
            message = await websocket.receive_text()
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

    # 按需创建后台长连接任务
    if CONFIG["MILKY_TYPE"] == "WS_CLIENT":
        bg_tasks.append(asyncio.create_task(source_ws_client_loop()))
    elif CONFIG["MILKY_TYPE"] == "SSE":
        bg_tasks.append(asyncio.create_task(source_sse_loop()))

    if CONFIG["ONEBOT_TYPE"] == "WS_CLIENT":
        bg_tasks.append(asyncio.create_task(onebot_ws_client_loop()))

    logging.info("Started.")
    yield
    for task in bg_tasks:
        task.cancel()
    await GatewayHub.HTTP_CLIENT.aclose()


app = FastAPI(lifespan=lifespan, title="Milky强兼器")

if CONFIG["MILKY_TYPE"] == "WEBHOOK":
    logging.info("注册 WebHook 接收端点..")
    app.add_api_route("/milky/webhook", endpoint_source_webhook, methods=["POST"])

if CONFIG["ONEBOT_TYPE"] == "WS_SERVER":
    logging.info("注册 OneBot 反向 WebSocket 服务器接收端点..")
    app.add_api_websocket_route("/onebot/v11/ws", endpoint_onebot_reverse_ws)


@app.get("/health")
async def health():
    return {"status": "running"}
