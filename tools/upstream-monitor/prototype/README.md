# prototype

试验合并阶段手工跑过的一次性脚本，upstream-monitor 正式实现时复用其中的函数，实现完成后删除本目录。

依赖：pyyaml、jsonschema。

- `render_sources.py`：从 `merges/<id>/sources.yaml`、`sources.lock.json`、`decisions.yaml` 和 `snapshots/*/LICENSE` 渲染 `skills/<id>/SOURCES.md`。
- `check_merge.py`：校验一个 merge 实例。三个子命令，upstream-monitor 的 `validate` 命令直接复用。

## check_merge.py

```
python3 tools/upstream-monitor/prototype/check_merge.py format \
    --root . --merge merges/maybe-humanizer

python3 tools/upstream-monitor/prototype/check_merge.py anchors \
    --root . --merge merges/maybe-humanizer --fetch-dir <仓库外的临时拉取目录>

python3 tools/upstream-monitor/prototype/check_merge.py coverage \
    --root . --merge merges/maybe-humanizer \
    --units <单元清单目录> --coverage <覆盖表.md> [--clusters <聚类表.md>]
```

| 子命令 | 查什么 |
|---|---|
| `format` | 四份 schema 校验；merge_id 三处一致；证据的 source_id 都在 sources.yaml；lock 与 sources 的 id 集合一致；evidence_count 等于 sources 长度；independent_sources 等于去重 lineage 数；规则 id 唯一、格式和分组编号符合 extraction.md；每条 `local.anchor` 在 `local.path` 里恰好命中一次（已落地规则找不到即 BLOCK）；history 末条与当前 decision 一致、长度等于 decision_revision；`relations` 的 rule_id 都存在、不自指、conflicts-with 与 pairs-with 双向 |
| `anchors` | decisions.yaml 每条证据的上游 anchor 能不能在快照里定位到；证据的 path 在不在 sources.yaml 的 paths 里；证据的 commit 与 lock 的 last_seen_commit 是否一致 |
| `coverage` | 拆规则阶段的单元清单每条恰好归入一条规则；覆盖表的规则 id、decision、成员数、来源分布与 decisions.yaml 一致；覆盖表、单元清单、decisions.yaml 三处的 anchor 一致；聚类表与覆盖表成员一致 |

有 BLOCK 或 HIGH 级问题时以退出码 1 结束，可以直接进 CI。

`--fetch-dir` 只给 `snapshot_policy` 为 metadata-only 的来源用。这类来源的原文不进仓库，`lock` 里对应 files 的 `stored_path` 是 null，校验时按 lock 的 commit 临时拉到仓库外的一个目录，目录结构与上游仓库内路径一致（`<fetch-dir>/<source_id>/<original_path>`），比完删掉。不给这个参数时，这些证据只报一条 MED，不算失败。

`coverage` 的三个输入是拆规则和归并阶段的中间产物，按 `skills/skill-merge/references/process.md` 不进仓库，所以路径必须显式传。单元清单目录里每个来源一份 `<source_id>.md`。

anchor 的匹配规则与 `skills/skill-merge/references/extraction.md` 一致：小节标题原文，或该段稳定的行首文本，多级之间用 ` / ` 分隔。匹配时忽略行首的列表符号、序号、表格竖线、引用块的 `> ` 前缀和行内的强调标记；围栏代码块里的 `#` 行不当成标题——上游常把 markdown 报告模板整段放进代码块，把块里的 `#` 当标题会让它上面那一节被提前截断。
