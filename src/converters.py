from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
import json
import time
from typing import Any, Literal

from .message_convert import milky_segment_to_onebot, msg2cq, normalize_message
from .msgId import UltimateSignedCompressor

Json = dict[str, Any]
ParamConverter = Callable[[Json], Json]
DataConverter = Callable[..., Any]
RouterResolver = str | Callable[[Json], str]
LocalResponder = Callable[[Json], Any]
FileUrlResolver = Callable[
    [Literal["group", "friend", "temp"], int, Json], Awaitable[str | None]
]
STARTUP_TIME = time.time()

MSG_STATS = {"received": 0, "sent": 0, "last_message_time": 0}


@dataclass(frozen=True)
class ActionMapping:
    milky_action: RouterResolver
    params: ParamConverter
    data: DataConverter | None = None
    local_response: LocalResponder | None = None
    resolve_file_urls: bool = False

    def resolve_action(self, params: Json) -> str:
        if callable(self.milky_action):
            return self.milky_action(params)
        return self.milky_action


def ok(data: Any = None, echo: Any = None) -> Json:
    response = {
        "status": "ok",
        "retcode": 0,
        "data": {} if data is None else data,
        "message": "",
        "wording": "",
    }
    if echo is not None:
        response["echo"] = echo
    return response


def failed(
    message: str, retcode: int = -400, echo: Any = None, data: Any = None
) -> Json:
    response = {
        "status": "failed",
        "retcode": retcode,
        "data": data,
        "message": message,
        "wording": message,
    }
    if echo is not None:
        response["echo"] = echo
    return response


def field_map(mapping: dict[str, str], defaults: Json | None = None) -> ParamConverter:
    def convert(params: Json) -> Json:
        converted = dict(defaults or {})
        for source, target in mapping.items():
            if source in params and params[source] is not None:
                converted[target] = params[source]
        return converted

    return convert


def passthrough(params: Json) -> Json:
    return dict(params)


def empty_params(_: Json) -> Json:
    return {}


def encode_flag(payload: Json) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def decode_flag(flag: Any) -> Json:
    if isinstance(flag, dict):
        return flag
    if not isinstance(flag, str):
        return {}
    try:
        decoded = json.loads(flag)
    except json.JSONDecodeError:
        return {"raw": flag}
    return decoded if isinstance(decoded, dict) else {"raw": flag}


def message_id_from_milky(
    scene: Literal["group", "friend", "temp"], peer_id: int, message_seq: int
) -> int:
    return UltimateSignedCompressor.compress(scene, peer_id, message_seq)


def parse_message_id(message_id: int) -> Json:
    return UltimateSignedCompressor.decompress(message_id)


def get_params(message: Json) -> Json:
    params = message.get("params")
    if params is None:
        return {k: v for k, v in message.items() if k not in {"action", "echo"}}
    if isinstance(params, dict):
        return dict(params)
    raise ValueError("OneBot action params must be an object")


def send_private_params(params: Json) -> Json:
    MSG_STATS["sent"] += 1
    return {
        "user_id": params["user_id"],
        "message": normalize_message(params["message"], parse_message_id),
    }


def send_group_params(params: Json) -> Json:
    MSG_STATS["sent"] += 1
    return {
        "group_id": params["group_id"],
        "message": normalize_message(params["message"], parse_message_id),
    }


def send_msg_params(params: Json) -> Json:
    if "group_id" in params:
        return send_group_params(params)
    if "user_id" in params:
        return send_private_params(params)
    raise ValueError("send_msg requires user_id or group_id")


def send_msg_action(params: Json) -> str:
    return "send_group_message" if "group_id" in params else "send_private_message"


def delete_msg_params(params: Json) -> Json:
    decoded = parse_message_id(params["message_id"])
    if decoded["message_scene"] == "group":
        return {"group_id": decoded["peer_id"], "message_seq": decoded["message_seq"]}
    return {"user_id": decoded["peer_id"], "message_seq": decoded["message_seq"]}


