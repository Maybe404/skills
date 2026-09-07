"""校验类命令共用的问题收集器：按严重程度分组，BLOCK/HIGH 视为失败。"""
from __future__ import annotations

import collections

SEVERITIES = ("BLOCK", "HIGH", "MED", "LOW")
FAIL_ON = {"BLOCK", "HIGH"}


class Report:
    def __init__(self) -> None:
        self.problems: list[tuple[str, str]] = []
        self.oks: list[str] = []

    def add(self, severity: str, message: str) -> None:
        assert severity in SEVERITIES, severity
        self.problems.append((severity, message))

    def ok(self, message: str) -> None:
        self.oks.append(message)

    def by_severity(self) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {s: [] for s in SEVERITIES}
        for sev, msg in self.problems:
            out[sev].append(msg)
        return out

    def counts(self) -> dict[str, int]:
        c = collections.Counter(s for s, _ in self.problems)
        return {s: c.get(s, 0) for s in SEVERITIES}

    def failed(self) -> bool:
        return any(self.counts()[s] for s in FAIL_ON)

    def exit_code(self) -> int:
        return 1 if self.failed() else 0

    def render_text(self) -> str:
        lines: list[str] = []
        grouped = self.by_severity()
        for sev in SEVERITIES:
            msgs = grouped[sev]
            if not msgs:
                continue
            lines.append(f"== {sev} ({len(msgs)}) ==")
            for m in msgs:
                lines.append(f"[{sev}] {m}")
        if not self.problems:
            lines.append("没有发现问题。")
        lines.append("")
        lines.append(f"问题汇总: {self.counts()}")
        return "\n".join(lines)
