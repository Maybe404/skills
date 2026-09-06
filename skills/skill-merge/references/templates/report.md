# 合并报告模板

文件名 `merges/<id>/reports/NNNN-YYYY-MM-DD-<slug>.md`。NNNN 是四位序号，接目录里最大的加一。十个章节固定，顺序不改，没有内容的写"无"，不删除章节。

---

# <merge_id> 合并报告 NNNN

日期：YYYY-MM-DD
模式：merge | sync
触发：首次合并 | PR #<号> | locate 输出

## 1 范围

这次处理了哪些来源、哪个提交区间、哪些文件。sync 要写清每个来源的 last_accepted_commit 到 last_seen_commit。不在范围内但相关的，写明为什么不在。

## 2 来源清单

| id | repository | branch | lineage | selection_status | license | snapshot_policy | stars | forks |
|---|---|---|---|---|---|---|---|---|

stars 取 sources.lock.json 里 stars_history 的最后一条，并注明 observed_at。stars 和 forks 是热度，不是采用依据。

## 3 统计

- 来源数：入围 <n> / 登记 <n>
- 规则单元数：<n>
- 聚类数：<n>
- 各 decision 计数：adopted <n>、adopted-with-modification <n>、duplicate <n>、rejected <n>、deferred <n>、reference-only <n>、unverified <n>、retired <n>
- 按 category 分布：pattern <n>、protection <n>、process <n>、style-opinion <n>、genre <n>、measurement <n>

## 4 覆盖矩阵

来源乘规则的表。行是规则 id，列是来源 id，格子里写这个来源是否支持这条规则（是写来源里的 anchor，否留空）。最后两列是 evidence_count 和 independent_sources。

规则超过三十条时按 category 分成多张表，不省略行。

## 5 冲突与取舍

每组冲突一小节：涉及的规则 id、各自主张什么、为什么选了这一条、被放弃的那条记成了什么 decision。单一来源的强风格意见没进默认规则的，也写在这里。

## 6 被拒绝规则与理由

decision 为 rejected 的每条一行：规则 id、rule_summary、拒绝理由、对应 criteria.md 的哪一条。落在 criteria.md 第 5 条三类内容里的单列，写明是哪一类。

## 7 影响的本地文件

改了哪些文件、每个文件改了什么。至少覆盖 `merges/<id>/decisions.yaml`、`skills/<id>/SKILL.md`、`skills/<id>/references/*`、`merges/<id>/CHANGELOG.md`。

## 8 如何验证

evals 三类样本各跑了多少条、通过多少、失败多少。第 2 类（事实不漂移）有失败的，逐条列出失败样本和失败点。附可以复跑的命令。

## 9 如何回滚

回到这次合并之前需要做什么：撤哪个提交、decisions.yaml 里哪些规则 id 要改回什么 decision 和 decision_revision、skill 正文里哪些小节要删。写成可以照着做的步骤，不写"revert 即可"。

## 10 未解决问题

拿不准的、需要用户拍板的、decision 为 deferred 或 unverified 的、上游文本里出现的指令内容。每条写清缺什么才能定。