def delete_msg_action(params: Json) -> str:
    decoded = parse_message_id(params["message_id"])
    if decoded["message_scene"] == "group":
        return "recall_group_message"
    return "recall_private_message"


def message_id_params(params: Json) -> Json:
    return parse_message_id(params["message_id"])


def set_essence_params(params: Json, is_set: bool) -> Json:
    decoded = parse_message_id(params["message_id"])
    if decoded["message_scene"] != "group":
        raise ValueError("essence message APIs only support group message_id")
    return {
        "group_id": decoded["peer_id"],
        "message_seq": decoded["message_seq"],
        "is_set": is_set,
    }


def group_reaction_params(params: Json) -> Json:
    decoded = parse_message_id(params["message_id"])
    if decoded["message_scene"] != "group":
        raise ValueError("set_msg_emoji_like only supports group message_id")
    emoji_id = params["emoji_id"]
    return {
        "group_id": decoded["peer_id"],
        "message_seq": decoded["message_seq"],
        "reaction": str(emoji_id),
        "reaction_type": (
            "face" if str(emoji_id).isdigit() and int(emoji_id) < 5000 else "emoji"
        ),
        "is_add": params.get("set", True),
    }


def unset_group_reaction_params(params: Json) -> Json:
    decoded = parse_message_id(params["message_id"])
    if decoded["message_scene"] != "group":
        raise ValueError("set_msg_emoji_like only supports group message_id")
    emoji_id = params["emoji_id"]
    return {
        "group_id": decoded["peer_id"],
        "message_seq": decoded["message_seq"],
        "reaction": str(emoji_id),
        "reaction_type": (
            "face" if str(emoji_id).isdigit() and int(emoji_id) < 5000 else "emoji"
        ),
        "is_add": False,
    }


def send_poke_action(params: Json) -> str:
    return "send_group_nudge" if "group_id" in params else "send_friend_nudge"


def send_poke_params(params: Json) -> Json:
    if "group_id" in params:
        return {"group_id": params["group_id"], "user_id": params["user_id"]}
    return {
        "user_id": params["user_id"],
        "is_self": params.get("user_id") == params.get("self_id"),
    }


def friend_request_action(params: Json) -> str:
    return (
        "accept_friend_request"
        if params.get("approve", True)
        else "reject_friend_request"
    )


def friend_request_params(params: Json) -> Json:
    converted = {"initiator_uid": str(params["flag"])}
    if not params.get("approve", True):
        converted["reason"] = params.get("reason") or ""
    return converted


def group_request_action(params: Json) -> str:
    flag = decode_flag(params.get("flag"))
    approve = params.get("approve", True)
    if flag.get("request_kind") == "invitation":
        return "accept_group_invitation" if approve else "reject_group_invitation"
    return "accept_group_request" if approve else "reject_group_request"


def group_request_params(params: Json) -> Json:
    flag = decode_flag(params.get("flag"))
    approve = params.get("approve", True)
    if flag.get("request_kind") == "invitation":
        return {
            "group_id": flag["group_id"],
            "invitation_seq": flag["invitation_seq"],
        }

    converted = {
        "notification_seq": flag["notification_seq"],
        "notification_type": flag.get("notification_type", "join_request"),
        "group_id": flag["group_id"],
        "is_filtered": flag.get("is_filtered", False),
    }
    if not approve:
        converted["reason"] = params.get("reason") or ""
    return converted


def history_params(scene: str, peer_field: str) -> ParamConverter:
    def convert(params: Json) -> Json:
        return {
            "message_scene": scene,
            "peer_id": params[peer_field],
            "start_message_seq": params.get("message_seq"),
            "limit": params.get("count", params.get("limit", 20)),
        }

    return convert


