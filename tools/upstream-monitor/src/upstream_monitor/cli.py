"""upstream-monitor 的命令行入口。所有路径可配置，默认从当前目录找
catalog/ 和 merges/。"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from upstream_monitor import approve as approve_mod
from upstream_monitor import check as check_mod
from upstream_monitor import diff as diff_mod
from upstream_monitor import issue as issue_mod
from upstream_monitor import lineage as lineage_mod
from upstream_monitor import locate as locate_mod
from upstream_monitor import pr as pr_mod
from upstream_monitor import render as render_mod
from upstream_monitor import report as report_mod
from upstream_monitor import retire as retire_mod
from upstream_monitor import validate as validate_mod
from upstream_monitor.github_client import RealGitHubClient
from upstream_monitor.paths import RepoPaths


def _add_common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--root", default=".", help="仓库根目录，默认当前目录")
    p.add_argument("--catalog-dir", default=None, help="catalog 目录，默认 <root>/catalog")
    p.add_argument("--merges-dir", default=None, help="merges 目录，默认 <root>/merges")
    p.add_argument("--skills-dir", default=None, help="skills 目录，默认 <root>/skills")
    p.add_argument(
        "--schemas-dir", default=None, help="schema 目录，默认 <root>/tools/upstream-monitor/schemas"
    )


def _paths_from_args(args: argparse.Namespace) -> RepoPaths:
    return RepoPaths.resolve(
        root=args.root,
        catalog_dir=args.catalog_dir,
        merges_dir=args.merges_dir,
        skills_dir=args.skills_dir,
        schemas_dir=args.schemas_dir,
    )


# ---------------------------------------------------------------- validate

def cmd_validate(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = None if args.offline else RealGitHubClient()
    rep = validate_mod.validate(
        paths,
        merge_id=args.merge,
        branch=args.branch,
        client=client,
        check_upstream_anchors=not args.offline,
    )
    print(rep.render_text())
    return rep.exit_code()


# ---------------------------------------------------------------- check

def cmd_check(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = RealGitHubClient()
    results = check_mod.run_check(paths, client, merge_id=args.merge)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            extra = ""
            if r.get("license_changed"):
                extra = f"；许可证变化：{r.get('license_detail')}"
            print(f"[{r['merge_id']}] {r['source_id']}: {r['change']}"
                  f"（{r.get('detail', '')}）{extra}")
    return 0


# ---------------------------------------------------------------- snapshot

def cmd_snapshot(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = RealGitHubClient()
    from upstream_monitor.snapshot import run_snapshot

    try:
        outs = run_snapshot(paths, client, args.merge, source_id=args.source)
    except Exception as e:  # noqa: BLE001 - 面向 CLI，统一转成失败退出码
        print(f"snapshot 失败: {e}", file=sys.stderr)
        return 1
    for o in outs:
        print(f"{o.source_id}: 写入 {len(o.files_written)} 个文件"
              + (f"，LICENSE -> {o.license_written}" if o.license_written else "，无 LICENSE"))
    return 0


# ---------------------------------------------------------------- diff

def cmd_diff(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = RealGitHubClient()
    text = diff_mod.run_diff(
        paths, client, args.merge, args.source, from_commit=args.from_, to_commit=args.to
    )
    print(text)
    return 0


# ---------------------------------------------------------------- locate

def cmd_locate(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    diff_path = Path(args.diff).resolve() if args.diff else None
    text = locate_mod.run_locate(paths, args.merge, args.source, diff_path=diff_path)
    print(text)
    return 0


# ---------------------------------------------------------------- pr

def cmd_pr(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = RealGitHubClient()
    result = pr_mod.run_pr(paths, client, args.merge, args.source, dry_run=args.dry_run)
    if result.get("idempotent"):
        print(result["message"])
        return 0
    if args.dry_run:
        print(result["body"])
        print()
        print("将要执行的命令：")
        for c in result["commands"]:
            print("  " + " ".join(c))
    else:
        print(f"已开 PR: {result.get('pr_url')}")
    return 0


# ---------------------------------------------------------------- approve

def cmd_approve(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    changed = approve_mod.run_approve(paths, args.merge, pr=args.pr, rules=args.rule)
    if changed:
        print(f"已改为 human-approved: {changed}")
    else:
        print("没有需要改动的规则。")
    return 0


# ---------------------------------------------------------------- render

def cmd_render(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    if args.readme_table:
        print(render_mod.render_readme_table(paths))
        return 0
    out = Path(args.out).resolve() if args.out else None
    render_mod.render_sources_for_merge(paths, args.merge, out_path=out)
    print(f"已渲染 {args.merge} 的 SOURCES.md")
    return 0


# ---------------------------------------------------------------- retire

def cmd_retire(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    affected = retire_mod.run_retire(paths, args.merge, args.source, args.reason)
    print(retire_mod.render_retire_markdown(args.merge, args.source, affected))
    return 0


# ---------------------------------------------------------------- issue

def cmd_issue(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    client = issue_mod.RealGhIssueClient(paths.root)
    result = issue_mod.run_issue(
        paths, client, args.merge, args.source, args.kind, detail=args.detail, dry_run=args.dry_run
    )
    if result.get("idempotent"):
        print(result["message"])
        return 0
    if args.dry_run:
        print(result["body"])
        return 0
    print(f"已开 issue: #{result['issue_number']}（{', '.join(result['labels'])}）")
    return 0


# ---------------------------------------------------------------- lineage

def cmd_lineage(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    relations_path = Path(args.relations).resolve() if args.relations else None
    result = lineage_mod.run_lineage(
        paths, args.merge, threshold=args.threshold, relations_path=relations_path, write=args.write
    )
    print(lineage_mod.render_lineage_text(result))
    if result["written"]:
        print(f"\n已写回 {args.merge} 的 sources.yaml 的 lineage 字段。")
    return 0


# ---------------------------------------------------------------- report

def cmd_report_new(args: argparse.Namespace) -> int:
    paths = _paths_from_args(args)
    target = report_mod.run_report_new(paths, args.merge, args.slug)
    print(f"已生成 {target}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="upstream-monitor", description="Maybe404/skills 仓库的上游监控与流转工具"
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("validate", help="校验 catalog、sources、lock、decisions 的一致性")
    _add_common_args(p)
    p.add_argument("--merge", default=None, help="只校验这一个 merge 实例，默认全部")
    p.add_argument("--branch", default=None, help="覆盖从 git 读到的当前分支名")
    p.add_argument(
        "--offline", action="store_true", help="跳过需要网络的 metadata-only 来源锚点校验"
    )
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("check", help="拉取上游 commit/hash/stars，更新 lock")
    _add_common_args(p)
    p.add_argument("--merge", default=None, help="只检查这一个 merge 实例，默认全部")
    p.add_argument("--json", action="store_true", help="以 JSON 输出结果")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("snapshot", help="把 full-text 来源的追踪文件写入 snapshots/")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", default=None, help="只处理这一个来源，默认全部 full-text 来源")
    p.set_defaults(func=cmd_snapshot)

    p = sub.add_parser("diff", help="按 commit 现取两个版本，输出统一 diff")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--from", dest="from_", default=None, help="默认 last_accepted_commit")
    p.add_argument("--to", default=None, help="默认 last_seen_commit")
    p.set_defaults(func=cmd_diff)

    p = sub.add_parser("locate", help="反查引用某来源的规则，可选按 diff 收窄")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--diff", default=None, help="unified diff 文件路径")
    p.set_defaults(func=cmd_locate)

    p = sub.add_parser("pr", help="生成 PR 正文，开分支、写快照或更新 lock、开 PR")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--dry-run", action="store_true", help="只打印正文和将要执行的命令")
    p.set_defaults(func=cmd_pr)

    p = sub.add_parser("approve", help="把 model-proposed 改成 human-approved")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--pr", type=int, default=None, help="只改这个 PR diff 里出现的规则 id")
    p.add_argument("--rule", action="append", default=None, help="只改这些规则 id，可重复给")
    p.set_defaults(func=cmd_approve)

    p = sub.add_parser("render", help="渲染 SOURCES.md 或 README 的 skill 表格")
    _add_common_args(p)
    p.add_argument("--merge", default=None, help="渲染这个 merge 实例的 SOURCES.md")
    p.add_argument(
        "--readme-table", action="store_true", help="改为输出 catalog 生成的 skill 表格，不写文件"
    )
    p.add_argument("--out", default=None, help="SOURCES.md 的输出路径，默认 skills/<id>/SOURCES.md")
    p.set_defaults(func=cmd_render)

    p = sub.add_parser("retire", help="把来源状态改成 removed，列出唯一来源支持的规则")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--reason", required=True)
    p.set_defaults(func=cmd_retire)

    p = sub.add_parser("issue", help="按情形开 issue，正文不含上游原文")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--source", required=True)
    p.add_argument(
        "--kind",
        required=True,
        choices=[
            "source-unavailable",
            "license-changed",
            "history-rewritten",
            "needs-decision",
            "retire-impact",
            "new-candidate",
        ],
    )
    p.add_argument("--detail", default=None, help="要做的决定的补充说明，不给时用该情形的默认提示")
    p.add_argument("--dry-run", action="store_true", help="只打印正文")
    p.set_defaults(func=cmd_issue)

    p = sub.add_parser("lineage", help="按文本相似度和人工核实关系聚类同源来源")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--threshold", type=float, default=lineage_mod.DEFAULT_THRESHOLD)
    p.add_argument(
        "--relations", default=None, help="人工核实关系文件，默认 merges/<id>/lineage-relations.yaml"
    )
    p.add_argument("--write", action="store_true", help="把聚类结果写回 sources.yaml 的 lineage 字段")
    p.set_defaults(func=cmd_lineage)

    p_report = sub.add_parser("report", help="报告相关命令")
    report_sub = p_report.add_subparsers(dest="report_cmd", required=True)
    p = report_sub.add_parser("new", help="生成一份空壳报告")
    _add_common_args(p)
    p.add_argument("--merge", required=True)
    p.add_argument("--slug", required=True)
    p.set_defaults(func=cmd_report_new)

    return ap


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
