"""`upstream-monitor report new` 的实现。

按 merges/<id>/reports/ 里最大的四位序号加一，生成一份空壳报告文件，
章节固定为 skills/skill-merge/references/templates/report.md 里的十节。
代码只搭骨架，内容由 skill-merge 填充。
"""
from __future__ import annotations

import datetime
import re
from pathlib import Path

from upstream_monitor.paths import RepoPaths

REPORT_NAME_RE = re.compile(r"^(\d{4})-\d{4}-\d{2}-\d{2}-.+\.md$")

SECTION_TITLES = [
    "1 范围",
    "2 来源清单",
    "3 统计",
    "4 覆盖矩阵",
    "5 冲突与取舍",
    "6 被拒绝规则与理由",
    "7 影响的本地文件",
    "8 如何验证",
    "9 如何回滚",
    "10 未解决问题",
]


def next_report_number(reports_dir: Path) -> int:
    if not reports_dir.is_dir():
        return 1
    nums = []
    for p in reports_dir.glob("*.md"):
        m = REPORT_NAME_RE.match(p.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def render_report_skeleton(merge_id: str, number: int, slug: str, date: str) -> str:
    lines = [
        f"# {merge_id} 合并报告 {number:04d}",
        "",
        f"日期：{date}",
        "模式：（待填写：merge 或 sync）",
        "触发：（待填写：首次合并 / PR #<号> / locate 输出）",
        "",
    ]
    for title in SECTION_TITLES:
        lines.append(f"## {title}")
        lines.append("")
        lines.append("无")
        lines.append("")
    return "\n".join(lines)


def run_report_new(paths: RepoPaths, merge_id: str, slug: str) -> Path:
    reports_dir = paths.reports_dir(merge_id)
    reports_dir.mkdir(parents=True, exist_ok=True)
    number = next_report_number(reports_dir)
    date = datetime.date.today().isoformat()
    filename = f"{number:04d}-{date}-{slug}.md"
    target = reports_dir / filename
    target.write_text(render_report_skeleton(merge_id, number, slug, date), encoding="utf-8")
    return target