def send_message_data(data: Any, params: Json) -> Json:
    scene = "group" if "group_id" in params else "friend"
    peer_id = params.get("group_id", params["user_id"])
    message_id = message_id_from_milky(scene, peer_id, data["message_seq"])
    return {
        "message_id": message_id,
        "time": data["time"],
        "message_seq": data["message_seq"],
    }


def friend_entity(friend: Json) -> Json:
    return {
        "user_id": friend["user_id"],
        "nickname": friend["nickname"],
        "remark": friend["remark"],
        "sex": friend["sex"],
        "birthday_year": 0,
        "birthday_month": 0,
        "birthday_day": 0,
        "age": 0,
        "qid": friend["qid"],
        "long_nick": "",
    }


def group_entity(group: Json) -> Json:
    return {
        "group_id": group["group_id"],
        "group_name": group["group_name"],
        "group_memo": group["description"],
        "group_create_time": group["created_time"],
        "member_count": group["member_count"],
        "max_member_count": group["max_member_count"],
        "remark_name": group["remark"],
        "avatar_url": f"https://p.qlogo.cn/gh/{group['group_id']}/{group['group_id']}/0",
    }


def group_member_entity(member: Json) -> Json:
    return {
        "group_id": member["group_id"],
        "user_id": member["user_id"],
        "nickname": member["nickname"],
        "card": member["card"],
        "card_or_nickname": member["card"] or member["nickname"],
        "sex": member["sex"],
        "age": 0,
        "area": "",
        "level": str(member["level"]),
        "qq_level": 0,
        "join_time": member["join_time"],
        "last_sent_time": member["last_sent_time"],
        "title_expire_time": 0,
        "unfriendly": False,
        "card_changeable": True,
        "is_robot": False,
        "shut_up_timestamp": member["shut_up_end_time"],
        "role": member["role"],
        "title": member["title"],
    }


def incoming_message_to_onebot(message: Json, self_id: int | None = None) -> Json:
    scene: Literal["group", "friend", "temp"] = message["message_scene"]
    peer_id: int = message["peer_id"]
    message_seq: int = message["message_seq"]
    sender_id: int = message["sender_id"]
    message_id = message_id_from_milky(scene, peer_id, message_seq)
    segments = [
        milky_segment_to_onebot(
            seg, message_id_from_milky, scene=scene, peer_id=peer_id
        )
        for seg in message["segments"]
    ]

    sender_source = message.get("group_member") or message.get("friend") or {}
    sender = {
        "user_id": sender_id,
        "nickname": sender_source.get("nickname", ""),
        "card": sender_source.get("card", ""),
        "sex": sender_source.get("sex", "unknown"),
        "age": 0,
        "level": str(sender_source.get("level", 0)),
        "role": sender_source.get("role", "member"),
        "title": sender_source.get("title", ""),
    }
    event = {
        "time": message["time"],
        "self_id": self_id,
        "post_type": "message",
        "message_type": "group" if scene == "group" else "private",
        "sub_type": "normal" if scene == "group" else scene,
        "message_id": message_id,
        "real_id": message_seq,
        "message_seq": message_seq,
        "user_id": sender_id,
        "message": segments,
        "message_format": "array",
        "raw_message": msg2cq(segments),
        "font": 14,
        "sender": sender,
    }
    if scene == "group":
        event["group_id"] = peer_id
    return event


async def resolve_message_file_urls(
    message: Json, file_url_resolver: FileUrlResolver | None = None
) -> Json:
    if file_url_resolver is None:
        return message

    scene: Literal["group", "friend", "temp"] = message["message_scene"]
    peer_id: int = message["peer_id"]
    pending: list[tuple[Json, Json]] = []
    for segment in message.get("segments", []):
        if segment.get("type") != "file":
            continue
        data = segment.get("data")
        if not isinstance(data, dict):
            continue
        if data.get("download_url") or data.get("temp_url"):
            continue
        pending.append((segment, data))

    if not pending:
        return message

    urls = await asyncio.gather(
        *(file_url_resolver(scene, peer_id, data) for _, data in pending)
    )
    for (segment, data), url in zip(pending, urls):
        segment["data"] = {**data, "download_url": url}
    return message


