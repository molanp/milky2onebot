from __future__ import annotations
from typing import Literal

from msgspec import Struct


class TextSegmentData(Struct):
    text: str


class TextSegment(Struct):
    type: Literal["text"]
    data: TextSegmentData


class ImageSegmentData(Struct):
    file: str
    url: str
    file_size: str | None = None
    summary: str | None = None
    subType: int | None = None
    type: Literal["flash", "show"] = "flash"
    thumb: str | None = None
    name: str | None = None


class ImageSegment(Struct):
    type: Literal["image"]
    data: ImageSegmentData


class VideoSegmentData(Struct):
    file: str
    url: str | None = None
    path: str | None = None
    file_size: str | None = None
    thumb: str | None = None
    name: str | None = None


class VideoSegment(Struct):
    type: Literal["video"]
    data: VideoSegmentData


class RecordSegmentData(Struct):
    file: str
    url: str | None = None
    path: str | None = None
    file_size: str | None = None
    thumb: str | None = None
    name: str | None = None


class RecordSegment(Struct):
    type: Literal["record"]
    data: RecordSegmentData


class FileSegmentData(Struct):
    file: str
    url: str | None = None
    path: str | None = None
    file_size: str | None = None
    file_id: str | None = None
    thumb: str | None = None
    name: str | None = None


class FileSegment(Struct):
    type: Literal["file"]
    data: FileSegmentData


class FlashFileSegmentData(Struct):
    title: str
    file_set_id: str
    scene_type: int


class FlashFileSegment(Struct):
    type: Literal["flash_file"]
    data: FlashFileSegmentData


class AtSegmentData(Struct):
    qq: Literal["all"] | int
    name: str | None = None


class AtSegment(Struct):
    type: Literal["at"]
    data: AtSegmentData


class ReplySegmentData(Struct):
    id: str


class ReplySegment(Struct):
    type: Literal["reply"]
    data: ReplySegmentData


class JsonSegmentData(Struct):
    data: str


class JsonSegment(Struct):
    type: Literal["json"]
    data: JsonSegmentData


class XmlSegmentData(Struct):
    data: str


class XmlSegment(Struct):
    type: Literal["xml"]
    data: XmlSegmentData


class FaceSegmentData(Struct):
    id: str


class FaceSegment(Struct):
    type: Literal["face"]
    data: FaceSegmentData


class MFaceSegmentData(Struct):
    emoji_package_id: int
    emoji_id: str
    key: str
    summary: str | None = None
    url: str | None = None


class MFaceSegment(Struct):
    type: Literal["mface"]
    data: MFaceSegmentData


class MarkdownSegmentData(Struct):
    content: str


class MarkdownSegment(Struct):
    type: Literal["markdown"]
    data: MarkdownSegmentData


class NodeSegmentData(Struct):
    id: int | str | None = None
    content: list[IncomingSegment] | None = None
    user_id: int | None = None
    nickname: str | None = None
    name: str | None = None
    uin: int | str | None = None


class NodeSegment(Struct):
    type: Literal["node"]
    data: NodeSegmentData


class ForwardSegmentData(Struct):
    id: str


class ForwardSegment(Struct):
    type: Literal["forward"]
    data: ForwardSegmentData


class MusicSegmentData(Struct):
    type: Literal["custom", "163", "qq", "xm"] | None = None
    id: str | None = None
    url: str | None = None
    audio: str | None = None
    title: str | None = None
    content: str | None = None
    image: str | None = None


class MusicSegment(Struct):
    type: Literal["music"]
    data: MusicSegmentData


class PokeSegmentData(Struct):
    qq: int | None = None
    id: int | None = None


class PokeSegment(Struct):
    type: Literal["poke"]
    data: PokeSegmentData


class DiceSegmentData(Struct):
    result: int | str
    """1-6"""


class DiceSegment(Struct):
    type: Literal["dice"]
    data: DiceSegmentData


class RpsSegmentData(Struct):
    result: Literal[1, 2, 3, "1", "2", "3"]
    """1=石头，2=剪刀，3=布"""


class RpsSegment(Struct):
    type: Literal["rps"]
    data: RpsSegmentData


class ContactSegmentData(Struct):
    type: Literal["qq", "group"]
    id: int


class ContactSegment(Struct):
    type: Literal["contact"]
    data: ContactSegmentData


class ShakeSegment(Struct):
    type: Literal["shake"]
    data: dict = {}


class KeyboardButtonRenderData(Struct):
    """按钮渲染数据"""

    label: str
    visited_label: str
    style: int


class KeyboardButtonPermission(Struct):
    """按钮权限设置"""

    type: int
    specify_role_ids: list[str]
    specify_user_ids: list[str]


class KeyboardButtonAction(Struct):
    """按钮动作配置"""

    type: int
    permission: KeyboardButtonPermission
    unsupport_tips: str
    data: str
    reply: bool
    enter: bool


class KeyboardButton(Struct):
    """单个按钮"""

    id: str
    render_data: KeyboardButtonRenderData
    action: KeyboardButtonAction


class KeyboardRow(Struct):
    """一行按钮"""

    buttons: list[KeyboardButton]


class KeyboardSegmentData(Struct):
    """键盘数据"""

    rows: list[KeyboardRow]


class KeyboardSegment(Struct):
    type: Literal["keyboard"]
    data: KeyboardSegmentData


IncomingSegment = (
    TextSegment
    | ImageSegment
    | VideoSegment
    | RecordSegment
    | FileSegment
    | FlashFileSegment
    | AtSegment
    | ReplySegment
    | JsonSegment
    | XmlSegment
    | FaceSegment
    | MFaceSegment
    | MarkdownSegment
    | NodeSegment
    | ForwardSegment
    | MusicSegment
    | PokeSegment
    | DiceSegment
    | RpsSegment
    | ContactSegment
    | ShakeSegment
    | KeyboardSegment
)
