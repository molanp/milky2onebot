from __future__ import annotations

from collections.abc import Callable
import logging
import re
from typing import Any, Literal

from .config import APP_LOGGER_NAME

LOGGER = logging.getLogger(f"{APP_LOGGER_NAME}.message_convert")
Json = dict[str, Any]
MessageIdBuilder = Callable[[Literal["group", "friend", "temp"], int, int], int]
MessageIdParser = Callable[[int], Json]
CQ_PATTERN = re.compile(r"(\[CQ:(.*?),(.*?)\]|.)", re.S)


def cq2msg(cq: str) -> list[Json]:
    msg: list[Json] = []
    text = ""

    for match in CQ_PATTERN.finditer(cq):
        full, seg_type, data_str = match.groups()
        if seg_type:
            if text:
                msg.append({"type": "text", "data": {"text": text}})
                text = ""
            data: dict[str, str] = {}
            if data_str:
                for pair in data_str.split(","):
                    if "=" in pair:
                        key, value = pair.split("=", 1)
                        data[key] = value
                    else:
                        data[pair] = ""
            msg.append({"type": seg_type, "data": data})
        else:
            text += full

    if text:
        msg.append({"type": "text", "data": {"text": text}})

    return msg


def msg2cq(segments: list[Json]) -> str:
    parts = []
    for segment in segments:
        seg_type = segment["type"]
        data = segment["data"]
        if seg_type == "text":
            parts.append(data["text"])
        else:
            data_str = ",".join([f"{key}={value}" for key, value in data.items()])
            parts.append(f"[CQ:{seg_type}" + (f",{data_str}]" if data_str else "]"))
    return "".join(parts)


def normalize_message(
    message: Any, message_id_parser: MessageIdParser | None = None
) -> list[Json]:
    if isinstance(message, str):
        result = cq2msg(message)
    elif isinstance(message, list):
        result = [onebot_segment_to_milky(seg, message_id_parser) for seg in message]
    else:
        result = [onebot_segment_to_milky(message, message_id_parser)]
    LOGGER.debug("[Milky] 转换 Onebot 消息: %s", message)
    return result


def onebot_segment_to_milky(
    segment: Json, message_id_parser: MessageIdParser | None = None
) -> Json:
    seg_type = segment.get("type")
    data = segment.get("data") or {}

    if seg_type == "text":
        return {"type": "text", "data": {"text": str(data["text"])}}
    if seg_type == "at":
        qq = data["qq"]
        if qq == "all":
            return {"type": "mention_all", "data": {}}
        return {"type": "mention", "data": {"user_id": int(qq)}}
    if seg_type == "face":
        return {
            "type": "face",
            "data": {"face_id": str(data.get("id", "")), "is_large": False},
        }
    if seg_type == "reply":
        message_id = int(data["id"])
        if message_id_parser is not None:
            message_seq = message_id_parser(message_id)["message_seq"]
        else:
            message_seq = message_id
        return {"type": "reply", "data": {"message_seq": message_seq}}
    if seg_type == "image":
        return {
            "type": "image",
            "data": {
                "uri": data.get("url") or data.get("file") or data.get("path") or "",
                "summary": data.get("summary"),
                "sub_type": "sticker" if data.get("subType") == 1 else "normal",
            },
        }
    if seg_type == "record":
        return {
            "type": "record",
            "data": {
                "uri": data.get("url") or data.get("file") or data.get("path") or ""
            },
        }
    if seg_type == "video":
        converted = {
            "type": "video",
            "data": {
                "uri": data.get("url") or data.get("file") or data.get("path") or ""
            },
        }
        if data.get("thumb"):
            converted["data"]["thumb_uri"] = data["thumb"]
        return converted
    if seg_type == "json":
        return {
            "type": "light_app",
            "data": {"app_name": "", "json_payload": str(data.get("data", ""))},
        }
    if seg_type == "xml":
        return {
            "type": "xml",
            "data": {"service_id": 0, "xml_payload": str(data.get("data", ""))},
        }
    if seg_type in {"forward", "node"}:
        return onebot_forward_to_milky(segment, message_id_parser)

    return {"type": "text", "data": {"text": f"[unsupported:{seg_type}]"}}


