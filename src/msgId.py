from typing import ClassVar, Literal


class UltimateSignedCompressor:
    FIELD_BITS = 64
    MAX_FIELD = (1 << FIELD_BITS) - 1
    LENGTH_BASE = FIELD_BITS + 1
    SCENE_COUNT = 3

    SCENE_TO_INT: ClassVar[dict[str, int]] = {
        "group": 0,
        "friend": 1,
        "temp": 2,
    }
    INT_TO_SCENE: ClassVar[dict[int, str]] = {v: k for k, v in SCENE_TO_INT.items()}

    @classmethod
    def compress(
        cls,
        message_scene: Literal["group", "friend", "temp"],
        peer_id: int,
        message_seq: int,
    ) -> int:
        try:
            scene_val = cls.SCENE_TO_INT[message_scene]
        except KeyError as e:
            raise ValueError(f"未知的场景: {message_scene}") from e
        if type(peer_id) is not int or type(message_seq) is not int:
            raise ValueError("peer_id 和 message_seq 必须为整数")
        if peer_id < 0 or message_seq < 0:
            raise ValueError("peer_id 和 message_seq 必须为非负整数")

        if peer_id > cls.MAX_FIELD:
            raise ValueError(f"peer_id 超过 {cls.FIELD_BITS} 位上限: {peer_id}")
        if message_seq > cls.MAX_FIELD:
            raise ValueError(f"message_seq 超过 {cls.FIELD_BITS} 位上限: {message_seq}")

        seq_bits = message_seq.bit_length()
        if scene_val == 0:
            use_compact = peer_id != 0 and seq_bits < 56
        else:
            packed_bits = peer_id.bit_length() + seq_bits if peer_id else seq_bits
            use_compact = packed_bits < 120 + scene_val

        if use_compact:
            packed_fields = (peer_id << seq_bits) | message_seq
            body = packed_fields * cls.LENGTH_BASE + seq_bits
            return -(body * cls.SCENE_COUNT + scene_val + 1)

        return (
            (scene_val << (2 * cls.FIELD_BITS))
            | (peer_id << cls.FIELD_BITS)
            | message_seq
        )

    @classmethod
    def decompress(cls, compressed_int: int) -> dict:
        if type(compressed_int) is not int:
            raise ValueError("compressed_int 必须为整数")

        if compressed_int < 0:
            return cls._decompress_compact(compressed_int)

        message_seq = compressed_int & cls.MAX_FIELD
        tmp = compressed_int >> cls.FIELD_BITS
        peer_id = tmp & cls.MAX_FIELD
        scene_val = tmp >> cls.FIELD_BITS

        if scene_val not in cls.INT_TO_SCENE:
            raise ValueError(f"compressed_int 中场景值未知: {scene_val}")

        return {
            "message_scene": cls.INT_TO_SCENE[scene_val],
            "peer_id": peer_id,
            "message_seq": message_seq,
        }

    @classmethod
    def _decompress_compact(cls, compressed_int: int) -> dict:
        payload = -compressed_int - 1
        body, scene_val = divmod(payload, cls.SCENE_COUNT)
        packed_fields, seq_bits = divmod(body, cls.LENGTH_BASE)

        if scene_val not in cls.INT_TO_SCENE or seq_bits > cls.FIELD_BITS:
            raise ValueError("compressed_int 中包含无效的紧凑编码")

        seq_mask = (1 << seq_bits) - 1
        message_seq = packed_fields & seq_mask
        peer_id = packed_fields >> seq_bits
        if (
            message_seq.bit_length() != seq_bits
            or peer_id > cls.MAX_FIELD
            or message_seq > cls.MAX_FIELD
        ):
            raise ValueError("compressed_int 中包含无效的紧凑编码")

        return {
            "message_scene": cls.INT_TO_SCENE[scene_val],
            "peer_id": peer_id,
            "message_seq": message_seq,
        }


if __name__ == "__main__":
    test_cases = [
        {
            "message_scene": "group",
            "peer_id": 9999999999999999999,
            "message_seq": 8000000000000000000,
        },
        {
            "message_scene": "friend",
            "peer_id": 5555555555555555555,
            "message_seq": 4000000000000000000,
        },
        {
            "message_scene": "temp",
            "peer_id": 1234567890123456789,
            "message_seq": 987654321098765432,
        },
        {"message_scene": "group", "peer_id": 999999999999, "message_seq": 8000000},
    ]

    for case in test_cases:
        code = UltimateSignedCompressor.compress(**case)
        decoded = UltimateSignedCompressor.decompress(code)
        assert case == decoded
