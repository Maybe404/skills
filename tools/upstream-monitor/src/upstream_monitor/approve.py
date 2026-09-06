"""`upstream-monitor approve` 的实现。

把 decisions.yaml 里 decision_origin 为 model-proposed 的条目改成
human-approved。--pr 给了 PR 号时只改该 PR diff 里出现的规则 id；--rule
给了具体 id 时只改这些；两者都不给时改全部 model-proposed。history 和
decided_at 不动——decision_origin 本身不是 decision，改它不算一次新的决定。
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.yamlio import dump_yaml, load_yaml


def rule_ids_from_pr_diff(diff_text: str) -> set[str]:
    """从一段 unified diff 的新增行里提取出现过的规则 id。"""
    ids: set[str] = set()
    for line in diff_text.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        for m in re.finditer(r"(ZH|EN|ALL)-[A-Z]{1,5}-\d{3}", line):
            ids.add(m.group(0))
    return ids


def fetch_pr_diff(root: Path, pr_number: int) -> str:
    out = subprocess.run(
        ["gh", "pr", "diff", str(pr_number)],
        cwd=str(root),
        capture_output=True,
        text=True,
        timeout=30,
        check=True,
    )
    return out.stdout


def approve_rules(decisions: dict, rule_ids: set[str] | None) -> tuple[dict, list[str]]:
    """返回 (更新后的 decisions 文档, 实际被改动的规则 id 列表)。不修改传入的对象。"""
    changed: list[str] = []
    new_rules = []
    for r in decisions["rules"]:
        r2 = dict(r)
        if r2["decision_origin"] == "model-proposed" and (rule_ids is None or r2["id"] in rule_ids):
            r2["decision_origin"] = "human-approved"
            changed.append(r2["id"])
        new_rules.append(r2)
    new_doc = dict(decisions)
    new_doc["rules"] = new_rules
    return new_doc, changed


def run_approve(
    paths: RepoPaths,
    merge_id: str,
    pr: int | None = None,
    rules: list[str] | None = None,
) -> list[str]:
    decisions_path = paths.decisions_yaml(merge_id)
    decisions = load_yaml(decisions_path)

    rule_ids: set[str] | None = None
    if rules:
        rule_ids = set(rules)
    elif pr is not None:
        diff_text = fetch_pr_diff(paths.root, pr)
        rule_ids = rule_ids_from_pr_diff(diff_text)

    new_doc, changed = approve_rules(decisions, rule_ids)
    if changed:
        validate_doc(paths.schemas_dir, "decisions", new_doc, target=str(decisions_path))
        dump_yaml(new_doc, decisions_path)
    return changed
