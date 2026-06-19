# {
from typing import Literal

from msgspec import Struct

class MessageEvent(Struct):
    time: int
    self_id: int
    post_type: Literal["message", "message_sent"]
    message_id: int

#     "time": 1640995200,
#     "self_id": 123456789,
#     "post_type": "message",
#     "message_id": 0,
#     "message_seq": 0,
#     "real_id": 0,
#     "user_id": 0,
#     "group_id": 0,
#     "message_type": "private",
#     "sub_type": "friend",
#     "sender": {
#         "user_id": 0,
#         "nickname": "string",
#         "card": "string",
#         "sex": "male",
#         "age": 0,
#         "level": "string",
#         "role": "owner",
#         "title": "string",
#         "group_id": 0
#     },
#     "message": [
#         {
#             "type": "text",
#             "data": {
#                 "text": "string"
#             }
#         }
#     ],
#     "message_format": "array",
#     "raw_message": "string",
#     "font": 14,
#     "target_id": 0,
#     "temp_source": 0
# }