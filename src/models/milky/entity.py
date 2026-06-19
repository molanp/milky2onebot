from typing import Literal

from msgspec import Struct


class FriendCategoryEntity(Struct):
    category_id: int
    category_name: str


class FriendEntity(Struct):
    user_id: int
    nickname: str
    sex: Literal["male", "female", "unknown"]
    qid: str
    remark: str
    category: FriendCategoryEntity


class GroupEntity(Struct):
    group_id: int
    group_name: str
    member_count: int
    max_member_count: int
    remark: str
    created_time: int
    description: str
    question: str
    announcement: str


class GroupMemberEntity(Struct):
    user_id: int
    nickname: str
    sex: Literal["male", "female", "unknown"]
    group_id: int
    card: str
    title: str
    level: int
    role: Literal["owner", "admin", "member"]
    join_time: int
    last_sent_time: int
    shut_up_end_time: int | None = None
