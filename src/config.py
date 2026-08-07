from __future__ import annotations

import contextlib
from dataclasses import dataclass
import os
from pathlib import Path
import sys
from typing import Any

import tomllib

APP_LOGGER_NAME = "M2O"
DEFAULT_CONFIG = """[server]
host = "127.0.0.1"
port = 8000

[logging]
level = "INFO"
color = true

[milky]
# 支持: "WEBSOCKET", "SSE", "WEBHOOK"
mode = "WEBSOCKET"
host = "127.0.0.1"
port = 30001
access_token = ""
reconnect_interval = 5.0

[onebot]
# 支持: "WS_CLIENT", "WS_SERVER"
mode = "WS_CLIENT"
host = "127.0.0.1"
port = 8080
access_token = ""
reconnect_interval = 5.0

[heartbeat.onebot]
enabled = true
interval = 5.0

[heartbeat.milky]
enabled = false
interval = 30.0

[performance]
http_timeout = 10.0
websocket_max_size = 16777216
"""


def _default_config_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "config.toml"
    return Path.cwd() / "config.toml"


@dataclass(frozen=True)
class ServerConfig:
    host: str = "127.0.0.1"
    port: int = 8000


@dataclass(frozen=True)
class LoggingConfig:
    level: str = "INFO"
    color: bool = True


@dataclass(frozen=True)
class MilkyConfig:
    mode: str = "WEBSOCKET"
    host: str = "127.0.0.1"
    port: int = 3000
    access_token: str = ""
    reconnect_interval: float = 5.0

    @property
    def api_base_url(self) -> str:
        return f"http://{self.host}:{self.port}/api"

    @property
    def ws_event_url(self) -> str:
        return f"ws://{self.host}:{self.port}/event"

    @property
    def sse_event_url(self) -> str:
        return f"http://{self.host}:{self.port}/event"


@dataclass(frozen=True)
class OneBotConfig:
    mode: str = "WS_CLIENT"
    host: str = "127.0.0.1"
    port: int = 8080
    access_token: str = ""
    reconnect_interval: float = 5.0

    @property
    def ws_url(self) -> str:
        return f"ws://{self.host}:{self.port}/onebot/v11/ws"


@dataclass(frozen=True)
class HeartbeatConfig:
    onebot_enabled: bool = True
    onebot_interval: float = 5.0
    milky_enabled: bool = False
    milky_interval: float = 30.0


@dataclass(frozen=True)
class PerformanceConfig:
    http_timeout: float = 10.0
    websocket_max_size: int = 16 * 1024 * 1024


@dataclass(frozen=True)
class AppConfig:
    server: ServerConfig = ServerConfig()  # noqa: RUF009
    logging: LoggingConfig = LoggingConfig()  # noqa: RUF009
    milky: MilkyConfig = MilkyConfig()  # noqa: RUF009
    onebot: OneBotConfig = OneBotConfig()  # noqa: RUF009
    heartbeat: HeartbeatConfig = HeartbeatConfig()  # noqa: RUF009
    performance: PerformanceConfig = PerformanceConfig()  # noqa: RUF009
    config_path: Path | None = None


def load_config(path: str | Path | None = None) -> AppConfig:
    config_path = Path(
        path or os.getenv("M2OB_CONFIG") or _default_config_path()
    ).expanduser()
    _create_default_config(config_path)
    raw = _read_toml(config_path)
    _apply_env_overrides(raw)

    milky = raw.get("milky", {})
    onebot = raw.get("onebot", {})
    heartbeat = raw.get("heartbeat", {})

    return AppConfig(
        server=ServerConfig(**_section(raw, "server")),
        logging=LoggingConfig(**_section(raw, "logging")),
        milky=MilkyConfig(
            **{
                **_section(raw, "milky"),
                "mode": str(milky.get("mode", MilkyConfig.mode)).upper(),
            }
        ),
        onebot=OneBotConfig(
            **{
                **_section(raw, "onebot"),
                "mode": str(onebot.get("mode", OneBotConfig.mode)).upper(),
            }
        ),
        heartbeat=HeartbeatConfig(
            **{
                **_section(heartbeat, "onebot", prefix="onebot_"),
                **_section(heartbeat, "milky", prefix="milky_"),
            }
        ),
        performance=PerformanceConfig(**_section(raw, "performance")),
        config_path=config_path,
    )


def _create_default_config(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with contextlib.suppress(FileExistsError):
        with path.open("x", encoding="utf-8", newline="\n") as config_file:
            config_file.write(DEFAULT_CONFIG)


def _read_toml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("rb") as f:
        return tomllib.load(f)


def _section(raw: dict[str, Any], name: str, prefix: str = "") -> dict[str, Any]:
    section = raw.get(name, {})
    if not isinstance(section, dict):
        raise ValueError(f"config section [{name}] must be a table")
    return {f"{prefix}{key}": value for key, value in section.items()}


def _apply_env_overrides(raw: dict[str, Any]) -> None:
    overrides: dict[str, tuple[str, str, Any]] = {
        "M2OB_SERVER_HOST": ("server", "host", str),
        "M2OB_SERVER_PORT": ("server", "port", int),
        "M2OB_LOG_LEVEL": ("logging", "level", str),
        "M2OB_LOG_COLOR": ("logging", "color", _bool),
        "M2OB_MILKY_MODE": ("milky", "mode", str),
        "M2OB_MILKY_HOST": ("milky", "host", str),
        "M2OB_MILKY_PORT": ("milky", "port", int),
        "M2OB_MILKY_ACCESS_TOKEN": ("milky", "access_token", str),
        "M2OB_MILKY_RECONNECT_INTERVAL": ("milky", "reconnect_interval", float),
        "M2OB_ONEBOT_MODE": ("onebot", "mode", str),
        "M2OB_ONEBOT_HOST": ("onebot", "host", str),
        "M2OB_ONEBOT_PORT": ("onebot", "port", int),
        "M2OB_ONEBOT_ACCESS_TOKEN": ("onebot", "access_token", str),
        "M2OB_ONEBOT_RECONNECT_INTERVAL": ("onebot", "reconnect_interval", float),
        "M2OB_ONEBOT_HEARTBEAT_ENABLED": (
            "heartbeat.onebot",
            "enabled",
            _bool,
        ),
        "M2OB_ONEBOT_HEARTBEAT_INTERVAL": (
            "heartbeat.onebot",
            "interval",
            float,
        ),
        "M2OB_MILKY_HEARTBEAT_ENABLED": ("heartbeat.milky", "enabled", _bool),
        "M2OB_MILKY_HEARTBEAT_INTERVAL": ("heartbeat.milky", "interval", float),
        "M2OB_HTTP_TIMEOUT": ("performance", "http_timeout", float),
        "M2OB_WEBSOCKET_MAX_SIZE": ("performance", "websocket_max_size", int),
    }
    for env_name, (section_path, key, caster) in overrides.items():
        if env_name not in os.environ:
            continue
        section = raw
        for part in section_path.split("."):
            section = section.setdefault(part, {})
        section[key] = caster(os.environ[env_name])


def _bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}