def onebot_forward_to_milky(
    segment: Json, message_id_parser: MessageIdParser | None = None
) -> Json:
    data = segment.get("data") or {}
    raw_messages = data.get("messages")
    if raw_messages is None:
        raw_messages = data.get("nodes")
    if raw_messages is None and segment.get("type") == "node":
        raw_messages = [data]
    if raw_messages is None:
        raise ValueError("forward segment requires data.messages or data.nodes")

    return {
        "type": "forward",
        "data": {
            "messages": [
                onebot_forward_node_to_milky(node, message_id_parser)
                for node in raw_messages
            ],
            "prompt": data.get("prompt"),
            "summary": data.get("summary"),
            "preview": data.get("preview"),
            "title": data.get("title"),
        },
    }


def onebot_forward_node_to_milky(
    node: Json, message_id_parser: MessageIdParser | None = None
) -> Json:
    node_data = node.get("data") if node.get("type") == "node" else node
    node_data = node_data or {}
    content = (
        node_data.get("segments")
        or node_data.get("content")
        or node_data.get("message")
        or ""
    )
    return {
        "user_id": int(node_data.get("user_id") or node_data.get("uin") or 0),
        "sender_name": node_data.get("sender_name")
        or node_data.get("nickname")
        or node_data.get("name")
        or "",
        "segments": normalize_message(content, message_id_parser),
    }


def milky_segment_to_onebot(
    segment: Json,
    message_id_builder: MessageIdBuilder,
    scene: Literal["group", "friend", "temp"] | None = None,
    peer_id: int | None = None,
) -> Json:
    seg_type = segment.get("type")
    data = segment["data"]

    if seg_type == "text":
        return {"type": "text", "data": {"text": data["text"]}}
    if seg_type == "mention":
        return {"type": "at", "data": {"qq": data["user_id"], "name": data["name"]}}
    if seg_type == "mention_all":
        return {"type": "at", "data": {"qq": "all"}}
    if seg_type == "face":
        return {"type": "face", "data": {"id": data.get("face_id")}}
    if seg_type == "image":
        return {
            "type": "image",
            "data": {
                "file": data.get("resource_id") or data.get("temp_url") or "",
                "url": data.get("temp_url"),
                "summary": data.get("summary"),
            },
        }
    if seg_type == "record":
        return {
            "type": "record",
            "data": {
                "file": data.get("resource_id") or data.get("temp_url") or "",
                "url": data.get("temp_url"),
            },
        }
    if seg_type == "video":
        return {
            "type": "video",
            "data": {
                "file": data.get("resource_id") or data.get("temp_url") or "",
                "url": data.get("temp_url"),
            },
        }
    if seg_type == "file":
        return {
            "type": "file",
            "data": {
                "file": data["file_name"],
                "file_id": data["file_id"],
                "file_size": data["file_size"],
                "name": data["file_name"],
                "url": data.get("download_url") or data.get("temp_url"),
            },
        }
    if seg_type == "forward":
        return {"type": "forward", "data": {"id": data["forward_id"]}}
    if seg_type == "market_face":
        return {
            "type": "mface",
            "data": {
                "emoji_package_id": data.get("emoji_package_id"),
                "emoji_id": str(data.get("emoji_id", "")),
                "key": data.get("key"),
                "summary": data.get("summary"),
                "url": data.get("url"),
            },
        }
    if seg_type == "light_app":
        return {"type": "json", "data": {"data": data.get("json_payload", "")}}
    if seg_type == "xml":
        return {"type": "xml", "data": {"data": data.get("xml_payload", "")}}
    if seg_type == "reply":
        if scene and peer_id is not None and data.get("message_seq") is not None:
            reply_id = message_id_builder(scene, peer_id, data["message_seq"])
        else:
            reply_id = data.get("message_seq")
        return {"type": "reply", "data": {"id": str(reply_id)}}

    return {"type": "text", "data": {"text": f"[unsupported:{seg_type}]"}}
