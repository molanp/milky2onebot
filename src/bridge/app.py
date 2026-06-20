from __future__ import annotations

import argparse
import logging

from .service import OnebotBridgeService


def create_service(milky_url: str, milky_token: str | None, host: str, port: int, ws_port: int | None) -> OnebotBridgeService:
    return OnebotBridgeService(milky_url, milky_token, host=host, port=port, ws_port=ws_port)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Start Milky -> Onebot bridge")
    parser.add_argument("--milky-url", default="http://127.0.0.1:8080", help="Milky base URL")
    parser.add_argument("--milky-token", default=None, help="Milky access token")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host")
    parser.add_argument("--port", type=int, default=8080, help="HTTP port")
    parser.add_argument("--ws-port", type=int, default=None, help="Optional WebSocket port")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    svc = create_service(args.milky_url, args.milky_token, args.host, args.port, args.ws_port)
    svc.start()


if __name__ == "__main__":
    main()
