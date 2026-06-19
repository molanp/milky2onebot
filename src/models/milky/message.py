from __future__ import annotations
from typing import Literal

from msgspec import Struct


class TextSegmentData(Struct):
    text: str


class TextSegment(Struct):
    type: Literal["text"]
    data: TextSegmentData


class MentionSegmentData(Struct):
    user_id: int
    name: str


class MentionSegment(Struct):
    type: Literal["mention"]
    data: MentionSegmentData


class MentionAllSegment(Struct):
    type: Literal["mention_all"]


class FaceSegmentData(Struct):
    face_id: str
    is_large: bool


class FaceSegment(Struct):
    type: Literal["face"]
    data: FaceSegmentData


class ImageSegmentData(Struct):
    resource_id: str
    temp_url: str
    width: int
    height: int
    summary: str
    sub_type: Literal["normal", "sticker"]


class ImageSegment(Struct):
    type: Literal["image"]
    data: ImageSegmentData


class RecordSegmentData(Struct):
    resource_id: str
    temp_url: str
    duration: int


class RecordSegment(Struct):
    type: Literal["record"]
    data: RecordSegmentData


class VideoSegmentData(Struct):
    resource_id: str
    temp_url: str
    width: int
    height: int
    duration: int


class VideoSegment(Struct):
    type: Literal["video"]
    data: VideoSegmentData


class FileSegmentData(Struct):
    file_id: str
    file_name: str
    file_size: int
    file_hash: str | None = None


class FileSegment(Struct):
    type: Literal["file"]
    data: FileSegmentData


class ForwardSegmentData(Struct):
    forward_id: str
    title: str
    preview: list[str]
    summary: str


class ForwardSegment(Struct):
    type: Literal["forward"]
    data: ForwardSegmentData


class MarketFaceSegmentData(Struct):
    emoji_package_id: int
    emoji_id: int
    key: str
    summary: str
    url: str


class MarketFaceSegment(Struct):
    type: Literal["market_face"]
    data: MarketFaceSegmentData


class LightAppSegmentData(Struct):
    app_name: str
    json_payload: str


class LightAppSegment(Struct):
    type: Literal["light_app"]
    data: LightAppSegmentData


class XmlSegmentData(Struct):
    service_id: int
    xml_payload: str


class XmlSegment(Struct):
    type: Literal["xml"]
    data: XmlSegmentData


class ReplySegmentData(Struct):
    message_seq: int
    sender_id: int
    sender_name: str
    time: int
    segments: list[IncomingSegment]


class ReplySegment(Struct):
    type: Literal["reply"]
    data: ReplySegmentData


IncomingSegment = (
    TextSegment
    | MentionSegment
    | MentionAllSegment
    | FaceSegment
    | ImageSegment
    | RecordSegment
    | VideoSegment
    | FileSegment
    | ForwardSegment
    | MarketFaceSegment
    | LightAppSegment
    | XmlSegment
    | ReplySegment
)
