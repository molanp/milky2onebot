from __future__ import annotations

import asyncio
import json
import logging
import queue
import threading
import time
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from msgspec import ValidationError

class BridgeError(RuntimeError):
    """Bridge-level error used locally when routing or validation fails."""
    pass
# Minimal local converters (replace with real implementations later)

def convert_onebot_api_to_milky(api_name: str, payload: dict[str, Any]) -> tuple[str, dict[str, Any]]:
    return api_name, payload


def convert_milky_event_to_onebot(event: dict[str, Any]) -> dict[str, Any]:
    # lightweight mapping: wrap event under Onebot message-like shape if possible
    return {
        "time": event.get("time", 0),
        "post_type": "message",
        "message": event.get("data", {}).get("segments", []),
        "raw_message": json.dumps(event, ensure_ascii=False),
        "sender": {"user_id": event.get("data", {}).get("sender_id", 0)},
        "target_id": event.get("data", {}).get("peer_id", 0),
    }

from ..models.milky.event import MessageReceiveEvent

# FUCK VIBE, THIS IS SHIT!!!
try:
    import websockets
    from websockets import WebSocketServerProtocol
except Exception:  # pragma: no cover - websocket optional
    websockets = None  # type: ignore
    WebSocketServerProtocol = Any  # type: ignore

logger = logging.getLogger(__name__)


class MilkyClient:
    """Minimal Milky HTTP client + SSE listener."""

    def __init__(self, base_url: str, access_token: str | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.access_token = access_token

    def send_request(self, api_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}/api/{api_name}"
        body = json.dumps(payload or {}).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read().decode("utf-8")
                return json.loads(data) if data else {}
        except urllib.error.HTTPError as exc:
            payload = exc.read().decode("utf-8")
            try:
                return json.loads(payload)
            except Exception:
                raise BridgeError(f"Milky HTTP error {exc.code}") from exc
        except urllib.error.URLError as exc:
            raise BridgeError(f"Milky unreachable: {exc.reason}") from exc

    def listen_events(self, callback: Callable[[dict[str, Any]], None]) -> None:
        t = threading.Thread(target=self._sse_loop, args=(callback,), daemon=True)
        t.start()

    def _sse_loop(self, callback: Callable[[dict[str, Any]], None]) -> None:
        url = f"{self.base_url}/event"
        headers = {"Authorization": f"Bearer {self.access_token}"} if self.access_token else {}
        while True:
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=60) as resp:
                    buf: list[str] = []
                    for raw in resp:
                        line = raw.decode("utf-8").rstrip("\r\n")
                        if line.startswith("data:"):
                            buf.append(line[5:].lstrip())
                        elif line == "":
                            if not buf:
                                continue
                            text = "\n".join(buf)
                            buf.clear()
                            try:
                                payload = json.loads(text)
                                callback(payload)
                            except Exception:
                                logger.warning("Invalid Milky event payload")
            except Exception as exc:
                logger.info("Milky event connection lost: %s", exc)
            time.sleep(2)


class EventBroadcaster:
    """Simple in-process broadcaster used by HTTP SSE endpoints."""

    def __init__(self) -> None:
        self._subs: list[queue.Queue[dict[str, Any]]] = []
        self._lock = threading.Lock()

    def subscribe(self) -> queue.Queue[dict[str, Any]]:
        q: queue.Queue[dict[str, Any]] = queue.Queue()
        with self._lock:
            self._subs.append(q)
        return q

    def unsubscribe(self, q: queue.Queue[dict[str, Any]]) -> None:
        with self._lock:
            if q in self._subs:
                self._subs.remove(q)

    def broadcast(self, event: dict[str, Any]) -> None:
        with self._lock:
            subs = list(self._subs)
        for q in subs:
            try:
                q.put_nowait(event)
            except queue.Full:
                logger.debug("subscriber queue full; drop event")


class BridgeHTTPServer(ThreadingHTTPServer):
    def __init__(self, addr, handler, app: "OnebotBridgeService") -> None:
        super().__init__(addr, handler)
        self.app = app


