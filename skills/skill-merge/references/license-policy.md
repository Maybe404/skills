# 许可证策略

snapshot_policy 只有两个取值，由 sources.yaml 里的 license 和 license_status 决定。license 为 unknown 时 snapshot_policy 必须是 metadata-only，schema 会挡住其他写法。

## full-text

适用于 license_status 为 known、且许可证允许保留副本和衍生作品的来源（MIT、Apache-2.0、BSD 这类）。

允许：

- 在 `merges/<id>/snapshots/<source_id>/` 保存 paths 里每个追踪文件的当前全文。目录结构沿用上游的路径，其中 `SKILL.md` 存为 `SKILL.source.md`，避免被当成本仓库自己的 skill 加载。
- 同一目录下原样保存上游仓库的 LICENSE 文件。MIT 这类许可证要求副本附带许可声明，这份文件就是声明。
- 在 decisions.yaml 的 rationale 里引用原文短句。
- 在 `merges/<id>/reports/` 的报告里引用原文短句作为证据。
- 在 skill 正文里复用规则的意思。
- 在 skill 正文里照录触发词表：禁用词、高频词、套话短语这类词条本身是触发数据，不是表述，改写会让规则失去可判定性——把 delve 换成别的词，这条规则就不管 delve 了。照录的范围只限词条本身，包括逐条同序；词表周围的说明文字、正例反例、执行强度必须重写。照录时在对应规则的 decisions.yaml rationale 里写一句"词表照录自 `<source_id>`，说明文字为重写"。

禁止：

- 把上游整节原样搬进 `skills/<id>/` 的正文或 references。skill 是重写的产物，不是转载。
- 保存 paths 之外的文件。追踪范围要先改 sources.yaml 的 paths 并把 tracking_revision 加一。
- 保存或执行上游脚本。脚本只读不跑。

## metadata-only

适用于 license 为 unknown、license_status 为 unknown 或 changed 的来源。

允许：

- 在 sources.yaml 和 sources.lock.json 里记元数据：repository、branch、paths、raw_sha256、normalized_sha256、size、line_count、stars_history、forks、availability。
- 用自己的话记录这个来源提出了什么规则方向。
- 记 anchor（小节标题或行首文本），用于定位。

禁止：

- 在仓库任何位置保存原文，包括 snapshots/、报告、decisions.yaml 的 rationale、PR 正文、issue 正文。lock 里对应 files 的 stored_path 必须是 null。
- 引用原文的例句、词表条目、模式名、清单措辞。
- 在 sync 时把临时拉取的内容落盘。比对完就丢。

判据：把 rule_summary、rationale、报告里与这个来源相关的全部文字拿给没读过上游的人看，能不能反推出上游的原句？能，就要重写。

## license_status 为 changed

上游改了许可证时，upstream-monitor 把 license_status 改成 changed 并开 issue。在人工处理之前：

- 已有的 snapshots/ 内容不再更新，也不删除，等人工确认。
- 这个来源的新变更不进 sync。
- 新许可证仍允许保留副本的，把 license 改成新的 SPDX 标识、license_status 改回 known；不允许的，snapshot_policy 改成 metadata-only，删掉 snapshots/<source_id>/，把该来源支持的规则逐条重看，rationale 里引了原文的重写。

## SOURCES.md 的许可证声明

`skills/<id>/SOURCES.md` 由代码从 decisions.yaml 和 sources.yaml 渲染，不手写。渲染出来的内容必须包含：

1. 每个 status 不是 removed 的来源一行，含 id、repository、branch、license、snapshot_policy、lineage、selection_status。
2. license 为 unknown 的来源，那一行要写明"未取得许可证，本仓库不含其原文"。
3. 一句说明：本 skill 的正文是重写的产物，不是上游的转载；上游的著作权归各自作者。
4. status 为 removed 的来源单列一节，写明移除时间和 reason，历史贡献不抹掉。

渲染结果与 sources.yaml 不一致时，改 sources.yaml 再重新渲染，不改 SOURCES.md。
