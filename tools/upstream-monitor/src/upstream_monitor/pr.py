"""`upstream-monitor pr` 的实现。

按 skills/skill-merge/references/templates/pr-body.md 的结构生成 PR 正文，
创建分支、写快照或只更新 lock、提交、用 `gh pr create` 开 PR。

幂等键 `source_id:path:commit`：path 段在来源只追踪一个文件时就是那个路径，
追踪多个文件时用逗号拼接（schema 只要求不含冒号，没有规定多路径怎么表示，
这是本实现的约定）。同一个键、且 lock 里 open_pr 非空时不重复开 PR。

真正执行 git / gh 的部分只在 dry_run=False 时跑；dry_run（含幂等短路）
不发起任何子进程，方便离线测试。
"""
from __future__ import annotations

import datetime
import re
import subprocess
from pathlib import Path

from upstream_monitor.diff import run_diff
from upstream_monitor.github_client import GitHubClient
from upstream_monitor.locate import render_locate_markdown, rules_for_source
from upstream_monitor.paths import RepoPaths
from upstream_monitor.schemas import validate_doc
from upstream_monitor.snapshot import snapshot_one_source
from upstream_monitor.yamlio import dump_json, load_json, load_yaml

DECISION_STRENGTH = [
    "adopted",
    "adopted-with-modification",
    "duplicate",
    "rejected",
    "deferred",
    "reference-only",
    "unverified",
    "retired",
]


def change_key_for(source_id: str, paths_list: list[str], commit: str) -> str:
    path_field = paths_list[0] if len(paths_list) == 1 else ",".join(paths_list)
    return f"{source_id}:{path_field}:{commit}"


def strongest_decision(decisions: list[str]) -> str:
    for d in DECISION_STRENGTH:
        if d in decisions:
            return d
    return "rejected"


def render_pr_title(merge_id: str, source_id: str) -> str:
    return f"chore({merge_id}): sync upstream {source_id}"


def render_pr_body(
    merge_id: str,
    source: dict,
    entry: dict,
    affected_rules: list[dict],
    locate_md: str,
) -> str:
    source_id = source["id"]
    from_commit = entry.get("last_accepted_commit") or "(无基线)"
    to_commit = entry.get("last_seen_commit")
    stars_hist = entry.get("stars_history", [])
    stars_before = stars_hist[-2]["value"] if len(stars_hist) >= 2 else None
    stars_after = stars_hist[-1]["value"] if stars_hist else None

    decisions = [r["decision"] for r in affected_rules] or ["rejected"]
    result = strongest_decision(decisions)

    lines: list[str] = []
    lines.append(f"## merge_result\n\n`{result}`\n")
    lines.append(
        f"共 {len(affected_rules)} 条规则引用来源 `{source_id}`；"
        f"逐条结论见下方受影响规则表和 locate 输出。\n"
    )
    lines.append("## 范围\n")
    lines.append(f"- merge_id：{merge_id}")
    lines.append(f"- 来源：{source_id}，{source['repository']}，{source['branch']}")
    lines.append(f"- 提交区间：{from_commit} .. {to_commit}")
    lines.append(f"- 追踪文件：{', '.join(source['paths'])}")
    lines.append("")
    lines.append("## 热度\n")
    lines.append(f"- stars：{stars_before if stars_before is not None else '未知'} -> "
                 f"{stars_after if stars_after is not None else '未知'}")
    lines.append(f"- forks：{entry.get('forks', '未知')}")
    lines.append("")
    lines.append("## 受影响规则\n")
    lines.append("| 规则 id | rule_summary | decision | decision_revision |")
    lines.append("|---|---|---|---|")
    for r in affected_rules:
        lines.append(f"| {r['id']} | {r['rule_summary']} | {r['decision']} | {r['decision_revision']} |")
    if not affected_rules:
        lines.append("| （无） | | | |")
    lines.append("")
    lines.append("这个 PR 里全部规则的 decision_origin 都是 model-proposed，合并前要改成 human-approved。\n")
    lines.append("## 原文声明\n")
    if source["snapshot_policy"] == "metadata-only":
        lines.append(f"本 PR 不含来源 `{source_id}` 的任何原文，snapshots/ 未新增内容，rationale 只写思路。")
    else:
        lines.append("本 PR 不涉及 metadata-only 来源。")
    lines.append("")
    lines.append("## locate 输出\n")
    lines.append(locate_md)
    return "\n".join(lines)


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=True)