async def resolve_action_file_urls(
    data: Any, file_url_resolver: FileUrlResolver | None = None
) -> Any:
    if file_url_resolver is None or not isinstance(data, dict):
        return data

    messages: list[Json] = []
    message = data.get("message")
    if isinstance(message, dict):
        messages.append(message)
    history = data.get("messages")
    if isinstance(history, list):
        messages.extend(item for item in history if isinstance(item, dict))

    if messages:
        await asyncio.gather(
            *(resolve_message_file_urls(item, file_url_resolver) for item in messages)
        )
    return data


async def incoming_message_to_onebot_async(
    message: Json,
    self_id: int | None = None,
    file_url_resolver: FileUrlResolver | None = None,
) -> Json:
    return incoming_message_to_onebot(
        await resolve_message_file_urls(message, file_url_resolver), self_id=self_id
    )


def get_message_data(data: Any) -> Json:
    return incoming_message_to_onebot(data["message"])


def history_data(data: Any) -> list[Json]:
    return [incoming_message_to_onebot(message) for message in data.get("messages", [])]


def onebot_version_info(_: Json) -> Json:
    return {"app_name": "LLOneBot", "protocol_version": "v11", "app_version": "9.9.9"}


def onebot_status(_: Json) -> Json:
    return {
        "online": True,
        "good": True,
        "stat": {
            "message_received": MSG_STATS["received"],
            "message_sent": MSG_STATS["sent"],
            "last_message_time": MSG_STATS["last_message_time"],
            "startup_time": STARTUP_TIME,
        },
    }


async def transform_action_response(
    milky_response: Json,
    mapping: ActionMapping,
    params: Json,
    echo: Any = None,
    file_url_resolver: FileUrlResolver | None = None,
) -> Json:
    status = milky_response["status"]
    retcode = milky_response["retcode"]
    if status != "ok" or retcode != 0:
        return failed(
            milky_response.get("message", "Milky API failed"),
            retcode=retcode,
            echo=echo,
            data=milky_response.get("data"),
        )

    data = milky_response.get("data", {})
    if mapping.resolve_file_urls:
        data = await resolve_action_file_urls(data, file_url_resolver)
    if mapping.data is not None:
        try:
            data = mapping.data(data, params)
        except TypeError:
            data = mapping.data(data)
    return ok(data, echo=echo)


def list_from_key(key: str, item_converter: DataConverter) -> DataConverter:
    def convert(data: Any) -> Any:
        return [item_converter(item) for item in data.get(key, [])]

    return convert


