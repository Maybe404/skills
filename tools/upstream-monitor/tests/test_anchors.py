"""anchors.locate 的子锚点定位和弱定位歧义测试。

覆盖两处修复：
1. 非小节标题的 anchor（纯行首文本）带子锚点时，子锚点必须真的核对到，
   胡说的子锚点要 MISS，而不是退化成只核对 head 的子串匹配。
2. 弱定位（子串匹配）命中不止一处时要报 ambiguous，而不是和只命中一次
   的 ok-substring 混在一起。
"""
from upstream_monitor.anchors import locate

HEADING_DOC_SINGLE = """# Doc

## Pattern table

The word delve appears here as a plain example of overused word choice.
"""

HEADING_DOC_REPEATED = """# Doc

## Pattern table

The word delve appears here as a plain example of overused word choice: delve.
"""

LINE_DOC = """# Doc

Stable lead text for the paragraph starts here and continues with extra detail A on the same line.
"""

SUBSTRING_DOC_SINGLE = """# Doc

Only one mention of the unique phrase for testing here.
"""

SUBSTRING_DOC_REPEATED = """# Doc

Somewhere mid-sentence we mention the shared phrase for testing.
Another paragraph again mentions the shared phrase for testing here too.
"""


def test_heading_sub_anchor_nonsense_is_miss():
    status, detail = locate(HEADING_DOC_SINGLE, "## Pattern table / 这段完全瞎编的内容在原文里没有")
    assert status == "MISS"
    assert "子锚点" in detail


def test_line_start_sub_anchor_nonsense_is_miss():
    """回归：修复前，非小节标题分支在 rest 非空时直接 break，
    根本不核对子锚点，胡说的子锚点也能返回 ok-substring。"""
    status, detail = locate(
        LINE_DOC, "Stable lead text for the paragraph starts here / 这段胡说的子锚点在原文里不存在"
    )
    assert status == "MISS"
    assert "子锚点" in detail


def test_line_start_sub_anchor_real_substring_is_ok():
    status, detail = locate(
        LINE_DOC, "Stable lead text for the paragraph starts here / extra detail A"
    )
    assert status == "ok-substring"


def test_heading_sub_anchor_single_hit_is_ok_substring():
    status, detail = locate(HEADING_DOC_SINGLE, "## Pattern table / delve")
    assert status == "ok-substring"


def test_heading_sub_anchor_repeated_hit_is_ambiguous():
    status, detail = locate(HEADING_DOC_REPEATED, "## Pattern table / delve")
    assert status == "ambiguous"
    assert "2" in detail


def test_plain_head_single_substring_hit_is_ok_substring():
    status, detail = locate(SUBSTRING_DOC_SINGLE, "the unique phrase for testing")
    assert status == "ok-substring"


def test_plain_head_repeated_substring_hit_is_ambiguous():
    status, detail = locate(SUBSTRING_DOC_REPEATED, "the shared phrase for testing")
    assert status == "ambiguous"
    assert "2" in detail
