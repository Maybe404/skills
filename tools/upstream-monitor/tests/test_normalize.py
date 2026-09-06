"""归一化定义的四个用例：CRLF、行尾空白、末尾空行、末尾换行。"""
from upstream_monitor.normalize import normalize_bytes, normalized_sha256


def test_crlf_converted_to_lf():
    raw = b"line1\r\nline2\r\nline3\r\n"
    assert normalize_bytes(raw) == b"line1\nline2\nline3\n"


def test_lone_cr_converted_to_lf():
    raw = b"line1\rline2\r"
    assert normalize_bytes(raw) == b"line1\nline2\n"


def test_trailing_whitespace_stripped_per_line():
    raw = b"line1   \nline2\t\t\nline3\n"
    assert normalize_bytes(raw) == b"line1\nline2\nline3\n"


def test_inline_whitespace_not_touched():
    # 行内空白不动，只去行尾。
    raw = b"a  b\t c\n"
    assert normalize_bytes(raw) == b"a  b\t c\n"


def test_trailing_blank_lines_collapsed():
    raw = b"line1\n\n\n\n"
    assert normalize_bytes(raw) == b"line1\n"


def test_missing_trailing_newline_gets_one_added():
    raw = b"line1\nline2"
    assert normalize_bytes(raw) == b"line1\nline2\n"


def test_already_normalized_file_is_unchanged():
    raw = b"line1\nline2\n"
    assert normalize_bytes(raw) == raw


def test_empty_file_stays_empty():
    assert normalize_bytes(b"") == b""


def test_normalized_sha256_equal_across_crlf_and_lf_variants():
    a = b"line1\r\nline2   \r\nline3\r\n\r\n"
    b = b"line1\nline2\nline3\n"
    assert normalized_sha256(a) == normalized_sha256(b)
