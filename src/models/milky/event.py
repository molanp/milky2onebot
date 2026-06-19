from typing import Any, Literal

from msgspec import Struct
from .message import IncomingSegment
from .entity import FriendEntity, GroupEntity, GroupMemberEntity


class Event(Struct):
    event_type: Any
    time: int
    self_id: int
    data: Any


class BotOfflineData(Struct):
    reason: str


class BotOfflineEvent(Event):
    event_type: Literal["bot_offline"]
    data: BotOfflineData


class FriendMessageData(Struct):
    message_scene: Literal["friend"]
    peer_id: int
    message_seq: int
    sender_id: int
    time: int
    segments: list[IncomingSegment]
    friend: FriendEntity


class GroupMessageData(Struct):
    message_scene: Literal["group"]
    peer_id: int
    message_seq: int
    sender_id: int
    time: int
    segments: list[IncomingSegment]
    group: GroupEntity
    group_member: GroupMemberEntity


class TempMessageData(Struct):
    message_scene: Literal["temp"]
    peer_id: int
    message_seq: int
    sender_id: int
    time: int
    segments: list[IncomingSegment]
    group: GroupEntity | None = None


class MessageReceiveEvent(Event):
    event_type: Literal["message_receive"]
    data: FriendMessageData | GroupMessageData | TempMessageData


class MessageRecallData(Struct):
    message_scene: Literal["friend", "group", "temp"]
    peer_id: int
    message_seq: int
    sender_id: int
    operator_id: int
    display_suffix: str


class MessageRecallEvent(Event):
    type: Literal["message_recall"]
    data: MessageRecallData


class PeerPinChangeData(Struct):
    message_scene: Literal["friend", "group", "temp"]
    peer_id: int
    is_pinned: bool


class PeerPinChangeEvent(Event):
    type: Literal["peer_pin_change"]
    data: PeerPinChangeData


class FriendRequestData(Struct):
    initiator_id: int
    initiator_uid: str
    comment: str
    via: str


class FriendRequestEvent(Event):
    type: Literal["friend_request"]
    data: FriendRequestData


class GroupJoinRequestData(Struct):
    group_id: int
    notification_seq: int
    is_filtered: bool
    initiator_id: int
    comment: str


class GroupJoinRequestEvent(Event):
    type: Literal["group_join_request"]
    data: GroupJoinRequestData


class GroupInviteRequestData(Struct):
    group_id: int
    notification_seq: int
    inviter_id: int
    target_user_id: int


class GroupInviteRequestEvent(Event):
    type: Literal["group_invite_request"]
    data: GroupInviteRequestData


class GroupInvitationData(Struct):
    group_id: int
    invitation_seq: int
    initiator_id: int
    source_group_id: int | None = None


class GroupInvitationEvent(Event):
    type: Literal["group_invitation"]
    data: GroupInvitationData


class FriendNudgeData(Struct):
    user_id: int
    is_self_send: bool
    is_self_receive: bool
    display_action: str
    display_suffix: str
    display_action_img_url: str


class FriendNudgeEvent(Event):
    type: Literal["friend_nudge"]
    data: FriendNudgeData


class FriendFileUploadData(Struct):
    user_id: int
    file_id: str
    file_name: str
    file_size: int
    file_hash: str
    is_self: bool


class FriendFileUploadEvent(Event):
    type: Literal["friend_file_upload"]
    data: FriendFileUploadData


class GroupAdminChangeData(Struct):
    group_id: int
    user_id: int
    operator_id: int
    is_set: bool


class GroupAdminChangeEvent(Event):
    type: Literal["group_admin_change"]
    data: GroupAdminChangeData


class GroupEssenceMessageChangeData(Struct):
    group_id: int
    message_seq: int
    operator_id: int
    is_set: bool


class GroupEssenceMessageChangeEvent(Event):
    type: Literal["group_essence_message_change"]
    data: GroupEssenceMessageChangeData


class GroupMemberIncreaseData(Struct):
    group_id: int
    user_id: int
    operator_id: int | None = None
    invitor_id: int | None = None


class GroupMemberIncreaseEvent(Event):
    type: Literal["group_member_increase"]
    data: GroupMemberIncreaseData


class GroupMemberDecreaseData(Struct):
    group_id: int
    user_id: int
    operator_id: int | None = None


class GroupMemberDecreaseEvent(Event):
    type: Literal["group_member_decrease"]
    data: GroupMemberDecreaseData


class GroupNameChangeData(Struct):
    group_id: int
    new_group_name: str
    operator_id: int


class GroupNameChangeEvent(Event):
    type: Literal["group_name_change"]
    data: GroupNameChangeData


class GroupMessageReactionData(Struct):
    group_id: int
    user_id: int
    message_seq: int
    face_id: str
    reaction_type: Literal["add", "remove"]
    is_add: bool


class GroupMessageReactionEvent(Event):
    type: Literal["group_message_reaction"]
    data: GroupMessageReactionData


class GroupMuteData(Struct):
    group_id: int
    user_id: int
    operator_id: int
    duration: int


class GroupMuteEvent(Event):
    type: Literal["group_mute"]
    data: GroupMuteData


class GroupWholeMuteData(Struct):
    group_id: int
    operator_id: int
    is_mute: bool


class GroupWholeMuteEvent(Event):
    type: Literal["group_whole_mute"]
    data: GroupWholeMuteData


class GroupNudgeData(Struct):
    group_id: int
    sender_id: int
    receiver_id: int
    display_action: str
    display_suffix: str
    display_action_img_url: str


class GroupNudgeEvent(Event):
    type: Literal["group_nudge"]
    data: GroupNudgeData


class GroupFileUploadData(Struct):
    group_id: int
    user_id: int
    file_id: str
    file_name: str
    file_size: int


class GroupFileUploadEvent(Event):
    type: Literal["group_file_upload"]
    data: GroupFileUploadData
