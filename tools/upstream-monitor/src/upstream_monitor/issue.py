"""`upstream-monitor issue` 的实现。

按 docs/design.md 第 6 节，issue 只用于六种情形：新候选上游
（new-candidate）、上游不可达或消失或转私有（source-unavailable）、许可证
变化（license-changed）、历史被重写（history-rewritten）、sync 后仍不确定
或涉及冲突/许可证（needs-decision）、removed 来源影响唯一来源规则
（retire-impact）。正文只放 source_id、repository、path、commit、hash、
stars、影响范围（needs-decision、retire-impact 时附 locate/retire 的输出）、
要做的决定，不放任何上游原文。

GitHub 访问和 pr.py、approve.py 一样只在真正执行时才发起子进程；这里额外
把 gh 相关调用收进一个可注入的 GhIssueClient 接口（对应
upstream_monitor.github_client.GitHubClient 的做法），测试用 FakeGhIssueClient
注入固定状态，不发真实 gh 调用。

幂等：lock 的 open_issue 非空、且该 issue 仍处于 open 状态时不重复开，只
返回已有编号；开成功后把 open_issue 写回 lock。--dry-run 只渲染并返回正文，
不读 open_issue 状态、不建标签、不开 issue、不写 lock。
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Protocol

from upstream_monitor.check import _blank_lock_entry
from upstream_monitor.locate import render_locate_markdown, rules_for_source
from upstream_monitor.paths import RepoPaths
from upstream_monitor.retire import render_retire_markdown, rules_only_supported_by
from upstream_monitor.schemas import validate_doc
from upstream_monitor.yamlio import dump_json, load_json, load_yaml

ISSUE_KINDS = (
    "source-unavailable",
    "license-changed",
    "history-rewritten",
    "needs-decision",
    "retire-impact",
    "new-candidate",
)

DEFAULT_DECISION_HINT = {
    "source-unavailable": "上游仓库、分支或追踪文件不可达、已删除或转为私有，"
    "需要决定是继续等待、找替代来源，还是 retire。",
    "license-changed": "GitHub 报告的许可证与 sources.yaml 记录的不一致，"
    "需要决定是否继续追踪、是否要把 snapshot_policy 改成 metadata-only，还是 retire。",
    "history-rewritten": "上游历史被重写（例如 force-push），"
    "需要决定是否重设基线并记录 baseline_reset_reason。",
    "needs-decision": "sync 后仍不确定、或涉及冲突或许可证的规则需要人工裁决，见下方受影响规则。",
    "retire-impact": "来源已 retire，以下规则目前只由它支持，需要决定是否跟着撤下。",
    "new-candidate": "发现新的候选上游，需要决定是否登记为 active 来源，以及 selection_status。",
}


class GhIssueClient(Protocol):
    """issue 命令依赖的最小 gh 接口。"""

    def list_labels(self) -> set[str]:
        """返回仓库现有的全部标签名。"""
        ...

    def create_label(self, label: str) -> None:
        """创建一个标签。"""
        ...

    def create_issue(self, title: str, body: str, labels: list[str]) -> int:
        """开一个 issue，返回编号。"""
        ...

    def get_issue_state(self, number: int) -> str:
        """返回 issue 当前状态，"OPEN" 或 "CLOSED"。"""
        ...


class RealGhIssueClient:
    """用 gh CLI 子进程实现，正文只经临时文件传递，不拼进 shell 命令行。"""

    def __init__(self, root: Path):
        self.root = root

    def _run(self, cmd: list[str]) -> subprocess.CompletedProcess:
        return subprocess.run(cmd, cwd=str(self.root), capture_output=True, text=True, check=True)

    def list_labels(self) -> set[str]:
        import json

        out = self._run(["gh", "label", "list", "--json", "name", "--limit", "1000"])
        return {item["name"] for item in json.loads(out.stdout)}

    def create_label(self, label: str) -> None:
        self._run(["gh", "label", "create", label, "--color", "ededed", "--force"])

    def create_issue(self, title: str, body: str, labels: list[str]) -> int:
        body_file = self.root / ".upstream-monitor-issue-body.md"
        body_file.write_text(body, encoding="utf-8")
        cmd = ["gh", "issue", "create", "--title", title, "--body-file", str(body_file)]
        for label in labels:
            cmd += ["--label", label]
        try:
            out = self._run(cmd)
        finally:
            body_file.unlink(missing_ok=True)
        m = re.search(r"/issues/(\d+)", out.stdout)
        if not m:
            raise RuntimeError(f"gh issue create 输出里没有找到 issue 编号: {out.stdout!r}")
        return int(m.group(1))

    def get_issue_state(self, number: int) -> str:
        out = self._run(["gh", "issue", "view", str(number), "--json", "state", "--jq", ".state"])
        return out.stdout.strip()


class FakeGhIssueClient:
    """测试用的固定状态客户端，不发真实 gh 调用。

    labels：预置的已存在标签集合。issues：{编号: "OPEN"|"CLOSED"} 的初始状态。
    created_issues / created_labels 记录本次调用实际发生的动作，供断言。
    """

    def __init__(self, labels: set[str] | None = None, issues: dict[int, str] | None = None):
        self.labels = set(labels or set())
        self.issues = dict(issues or {})
        self.created_issues: list[dict] = []
        self.created_labels: list[str] = []
        self._next_number = max(self.issues.keys(), default=0) + 1

    def list_labels(self) -> set[str]:
        return set(self.labels)

    def create_label(self, label: str) -> None:
        self.labels.add(label)
        self.created_labels.append(label)

    def create_issue(self, title: str, body: str, labels: list[str]) -> int:
        number = self._next_number
        self._next_number += 1
        self.issues[number] = "OPEN"
        self.created_issues.append({"number": number, "title": title, "body": body, "labels": list(labels)})
        return number

    def get_issue_state(self, number: int) -> str:
        return self.issues.get(number, "CLOSED")


def render_issue_title(kind: str, merge_id: str, source_id: str) -> str:
    return f"[{kind}] {merge_id}: {source_id}"


def render_issue_body(
    kind: str,
    merge_id: str,
    source: dict,
    entry: dict | None,
    extra_md: str | None,
    detail: str | None,
) -> str:
    entry = entry or {}
    lines: list[str] = [f"# {kind}: {merge_id} / {source['id']}", ""]

    lines.append("## 事实")
    lines.append("")
    lines.append(f"- source_id: {source['id']}")
    lines.append(f"- repository: {source.get('repository') or '（无）'}")
    paths_list = source.get("paths") or []
    lines.append(f"- path: {', '.join(paths_list) if paths_list else '（无）'}")
    lines.append(f"- commit: {entry.get('last_seen_commit') or '未知'}")
    lines.append(
        f"- hash: raw_sha256={entry.get('raw_sha256') or '未知'}, "
        f"normalized_sha256={entry.get('normalized_sha256') or '未知'}"
    )
    stars_hist = entry.get("stars_history") or []
    stars = stars_hist[-1]["value"] if stars_hist else "未知"
    lines.append(f"- stars: {stars}")
    lines.append("")

    lines.append("## 影响范围")
    lines.append("")
    lines.append(extra_md if extra_md else "（本情形不附受影响规则清单，见下方「要做的决定」。）")
    lines.append("")

    lines.append("## 要做的决定")
    lines.append("")
    lines.append(detail or DEFAULT_DECISION_HINT[kind])
    lines.append("")
    return "\n".join(lines)


def _extra_markdown_for_kind(paths: RepoPaths, merge_id: str, source_id: str, kind: str) -> str | None:
    if kind == "needs-decision":
        decisions = load_yaml(paths.decisions_yaml(merge_id))
        candidate_rules = rules_for_source(decisions, source_id)
        return render_locate_markdown(merge_id, source_id, candidate_rules, decisions["rules"], None)
    if kind == "retire-impact":
        decisions = load_yaml(paths.decisions_yaml(merge_id))
        affected = rules_only_supported_by(decisions, source_id)
        return render_retire_markdown(merge_id, source_id, affected)
    return None


def run_issue(
    paths: RepoPaths,
    client: GhIssueClient,
    merge_id: str,
    source_id: str,
    kind: str,
    detail: str | None = None,
    dry_run: bool = False,
) -> dict:
    """返回一个结果字典，字段视是否幂等短路、是否 dry_run 而不同。"""
    if kind not in ISSUE_KINDS:
        raise ValueError(f"未知的 issue kind: {kind!r}，必须是 {ISSUE_KINDS} 之一")

    sources_path = paths.sources_yaml(merge_id)
    S = load_yaml(sources_path)
    source = next((s for s in S["sources"] if s["id"] == source_id), None)
    if source is None:
        raise KeyError(f"{merge_id}: 找不到来源 {source_id}")

    lock_path = paths.lock_json(merge_id)
    L = load_json(lock_path)
    entry = L["sources"].get(source_id)

    extra_md = _extra_markdown_for_kind(paths, merge_id, source_id, kind)
    title = render_issue_title(kind, merge_id, source_id)
    body = render_issue_body(kind, merge_id, source, entry, extra_md, detail)
    labels = [f"upstream:{merge_id}", kind]

    if dry_run:
        return {"dry_run": True, "idempotent": False, "title": title, "body": body, "labels": labels}

    if entry and entry.get("open_issue") and client.get_issue_state(entry["open_issue"]) == "OPEN":
        return {
            "idempotent": True,
            "issue_number": entry["open_issue"],
            "message": f"来源 {source_id} 已经开着 issue #{entry['open_issue']}（{kind}），不重复开。",
        }

    existing_labels = client.list_labels()
    for label in labels:
        if label not in existing_labels:
            client.create_label(label)

    issue_number = client.create_issue(title, body, labels)

    new_entry = dict(entry) if entry else _blank_lock_entry()
    new_entry["open_issue"] = issue_number
    L2 = dict(L)
    L2["sources"] = dict(L["sources"])
    L2["sources"][source_id] = new_entry
    validate_doc(paths.schemas_dir, "lock", L2, target=str(lock_path))
    dump_json(L2, lock_path)

    return {
        "idempotent": False,
        "issue_number": issue_number,
        "title": title,
        "body": body,
        "labels": labels,
    }
