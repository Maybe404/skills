"""归一化定义，逐字对应 docs/design.md 第 3 节 "normalized_sha256 的归一化定义"。

变换只在字节层面做。UTF-8 编码下 0x0D（\\r）和 0x0A（\\n）不会出现在任何
多字节序列的续字节里（续字节的最高位恒为 1），因此按字节做换行和行尾空白
处理，不需要先解码成文本。
"""
from __future__ import annotations

import hashlib

_TRAILING_WS = b" \t"


def normalize_bytes(raw: bytes) -> bytes:
    """把原始字节按四步归一化，返回归一化后的字节。

    1. 统一换行：\\r\\n 和单独的 \\r 都换成 \\n。
    2. 去掉每一行行尾的空格和制表符。
    3. 去掉文件末尾多余的空行。
    4. 非空文件保证以且仅以一个 \\n 结尾；空文件不补。
    """
    if not raw:
        return b""

    text = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    lines = [line.rstrip(_TRAILING_WS) for line in text.split(b"\n")]
    text = b"\n".join(lines)
    text = text.rstrip(b"\n")
    if not text:
        return b""
    return text + b"\n"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def raw_sha256(raw: bytes) -> str:
    return sha256_hex(raw)


def normalized_sha256(raw: bytes) -> str:
    return sha256_hex(normalize_bytes(raw))


def concat_raw(parts: list[bytes]) -> bytes:
    """来源级 raw_sha256 的拼接：按顺序逐个原始字节直接拼接，不插分隔符。"""
    return b"".join(parts)


def concat_normalized(parts: list[bytes]) -> bytes:
    """来源级 normalized_sha256 的拼接：按顺序逐个归一化后直接拼接。"""
    return b"".join(normalize_bytes(p) for p in parts)


def source_raw_sha256(parts: list[bytes]) -> str:
    return sha256_hex(concat_raw(parts))


def source_normalized_sha256(parts: list[bytes]) -> str:
    return sha256_hex(concat_normalized(parts))