ACTION_MAP: dict[str, ActionMapping] = {
    "send_private_msg": ActionMapping(
        "send_private_message", send_private_params, send_message_data
    ),
    "send_group_msg": ActionMapping(
        "send_group_message", send_group_params, send_message_data
    ),
    "send_msg": ActionMapping(send_msg_action, send_msg_params, send_message_data),
    "delete_msg": ActionMapping(delete_msg_action, delete_msg_params),
    "get_msg": ActionMapping(
        "get_message", message_id_params, get_message_data, resolve_file_urls=True
    ),
    "mark_msg_as_read": ActionMapping("mark_message_as_read", message_id_params),
    "get_login_info": ActionMapping(
        "get_login_info",
        empty_params,
        lambda data: {"user_id": data["uin"], "nickname": data["nickname"]},
    ),
    "get_cookies": ActionMapping(
        "get_cookies",
        field_map({"domain": "domain"}),
        lambda data: {"cookies": data["cookies"]},
    ),
    "get_version_info": ActionMapping(
        "",
        empty_params,
        local_response=onebot_version_info,
    ),
    "get_status": ActionMapping(
        "",
        empty_params,
        local_response=onebot_status,
    ),
    "get_friend_list": ActionMapping(
        "get_friend_list",
        field_map({"no_cache": "no_cache"}),
        list_from_key("friends", friend_entity),
    ),
    "get_stranger_info": ActionMapping(
        "get_friend_info",
        field_map({"user_id": "user_id", "no_cache": "no_cache"}),
        friend_entity,
    ),
    "get_group_list": ActionMapping(
        "get_group_list",
        field_map({"no_cache": "no_cache"}),
        list_from_key("groups", group_entity),
    ),
    "get_group_info": ActionMapping(
        "get_group_info",
        field_map({"group_id": "group_id", "no_cache": "no_cache"}),
        lambda data: group_entity(data.get("group", data)),
    ),
    "get_group_member_list": ActionMapping(
        "get_group_member_list",
        field_map({"group_id": "group_id", "no_cache": "no_cache"}),
        list_from_key("members", group_member_entity),
    ),
    "get_group_member_info": ActionMapping(
        "get_group_member_info",
        field_map(
            {"group_id": "group_id", "user_id": "user_id", "no_cache": "no_cache"}
        ),
        lambda data: group_member_entity(data.get("member", data)),
    ),
    "set_group_admin": ActionMapping(
        "set_group_member_admin",
        field_map({"group_id": "group_id", "user_id": "user_id", "enable": "is_set"}),
    ),
    "set_group_card": ActionMapping(
        "set_group_member_card",
        field_map(
            {"group_id": "group_id", "user_id": "user_id", "card": "card"}, {"card": ""}
        ),
    ),
    "set_group_ban": ActionMapping(
        "set_group_member_mute",
        field_map(
            {"group_id": "group_id", "user_id": "user_id", "duration": "duration"},
            {"duration": 0},
        ),
    ),
    "set_group_whole_ban": ActionMapping(
        "set_group_whole_mute",
        field_map({"group_id": "group_id", "enable": "is_mute"}, {"is_mute": True}),
    ),
    "set_group_name": ActionMapping(
        "set_group_name",
        field_map({"group_id": "group_id", "group_name": "new_group_name"}),
    ),
    "set_group_kick": ActionMapping(
        "kick_group_member",
        field_map(
            {
                "group_id": "group_id",
                "user_id": "user_id",
                "reject_add_request": "reject_add_request",
            },
            {"reject_add_request": False},
        ),
    ),
    "set_group_special_title": ActionMapping(
        "set_group_member_special_title",
        field_map(
            {
                "group_id": "group_id",
                "user_id": "user_id",
                "special_title": "special_title",
            },
            {"special_title": ""},
        ),
    ),
    "set_essence_msg": ActionMapping(
        "set_group_essence_message", lambda params: set_essence_params(params, True)
    ),
    "delete_essence_msg": ActionMapping(
        "set_group_essence_message", lambda params: set_essence_params(params, False)
    ),
    "send_like": ActionMapping(
        "send_profile_like",
        field_map({"user_id": "user_id", "times": "count"}, {"count": 1}),
    ),
    "friend_poke": ActionMapping(
        "send_friend_nudge", field_map({"user_id": "user_id"})
    ),
    "group_poke": ActionMapping(
        "send_group_nudge", field_map({"group_id": "group_id", "user_id": "user_id"})
    ),
    "send_poke": ActionMapping(send_poke_action, send_poke_params),
    "delete_friend": ActionMapping("delete_friend", field_map({"user_id": "user_id"})),
    "set_friend_add_request": ActionMapping(
        friend_request_action, friend_request_params
    ),
    "set_group_add_request": ActionMapping(group_request_action, group_request_params),
    "set_msg_emoji_like": ActionMapping(
        "send_group_message_reaction", group_reaction_params
    ),
    "unset_msg_emoji_like": ActionMapping(
        "send_group_message_reaction", unset_group_reaction_params
    ),
    "get_friend_msg_history": ActionMapping(
        "get_history_messages",
        history_params("friend", "user_id"),
        history_data,
        resolve_file_urls=True,
    ),
    "get_group_msg_history": ActionMapping(
        "get_history_messages",
        history_params("group", "group_id"),
        history_data,
        resolve_file_urls=True,
    ),
    "fetch_custom_face": ActionMapping(
        "get_custom_face_url_list", empty_params, lambda data: [data["urls"]]
    ),
}


