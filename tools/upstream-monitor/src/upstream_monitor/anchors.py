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


def locate(text: str, anchor: str) -> tuple[str, str]:
    """在 text 里定位 anchor。

    返回 (status, detail)，status 取值：
    ok-heading / ok-linestart / ok-substring / weak-heading / MISS。
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
            for sub in rest:
                target = sub.strip('"')
                if any(
                    strip_md(ln).startswith(sub) or strip_md(ln).startswith(target)
                    for ln in body
                ):
                    continue
                if any(target in ln for ln in body):
                    return "ok-substring", f"{how}; 子锚点 {sub!r} 只作为子串出现在小节内"
                break
            else:
                return (
                    "ok-linestart" if how == "heading-exact" else "weak-heading",
                    f"{how}; 子锚点均在行首",
                )
        return "MISS", f"小节 {head!r} 找到但子锚点 {rest} 定位不到"

    for ln in lines:
        if strip_md(ln).startswith(head):
            if not rest:
                return "ok-linestart", "行首文本"
            break
    if any(head in ln for ln in lines):
        return "ok-substring", "只作为子串出现，不在行首"
    return "MISS", f"行首文本找不到: {head!r}"


def count_occurrences(text: str, anchor: str) -> int:
    """local.anchor 校验用：anchor 在 text 里作为子串出现几次。"""
    return text.count(anchor)
