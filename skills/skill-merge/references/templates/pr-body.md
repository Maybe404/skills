# PR 正文模板

`merge_result`、`受影响规则`、`原文声明` 是 PR 正文里的段落名，不是 schema 字段；只有 merge_result 的取值与 decisions.schema.json 的 decision 枚举相同。

PR 标题用英文 conventional commits，例如 `chore(maybe-humanizer): sync upstream-aboudjem-humanizer-skill`。

---

## merge_result

`adopted` | `adopted-with-modification` | `duplicate` | `rejected` | `deferred` | `reference-only` | `unverified` | `retired`

这个 PR 里全部变更的合并结论。多条规则结论不一致时，取其中"最强"的一个：有 adopted 就写 adopted，其次 adopted-with-modification，依此类推，末位是 rejected。逐条结论在下面的表里。

一行说明这个结论意味着什么，例如"新增两条 protection 规则，一条上游风格意见未采纳"。

## 范围

- merge_id：
- 来源：<source_id>，repository，branch
- 提交区间：last_accepted_commit .. last_seen_commit
- 追踪文件：paths 里的哪几个有变更

## 受影响规则

| 规则 id | rule_summary | 变更前 decision | 变更后 decision | decision_revision |
|---|---|---|---|---|

新增的规则"变更前 decision"写"新增"。这个 PR 里全部规则的 decision_origin 都是 model-proposed，合并前要改成 human-approved。

## 原文声明

snapshot_policy 为 metadata-only 的来源在这个 PR 里的处理：本 PR 不含这些来源的任何原文，snapshots/ 未新增内容，rationale 只写思路。逐个列出涉及的 source_id；没有涉及的写"本 PR 不涉及 metadata-only 来源"。

## 报告

`merges/<id>/reports/NNNN-YYYY-MM-DD-<slug>.md`

## 检查项

- [ ] decisions.yaml 通过 decisions.schema.json 校验
- [ ] sources.yaml 通过 sources.schema.json 校验
- [ ] 每条规则的 sources 里的 source_id 存在于 sources.yaml
- [ ] metadata-only 来源没有原文进仓库
- [ ] 报告十个章节齐全
- [ ] CHANGELOG.md 已加一节
- [ ] 合并前把本 PR 内的 model-proposed 改成 human-approved