async def transform_event_async(
    event: Json, file_url_resolver: FileUrlResolver | None = None
) -> Json | None:
    event_type = event["event_type"]
    data = event["data"]
    self_id: int = event["self_id"]
    event_time = event["time"]

    if event_type == "message_receive":
        MSG_STATS["received"] += 1
        MSG_STATS["last_message_time"] = event_time
        converted = await incoming_message_to_onebot_async(
            data, self_id=self_id, file_url_resolver=file_url_resolver
        )
        converted["time"] = event_time
        return converted
    if event_type == "message_recall":
        message_id = message_id_from_milky(
            data["message_scene"], data["peer_id"], data["message_seq"]
        )
        if data.get("message_scene") == "group":
            return {
                "time": event_time,
                "self_id": self_id,
                "post_type": "notice",
                "notice_type": "group_recall",
                "group_id": data["peer_id"],
                "user_id": data["sender_id"],
                "operator_id": data["operator_id"],
                "message_id": message_id,
                "display_suffix": data["display_suffix"],
            }
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "friend_recall",
            "user_id": data["sender_id"],
            "message_id": message_id,
            "display_suffix": data["display_suffix"],
        }
    if event_type == "friend_request":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "request",
            "request_type": "friend",
            "user_id": data["initiator_id"],
            "comment": data["comment"],
            "flag": data["initiator_uid"],
            "via": data["via"],
        }
    if event_type == "group_join_request":
        return group_request_event(
            event_time,
            self_id,
            "add",
            data,
            {
                "request_kind": "notification",
                "notification_seq": data["notification_seq"],
                "notification_type": "join_request",
                "group_id": data["group_id"],
                "is_filtered": data["is_filtered"],
            },
        )
    if event_type == "group_invite_request":
        return group_request_event(
            event_time,
            self_id,
            "invite",
            data,
            {
                "request_kind": "notification",
                "notification_seq": data["notification_seq"],
                "notification_type": "invited_join_request",
                "group_id": data["group_id"],
                "is_filtered": False,
            },
        )
    if event_type == "group_invitation":
        return group_request_event(
            event_time,
            self_id,
            "invite",
            data,
            {
                "request_kind": "invitation",
                "group_id": data["group_id"],
                "invitation_seq": data["invitation_seq"],
            },
        )
    if event_type == "friend_nudge":
        target_id = self_id if data["is_self_receive"] else data["user_id"]
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "notify",
            "sub_type": "poke",
            "user_id": data["user_id"],
            "target_id": target_id,
            "raw_info": f'<gtip align="center"> <qq uin="{data["user_id"]}" col="1" nm="" /> <img src="{data["display_action_img_url"]}"/> <nor txt="{data["display_action"]}"/> <qq uin="{target_id}" col="1" nm="" tp="0"/>  <nor txt="{data["display_suffix"]}"/> </gtip>',  # noqa: E501
        }
    if event_type == "group_nudge":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "notify",
            "sub_type": "poke",
            "group_id": data["group_id"],
            "user_id": data["sender_id"],
            "target_id": data["receiver_id"],
            "raw_info": f'<gtip align="center"> <qq uin="{data["sender_id"]}" col="1" nm="" /> <img src="{data["display_action_img_url"]}"/> <nor txt="{data["display_action"]}"/> <qq uin="{data["receiver_id"]}" col="1" nm="" tp="0"/>  <nor txt="{data["display_suffix"]}"/> </gtip>',  # noqa: E501
        }
    if event_type == "friend_file_upload":
        # HACK: Onebot 无事件, 这里按照理论格式写
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "friend_upload",
            "user_id": data["user_id"],
            "file": {
                "id": data["file_id"],
                "name": data["file_name"],
                "size": data["file_size"],
                "busid": 0,
            },
            "is_self": data["is_self"],
        }

    if event_type == "group_file_upload":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_upload",
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "file": {
                "id": data["file_id"],
                "name": data["file_name"],
                "size": data["file_size"],
                "busid": 0,
            },
        }
    if event_type == "group_admin_change":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_admin",
            "sub_type": "set" if data["is_set"] else "unset",
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "operator_id": data["operator_id"],
        }
    if event_type == "group_essence_message_change":
        message_id = message_id_from_milky(
            "group", data["group_id"], data["message_seq"]
        )
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "essence",
            "sub_type": "add" if data["is_set"] else "delete",
            "group_id": data["group_id"],
            "user_id": 0,  # TODO: Milky 未支持
            "sender_id": 0,
            "operator_id": data["operator_id"],
            "message_id": message_id,
        }
    if event_type == "group_member_increase":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_increase",
            "sub_type": "invite" if data.get("invitor_id") else "approve",
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "operator_id": data.get("operator_id") or data.get("invitor_id") or 0,
        }
    if event_type == "group_member_decrease":
        operator_id = data.get("operator_id", 0)
        if operator_id:
            sub_type = "kick_me" if data["user_id"] == self_id else "kick"
        else:
            sub_type = "leave"
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_decrease",
            "sub_type": sub_type,
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "operator_id": operator_id,
        }
    if event_type == "group_name_change":
        return None  # TODO: Milky 未支持群名片事件，Onebot 无群昵称事件
        # {
        #     "time": event_time,
        #     "self_id": self_id,
        #     "post_type": "notice",
        #     "notice_type": "group_card",
        #     "group_id": data.get("group_id"),
        #     "user_id": data.get("operator_id"),
        #     "card_new": data.get("card_new", ""),
        # }
    if event_type == "group_message_reaction":
        message_id = message_id_from_milky(
            "group", data["group_id"], data["message_seq"]
        )
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_msg_emoji_like",
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "message_id": message_id,
            "likes": [{"emoji_id": data["face_id"], "count": 1}],
            "is_add": data["is_add"],
        }
    if event_type == "group_mute":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_ban",
            "sub_type": "ban" if data["duration"] else "lift_ban",
            "group_id": data["group_id"],
            "user_id": data["user_id"],
            "operator_id": data["operator_id"],
            "duration": data["duration"],
        }
    if event_type == "group_whole_mute":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "group_ban",
            "sub_type": "ban" if data["is_mute"] else "lift_ban",
            "group_id": data["group_id"],
            "user_id": 0,
            "operator_id": data["operator_id"],
            "duration": -1 if data["is_mute"] else 0,
        }
    if event_type == "bot_offline":
        return {
            "time": event_time,
            "self_id": self_id,
            "post_type": "notice",
            "notice_type": "bot_offline",
            "reason": data["reason"],
            "user_id": self_id,
        }
    return None


def group_request_event(
    event_time: int,
    self_id: int,
    sub_type: str,
    data: Json,
    flag_payload: Json,
) -> Json:
    flag = encode_flag(flag_payload)
    return {
        "time": event_time,
        "self_id": self_id,
        "post_type": "request",
        "request_type": "group",
        "sub_type": sub_type,
        "comment": data["comment"],
        "flag": flag,
        "group_id": data["group_id"],
        "user_id": data.get("target_user_id") or data.get("initiator_id"),
        "invitor_id": data.get("initiator_id", 0),
        "source_group_id": data.get("source_group_id", 0),
    }
