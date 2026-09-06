# 术语、多义词与排版约定

## 术语的三种处理方式

判断标准是中文技术圈实际怎么说，不是词典。

1. **保留英文**：没有公认中文译法，或中文译法会引起歧义的。prompt、token、subagent、agent、Workflow、MCP、resume、commit、PR、issue、CLI、API、SDK、harness、worktree、hook、skill、artifact、diff、bug。
2. **用中文**：有公认译法且无歧义的。缓存（cache）、回调（callback）、并发（concurrency）、依赖（dependency）、上下文（context）、会话（session）、仓库（repository）、分支（branch）、合并（merge）、重构（refactor）、部署（deploy）、回滚（roll back）、日志（log）、测试（test）、断言（assertion）、类型检查（typecheck）、编排器（orchestrator）、工作树（worktree 作普通名词时）。
3. **保留英文并在首次出现时括注中文**：读者可能不熟的英文词。括注写这个上下文里的意思，不写词典义。resume（续用已有 agent）、TTFT（首字延迟）、compaction（上下文压缩）、effort（推理深度档位）、dispatch（派发）、escalate（升档）、scout（先摸清情况）。

同一文档里同一个词只用一种处理方式。用户已有的用法优先于本表。

## 容易译错的词

| 英文 | 常见误译 | 在技术或指令文本里通常指 |
|---|---|---|
| check in (with someone) | 签入 | 向某人确认、征求意见 |
| address (a problem) | 地址 | 处理（一个问题） |
| hold（the rule holds） | 拿着 | 成立、仍然有效 |
| scope | 作用域 | 任务范围；只有在代码语境才是作用域 |
| surface（动词） | 表面 | 暴露出来、显示给人看 |
| argument | 论点 | 实参、参数；讨论语境才是论点 |
| reference | 参考 | 引用、指向（代码）；参考资料（文档） |
| resolve | 解决 | 解析（路径、依赖）；解决（冲突、问题），看上下文 |
| issue | 问题 | GitHub issue 保留原词；泛指时是问题 |
| handle | 把手 | 处理 |
| support | 支持 | 支持（功能）；有时是"撑住、承受" |
| ship | 运输 | 发布、上线 |
| land | 降落 | 合入（PR） |
| flag | 旗帜 | 命令行参数；标记 |
| default | 违约 | 默认 |
| expect | 期待 | 预期；测试里的 expect 是断言 |
| gate | 大门 | 审批点、门槛、前置条件 |
| narrow / widen | 变窄 / 变宽 | 缩小 / 扩大（范围） |
| swap | 交换 | 换成别的 |
| extend | 延长 | 扩展（功能） |
| override | 越过 | 覆盖（设置）、重写（方法） |
| fall back | 后退 | 退回到备用方案 |
| degrade | 降级 | 退化成更差的做法 |
| retry / re-prompt | 重试 | 同一 agent 再试一次 / 换措辞再问一次 |
| spawn / launch / dispatch | 生成 / 发射 | 启动、派发（agent） |
| orchestrator | 指挥 | 编排器 |
| harness | 马具 | 运行框架 |
| verbatim / as is / in place | 逐字 | 原样 / 原样 / 就地 |
| stale / fresh | 陈旧 / 新鲜 | 过期的 / 新的（上下文、缓存） |
| upstream / downstream | 上游 / 下游 | 可直译 |
| green / red（测试） | 绿 / 红 | 通过 / 失败 |
| in the loop | 在循环里 | 参与决策；human-in-the-loop = 人在回路 |
| trivial / non-trivial | 琐碎 / 不琐碎 | 简单到不值一提的 / 有一定难度的 |
| arguably | 可争论地 | 可以说、基本上 |
| roughly / about | 粗糙 | 大约 |
| at most / up to | 最多 | 最多（上限） |
| at least / over | 至少 | 至少 / 超过（下限） |
| follow-up | 后续 | 后续动作、后续查找；不是"追问" |
| assume / assumption | 假装 | 假设、前提 |
| commit（动词，非 git） | 提交 | 决定采用、承诺 |
| drop | 掉落 | 删掉、放弃 |
| pin | 大头针 | 固定（版本、位置） |
| bump | 撞 | 升版本号 |
| clean / dirty（工作树） | 干净 / 脏 | 无未提交改动 / 有未提交改动 |

## 标点和排版

- 中文正文用全角标点：，。；：？！（）""
- 反引号内、代码块内、URL、文件路径、命令、环境变量、flag 内一律半角。
- 中文与英文单词、数字之间加一个空格："5 次调用""用 Workflow 工具"；中文标点与英文之间不加空格。
- 一句话最多一个冒号。
- 破折号用"——"，不用"-"或"–"。
- 省略号用"……"。
- 引用和举例用引号，书名用《》，代码用反引号。不用引号表示强调。
- 列表项末尾的标点全文统一：都加句号，或都不加。
- 括注英文术语时用全角括号：resume（续用已有 agent）。
- 数字用阿拉伯数字，百分号紧跟数字：40%。
- 作为工具名、产品名的英文词（Workflow、Agent、Claude Code）保留原有大小写；作为普通名词时小写（agent、workflow）。

## 情态动词强度

| 英文 | 中文 |
|---|---|
| must / shall / always | 必须 / 一律 |
| must not / never | 不得 / 绝不 / 一律不 |
| should | 应当 / 要 |
| should not | 不应 / 不要 |
| may / can | 可以 |
| need not | 不必 |
| might / could | 可能会 |