class OnebotBridgeService:
    """Coordinator: Milky client, event broadcaster, HTTP SSE and Onebot HTTP API."""

    def __init__(self, milky_base_url: str, milky_token: str | None = None, host: str = "0.0.0.0", port: int = 8080, ws_port: int | None = None) -> None:
        self.milky = MilkyClient(milky_base_url, milky_token)
        self.broadcaster = EventBroadcaster()
        self.host = host
        self.port = port
        self.ws_port = ws_port
        self._ws_loop: asyncio.AbstractEventLoop | None = None
        self._ws_server = None

    def start(self) -> None:
        # start Milky listener
        self.milky.listen_events(self.handle_milky_event)

        # start HTTP server
        srv = BridgeHTTPServer((self.host, self.port), OnebotRequestHandler, app=self)
        th = threading.Thread(target=srv.serve_forever, name="onebot-http", daemon=True)
        th.start()
        logger.info("Onebot HTTP listening on %s:%d", self.host, self.port)

        # optional websockets: run simple dispatcher if requested
        if self.ws_port and websockets is not None:
            self._ws_loop = asyncio.new_event_loop()
            t = threading.Thread(target=self._run_ws, daemon=True)
            t.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("shutting down bridge")
            try:
                srv.shutdown()
                srv.server_close()
            except Exception:
                pass

    def _run_ws(self) -> None:
        assert websockets is not None
        loop = self._ws_loop or asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        clients: set[WebSocketServerProtocol] = set()

        async def handler(ws: WebSocketServerProtocol):
            clients.add(ws)
            try:
                async for raw in ws:
                    try:
                        msg = json.loads(raw)
                    except Exception:
                        await ws.send(json.dumps({"status": "failed", "retcode": -400, "message": "invalid json"}, ensure_ascii=False))
                        continue
                    api = msg.get("api") or msg.get("action")
                    params = msg.get("params") or {}
                    rid = msg.get("id")
                    if not api:
                        await ws.send(json.dumps({"id": rid, "status": "failed", "retcode": -400, "message": "api missing"}, ensure_ascii=False))
                        continue
                    res = self.handle_onebot_api(api, params)
                    await ws.send(json.dumps({"id": rid, "result": res}, ensure_ascii=False))
            finally:
                clients.discard(ws)

        async def run_server() -> None:
            server = await websockets.serve(lambda ws, path: handler(ws), "0.0.0.0", self.ws_port)
            self._ws_server = server
            await server.wait_closed()

        loop.run_until_complete(run_server())

    def _validate(self, event: dict[str, Any]) -> dict[str, Any]:
        if event.get("event_type") == "message_receive":
            try:
                MessageReceiveEvent(**event)
            except (ValidationError, TypeError) as exc:
                raise BridgeError(f"invalid event: {exc}") from exc
        return event

    def handle_milky_event(self, event: dict[str, Any]) -> None:
        try:
            event = self._validate(event)
            onebot = convert_milky_event_to_onebot(event)
        except BridgeError as exc:
            logger.debug("drop milky event: %s", exc)
            return
        self.broadcaster.broadcast(onebot)

    def handle_onebot_api(self, api_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            milky_api, milky_payload = convert_onebot_api_to_milky(api_name, payload)
        except BridgeError as exc:
            return {"status": "failed", "retcode": -400, "data": None, "message": str(exc), "wording": str(exc)}
        try:
            return self.milky.send_request(milky_api, milky_payload)
        except BridgeError as exc:
            return {"status": "failed", "retcode": -500, "data": None, "message": str(exc), "wording": str(exc)}


class OnebotRequestHandler(BaseHTTPRequestHandler):
    server_version = "milky2onebot/0.1"

    def do_POST(self) -> None:
        path = self.path
        api = path.split("/api/")[-1] if "/api/" in path else path.lstrip("/")
        try:
            body = int(self.headers.get("Content-Length", "0"))
        except Exception:
            body = 0
        data = {}
        if body > 0:
            raw = self.rfile.read(body).decode("utf-8")
            try:
                data = json.loads(raw)
            except Exception:
                self._send_json(400, {"status": "failed", "retcode": -400, "message": "invalid json"})
                return
        res = self.server.app.handle_onebot_api(api, data)
        self._send_json(200, res)

    def do_GET(self) -> None:
        if self.path == "/_events":
            self._sse()
            return
        if self.path == "/health":
            self._send_json(200, {"status": "ok", "retcode": 0, "data": {"service": "milky2onebot"}})
            return
        self._send_json(404, {"status": "failed", "retcode": -404, "message": "not found"})

    def _sse(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        q = self.server.app.broadcaster.subscribe()
        try:
            while True:
                try:
                    ev = q.get(timeout=1)
                except queue.Empty:
                    continue
                payload = json.dumps(ev, ensure_ascii=False)
                try:
                    self.wfile.write(f"data: {payload}\n\n".encode("utf-8"))
                    self.wfile.flush()
                except BrokenPipeError:
                    break
        finally:
            self.server.app.broadcaster.unsubscribe(q)

    def _send_json(self, code: int, body: dict[str, Any]) -> None:
        b = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)
