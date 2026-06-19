from typing import Literal


class UltimateSignedCompressor64:

    INT64_MIN = -9223372036854775808
    INT64_MAX = 9223372036854775807
    PEER_BITS = 40

    @classmethod
    def _to_signed_int64(cls, val: int) -> int:
        return (val + 2**63) % 2**64 - 2**63

    @classmethod
    def _to_unsigned_int64(cls, val: int) -> int:
        return val & 0xFFFFFFFFFFFFFFFF

    @classmethod
    def compress(
        cls,
        message_scene: Literal["group", "friend", "temp"],
        peer_id: int,
        message_seq: int,
    ) -> int:
        if peer_id < 0 or message_seq < 0:
            raise ValueError("ID 和 Seq 必须为正整数")

        if peer_id >= (1 << cls.PEER_BITS):
            raise ValueError(
                f"peer_id ({peer_id}) 超过 12 位 (最大支持 1.09万亿)"
            )

        if message_scene == "group":
            if message_seq >= (1 << 23):
                raise ValueError(
                    "group 场景下 message_seq 超过 838 万"
                )
            unsigned_res = (0 << 63) | (peer_id << 23) | message_seq

        elif message_scene in {"friend", "temp"}:
            if message_seq >= (1 << 22):
                raise ValueError(
                    f"{message_scene} 场景下 message_seq 超过 419 万"
                )

            scene_bit = 0 if message_scene == "friend" else 1
            unsigned_res = (1 << 63) | (scene_bit << 62) | (peer_id << 22) | message_seq
        else:
            raise ValueError(f"未知的场景: {message_scene}")

        return cls._to_signed_int64(unsigned_res)

    @classmethod
    def decompress(cls, compressed_int: int) -> dict:
        if not (cls.INT64_MIN <= compressed_int <= cls.INT64_MAX):
            raise ValueError("不合法的 int64 数字")

        u_val = cls._to_unsigned_int64(compressed_int)
        sign_bit = (u_val >> 63) & 1

        if sign_bit == 0:
            peer_id = (u_val >> 23) & 0xFFFFFFFFFF
            message_seq = u_val & 0x7FFFFF
            return {
                "message_scene": "group",
                "peer_id": peer_id,
                "message_seq": message_seq,
            }
        else:
            scene_bit = (u_val >> 62) & 1
            peer_id = (u_val >> 22) & 0xFFFFFFFFFF
            message_seq = u_val & 0x3FFFFF
            scene = "friend" if scene_bit == 0 else "temp"
            return {
                "message_scene": scene,
                "peer_id": peer_id,
                "message_seq": message_seq,
            }


if __name__ == "__main__":
    test_cases = [
        {"message_scene": "group", "peer_id": 99999999999, "message_seq": 8000000},
        {"message_scene": "friend", "peer_id": 555555555555, "message_seq": 4000000},
        {"message_scene": "temp", "peer_id": 12345678901, "message_seq": 100},
    ]

    for case in test_cases:
        code = UltimateSignedCompressor64.compress(**case)
        decoded = UltimateSignedCompressor64.decompress(code)

        print(
            f"scene: {case['message_scene']:<6} | peer_id: {case['peer_id']:<14} | int64: {code:<20}"
        )
        assert case == decoded
