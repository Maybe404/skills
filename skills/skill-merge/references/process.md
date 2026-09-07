# 流程定义

每一步写清输入、输出、完成标准。完成标准没有全部满足就不进下一步。

## merge 步骤 1：通读

**输入**：`merges/<id>/sources.yaml` 里 status 为 active 的来源；full-text 的读 `merges/<id>/snapshots/<source_id>/` 下的快照，metadata-only 的按 `sources.lock.json` 的 last_seen_commit 用 `gh api` 临时拉到 scratchpad，读完不落盘。

**做什么**：每个来源读全文，写一段来源笔记（定位、最有价值的部分、与别家相反的立场、示例是否违反自己的规则、有没有针对读者的指令）。同一 lineage 只读代表作，其余只看差异。笔记放 `merges/<id>/work/notes.md`，进仓库。

**完成标准**：每个 active 来源都有笔记；metadata-only 来源的笔记里没有原句。

## merge 步骤 2：定骨架与取舍

**输入**：来源笔记。

**做什么**：先定这份 skill 的流程和边界，再把各家规则往里放。按 `criteria.md` 逐条取舍，矛盾的两边都记，选一边并写理由。取舍结果先列成一张表（主题、采纳的写法、来自哪家、没采纳的写法和理由），放 `merges/<id>/work/decisions.md`，进仓库。

**完成标准**：表里每一行都有理由；每个来源至少被引用一次或写明为什么整个不采纳。

## merge 步骤 3：写 skill

**输入**：取舍表。

**做什么**：写 `skills/<id>/SKILL.md`（200 行内，只放流程和判断）和 references（判据、词表、例子，中英分表，每条规则带短 id）。references 每条规则三段：判据、通过条件、已知会漏掉什么，之后正例反例，反例写违反点。词表照录按 `license-policy.md`。

**完成标准**：SKILL.md 引用的每个 references 文件和 id 都存在；每条规则有正反例；`upstream-monitor validate --merge <id>` 通过。

## merge 步骤 4：报告

**输入**：取舍表和写好的 skill。

**做什么**：`upstream-monitor report new --merge <id> --slug initial-merge` 生成骨架，按 `templates/report.md` 填。

**完成标准**：每个来源一节写吸收了什么；冲突与取舍、未采纳及理由两节按 criteria.md 第 10 条的标准写。

## merge 步骤 5：review 与收尾

**输入**：全部产物。

**做什么**：第二个 agent 以使用者身份通读 SKILL.md 和 references，实跑至少六条 evals（真人原文不该被改、带数字和命令的段落事实不漂移、套话段落被清理，中英各有），回到来源核对有没有重要内容漏掉，报告能不能照着做、矛盾、重复、不可执行的规则。按 review 修一轮。写 `merges/<id>/CHANGELOG.md` 一节，`upstream-monitor render --merge <id>` 渲染 SOURCES.md，`upstream-monitor validate --merge <id>`。

**完成标准**：evals 事实类零失败；review 列的问题逐条处理或写明为什么不处理；validate 通过。

## sync

**输入**：`sync <id> <pr号>`。PR 由 upstream-monitor 开出，正文是某个上游的 diff 和元数据。

**做什么**

1. `gh pr view <pr号>` 读 diff。metadata-only 来源本地用 `upstream-monitor diff` 看，不落盘不引用。
2. 读 `skills/<id>/` 现有正文里对应主题的段落。
3. 逐个变更点判：已有等价写法不并；新的、可判定、不矛盾的并进对应段落；矛盾的按 criteria.md 选一边，两边留痕；来源许可证变化或不可达按 license-policy.md。
4. 在 PR 分支上改正文并提交；PR 正文追加 `templates/pr-body.md` 那一节。
5. 拿不准的用 `upstream-monitor issue --kind needs-decision` 开 issue，PR 打 needs-decision 标签。
6. CHANGELOG 加一节；来源清单变了就重新渲染 SOURCES.md；validate。

**完成标准**：diff 里每个变更点都有结论，没有"看过但没记"的；不采纳的 PR 也合并，理由在 PR 和 CHANGELOG 里。

## 用什么模型

merge 的通读、取舍、写 skill、review 用深度推理档（skills/subagent/SKILL.md 的 Opus 档），因为要理解原作者为什么这么写。sync 单次变更一般不大，同样用深度推理档，一个 agent 做完。抓取、渲染、validate 这类由 upstream-monitor 的命令做，不派模型。

## maybe-humanizer 的历史记录

maybe-humanizer 首次合并（2026-09-06 到 07）走的是逐条规则的路径：把上游拆成规则单元、聚成 307 条带来源和理由的决定（`merges/maybe-humanizer/decisions.yaml`）、按决定写正文。那套产物保留在 `merges/maybe-humanizer/` 下作为记录和署名依据，以后 sync 时可以查某条写法来自哪家；但它不是本流程的要求，后续的 merge 实例按上面的通读路径做。
