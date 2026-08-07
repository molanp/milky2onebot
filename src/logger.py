from __future__ import annotations

from contextlib import suppress
from datetime import date, datetime, timedelta
from datetime import time as datetime_time
import logging
import os
from pathlib import Path
import sys
import threading
from typing import Any, ClassVar

from .config import APP_LOGGER_NAME, AppConfig

LOG_RETENTION_DAYS = 30
SILENCED_LOGGERS = (
    "asyncio",
    "fastapi",
    "httpcore",
    "httpx",
    "multipart",
    "starlette",
    "uvicorn",
    "uvicorn.access",
    "uvicorn.error",
    "websockets",
)
RUNTIME_LOGGER = logging.getLogger(f"{APP_LOGGER_NAME}.runtime")


def get_logger(component: str) -> logging.Logger:
    return logging.getLogger(f"{APP_LOGGER_NAME}.{component}")


class ColorFormatter(logging.Formatter):
    COLORS: ClassVar[dict[str, str]] = {
        "DEBUG": "\033[36m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[41m",
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        original_levelname = record.levelname
        color = self.COLORS.get(record.levelname, "")
        record.levelname = f"{color}{record.levelname}{self.RESET}"
        try:
            return super().format(record)
        finally:
            record.levelname = original_levelname


class DailyFileHandler(logging.FileHandler):
    def __init__(self, directory: Path, retention_days: int):
        self.directory = directory
        self.retention_days = max(0, retention_days)
        self.current_date = date.today()
        self.rollover_at = self._midnight_after(self.current_date)
        self.directory.mkdir(parents=True, exist_ok=True)
        super().__init__(self._log_path(self.current_date), encoding="utf-8")
        self._delete_expired_logs(self.current_date)

    def emit(self, record: logging.LogRecord) -> None:
        if record.created >= self.rollover_at:
            log_date = datetime.fromtimestamp(record.created).date()
            if self.stream:
                self.stream.flush()
                self.stream.close()
                self.stream = None
            self.current_date = log_date
            self.rollover_at = self._midnight_after(log_date)
            self.baseFilename = os.path.abspath(self._log_path(log_date))
            self.stream = self._open()
            self._delete_expired_logs(log_date)
        super().emit(record)

    def _log_path(self, log_date: date) -> Path:
        return self.directory / f"{log_date.isoformat()}.log"

    @staticmethod
    def _midnight_after(log_date: date) -> float:
        next_date = log_date + timedelta(days=1)
        return datetime.combine(next_date, datetime_time.min).timestamp()

    def _delete_expired_logs(self, current_date: date) -> None:
        if self.retention_days <= 0:
            return
        oldest_date = current_date - timedelta(days=self.retention_days - 1)
        for log_path in self.directory.glob("????-??-??.log"):
            try:
                log_date = date.fromisoformat(log_path.stem)
            except ValueError:
                continue
            if log_date < oldest_date:
                with suppress(OSError):
                    log_path.unlink()


def setup_logging(settings: AppConfig) -> None:
    app_level = getattr(logging, settings.logging.level.upper(), logging.INFO)
    message_format = "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"

    console_handler = logging.StreamHandler()
    console_handler.setLevel(app_level)
    formatter_cls = ColorFormatter if settings.logging.color else logging.Formatter
    console_format = message_format
    if settings.logging.color:
        console_format = (
            "%(asctime)s [%(levelname)s] [%(name)s] \033[37m%(message)s\033[0m"
        )
    console_handler.setFormatter(formatter_cls(console_format))

    config_dir = settings.config_path.parent if settings.config_path else Path.cwd()
    file_handler = DailyFileHandler(
        config_dir / "logs",
        retention_days=LOG_RETENTION_DAYS,
    )
    file_handler.setLevel(app_level)
    file_handler.setFormatter(logging.Formatter(message_format))

    app_logger = logging.getLogger(APP_LOGGER_NAME)
    _close_handlers(app_logger)
    app_logger.addHandler(console_handler)
    app_logger.addHandler(file_handler)
    app_logger.setLevel(app_level)
    app_logger.disabled = False
    app_logger.propagate = False

    root_logger = logging.getLogger()
    _close_handlers(root_logger)
    root_logger.addHandler(logging.NullHandler())
    root_logger.setLevel(logging.CRITICAL + 1)

    for logger_name, logger in logging.root.manager.loggerDict.items():
        if not isinstance(logger, logging.Logger):
            continue
        if logger_name == APP_LOGGER_NAME or logger_name.startswith(
            f"{APP_LOGGER_NAME}."
        ):
            logger.disabled = False
            continue
        _close_handlers(logger)
        logger.propagate = False
        logger.disabled = True

    for logger_name in SILENCED_LOGGERS:
        logger = logging.getLogger(logger_name)
        _close_handlers(logger)
        logger.propagate = False
        logger.disabled = True

    sys.excepthook = _log_uncaught_exception
    threading.excepthook = _log_thread_exception


def _close_handlers(logger: logging.Logger) -> None:
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()


def _log_uncaught_exception(
    exc_type: type[BaseException],
    exc_value: BaseException,
    exc_traceback: Any,
) -> None:
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    RUNTIME_LOGGER.critical(
        "未捕获异常",
        exc_info=(exc_type, exc_value, exc_traceback),
    )


def _log_thread_exception(args: threading.ExceptHookArgs) -> None:
    if args.exc_value is None:
        RUNTIME_LOGGER.critical("线程出现未捕获异常: %s", args.exc_type.__name__)
        return
    _log_uncaught_exception(args.exc_type, args.exc_value, args.exc_traceback)