def run_pr(
    paths: RepoPaths,
    client: GitHubClient,
    merge_id: str,
    source_id: str,
    dry_run: bool = True,
) -> dict:
    """返回一个结果字典，字段视是否幂等短路、是否 dry_run 而不同。"""
    sources_path = paths.sources_yaml(merge_id)
    lock_path = paths.lock_json(merge_id)
    S = load_yaml(sources_path)
    L = load_json(lock_path)
    source = next((s for s in S["sources"] if s["id"] == source_id), None)
    if source is None:
        raise KeyError(f"{merge_id}: 找不到来源 {source_id}")
    entry = L["sources"].get(source_id)
    if entry is None:
        raise KeyError(f"{merge_id}: lock 里没有来源 {source_id}，请先跑一次 check。")

    commit = entry.get("last_seen_commit")
    if not commit:
        raise ValueError(f"{source_id}: lock 里没有 last_seen_commit，请先跑一次 check。")

    change_key = change_key_for(source_id, source["paths"], commit)

    if entry.get("last_change_key") == change_key and entry.get("open_pr"):
        return {
            "idempotent": True,
            "change_key": change_key,
            "open_pr": entry["open_pr"],
            "message": f"变更键 {change_key} 已经开过 PR #{entry['open_pr']}，不重复开。",
        }

    decisions = load_yaml(paths.decisions_yaml(merge_id))
    affected_rules = rules_for_source(decisions, source_id)
    diff_text = run_diff(paths, client, merge_id, source_id)
    locate_md = render_locate_markdown(
        merge_id, source_id, affected_rules, decisions["rules"], diff_text
    )
    body = render_pr_body(merge_id, source, entry, affected_rules, locate_md)
    title = render_pr_title(merge_id, source_id)
    date = datetime.date.today().isoformat()
    branch = f"upstream-sync/{date}-{source_id}"

    commands = [
        ["git", "checkout", "-b", branch],
    ]
    if source["snapshot_policy"] == "full-text":
        commands.append(["<internal>", "snapshot", source_id])
    commands += [
        ["git", "add", "-A"],
        ["git", "commit", "-m", title],
        ["git", "push", "-u", "origin", branch],
        ["gh", "pr", "create", "--title", title, "--body-file", "<临时文件>", "--head", branch],
    ]

    result = {
        "idempotent": False,
        "change_key": change_key,
        "branch": branch,
        "title": title,
        "body": body,
        "commands": commands,
    }

    if dry_run:
        return result

    _run(["git", "checkout", "-b", branch], paths.root)

    new_entry = entry
    if source["snapshot_policy"] == "full-text":
        new_entry, _snap_result = snapshot_one_source(paths, client, merge_id, source, entry)

    _run(["git", "add", "-A"], paths.root)
    _run(["git", "commit", "-m", title], paths.root)
    _run(["git", "push", "-u", "origin", branch], paths.root)

    body_file = paths.root / f".upstream-monitor-pr-body-{source_id}.md"
    body_file.write_text(body, encoding="utf-8")
    try:
        pr_out = _run(
            ["gh", "pr", "create", "--title", title, "--body-file", str(body_file), "--head", branch],
            paths.root,
        )
    finally:
        body_file.unlink(missing_ok=True)

    pr_number = None
    m = re.search(r"/pull/(\d+)", pr_out.stdout)
    if m:
        pr_number = int(m.group(1))

    new_entry = dict(new_entry)
    new_entry["last_change_key"] = change_key
    new_entry["open_pr"] = pr_number
    L2 = dict(L)
    L2["sources"] = dict(L["sources"])
    L2["sources"][source_id] = new_entry
    validate_doc(paths.schemas_dir, "lock", L2, target=str(lock_path))
    dump_json(L2, lock_path)

    result["open_pr"] = pr_number
    result["pr_url"] = pr_out.stdout.strip()
    return result
