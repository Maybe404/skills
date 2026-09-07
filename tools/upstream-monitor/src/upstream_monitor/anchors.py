"""在 markdown 正文里定位 anchor。

anchor 的写法见 skills/skill-merge/references/extraction.md：小节标题原文，
或者稳定的行首文本；多级用 " / " 分隔。这里的实现从
tools/upstream-monitor/prototype/check_merge.py 移植，逻辑不变。
"""
from __future__ import annotations

import re

HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
QUOTE = re.compile(r"^\s*(?:>\s?)+")


def unquote_md(line: str) -> str:
    """去掉引用块的 `> ` 前缀。引用块里的标题仍然是标题。"""
    return QUOTE.sub("", line)


def heading_lines(lines: list[str]) -> dict[int, tuple[int, str]]:
    """返回 {行号: (层级, 标题文本)}，围栏代码块里的 # 行不算标题。"""
    out: dict[int, tuple[int, str]] = {}
    in_fence = False
    for i, ln in enumerate(lines):
        ln = unquote_md(ln)
        if FENCE.match(ln):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEAD.match(ln)
        if m:
            out[i] = (len(m.group(1)), m.group(2).strip())
    return out


def strip_md(line: str) -> str:
    """去掉行首的列表符号、序号、表格竖线和行内的强调标记。"""
    s = unquote_md(line).strip()
    s = re.sub(r"^[-*+]\s+", "", s)
    s = re.sub(r"^\d+\.\s+", "", s)
    s = re.sub(r"^\|\s*", "", s)
    return s.replace("**", "").replace("`", "").replace("*", "").strip()


def find_heading(heads: dict[int, tuple[int, str]], want: str) -> tuple[list[int], str]:
    w = want.lstrip("#").strip()
    exact = [i for i, (_, t) in heads.items() if t == w]
    if exact:
        return sorted(exact), "heading-exact"
    loose = [i for i, (_, t) in heads.items() if w in t]
    return sorted(loose), ("heading-contains" if loose else "none")


def section_bounds(heads: dict[int, tuple[int, str]], total: int, idx: int) -> tuple[int, int]:
    level = heads[idx][0]
    for j in sorted(heads):
        if j > idx and heads[j][0] <= level:
            return idx, j
    return idx, total


def _match_rest_in_scope(rest: list[str], scope: list[str], scope_desc: str) -> tuple[str, str] | None:
    """在 scope（若干行）内核对子锚点列表 rest。

    子锚点在 scope 里若都能在行首命中，返回 ("ok-linestart", ...)。
    第一个在行首命不中的子锚点，退而找它在 scope 内作为子串的命中次数：
    1 次记 ok-substring，大于 1 次记 ambiguous（指不清是哪一处）。
    这个子锚点在 scope 内连子串都找不到，返回 None，调用方按 MISS 处理。
    """
    for sub in rest:
        target = sub.strip('"')
        if any(strip_md(ln).startswith(sub) or strip_md(ln).startswith(target) for ln in scope):
            continue
        n = "\n".join(scope).count(target)
        if n == 0:
            return None
        if n == 1:
            return "ok-substring", f"子锚点 {sub!r} 只作为子串出现在{scope_desc}"
        return "ambiguous", f"子锚点 {sub!r} 在{scope_desc}出现 {n} 次，指不清是哪一处"
    return "ok-linestart", "子锚点均在行首"


def locate(text: str, anchor: str) -> tuple[str, str]:
    """在 text 里定位 anchor。

    返回 (status, detail)，status 取值：
    ok-heading / ok-linestart / ok-substring / weak-heading / ambiguous / MISS。
    ambiguous 表示弱定位（子串匹配）命中了不止一处，指不清是哪一处。
    """
    lines = text.splitlines()
    heads = heading_lines(lines)
    parts = [p.strip() for p in (anchor or "").split(" / ")]
    head, rest = parts[0], parts[1:]

    if head.startswith("#"):
        hits, how = find_heading(heads, head)
        if not hits:
            return "MISS", f"小节标题找不到: {head!r}"
        if not rest:
            return (
                "ok-heading" if how == "heading-exact" else "weak-heading",
                f"{how}, {len(hits)} 处",
            )
        for i in hits:
            a, b = section_bounds(heads, len(lines), i)
            body = lines[a:b]
            result = _match_rest_in_scope(rest, body, "小节内")
            if result is None:
                continue
            status, detail = result
            if status == "ok-linestart":
                return (
                    "ok-linestart" if how == "heading-exact" else "weak-heading",
                    f"{how}; {detail}",
                )
            return status, f"{how}; {detail}"
        return "MISS", f"小节 {head!r} 找到但子锚点 {rest} 定位不到"

    head_line_idx = None
    for i, ln in enumerate(lines):
        if strip_md(ln).startswith(head):
            head_line_idx = i
            break

    if head_line_idx is not None:
        if not rest:
            return "ok-linestart", "行首文本"
        result = _match_rest_in_scope(rest, [lines[head_line_idx]], "行内")
        if result is None:
            return "MISS", f"行首文本 {head!r} 找到但子锚点 {rest} 在该行内定位不到"
        return result

    n = count_occurrences(text, head)
    if n == 0:
        return "MISS", f"行首文本找不到: {head!r}"
    if n == 1:
        return "ok-substring", "只作为子串出现，不在行首"
    return "ambiguous", f"只作为子串出现 {n} 次，不在行首，指不清是哪一处"


def count_occurrences(text: str, anchor: str) -> int:
    """local.anchor 校验用：anchor 在 text 里作为子串出现几次。"""
    return text.count(anchor)
