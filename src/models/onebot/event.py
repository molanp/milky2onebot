from typing import Literal

from msgspec import Struct

from .message import IncomingSegment


class Event(Struct):
    time: int
    self_id: int
    post_type: Literal["message", "notice", "request", "meta_event"]


class Sender(Struct):
    user_id: int
    nickname: str
    card: str | None = None
    sex: Literal["male", "female", "unknown"] = "unknown"
    age: int = 0
    level: int = 0
    """群等级"""
    role: Literal["owner", "admin", "member"] = "member"
    title: str | None = None


class MessageEvent(Struct):
    message_id: int
    message_seq: int
    user_id: int
    message_type: Literal["private", "group"]
    sub_type: Literal["friend", "group", "normal"]
    sender: Sender
    message: list[IncomingSegment]
    post_type = "message"
    message_format: Literal["array"] = "array"
    raw_message: str = ""  # TODO: CQ码太麻烦了
    font: int = 14


class PrivateMessageEvent(MessageEvent):
    message_type = "private"


class GroupMessageEvent(MessageEvent):
    group_id: int = 0
    message_type = "group"


class NoticeEvent(Event):
    post_type = "notice"
    notice_type: str


class PokeEvent(NoticeEvent):
    notice_type = "notify"
    sub_type = "poke"
    user_id: int
    target_id: int
    group_id: int | None = None
    raw_info: str | None = None


class PokeRecallEvent(PokeEvent):
    sub_type = "poke_recall"


class FriendRecallNoticeEvent(NoticeEvent):
    notice_type = "friend_recall"
    user_id: int
    message_id: int


class RequestEvent(Event):
    post_type = "request"
    request_type: str


class FriendRequestEvent(RequestEvent):
    request_type = "friend"
    user_id: int
    comment: str
    flag: str
    via: str


class FriendAddNoticeEvent(NoticeEvent):
    notice_type = "friend_add"
    user_id: int


class ProfileLikeEvent(NoticeEvent):
    notice_type = "notify"
    sub_type = "profile_like"
    operator_id: int
    operator_nick: str
    times: int


class GroupUploadFile(Struct):
    id: str
    name: str
    size: int
    busid: int


class GroupUploadNoticeEvent(NoticeEvent):
    notice_type = "group_upload"
    group_id: int
    user_id: int
    file: GroupUploadFile


class GroupRequestEvent(RequestEvent):
    request_type = "group"
    sub_type: Literal["add", "invite"]
    comment: str
    flag: str
    group_id: int
    user_id: int
    invitor_id: int = 0
    source_group_id: int = 0


class GroupDismissEvent(NoticeEvent):
    notice_type = "group_dismiss"
    group_id: int
    user_id: int


class GroupIncreaseEvent(NoticeEvent):
    notice_type = "group_increase"
    sub_type: Literal["approve", "invite"]
    group_id: int
    user_id: int
    operator_id: int


class GroupDecreaseEvent(NoticeEvent):
    notice_type = "group_decrease"
    sub_type: Literal["leave", "kick", "kick_me"]
    group_id: int
    user_id: int
    operator_id: int


class GroupTitleEvent(NoticeEvent):
    notice_type = "notify"
    sub_type = "title"
    group_id: int
    user_id: int
    title: str


class GroupCardEvent(NoticeEvent):
    notice_type = "group_card"
    group_id: int
    user_id: int
    card_new: str
    card_old: str


class MsgEmojiLike(Struct):
    emoji_id: str
    count: int


class GroupMsgEmojiLikeEvent(NoticeEvent):
    notice_type = "group_msg_emoji_like"
    group_id: int
    user_id: int
    message_id: int
    likes: list[MsgEmojiLike]
    is_add: bool


class GroupRecallNoticeEvent(NoticeEvent):
    notice_type = "group_recall"
    group_id: int
    user_id: int
    operator_id: int
    message_id: int


class GroupAdminNoticeEvent(NoticeEvent):
    notice_type = "group_admin"
    sub_type: Literal["set", "unset"]
    group_id: int
    user_id: int


class GroupBanEvent(NoticeEvent):
    notice_type = "group_ban"
    sub_type: Literal["ban", "lift_ban"]
    group_id: int
    user_id: int
    """0表示全员"""
    operator_id: int
    duration: int
    """(s)-1为永久, 0为解禁"""


class EssenceEvent(NoticeEvent):
    notice_type = "essence"
    sub_type: Literal["add", "delete"]
    group_id: int
    user_id: int
    sender_id: int
    operator_id: int
    message_id: int


class MetaEvent(Event):
    post_type = "meta_event"
    meta_event_type: str


class HeartbeatEvent(MetaEvent):
    meta_event_type = "heartbeat"
    interval: int = 5000
    status: dict = {"online": True, "good": True}


class LifeCycleEvent(MetaEvent):
    meta_event_type = "lifecycle"
    sub_type: Literal["connect", "disable", "enable"] = "enable"
