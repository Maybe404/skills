# 来源拆分：upstream-mrgediao-shuorenhua

## 1 来源摘要

- 文件：`merges/maybe-humanizer/snapshots/upstream-mrgediao-shuorenhua/SKILL.source.md`
- 上游原路径：`SKILL.md`（仓库 `MrGeDiao/shuorenhua`，branch `main`）
- commit（sources.lock.json 的 last_seen_commit）：`d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8`
- 许可证：MIT，license_status 为 known，snapshot_policy 为 full-text，允许在本清单中引用原文短句。
- 上游自述的定位：中英文通用的「去 AI 味」审稿与改写 skill，frontmatter 声明适用于「去 AI 味」「说人话」「自然一点」「别像模板」「先标问题」这类需求，明确按场景控制力度，同时保留事实、术语、语域和责任主体。正文开篇把目标写成「把文本从像模型在表演写作拉回像具体人在当前场景下表达」，并声明自己不是敏感词替换器、不反技术、不反抽象、不反专业。
- 结构上它是三个来源里唯一一个把**场景**当成一等概念的：先判 `chat / status / docs / public-writing` 四个主场景和六个子场景（README、release-note、forum-post、issue-reply、api-reference、faq），再判 Tier（问题命中强度）、档位（`minimal / standard / aggressive`）和 scope（`structural / bounded / in-place`，即这次允不允许删整句），最后固定做两遍回读。它对技术文本的保护对象写得最细：接口名、参数名、字段名、配置项、命令、日志、报错、系统行为主语、责任主体，以及范围、条件、否定、情态、完成态、方向、强度这一组条件关系。
- 本文件只追踪 `SKILL.md`；上游正文引用的 `references/`、`evals/` 不在 sources.yaml 的 paths 里，快照中没有，本清单不含它们的内容，涉及处只记导航关系。
- 总单元数：135（U-srh-001 至 U-srh-135）
- 按 category 计数：
  - process：51
  - protection：40
  - genre：17
  - pattern：14
  - measurement：8
  - style-opinion：5
- 按 language 计数：zh 129，both 6（U-srh-001、031、032、034、081、084，这几条的触发词表或适用声明同时给了中英文条目），en 0

## 2 单元清单

### U-srh-001

```
id: U-srh-001
category: genre
language: both
rule_summary: 适用于用户提出「去 AI 味」「说人话」「自然一点」「别像模板」「别太像 ChatGPT」「先标问题」的中文或英文文本改写与审稿；不适用于逐字翻译、保留原文风格、仿官方模板或仿特定品牌 voice，不适用于主要由代码、日志、命令、配置、接口名、报错构成的文本，也不适用于用户要的是事实校对而不是风格改写的情形。
positive: 「这段发布说明别太像模板，帮我改得像人写的」——属于风格改写请求，适用。（自造）
negative: 「帮我核对一下这段里的版本号和日期对不对」——违反点：请求是事实校对，不是风格改写，不在适用范围内。（自造）
positive（英文）: "Rewrite this release note so it stops sounding like a template." ——属于英文文本的风格改写请求，适用。（自造）
negative（英文）: "Translate this release note into Japanese, keeping the original wording." ——违反点：请求是逐字翻译并保留原文风格，不在适用范围内。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## When to use"
notes: |
  intent: 三条排除项各针对一种误用：仿模板和仿品牌 voice 与本 skill 的目标（减少模板感）方向相反；代码日志类文本里模式表几乎全是误杀；事实校对是另一件事，做风格改写会让用户以为事实也核过了。正反两个方向共用同一条"是否适用"的判定逻辑，按 extraction.md 合成一个单元。
  existing: 疑似对应 ALL-G-001（适用与不适用范围）与 ALL-PROC-017（文件是源代码、配置或结构化数据时停手）。
```

### U-srh-002

```
id: U-srh-002
category: protection
language: zh
rule_summary: 不得因为某个词出现在词表里就替换它，也不得以「更像人」为由删掉专业、抽象或技术性的表达；要处理的是模板感、表演感和语域漂移。
positive: 一份事故复盘里出现「根因」「降级」，判定为专业表达，保留不动。（自造）
negative: 把复盘里的「触发了限流降级」改成「当时系统扛不住就先关掉了一部分」，理由是这样更像人话。——违反点：以"更像人"为由把专业表达改成了口语，属于该 skill 明确排除的反技术操作。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "这份 skill 不是敏感词替换器"
notes: |
  intent: 上游把这句放在正文第一段，是因为「去 AI 味」最常见的失败模式就是被执行成"看到词表里的词就换"。作者要的是判断（这个词在这句话里是不是在表演），不是匹配。
  existing: 疑似对应 ALL-PROT-009（模式清理有三类例外）与 ALL-PROC-029（只改有问题的地方）。本单元把它写成了一条统领性的态度规则，可判定性依赖后面各条具体规则。
```

### U-srh-003

```
id: U-srh-003
category: protection
language: zh
rule_summary: 专业词、技术文档里的系统主语、事故复盘用语，以及 postmortem、incident、PRD、release note 里的专业术语，默认可以保留，不因为通用词表命中而改写。
positive: 一份 PRD 里的「灰度」「回滚窗口」原样保留。（自造）
negative: 把 release note 里的「回滚窗口」改成「可以撤回的时间」。——违反点：把发布说明里的专业术语按通用词表改成了日常说法。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 保留技术性。"
notes: |
  intent: 上游把"保留技术性"写在 Core stance 的第二条，位置仅次于总的态度声明，说明它认为通用去 AI 味词表对技术文本的误杀是最大的风险。第 5 节「No-touch and keep rules」里有同一条规则的更完整表述（列出了 postmortem / incident / PRD / release note），两处是同一条规则的两次出现，本单元以 Core stance 为主锚点。
  existing: 疑似对应 ALL-PROT-009（行业固定表述属于例外）。本单元点名的四类文档在现有规则里没有。
```

### U-srh-004

```
id: U-srh-004
category: protection
language: zh
rule_summary: 任何改写都不得新增原文没有的事实，也不得删掉原文的核心事实。
positive: 原文只说「上周做了一次演练」，改写后仍只说做了演练。（自造）
negative: 原文只说「上周做了一次演练」，改写成「上周做了一次全链路演练，覆盖了所有核心服务」。——违反点：补出了"全链路""覆盖所有核心服务"两项原文没有的事实。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 优先保信息，再谈风格。"
notes: |
  intent: 上游把这条写成"优先保信息，再谈风格"，是一条优先级声明而不只是禁令：它规定了风格规则在与信息冲突时让位。
  existing: 疑似对应 ALL-PROT-001（不得新增事实）与 ALL-PROT-003（不得默认摘要压缩）。
```

### U-srh-005

```
id: U-srh-005
category: protection
language: zh
rule_summary: 任何改写都不得改变责任主体，即不得改变一件事是谁做的、谁负责、谁受影响。
positive: 原文「配置由运维在周五改的」，改写后仍写明是运维改的。（自造）
negative: 原文「配置由运维在周五改的」，改写成「配置在周五被调整过」。——违反点：责任主体"运维"被隐去，读者无法判断是谁改的。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 优先保信息，再谈风格。"
notes: |
  intent: 责任主体在这份 skill 里被单列成一个与"事实"并列的保护对象，针对的是技术写作特有的风险：事故复盘、变更记录、issue 回复里"谁做的"就是全部信息，而去 AI 味的常见动作（改被动为主动、缩短句子、并句）恰恰最容易把主体挤掉。上游在 frontmatter 里也把"责任主体"写进了保护清单。
  existing: 疑似对应 ALL-P-004（指名动作的执行者，不用隐藏施事者的无主句和被动式）。ALL-P-004 是 pattern（要求写出执行者），本单元是 protection（不得改变执行者），判定方向不同，归并时不要合并成一条。
```

### U-srh-006

```
id: U-srh-006
category: protection
language: zh
rule_summary: 原文的量化表述有歧义时，保留原来的数量关系并标出待确认，不替作者修正成某一种数量关系。
positive: 原文「三个团队的两位负责人」读不出是共两位还是各两位，改写后保持原表述并标注待确认。（自造）
negative: 原文「三个团队的两位负责人」，改写成「三个团队各有两位负责人」。——违反点：替作者选了一种数量关系，把歧义消解成了确定表述。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 原文的量化表述有歧义时"
notes: |
  intent: 针对的现象是改写为了让句子通顺，必须在几种读法里选一种，于是歧义被静默消除。上游要求把这个选择还给作者：保留原关系＋标出待确认。这条同时防的是"改写读起来更清楚了，但清楚的是模型选的那个意思"。
  existing: 疑似对应 ALL-PROT-014（结论可能超出证据时不静默改动，风险写进"需作者确认"一节）与 ALL-PROC-004（读不明白先问）。数量关系的歧义在现有规则里没有单列。
```

### U-srh-007

```
id: U-srh-007
category: protection
language: zh
rule_summary: 任何情况下都不得补出原文没有的基数、年份、期限或测量结果。
positive: 原文只写「延迟降下来了」，改写后仍不写具体毫秒数。（自造）
negative: 原文只写「延迟降下来了」，改写成「延迟从 300ms 降到 80ms」。——违反点：补出了原文没有的测量结果。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 原文的量化表述有歧义时"
notes: |
  intent: 上游用"任何情况下"这个措辞，说明它把补数字列为无例外禁令——因为补出来的数字看起来最像"改写得更具体了"，也最难被读者发现是假的。四类对象（基数、年份、期限、测量结果）是模型最常自动补的四种。
  existing: 疑似对应 ALL-PROT-001。本单元点名的四类对象比 ALL-PROT-001 更具体，可以并进它的表述。
```

### U-srh-008

```
id: U-srh-008
category: pattern
language: zh
rule_summary: 不使用机械同义词替换表，也不得为了躲开重复而轮换同义词；同一个关键词该重复就重复。
positive: 一段里三次提到「灰度」都写「灰度」。（自造）
negative: 「先做灰度，这一轮小流量验证之后，再看这次分批放量的结果。」——违反点：同一个动作在三句里被换成三种说法，属于为躲重复而轮换同义词。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 不用机械同义词替换表"
notes: |
  intent: 上游明说「换词躲重复本身就是模型腔」，指出了一个反直觉的事实：重复在中文里是正常的，刻意避免重复才是模型的习惯（来自重复惩罚）。这条同时禁止了两件事：用同义词表做替换，以及为了不重复而换词。
  existing: 疑似对应 ALL-PROT-009（不得为避免重复而换称）、EN-P-019、EN-P-020。中文侧的同一规则在 §2 还有一次更具体的表述（U-srh-039），本单元是 Core stance 里的原则表述。
```

### U-srh-009

```
id: U-srh-009
category: process
language: zh
rule_summary: 默认允许删句、并句、降调、换主语、去掉总结式收尾；一旦进入 `in-place` scope，就只做句内改写。
positive: 默认 scope 下把两句事实合成一句，并删掉段末的总结句。（自造）
negative: 用户已要求一句都不删（`in-place`），改写时仍把两个相邻句合并成一句。——违反点：在 in-place 下做了并句，超出句内改写的范围。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 不用机械同义词替换表"
notes: |
  intent: 这条给"默认能改到什么程度"划了一条明线，防的是两个方向的错：一是不敢删，只做换词；二是拿到 in-place 授权后仍按默认动作集操作。它是 §3.5 Edit scope 的前置摘要，完整定义在那一节。
  existing: 疑似对应 ALL-PROC-012（拿到改写级授权时允许的动作）与 ALL-PROC-005（改动幅度按用户措辞定）。in-place 这一档在现有规则里没有对应。
```

### U-srh-010

```
id: U-srh-010
category: process
language: zh
rule_summary: 短语表默认只列代表项，不追求穷举变体；遇到词表里没有的新口癖，先按现有模式归类，只有当它改变了误杀边界或明显不属于任何现有模式时，才作为新增词条处理。
positive: 遇到「说到底还是」这个没收录的说法，判定它属于已有的"空总结"模式，按该模式处理，不新增词条。（自造）
negative: 遇到「说到底还是」，因为词表里没有就放行不处理。——违反点：没有先按现有模式归类，把"未收录"当成了"不命中"。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 短语表默认只列代表项"
notes: |
  intent: 中文口癖的变体是无穷的，穷举词表既做不到也会让词表失去可读性。上游的解法是把词表定位成"模式的样例"而不是"完整枚举"，并给出补词的两个门槛（改变误杀边界、不属于现有模式），防的是词表无限膨胀。
  existing: 疑似对应 ALL-PROC-028（判断以本 skill 的 references 为准，references 里没有的现象写进改动说明交给用户，不自行加规则）。两条的处理相反：ALL-PROC-028 要求交给用户，本单元要求先按现有模式归类。归并时需要对齐。
```

### U-srh-011

```
id: U-srh-011
category: process
language: zh
rule_summary: 按固定的八步顺序执行，不跳步：判场景 → 查禁改项 → 判 Tier → 判档位 → 判 scope → 执行规则 → 分两步回读 → 输出。
positive: 拿到文本先写下"场景：docs；protected spans：三处字段名；Tier 2；minimal；bounded"，再动手改。（自造）
negative: 拿到文本直接开始按词表逐句改，场景和 scope 都没有判定过。——违反点：跳过第 1 到第 5 步，直接进入第 6 步的执行。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## Execution order"
notes: |
  intent: 前五步都是判定、第六步才动手，这个顺序本身是规则：场景决定档位下限，protected spans 决定哪些地方不能碰，scope 决定能不能删整句——任何一项后判都会导致已经改过的地方要回退。上游明写"不要跳步"，说明它见过跳步的后果。
  existing: 疑似对应 ALL-PROC-001（动手改之前先确定体裁、读者、目的、语体并写成一行）。本单元的步骤更多且包含 scope 这一维。
```

### U-srh-012

```
id: U-srh-012
category: process
language: zh
rule_summary: 第二步固定要做两件事：划出 protected spans，并记一份事实与关系账本，账本至少包含实体类型、数字修饰的对象、每个主体各自的动作与目标、以及实现关系。
positive: 改前记下"『两个团队』的二修饰的是团队数；『企业』的目标是降本，『开发者』的目标是省事；A 基于 B 实现"。（自造）
negative: 改前只标出了不能动的字段名，没有记录主体与各自目标的配对。——违反点：账本缺了"主体与各自动作/目标"这一项。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## Execution order"
notes: |
  intent: 账本的四项不是随便选的，它们正好对应本 skill 后面列出的四类最常见漂移（实体类型被换、数字被挂到别的对象上、目标被并给错误的主体、实现关系被凭空建立）。先记账才能在回读时逐项核对，否则"信息有没有丢"无法判定。
  existing: 疑似对应 ALL-PROT-019（动手前先列两份清单，改完逐项核对）。本单元的账本项目与 ALL-PROT-019 的两份清单可以对齐，"实现关系"是本单元独有的一项。
```

### U-srh-013

```
id: U-srh-013
category: process
language: zh
rule_summary: 执行改写时先按模式处理，再按词条兜底：同一类调试腔、暴力动作腔、主动出击腔、总结提示腔按同一模式处理，不要求逐词命中词表。
positive: 「先把这块儿盘一盘」不在词表里，判定属于调试腔模式，按该模式处理。（自造）
negative: 因为「盘一盘」不在词表里就放行。——违反点：先查词条后查模式，颠倒了处理顺序，未命中词表就不处理。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "执行第 6 步时"
notes: |
  intent: 与 U-srh-010 是一对：010 讲要不要补词，本条讲执行时按什么顺序判。上游把模式放在词条之前，是因为词表永远追不上口癖的产生速度，而模式相对稳定。
  existing: 疑似对应 ALL-PROC-028。现有规则里没有"模式优先于词条"这一层顺序。
```

### U-srh-014

```
id: U-srh-014
category: genre
language: zh
rule_summary: 先判定主场景（`chat`、`status`、`docs`、`public-writing`）再处理局部问题；混合文本只保留一个主语域，其他语域只在必要信息层面留下。
positive: 一段既像站会同步又像公开帖，判定主场景为 status，公开帖的语气不保留，只保留其中的事实。（自造）
negative: 一段混合文本改完后前半是站会口吻、后半是公众号口吻。——违反点：没有收敛到一个主语域，两种语域都保留在了输出里。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 1. Scene detection"
notes: |
  intent: 场景是这份 skill 的第一层判断，因为同一句话在 chat 里正常、在 docs 里就是问题。"混合文本只保留一个主语域"针对的是语域漂移——它是本 skill 列出的四大病灶之一，而漂移最常见的成因就是原文本身跨了场景。
  existing: 疑似对应 ALL-G-002（体裁在语体之上叠加限制）与 EN-P-040（同一篇里的语域断裂提示拼接）。四场景的划分方式在现有规则里没有。
```

### U-srh-015

```
id: U-srh-015
category: genre
language: zh
rule_summary: `chat` 场景的信号是短回复、日常对话、协作沟通、评论、即时反馈；这类文本允许口语但不该端着说话，默认档位是 `minimal`。
positive: 一条群里的回复，只删掉开头的「好的，这是一个很好的问题」，其余不动。（自造）
negative: 一条群里的三句话回复，被重写成结构完整、带小标题的说明。——违反点：chat 场景默认 minimal，却做了结构级重写。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `chat`"
notes: |
  intent: chat 的默认档位定在最低，是因为日常对话本来就短、本来就该随便；对它做重改会立刻显得不自然。"不该端着说话"点出了 chat 场景真正的病灶：不是不够正式，而是过于正式。
  existing: 疑似对应 ALL-G-002。chat 作为独立场景及其默认档位在现有规则里没有。
```

### U-srh-016

```
id: U-srh-016
category: genre
language: zh
rule_summary: `status` 场景的信号是站会更新、进度同步、复盘摘要、汇报式状态说明，重点是时间线、动作、结果、风险；默认档位是 `minimal` 或 `standard`。
positive: 一条进度同步，改写后仍然按时间线—动作—结果—风险的顺序，只删掉套话。（自造）
negative: 一条进度同步被改写成一段流畅的叙述，时间线和风险项被并进了正文，读者要读完才知道有没有风险。——违反点：破坏了 status 场景要保住的四个重点结构。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `status`"
notes: |
  intent: status 是唯一一个给出"重点是哪四项"的场景，因为进度同步的读者是扫读的：他要找的是时间、做了什么、结果、有没有风险。去 AI 味如果把这四项揉进流畅的叙述里，读起来更像人，用起来更差。
  existing: 疑似对应 ALL-G-002。
```

### U-srh-017

```
id: U-srh-017
category: genre
language: zh
rule_summary: `docs` 场景的信号是操作文档、技术说明、接口说明、FAQ、事故复盘，重点是可检索、可复现、术语稳定；默认档位是 `minimal`。
positive: 一份操作文档只删掉开场白，步骤编号、术语和命令一个字不动。（自造）
negative: 一份操作文档里同一个术语被换成三种说法以避免重复。——违反点：破坏了 docs 场景要求的术语稳定，也让文档不可检索。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `docs`"
notes: |
  intent: 三个重点里"可检索"最容易被忽略：文档是拿来搜的，同一个概念换了说法，用户就搜不到。这解释了为什么本 skill 在 docs 场景里把"术语稳定"看得比"读起来自然"重。
  existing: 疑似对应 ALL-G-002 与 ALL-PROT-009。"可检索"这个理由在现有规则里没有出现过。
```

### U-srh-018

```
id: U-srh-018
category: genre
language: zh
rule_summary: `public-writing` 场景的信号是公众号、小红书、公开帖、对外文章、观点写作，重点是语域一致、不装「有洞见」；默认档位是 `standard`。
positive: 一篇公开帖统一用一种语域，删掉三处故作洞见的铺垫。（自造）
negative: 一篇公开帖里技术腔、商业腔和自媒体腔各占一段。——违反点：语域不一致，未收敛到一种。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `public-writing`"
notes: |
  intent: public-writing 是四个场景里默认档位最高的（standard），因为对外写作的 AI 味最重也最容易被读者认出来。"不要装有洞见"点名了这个场景的特征病灶：把普通判断包装成独家发现。
  existing: 疑似对应 ALL-G-002 与 EN-P-008（删掉故作洞见的铺垫）。
```

### U-srh-019

```
id: U-srh-019
category: genre
language: zh
rule_summary: 文本命中任一子场景信号（README、release-note、forum-post、issue-reply、api-reference、faq）时，不依赖用户是否明说，也不受主场景初判限制，都要按该子场景的策略处理。
positive: 一段文字里出现了安装方式和功能列表，即使用户没说这是 README，也按 README 子场景处理。（自造）
negative: 文本里有版本标题和 Added/Changed/Fixed 列表，但因为用户没说这是发布说明，就只按主场景 public-writing 处理。——违反点：子场景信号已命中却未触发，理由是用户没明说。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 子场景的触发条件被明确写成"不依赖用户是否明说"，针对的现象是用户贴一段 README 时不会声明它是 README，而 README 有一套只对它成立的要求（第一屏说清是什么）。"不受主场景初判限制"则防的是主场景判错时子场景跟着失效。
  existing: 现有规则里没有（现有的 ALL-G-002 按体裁叠加限制，但没有"信号触发、不依赖用户声明"这一层）。
```

### U-srh-020

```
id: U-srh-020
category: genre
language: zh
rule_summary: 文本是 README（出现项目介绍、快速开始、安装方式、功能列表、README intro 等信号）时，第一屏要说清这是什么、给谁用、解决什么问题。
positive: 第一段写「这是一个把 markdown 转成幻灯片的命令行工具，给写技术分享的人用，省掉排版这一步」。（自造）
negative: 第一屏写「本项目致力于为开发者提供更优雅的内容创作体验」。——违反点：读完不知道它是什么、给谁用、解决什么问题。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: README 的第一屏是读者决定要不要继续看的地方，而 AI 写的 README 开头几乎必然是一句可以套在任何项目上的价值宣言。三问（是什么、给谁用、解决什么问题）把这个场景的验收变成可判定的。
  existing: 现有规则里没有（现有的 ALL-M-001 可移植性测试可以判出反例，但没有 README 专属的三问要求）。
```

### U-srh-021

```
id: U-srh-021
category: genre
language: zh
rule_summary: 文本是发布说明（出现版本标题、Release Highlights、Added / Changed / Fixed / Tested、changelog 列表等信号）时，列清本版的变更、验证和限制，不写发布宣言。
positive: 「新增批量导入；修复了并发下的重复写入；本版未覆盖 Windows。」（自造）
negative: 「这一版是我们在性能之路上迈出的关键一步，未来我们将持续为用户带来更好的体验。」——违反点：整段是发布宣言，没有列出任何变更、验证或限制。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 三项内容（变更、验证、限制）里"限制"最容易被删掉——它读起来负面，而 AI 的发布说明倾向于只留正面的部分。上游把它写进必须项，防的是改写把已知限制洗掉。
  existing: 疑似对应 ALL-G-002。发布说明的三项必须内容在现有规则里没有。
```

### U-srh-022

```
id: U-srh-022
category: genre
language: zh
rule_summary: 文本是论坛帖（出现社区帖、发帖复盘等信号）时，保留维护者的真实观察和社区语气，不改成公告。
positive: 保留「我自己用下来最烦的是每次都要重新登录」这句原话和它的口气。（自造）
negative: 把「我自己用下来最烦的是每次都要重新登录」改成「经实际使用验证，重复登录问题影响了使用体验」。——违反点：把维护者的第一人称观察改成了公告语气。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 论坛帖的价值恰恰在于它不是公告：真实的观察、带情绪的判断、没修饰的语气，是读者判断可信度的依据。去 AI 味在这个场景里最容易好心办坏事——把帖子改"规范"了，就把它改成了另一种模板。
  existing: 疑似对应 ALL-PROT-017（作者的词汇、直率程度、犹疑属于作者）。
```

### U-srh-023

```
id: U-srh-023
category: genre
language: zh
rule_summary: 文本是 issue 或 PR 回复（出现 bad case、复现、下一版补 benchmark 等信号）时，先确认问题和下一步，不做客服式安抚。
positive: 「确认能复现，是并发下的竞态。下一版修，会补一个回归用例。」（自造）
negative: 「非常感谢您的反馈！我们非常重视每一位用户的意见，会尽快跟进处理。」——违反点：整条是客服式安抚，没有确认问题，也没有下一步。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: issue 回复的读者要的是两件事：你认不认这个问题、下一步是什么。客服话术把这两件事都省了，还显得在敷衍。这条与本 skill 关于"过度接住"的规则同源：都是拒绝用姿态替代内容。
  existing: 疑似对应 EN-P-028（删掉聊天残留与谄媚）。issue 回复要"先确认问题和下一步"这个正向要求在现有规则里没有。
```

### U-srh-024

```
id: U-srh-024
category: genre
language: zh
rule_summary: 文本是接口文档（出现 endpoint、HTTP 方法、参数字段、类型或默认值、状态码或错误码、鉴权、请求响应示例等信号）时，删掉宣传和元评论；接口合同有缺失时只标出待确认，不替作者补。
positive: 删掉「本接口设计简洁优雅」，保留全部字段与状态码；发现某字段没写默认值，标注「默认值待确认」。（自造）
negative: 发现某字段没写默认值，按常见做法补上「默认为 false」。——违反点：替作者补了缺失的接口合同。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 接口文档是"补一个看起来合理的值"后果最严重的场景：读者会照着调用。上游在这一节同时要求 method、path、字段、约束、字面量与恢复动作零漂移（这几项在本清单里按保护对象各自成条），本单元只承担这个子场景的两条特有要求。
  existing: 疑似对应 ALL-PROT-001 与 ALL-PROC-004（缺失部分影响事实时先问）。接口合同缺失只标不补这条在现有规则里没有。
```

### U-srh-025

```
id: U-srh-025
category: genre
language: zh
rule_summary: 文本是 FAQ 或排障问答（出现 FAQ、常见问题、排障问答等发布结构）时，尽早给出结论或动作。
positive: 「先重启服务。如果还不行，再看下面第 3 条。」（自造）
negative: 「这个问题涉及多个层面。首先我们需要理解缓存的工作机制……」（三段之后才说该怎么做）——违反点：FAQ 里结论和动作被推到了最后。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: FAQ 的读者是带着一个具体故障来的，铺垫对他没有价值。这条是这个子场景唯一的正向结构要求，紧接着的三条限制（本清单 U-srh-026 至 U-srh-028）都是给它设边界的。
  existing: 疑似对应 ALL-G-002。
```

### U-srh-026

```
id: U-srh-026
category: protection
language: zh
rule_summary: 在 FAQ 里把结论前置时，原本在操作前的执行条件和警告不得因此挪到操作后，真实的事后检查和失败分支也不得改成前置步骤。
positive: 「先停写入（否则会丢数据），再执行迁移。」——警告仍在操作之前。（自造）
negative: 「先执行迁移。注意：执行前需要先停写入，否则会丢数据。」——违反点：把操作前的警告挪到了操作之后，读者按顺序执行就会踩坑。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 这是本 skill 里对"条件关系"保护得最具体的一条：条件和警告的位置本身就是信息，前置还是后置决定读者会不会踩坑。它针对的现象是"结论先行"这条写作建议被机械执行，把顺序敏感的内容也重排了。
  existing: 疑似对应 ZH-P-009（限定适用范围的条件、时间和对象要出现在被限定内容之前）与 ALL-PROT-020（删改时保留真实存在的逻辑关系）。ZH-P-009 管句内位置，本单元管步骤之间的顺序，判定对象不同。
```

### U-srh-027

```
id: U-srh-027
category: protection
language: zh
rule_summary: 改写 FAQ 时不得扩大问题的适用范围、否定、期限与支持承诺，也不得补出原文没有的操作。
positive: 原文「2.3 之后的版本不支持」，改写后仍限定在 2.3 之后。（自造）
negative: 原文「2.3 之后的版本不支持」，改写成「旧版本均不支持」。——违反点：把一个有版本边界的否定扩大成了无边界的否定。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: FAQ 里的每一句都会被当成承诺来读，所以范围、否定、期限、支持这四类的边界一旦被改宽，就变成了对用户的错误保证。上游把它们并列，是因为它们共用同一种漂移方式：改写为了句子更利落，去掉了限定词。
  existing: 疑似对应 ALL-PROT-020 与 ALL-PROT-004。四类对象（范围、否定、期限、支持承诺）在现有规则里没有点名。
```

### U-srh-028

```
id: U-srh-028
category: genre
language: zh
rule_summary: 不得把采访或讨论式问答重新包装成 FAQ 结构。
positive: 一段访谈问答保留原来的问答形态和口语，不改成「常见问题」小节。（自造）
negative: 把一段两人对谈整理成「Q：……A：……」的 FAQ 小节。——违反点：把讨论式问答套成了 FAQ 发布结构，读者会以为这是官方答复。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: FAQ 是一种有权威含义的发布结构：它意味着"这是官方答案"。把访谈或讨论套进这个壳子，等于给一段个人观点加上了官方背书，是体裁层面的失真。
  existing: 现有规则里没有。
```

### U-srh-029

```
id: U-srh-029
category: process
language: zh
rule_summary: 子场景只负责收束发布目的和语气，不覆盖 protected spans、Tier、档位和回读规则。
positive: 判定为 issue-reply 之后仍然照常划 protected spans、判 Tier 和档位，回读两遍不省。（自造）
negative: 判定为 forum-post 之后，认为社区场景比较随意，跳过了 protected spans 的检查。——违反点：用子场景覆盖了 protected spans 这条不受子场景管辖的规则。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Scene Packs"
notes: |
  intent: 上游给子场景机制加了一条作用域声明，防的是"场景特例"被用来绕开保真规则。它对应 SKILL.md 全局的优先级安排：保护对象在任何场景下都不让步。
  existing: 疑似对应 ALL-PROC-023（仲裁顺序，事实与原意排第一）与 ALL-PROC-010（体裁只调整触发门槛和改动幅度，不得整组跳过）。
```

### U-srh-030

```
id: U-srh-030
category: process
language: zh
rule_summary: 只加载 SKILL.md 时，本文件里的兜底规则默认直接生效；但只要环境里能读 `references/`，就必须继续按问题类型补看对应文件，只有在系统提示确实只给了 SKILL.md 时才停留在兜底规则。
positive: 环境能读 references/，处理无源引用前补看对应的模式文件，再动手。（自造）
negative: 环境能读 references/，仍然只按 SKILL.md 的兜底规则改完交付。——违反点：在可以读 references 的情况下停留在了兜底模式。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "单文件模式只是兜底"
notes: |
  intent: 上游把 SKILL.md 设计成"能单独工作但不完整"，针对的是安装方式的不确定：有的环境只注入主文件。这条规则确保两种情况下都有确定行为，同时不让兜底模式变成默认路径。
  existing: 疑似对应 ALL-PROC-028（判断以 references 为准）。"单文件兜底"这个机制在现有规则里没有。本单元涉及上游自己的目录结构，归并时多半只作为流程参考，不进本仓库 skill。
```

### U-srh-031

```
id: U-srh-031
category: pattern
language: both
rule_summary: 删掉开场套话、谄媚和元评论，例如「值得注意的是」「让我来为你解释」「希望这对你有帮助」「Great question!」。
positive: 直接从内容开始：「这个字段默认关闭。」（自造）
negative: 「让我来为你解释一下这个字段。值得注意的是，它默认是关闭的。希望这对你有帮助！」——违反点：「让我来为你解释」是元评论，「值得注意的是」是开场套话，「希望这对你有帮助」是谄媚收尾。（自造）
positive（英文）: "The field is off by default." ——直接从内容开始。（自造）
negative（英文）: "Great question! Let me walk you through how this field works." ——违反点："Great question!" 是谄媚开场，"Let me walk you through" 是元评论。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 删开场套话、谄媚和元评论"
notes: |
  intent: 这三类共用同一条判定逻辑（删掉之后句子的信息不变），所以上游放在一条里。它们是助手对话残留在正文里的痕迹，出现位置固定在段首和段尾。词表照录自上游，说明文字为重写。
  existing: 疑似对应 ZH-P-001（含"值得注意的是"）与 EN-P-028（删掉聊天残留与谄媚）。
```

### U-srh-032

```
id: U-srh-032
category: pattern
language: both
rule_summary: 删掉空总结和收尾腔，例如「综上所述」「归根结底」「本质上」「At the end of the day」。
positive: 段落停在最后一条具体信息上，不加总结句。（自造）
negative: 「综上所述，归根结底，这件事本质上还是一个协作问题。」——违反点：一句里叠了「综上所述」「归根结底」「本质上」三个空收尾。（自造）
positive（英文）: "The rollback took eleven minutes." ——段落停在最后一条具体信息上。（自造）
negative（英文）: "At the end of the day, it all comes down to collaboration." ——违反点："At the end of the day" 是空收尾，整句没有新增信息。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 删空总结和收尾腔"
notes: |
  intent: 空总结的判据是"删掉之后不丢信息"——它只是把上文重说一遍并抬高一级。上游在 Pass 2 的残留检查里又列了一次（总结残留），说明它是最难删干净的一类：删了一处，模型会在别处再生成一处。词表照录自上游，说明文字为重写。
  existing: 疑似对应 ZH-P-001（含"综上所述"）与 EN-P-023（结尾停在最后一个具体事实上）。
```

### U-srh-033

```
id: U-srh-033
category: pattern
language: zh
rule_summary: 处理二元对比骨架「不是 X，而是 Y」「与其 X，不如 Y」时，多数情况删掉前半句，直接说 Y。
positive: 「这是排期问题。」（自造）
negative: 「这不是技术问题，而是排期问题。」——违反点：用二元对比骨架承担对比，前半句「不是技术问题」不承载信息。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 处理二元对比骨架"
notes: |
  intent: 上游给的处理动作很具体——删前半句——因为这个骨架的前半通常是模型自己造出来的假对立，读者从没提出过"这是技术问题"。措辞是"多数删"，留了前半句确实在回应某个真实主张时的余地。
  existing: 疑似对应 ALL-P-005 与 EN-P-006（拆掉二元对比和否定式排比，直接陈述结论）。中文的「与其 X，不如 Y」在现有中文规则里没有。与 ai-zixun 的 U-azh-026 是同一条规则。
```

### U-srh-034

```
id: U-srh-034
category: pattern
language: both
rule_summary: 把商业黑话和表演性技术腔改回普通动作，例如「赋能」「抓手」「闭环」「收窄」「兜住」「落盘」「leverage」。
positive: 「把这批数据写进库里。」（自造）
negative: 「先把这批数据落盘，再看能不能兜住下游的抖动。」——违反点：「落盘」「兜住」是表演性技术腔，换成普通动作后信息不变。（自造）
positive（英文）: "We can use the existing pipeline here." ——普通动作，信息不变。（自造）
negative（英文）: "We can leverage the existing pipeline here." ——违反点："leverage" 是商业黑话，直接写 use 信息不变。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 把商业黑话和表演性技术腔改回普通动作"
notes: |
  intent: 上游把"商业黑话"和"表演性技术腔"合成一类，因为它们的机制相同：用一个圈内词代替一个普通动作，让说话的人显得在行。判据是能不能换成普通动作而信息不变——能，就是表演。注意它与 U-srh-097 的分工：同一个词（如"闭环"）在讨论机制时保留，在包装进展时改写。词表照录自上游，说明文字为重写。
  existing: 疑似对应 ZH-P-001（含"赋能""抓手""闭环"）与 EN-P-001（英文禁用词表，含 leverage）。「收窄」「兜住」「落盘」在现有中文词表里没有。
```

### U-srh-035

```
id: U-srh-035
category: pattern
language: zh
rule_summary: 遇到过度接住、替用户做心理判断或身份认证式夸奖（例如「你不是敏感」「你只是太久没被稳稳接住了」「你问到了问题的核心」「顶刊作者的素养」），默认删掉姿态层，改回低承诺回应或具体判断，不硬演「我懂了」。
positive: 「这个问题我也没有把握，我能说的是第二种做法在我们这边跑通过。」（自造）
negative: 「你问到了问题的核心。你不是想太多，你只是太久没有被认真回应过了。」——违反点：两句都是姿态层，替对方下了心理判断，没有任何具体回应。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 遇到过度接住、替用户做心理判断或身份认证式夸奖"
notes: |
  intent: 这是中文对话模型近年最显眼的一类口癖，上游给了它一个准确的名字（姿态层）：这些句子不传达内容，只表演理解和接纳。"不要硬演我懂了"是这条规则的判据——判断自己有没有在表演共情，而不是判断某个词在不在词表里。
  existing: 疑似对应 EN-P-028（谄媚）与 ALL-PROT-012（不得据文本评价作者）。中文的"过度接住"和"身份认证式夸奖"在现有规则里完全没有对应，是本来源的显著增量。
```

### U-srh-036

```
id: U-srh-036
category: protection
language: zh
rule_summary: 方向或进度认证式的判断（例如「走在正确的路上」「完全不用担心」）只能删除或标注为「现有信息不足以判断」，不得降格成「方向没问题」「不用太担心」这类弱安抚继续替对方下结论。
positive: 把「你完全不用担心」删掉，或改成「就现在给的信息，我判断不了这样会不会出问题」。（自造）
negative: 把「你完全不用担心」改成「应该问题不大」。——违反点：只是降低了强度，仍在替对方下没有依据的结论。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 遇到过度接住、替用户做心理判断或身份认证式夸奖"
notes: |
  intent: 这条堵的是执行 U-srh-035 时最常见的偷懒方式——把强安抚改成弱安抚，看起来收敛了，实质没变：仍然是在没有依据的情况下替对方判断"没问题"。上游要求的是二选一：删掉，或者明说信息不足。
  existing: 现有规则里没有。这是本来源在"共情腔"上最细的一条，归并时值得单独立条。
```

### U-srh-037

```
id: U-srh-037
category: pattern
language: zh
rule_summary: 发现翻译腔时优先缩短主语和动作，少用长定语链、被动堆砌、「基于……」「通过……来……」。
positive: 「运维周五改了配置。」（自造）
negative: 「基于对当前系统稳定性的综合考量，相关的配置调整已由运维团队于上周五通过变更流程来完成。」——违反点：「基于……」开头、长定语链、被动式「已由……完成」和「通过……来……」四处翻译腔叠加，主语和动作被埋在句末。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 发现翻译腔时"
notes: |
  intent: 上游给的处理动作是"优先缩短主语和动作"，不是"删掉某个词"——因为翻译腔是结构问题：中文的主干被英文式的状语和定语推到了后面。四个具体信号（长定语链、被动堆砌、基于、通过……来）是这个结构问题在中文里的可见形态。
  existing: 疑似对应 ZH-P-008（主语和谓语之前有两层以上前置状语即命中）与 ZH-P-011（unverified）。与 ai-zixun 的 U-azh-024、U-azh-025 是同一主题。
```

### U-srh-038

```
id: U-srh-038
category: pattern
language: zh
rule_summary: 把名词化结构还原成动词：「进行 / 实现 / 完成 / 开展 / 起到 / 具有」带一个动名词是典型信号；公文固定表述和 `docs` 里的稳定术语除外。
positive: 「对流程进行了优化」改成「把流程改顺了」；「实现了效率的提升」改成写清快了多少、省了几个人。（引自上游示例）
negative: 「本次变更对现有流程进行了优化，并实现了整体效率的提升。」——违反点：「进行了优化」「实现了……提升」两处名词化，把两个动作写成了名词。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 把名词化还原成动词"
notes: |
  intent: 名词化是中文公文腔最稳定的标志，也是信息被抹掉的地方：「实现了效率的提升」不需要说明快了多少，「快了多少」必须给数。上游给的六个动词是可以直接匹配的触发词，例外条款（公文固定表述、docs 稳定术语）防的是把正式文体的必要表述也拆掉。
  existing: 疑似对应 ZH-P-011（"进行＋动词"代替直接动词，decision 为 unverified）与 EN-P-016（用直接动词代替绕弯子的动词短语）。本单元给了六个触发词和两条例外，可以把 ZH-P-011 的这一半变成可判定的。
```

### U-srh-039

```
id: U-srh-039
category: pattern
language: zh
rule_summary: 同一个对象不要在相邻几句里换三种说法（例如「修表 → 这门手艺 → 这项技能」），关键词重复是正常中文，逐次升格换词是模型腔；代词照应不算违反。
positive: 「修表这门活我干了十年。修表不挣钱，但我不想改行。」（自造）
negative: 「修表我干了十年。这门手艺越来越少人做。这项技能在今天已经很难变现。」——违反点：同一个对象在三句里被逐次升格成"手艺""技能"，属于换词躲重复。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 同一个对象不要在相邻几句里换三种说法"
notes: |
  intent: "逐次升格"是这条规则最准的观察：换词不是随机的，每换一次都更抽象、更文雅，因为模型在避免重复的同时也在追求"更好的词"。加上"代词照应不算"这条例外，规则才可判定——否则正常的中文指代会被误判。
  existing: 疑似对应 ALL-PROT-009、EN-P-019、EN-P-020。中文侧的"逐次升格"现象和"代词照应不算"的例外在现有规则里没有。
```

### U-srh-040

```
id: U-srh-040
category: protection
language: zh
rule_summary: 清理姿态层时按子句和事实要素判断，不按整句或整行一刀切；删掉某个子句如果会改变命题真值、适用范围或成立条件，它就是保真对象，不是可以随姿态一起删掉的空话。
positive: 「这个做法在单机上没问题（前提是并发不超过十）」——删掉姿态词，保留括号里的成立条件。（自造）
negative: 整句删掉「这个做法在单机上没问题，前提是并发不超过十」，理由是这句读着像套话。——违反点：删掉的子句承载着成立条件，删后命题的适用范围变了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 清理姿态层时按子句和事实要素判断"
notes: |
  intent: 这是姿态层清理的安全阀：姿态词和实质内容常常长在同一句里，整句删掉最省事也最危险。上游给的判据（删掉会不会改变真值、适用范围、成立条件）是可以逐句执行的。
  existing: 疑似对应 ALL-PROT-020（删掉无功能连接词时保留真实逻辑关系）与 ALL-P-010（不得靠删信息把句子变短）。"按子句而不是整句判断"这个操作要求在现有规则里没有。
```

### U-srh-041

```
id: U-srh-041
category: process
language: zh
rule_summary: 输出前做双向核对：先确认输入里的范围、条件、否定、情态、完成态、方向和强度在输出里能逐项找回，再确认输出里新增或改写的每个关系都能回指到输入的依据。
positive: 逐项核对后确认「只在测试环境」「尚未」「变慢」这三项在改写稿里都在，且改写稿里没有输入中不存在的关系。（自造）
negative: 只检查了改写稿有没有丢信息，没有反过来检查改写稿里多出来的关系有没有依据。——违反点：只做了输入到输出这一个方向，漏掉了输出回指输入这一半。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 清理姿态层时按子句和事实要素判断"
notes: |
  intent: 两个方向分别防两种错：输入→输出防丢信息，输出→输入防加信息。上游列的七项（范围、条件、否定、情态、完成态、方向、强度）是这份 skill 对"条件关系"的完整定义，后面 Pass 1 回读又原样重复了一次，说明它是核心检查项。
  existing: 疑似对应 ALL-PROT-019（改完逐项核对两份清单）。七项条件关系的具体列举是本来源的增量，现有规则只笼统写"关系没变"。
```

### U-srh-042

```
id: U-srh-042
category: protection
language: zh
rule_summary: `code-context` 里的真实运行行为、适用条件和边界说明属于 protected spans；清理注释、docstring 或 commit message 时只去掉姿态词，保留这些信息。
positive: 注释「这里必须先加锁，否则并发写会丢数据（实测 8 线程以上必现）」——只删掉多余的语气词，运行行为和条件保留。（自造）
negative: 把上面那条注释精简成「这里加锁」。——违反点：删掉了"否则并发写会丢数据"和"8 线程以上必现"，这两项是真实运行行为和边界说明。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- `code-context` 里的真实运行行为"
notes: |
  intent: 代码注释是本 skill 唯一为"非散文"留的场景。注释里的姿态词确实该删，但注释同时是唯一记录"为什么这么写"的地方，删多了信息就永久丢了。上游把三类（运行行为、适用条件、边界说明）列成 protected spans，等于把注释当成技术文档而不是散文。
  existing: 疑似对应 ALL-PROC-016（扫描前把代码块整体标出跳过）与 ALL-PROC-017（源代码文件停手）。现有规则的做法是整体跳过，本单元的做法是允许改但限定改什么，两者是不同的处理策略，归并时需要裁决。
```

### U-srh-043

```
id: U-srh-043
category: protection
language: zh
rule_summary: 不得因为相邻行已经有指标或结果，就认定某一行重复而整行删除。
positive: 相邻两行分别写「P99 降到 80ms」和「这条链路上的重试基本没有了」，两行都保留。（自造）
negative: 因为上一行已经给了 P99 数字，就把下一行「这条链路上的重试基本没有了」整行删掉。——违反点：以"相邻行已有结果"为由删掉了另一项独立信息。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- `code-context` 里的真实运行行为"
notes: |
  intent: 针对的是一种很具体的误判：两行都在讲"效果"，模型据此认为是重复表述，其实一行讲延迟、一行讲重试，是两件事。判据是内容是否相同，不是主题是否相同。
  existing: 疑似对应 ALL-PROT-003（独立的事实一律保留）与 ALL-P-011（同一个意思绕几遍才删）。"相邻行主题相同不等于内容重复"这个判据在现有规则里没有。
```

### U-srh-044

```
id: U-srh-044
category: protection
language: zh
rule_summary: 抽象信息与实体类型不得擅自具体化、合并、互换或删除：「方案」不能改成「工具」或「产品」，「目标」不能改成「产品」，描述某种架构的潜力不能改成「系统基于该架构构建」。
positive: 原文写「这个方案」，改写后仍写「这个方案」。（自造）
negative: 原文「这套方案有可能支撑更大的规模」，改写成「这个产品基于该架构构建，能支撑更大的规模」。——违反点：把实体类型从"方案"换成了"产品"，并把"有可能支撑"的潜力改成了已实现的构建关系。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 实体类型的漂移是一种很隐蔽的失真：方案、工具、产品在中文里都可以指"那个东西"，但它们对读者承诺的完成度完全不同（方案是想法，产品是已经存在的东西）。上游把它排在这一长段的第一条，说明它见过这类漂移的后果。
  existing: 现有规则里没有（现有 ALL-PROT-001 管新增事实，本单元管的是已有实体被换了类型，属于同一族但判定对象不同）。
```

### U-srh-045

```
id: U-srh-045
category: protection
language: zh
rule_summary: 数字与它所修饰的对象的配对关系必须一起保留，不得把数字挂到别的对象上（不能把「两个团队」写成「换过两个团队」）。
positive: 原文「两个团队一起做的」，改写后仍写两个团队。（自造）
negative: 原文「两个团队一起做的」，改写成「换过两个团队」。——违反点：数字"二"从"参与的团队数"被挂到了"更换次数"上。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 数字本身没被改，改的是它修饰谁——这类错误在核对"数字有没有改"时查不出来，所以上游要求在第二步的账本里专门记"数字修饰对象"。这是这份 skill 对数字保护最有价值的一条。
  existing: 疑似对应 ALL-PROT-002（数字不得改写成概括说法）。ALL-PROT-002 管数字本身，本单元管数字与对象的绑定，现有规则里没有。
```

### U-srh-046

```
id: U-srh-046
category: protection
language: zh
rule_summary: 主体与各自动作或目标的配对关系必须一起保留，不得把只属于某一方的目标顺手并给另一方。
positive: 原文「企业想降本，开发者想少写重复代码」，改写后两个目标仍分属两方。（自造）
negative: 改写成「企业和开发者都想降本增效」。——违反点：把只属于企业的目标并给了开发者，主体与目标的配对被打乱。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 合并同类项是改写时最自然的简化动作，而"两个主体各有目标"看起来就是同类项。上游点名这一条，是因为合并之后句子更短更整齐，错误却不容易被发现。
  existing: 疑似对应 ALL-PROT-003 与 U-srh-005（责任主体）。主体—目标配对在现有规则里没有单列。
```

### U-srh-047

```
id: U-srh-047
category: protection
language: zh
rule_summary: 谓词的方向、完成态、强度和效果类型属于关系，必须保留：「性能提升 / 体验改善 / 安全性加强」不得弱化成「涉及这些方面」，「提升效率」也不得扩写成「节省时间 / 成本」。
positive: 原文「安全性加强了」，改写后仍写明是加强，不写成"在安全性方面做了工作"。（自造）
negative: 原文「性能提升、体验改善、安全性加强」，改写成「在性能、体验和安全性方面都有涉及」。——违反点：三个已完成的正向谓词被弱化成了"涉及"，方向和完成态都丢了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 上游同时点了两个方向的错：弱化（提升→涉及）和扩写（提升效率→节省成本）。前者常发生在"避免夸大"的动机下，后者常发生在"写得更具体"的动机下——两种都改变了原文实际声称的东西。
  existing: 疑似对应 ALL-PROT-004、ALL-PROT-005。谓词的"效果类型"（效率≠成本）在现有规则里没有。
```

### U-srh-048

```
id: U-srh-048
category: protection
language: zh
rule_summary: 删掉「显著」「大幅」这类渲染词时，仍要保留原文实际声称发生了什么。
positive: 「显著缩短了构建时间」改成「构建时间缩短了」。（自造）
negative: 「显著缩短了构建时间」改成「对构建时间做了优化」。——违反点：删渲染词的同时把"缩短了"这个已发生的结果也改没了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 渲染词和它修饰的动词长在一起，删词时容易把动词一起改软。上游要求分清两件事：夸张的程度可以删，发生过的事不能删。
  existing: 疑似对应 ALL-PROT-020（删修饰时保留真实关系）与 U-srh-047。
```

### U-srh-049

```
id: U-srh-049
category: protection
language: zh
rule_summary: 背景、主题或相邻句共现不等于能力关系；输出里任何「X 用来做 Y」「X 基于 Y」「X 处理 Y」都必须能在原文的谓词里找到依据。
positive: 原文同段提到了 AI 和一个中文表达工具，改写后不写"这个工具处理 AI 生成的文本"，因为原文没有这个谓词。（引自上游的判例）
negative: 原文同段提到 AI 和中文表达工具，改写成「这是一个处理 AI 生成文本的中文工具」。——违反点：两个概念只是同段共现，原文没有任何谓词表达"处理"这个关系。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 这条抓的是模型最典型的一种编造：不是凭空造事实，而是把同一段里出现的两个东西连起来，连接词看起来非常合理。上游给的判据很硬——必须能回指原文的同一个谓词，共现不算。
  existing: 现有规则里没有。这是本来源在保真上最有价值的一条，归并时建议单独立条。
```

### U-srh-050

```
id: U-srh-050
category: protection
language: zh
rule_summary: 目的、适用条件、风险和限制即使对象仍然抽象也属于信息：「为了解决这一痛点」可以压成「为了解决这个问题」，但不能因为没写清是什么问题就把「解决问题」这个目的整个删掉。
positive: 「为了解决这个问题，团队加了一层缓存。」（自造）
negative: 原文「为了解决这一痛点，团队加了一层缓存」，改写成「团队加了一层缓存」。——违反点：因为"痛点"抽象就把目的删掉了，读者不再知道这个动作是为了解决问题。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 去 AI 味会培养出一种反射：抽象的就是空的，空的就删。上游在这里区分了两件事——抽象的措辞可以压缩，抽象的信息不能删。目的、条件、风险、限制这四类即使写得很虚，也仍然告诉了读者一些东西。
  existing: 疑似对应 ALL-P-010（简化只处理表达障碍，不得靠删信息把句子变短）与 ALL-PROT-020。四类对象的点名在现有规则里没有。
```

### U-srh-051

```
id: U-srh-051
category: protection
language: zh
rule_summary: 原文没有具体能力、实现关系或对象时，允许保留原来的抽象层级、把表述缩短、或标注缺口，但不得用看起来合理的新事实给句子补一个落点。
positive: 原文只说「这套东西还在早期」，改写后保持同样的抽象层级，或标注"具体做到哪一步待确认"。（自造）
negative: 原文只说「这套东西还在早期」，改写成「目前已完成核心模块，正在做接口联调」。——违反点：用两项听起来合理的新事实给句子补了落点。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 抽象信息、实体类型和关系不能擅自具体化"
notes: |
  intent: 这条给"写具体"这个普遍要求设了上限：具体的来源只能是原文。上游给出了三个合法出口（保留抽象、缩短、标注缺口），等于告诉执行者遇到没有落点的句子该怎么办——否则"必须具体"这条规则本身就会逼出编造。
  existing: 疑似对应 ALL-P-007（原文里找不到就标出缺口去问，不得自己编）。两条几乎一致，归并时大概率合并。
```

### U-srh-052

```
id: U-srh-052
category: process
language: zh
rule_summary: 中英混排句子里的英文词，按它在当前句子里的实际语义判断要不要改，不机械套用英文词表。
positive: 「这次的 key 是配置文件里的那个键名」——判定 key 是字段名而不是英文高频词 key，保留。（自造）
negative: 因为 key 在英文 AI 词表里，就把「配置里的 key」改成「配置里的关键项」。——违反点：机械套用英文词表，没有判断这个词在当前句子里的实际语义。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 中英混排句中的英文词"
notes: |
  intent: 中文技术写作里英文词大量出现，而它们多数是术语不是修辞。直接套英文 AI 词表会造成成片误杀，这条是中文场景特有的防误杀规则。
  existing: 疑似对应 ALL-PROT-009 与 EN-M-001（英文高频词分档处理）。"中英混排时不套英文词表"在现有规则里没有，是中文侧的重要缺口。
```

### U-srh-053

```
id: U-srh-053
category: process
language: zh
rule_summary: 处理无源引用（「研究表明」「数据显示」「studies show」「experts say」）时，固定只在 `rewrite-safe`、`audit-only`、`rewrite-with-placeholder` 三种模式里选一种，任何模式下都不得补虚构来源。
positive: 判定当前场景是 docs，选 `audit-only`，指出这里缺来源。（自造）
negative: 遇到「研究表明」，直接补上一个看起来合理的机构名和年份。——违反点：补了虚构来源，且不在任何一种允许的模式里。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: 上游没有给一个统一处理方式，而是给了三种并要求显式选择，因为无源引用的正确处理取决于场景：对外写作里应该删，文档里应该标，编辑稿里可以留占位。强制选择防的是"随手改一改"。
  existing: 疑似对应 EN-P-017（模糊归因要点名来源或删掉整个论断）与 ALL-PROT-001。三模式机制在现有规则里没有。
```

### U-srh-054

```
id: U-srh-054
category: process
language: zh
rule_summary: `rewrite-safe` 模式下，去掉「研究表明 / studies show / 业内人士认为」之后，只有不依赖该来源也能独立成立的判断才保留；如果数字、预测或结论本身全靠这条无源引用成立，删掉整条论断。默认用于 `chat` 和 `public-writing`。
positive: 「业内人士认为这类工具三年内会普及」——整条依赖该来源，删掉。（自造）
negative: 「业内人士认为这类工具三年内会普及」改成「这类工具三年内会普及」。——违反点：只删了权威铺垫，把完全依赖该来源的预测留了下来，还变成了作者自己的断言。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: 这条防的是最常见的错误处理：把"专家说 X"改成"X"。删掉归属之后，一个没有依据的说法反而变成了作者的直接主张，可信度问题不但没解决，还加重了。判据是"去掉来源之后这句还站不站得住"。
  existing: 疑似对应 EN-P-017。"删掉归属会让论断变成作者主张"这个判据在现有规则里没有明写。
```

### U-srh-055

```
id: U-srh-055
category: protection
language: zh
rule_summary: 处理无源论断时不得删掉数字后留下更泛的同向断言：不能删掉「40%」改成「会更快」，也不能把「未来十年」改成「未来几年」。
positive: 「研究表明效率能提升 40%」——整条删掉，或保留原样并标注缺来源。（自造）
negative: 「研究表明效率能提升 40%」改成「效率会有明显提升」。——违反点：删掉数字之后留下了一个方向相同但更模糊的断言，等于把无依据的说法变得更难核查。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: 这是 U-srh-054 的具体化，抓的是一种看起来很负责任的错误：把可疑的精确数字改成模糊表述。上游指出这样做没有降低风险，只是让错误不可验证了。
  existing: 疑似对应 ALL-PROT-002（数字不得改写成概括说法）。ALL-PROT-002 的理由是丢信息，本单元的理由是让无依据的断言变得不可核查，两条理由互补。
```

### U-srh-056

```
id: U-srh-056
category: process
language: zh
rule_summary: `audit-only` 模式下不替作者补写来源，也不把无证据判断改写成像是已有证据；明确指出这里缺来源或缺归属，必要时保留原句不重写。默认用于 `docs` 和 `status`。
positive: 「数据显示这条链路最慢」保留原句，另起一行标注"这里缺来源"。（自造）
negative: 「数据显示这条链路最慢」改成「监控数据表明这条链路最慢」。——违反点：把无证据判断改写得更像已有证据，等于替作者加了一层可信度。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: docs 和 status 里的无源引用不适合删——那里的每句话可能都是工作依据，删掉会丢事实。审计模式把问题暴露给作者，由作者补来源。这是三种模式里最保守的一种，所以也是跨场景时的默认。
  existing: 疑似对应 ALL-PROT-014（风险写进"需作者确认"一节，不在正文静默改动）与 ALL-PROT-015（默认不外部核实）。
```

### U-srh-057

```
id: U-srh-057
category: process
language: zh
rule_summary: `audit-only` 只约束无源论断本身；同一段里的其他病灶（对比骨架、黑话、空总结、姿态层）仍按各自规则清理，不得因为一处审计就把整段冻结成风险说明。
positive: 一段里有一处无源引用和两处空总结，无源引用只标注，两处空总结照删。（自造）
negative: 因为段里有一处缺来源，就整段不改，只输出一句"本段存在无源引用风险"。——违反点：把审计范围扩大到整段，其他病灶未按各自规则处理。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: 这条防的是"保守"被执行成"什么都不做"：一处风险让整段停摆，用户拿到的是一份没有改过的稿子加一句免责说明。上游明确把审计的作用范围限定在那一条论断上。
  existing: 现有规则里没有。
```

### U-srh-058

```
id: U-srh-058
category: process
language: zh
rule_summary: `rewrite-with-placeholder` 只在用户明确要求保留原结构、原语气或编辑稿框架时使用；可以写成「有研究认为……，但这里没有给出处」这类占位提醒，但不得补具体机构、数据、年份或研究名称。
positive: 用户要求保留原论证骨架，改写成「有研究认为效率会提升，但这里没有给出处」。（自造）
negative: 用户没有提出保留原结构的要求，就用了占位模式并写成「有研究认为……（来源待补）」。——违反点：触发条件不成立时使用了这一模式。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: 占位模式保留了一个空的论证位置，只有在作者打算自己去补来源时才有意义，所以上游把它锁在"用户明确要求"后面。禁止补具体机构、数据、年份、研究名这四项，是因为占位一旦被填成具体内容就变成了伪造。
  existing: 疑似对应 ALL-PROT-001 与 ALL-PROC-005（用户给出的具体范围优先）。
```

### U-srh-059

```
id: U-srh-059
category: process
language: zh
rule_summary: 用户没有指定无源引用处理模式时按场景默认值走；文本跨场景时取更保守的 `audit-only`。
positive: 一段文字既像内部同步又像对外说明，按更保守的 audit-only 处理无源引用。（自造）
negative: 文本跨 status 和 public-writing 两个场景，选了 rewrite-safe 把无源论断整条删掉。——违反点：跨场景时未取更保守的 audit-only。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Unsourced citation modes"
notes: |
  intent: "跨场景取保守"是一条兜底规则：场景判不准时，宁可少改。它与 U-srh-014（混合文本只保留一个主语域）不冲突——那条讲语域收敛，这条讲处理力度取下限。
  existing: 疑似对应 ALL-PROC-003（信息不明时先问）。本单元的做法是不问、直接取保守值，与现有规则的做法不同，归并时需要裁决。
```

### U-srh-060

```
id: U-srh-060
category: process
language: zh
rule_summary: `minimal` 档适用于本身基本自然、只需去掉局部模板感和收尾腔的文本；默认动作是删空总结、把过度抬高的语气压回常规、把「像在解释自己会写作」的句子压回事实句。
positive: 一段自然的说明只删掉末尾的「总的来说，这是一个不错的选择」。（自造）
negative: 判定为 minimal 的文本被重排了段落顺序并合并了三处句子。——违反点：minimal 档只做局部处理，做了结构级改动。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `minimal`"
notes: |
  intent: 三个默认动作里，"把像在解释自己会写作的句子压回事实句"是最有信息量的一条：它指的是那种一边写一边说明自己在做什么的句子（"接下来我会从三个方面展开"），这是 AI 文本特有的自我解说。
  existing: 疑似对应 ALL-PROC-005（改动幅度三档）。档位的划分依据不同：ALL-PROC-005 按用户措辞，本单元按文本本身的状态。
```

### U-srh-061

```
id: U-srh-061
category: process
language: zh
rule_summary: `standard` 档适用于有明显 AI 腔或语域混搭、但信息骨架完好的文本；默认动作是统一语域、改掉工程师表演腔和商业黑话和 narrator 腔、必要时并句或换主语。
positive: 一篇语域在技术腔和自媒体腔之间跳的文章，统一到一种语域并合并了两处碎句。（自造）
negative: 判定为 standard 的文本被整篇重写、信息骨架也被打散重排。——违反点：standard 档保留信息骨架，只做语域与句式处理，做了超出范围的重写。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `standard`"
notes: |
  intent: 上游给 standard 的定义带一个前提——"信息骨架是好的"，所以这一档只处理表达层。它同时点名了三种腔（工程师表演腔、商业黑话、narrator 腔），这三种正是语域混搭最常见的来源。
  existing: 疑似对应 ALL-PROC-005 的第二档（润色）。
```

### U-srh-062

```
id: U-srh-062
category: process
language: zh
rule_summary: 只有在 `Tier 1` 命中明显密集，或多类结构问题叠加时，才允许升到 `aggressive` 档。
positive: 一段里连续命中六处 Tier 1，加上二元对比骨架和空总结叠加，升到 aggressive。（自造）
negative: 一段里只有两处 Tier 1 命中，就升到 aggressive 做整段重写。——违反点：命中密度和结构问题都不满足升档条件。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `aggressive`"
notes: |
  intent: aggressive 是唯一会大幅改变原文的档位，所以上游给它设了准入条件而不是让执行者凭感觉。两个条件（Tier 1 密集、多类结构问题叠加）都要求"多"，防的是因为一两处刺眼的句子就整段推倒。
  existing: 疑似对应 ALL-PROC-005（改动幅度按用户措辞定）。本单元的升档依据是文本状态而不是用户措辞，两套依据并存时如何裁决需要归并阶段处理。
```

### U-srh-063

```
id: U-srh-063
category: process
language: zh
rule_summary: 在 `aggressive` 档下先保护事实和术语，再做重写。
positive: 升到 aggressive 之前先把字段名、数字和术语标出来，再动结构。（自造）
negative: 判定 aggressive 后直接整段重写，事后再检查术语有没有丢。——违反点：保护动作排在了重写之后。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `aggressive`"
notes: |
  intent: 顺序本身是规则：重写幅度越大，事后核对越难还原。先冻结保护对象再动手，是这份 skill 在最高档位上唯一的安全保证。
  existing: 疑似对应 ALL-PROC-023（仲裁顺序，事实第一）与 U-srh-012（先记账本）。
```

### U-srh-064

```
id: U-srh-064
category: genre
language: zh
rule_summary: `docs` 场景默认不升到 `aggressive` 档。
positive: 一份操作文档即使 Tier 1 命中密集，仍停在 standard。（自造）
negative: 一份接口文档因为套话很多就升到 aggressive 整篇重写。——违反点：docs 场景默认不允许升到 aggressive。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `aggressive`"
notes: |
  intent: 文档的价值在可检索和可复现，重写会同时破坏这两项（搜索词变了、步骤顺序变了）。上游用一条场景禁令把最高档位挡在 docs 之外，比靠执行者自觉更可靠。
  existing: 疑似对应 ALL-G-002（体裁叠加限制）。docs 不升 aggressive 这条具体禁令在现有规则里没有。
```

### U-srh-065

```
id: U-srh-065
category: process
language: zh
rule_summary: scope 与档位是两条独立的轴：档位（`minimal / standard / aggressive`）表示改写力度，scope（`structural / bounded / in-place`）表示能不能删整句和怎么删，两者要分别判定。
positive: 判定为「standard + bounded」：力度中等，但整句空话要走删除清单交用户确认。（自造）
negative: 判定档位为 standard 之后就直接开始改，没有判定这次能不能删整句。——违反点：把 scope 当成档位的附属，未独立判定。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 3.5 Edit scope"
notes: |
  intent: 把"改多狠"和"能不能删"拆成两条轴，是这份 skill 结构上最有价值的设计：用户说"改得自然一点但别删"是一个常见需求，只有一条力度轴的话表达不出来。
  existing: 现有规则里没有（ALL-PROC-005 只有一条力度轴）。这是本来源的显著增量，归并时值得单独裁决。
```

### U-srh-066

```
id: U-srh-066
category: process
language: zh
rule_summary: `structural` 是默认 scope，适用于短文本、明确要求重写的文本、AI 味密度很高且不需要保留原节奏的文本；允许删整句空总结、合并相邻事实句、轻量调整句序或段落落点、按场景重写局部结构。
positive: 一段三百字的公开帖按 structural 处理，删掉两句空总结并合并了两句事实。（自造）
negative: 一篇一千五百字的中文公开写作长文按 structural 自由删并重排。——违反点：中文 public-writing 长文的默认 scope 是 bounded，不是 structural。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `structural`"
notes: |
  intent: structural 作为默认值适用于多数短文本，四条允许动作是这份 skill 认定的"正常改写"边界。反例取自下一条规则划出的例外，两条要一起读。
  existing: 疑似对应 ALL-PROC-012（改写级授权允许的动作）。
```

### U-srh-067

```
id: U-srh-067
category: genre
language: zh
rule_summary: 中文 `public-writing` 长文（约 1000 字以上）的默认 scope 是 `bounded`，不是 `structural`。
positive: 一篇 1200 字的公众号文章默认按 bounded 处理，整句空话进删除清单交用户确认。（自造）
negative: 一篇 1200 字的公众号文章按 structural 自由删并重排，交付时篇幅少了三分之一。——违反点：中文长文默认 scope 应为 bounded，缩水程度不该由模型决定。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 上游给了实测理由：长文走 structural 时缩水程度依模型而定，同一篇可能少 18%，也可能少 39%，用户无法预期。bounded 的作用是把"删多少"这个决定交还给用户。这是本清单里少见的、带实测依据的规则。
  existing: 现有规则里没有。长文默认 scope 这个概念在现有规则里不存在。
```

### U-srh-068

```
id: U-srh-068
category: process
language: zh
rule_summary: `bounded` 比 `structural` 克制：不合并相邻句、不重排段落、不删承担节奏的实句或有意重复。
positive: bounded 下保留了作者刻意重复的那句「还是不行。还是不行。」（自造）
negative: bounded 下把两句相邻的事实句合并成一句。——违反点：bounded 不允许合并相邻句。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 四条禁令都指向同一件事：保住原文的节奏。长文的节奏由句子数量和段落切分决定，合并和重排会在不丢信息的情况下把节奏改掉——而节奏正是作者最容易察觉被动过的东西。
  existing: 疑似对应 ALL-PROC-030（不为整齐而统一结构，作者原本的顺序和跳跃在不损害表达时保留）与 ALL-PROT-017（作者的节奏属于作者）。
```

### U-srh-069

```
id: U-srh-069
category: process
language: zh
rule_summary: 一个句子要进 `bounded` 的删除清单，必须同时满足三条：删掉后该段的信息点不变、它不是相邻两个实句之间的唯一过渡、它命中纯空句型（空总结 / 价值拔高收尾 / 无源权威铺垫 / 谄媚开场 / 整句旁白）。
positive: 一句「这一切都指向同一个方向」删掉后信息不变、不承担过渡、命中空总结，进删除清单。（自造）
negative: 把一句承担着上下两段唯一衔接的句子放进删除清单，理由是它本身没有新信息。——违反点：它是相邻两实句之间的唯一过渡，第二条不满足。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 三条同时满足才能删，其中"唯一过渡"这一条是最容易被忽略的：过渡句本身没有信息，但删掉之后上下两段会硬接。上游把它写成必要条件，防的是"没有信息就删"这个过于简单的判据。
  existing: 疑似对应 ALL-PROT-003（独立信息一律保留）与 ALL-P-008。三条必要条件的组合在现有规则里没有。
```

### U-srh-070

```
id: U-srh-070
category: protection
language: zh
rule_summary: 上一条的例外只有一个：整条无源论断里的数字或时间跨度，如果只依赖未提供的来源才成立，可以随整句一起进删除清单；但如果选择保留这条论断，就不得改动它的数值或时间跨度。
positive: 「研究表明未来十年会增长 40%」——整句进删除清单；用户决定保留时，40% 和"十年"原样不动。（自造）
negative: 用户决定保留这条论断，改写时把「未来十年」改成「未来几年」。——违反点：保留论断的同时改了时间跨度。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 这条把"整句删"和"改数字"分成互斥的两个选项：要么整条拿掉，要么原样保留。中间状态（保留论断但模糊化数字）被明确禁止，理由与 U-srh-055 相同——那会让一个无依据的说法变得不可核查。
  existing: 疑似对应 ALL-PROT-002 与 U-srh-055（同一条禁令在两处出现）。
```

### U-srh-071

```
id: U-srh-071
category: process
language: zh
rule_summary: 句首可以剥离的引导词（「值得一提的是」「归根到底」「这说明」）后面还跟着实质内容时，直接在句内清掉引导词、留下骨架，不进删除清单。
positive: 「值得一提的是，这版把重试次数从五次降到了两次」改成「这版把重试次数从五次降到了两次」。（自造）
negative: 把上面这句整句放进删除清单交用户确认。——违反点：它剥掉引导词之后还有实质内容，应当句内清洗而不是进清单。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 上游给了实测依据：长文里句首引导词模型能在句内清掉，整句空话在受限 scope 下删不掉，只会被软化成另一种说法。因此它把两类动作分开走——能句内解决的不占用用户的确认成本。
  existing: 疑似对应 ALL-PROT-020（删连接词时保留真实内容）。"两类动作分开走"这个操作区分在现有规则里没有。
```

### U-srh-072

```
id: U-srh-072
category: process
language: zh
rule_summary: 整句都是空的、剥掉引导词就什么都不剩的句子（无源论断、「不仅仅是……更是……」式的价值拔高），进删除清单，不得擅自软化成另一种说法。
positive: 「这不仅仅是一次更新，更是一种态度」——整句进删除清单。（自造）
negative: 把这句改成「这次更新体现了团队的态度」。——违反点：整句空话被软化成了另一种说法，而不是进删除清单。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: "软化成另一种说法"是受限 scope 下最典型的失败：模型不能删句，于是把空话改写成一句不那么难看的空话，篇幅保住了、AI 味没去掉。上游明确禁止这个出口。
  existing: 疑似对应 ALL-P-005（对称骨架要重建结构，不是换几个近义词）。"不得软化成另一种说法"这条禁令在现有规则里没有。
```

### U-srh-073

```
id: U-srh-073
category: process
language: zh
rule_summary: `bounded` 的输出形态固定：正文给句内清洗后的稿子，末尾附一份「建议删除（待确认）」清单，每条写出原文和为什么删了不丢信息；删不删由用户决定。
positive: 交付正文＋清单，清单里每条写「原文：……；删除理由：整句为价值拔高，无独有事实」。（自造）
negative: bounded 下直接把判定为空话的整句删掉，交付里没有删除清单。——违反点：未走删除清单流程，替用户做了删除决定。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `bounded`"
notes: |
  intent: 清单里必须写"为什么删了不丢信息"，是为了让用户能核对这个判断，而不是只看到一个删除建议。整个 bounded 机制的目的就是把长度决定权交还给用户，输出形态是这个目的的落地。
  existing: 疑似对应 ALL-PROC-008（改动说明写改了什么、为什么改、保留了什么）。"待确认的删除清单"这种输出形态在现有规则里没有。
```

### U-srh-074

```
id: U-srh-074
category: process
language: zh
rule_summary: `in-place` 的触发条件是用户明确要求保留句数、完全原样、一句不删，或者用户反馈 `bounded` 仍然删多了。
positive: 用户说"一句都别删，只把味儿去掉"，切到 in-place。（自造）
negative: 用户只说"改得克制一点"，就切到 in-place。——违反点："克制一点"不构成明确要求保留句数，触发条件不成立。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: in-place 是三档里最受限的，改写效果最弱，所以上游要求明确触发而不是靠推测。第二个触发条件（bounded 仍删多了）说明这三档设计成了一条可以逐级收紧的路径。
  existing: 疑似对应 ALL-PROC-005（用户给出的具体范围优先于默认档位）。
```

### U-srh-075

```
id: U-srh-075
category: process
language: zh
rule_summary: `in-place` 下禁止四类动作：不删整句（即使整句是空话）、不合并相邻句、不重排段落、不把多段压成一段。
positive: in-place 下把一句空话保留在原位，只把语气降下来。（自造）
negative: in-place 下把两个短段合并成一段，理由是这样更紧凑。——违反点：in-place 禁止把多段压成一段。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: 四条禁令覆盖了所有会改变句数和段数的动作，因为用户选 in-place 的诉求就是"形状不要变"。上游特意加了"即使整句是空话"这个括号，堵死最容易被合理化的例外。
  existing: 现有规则里没有对应档位。
```

### U-srh-076

```
id: U-srh-076
category: process
language: zh
rule_summary: `in-place` 下允许四类动作：句内替换词或短语、删除句内的提示层和空泛修饰和语气垫片、把句内拔高的语气降回普通判断、在单句内部拆短过满的结构（但不改变段落顺序）。
positive: 把「毫无疑问，这次改动无疑是极其关键的一步」改成「这次改动很关键」，句子数量不变。（自造）
negative: in-place 下把一个长句拆成两句并调整了它在段里的位置。——违反点：拆句可以，改变段落顺序不行。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: 允许清单说明 in-place 不是"不改"，而是把改动全部收进句子内部。"语气垫片"这个说法指的是那些只承担缓冲功能的词（其实、某种程度上、可以说），在中文里数量很大且删掉不影响句子成立。
  existing: 疑似对应 EN-P-003（不承担功能的副词删掉）与 ZH-P-001。
```

### U-srh-077

```
id: U-srh-077
category: protection
language: zh
rule_summary: 删短语之前先做语义独立性检查：删掉之后剩余部分必须仍是完整、可读、没有悬空指代的陈述句；否则改用句内替换，不硬删。
positive: 「这一点其实很重要」删掉"其实"仍成句，删；「就这一点而言，问题不大」删掉"就这一点而言"会让"问题不大"没有指向，改用替换。（自造）
negative: 把「就这一点而言，问题不大」删成「问题不大」。——违反点：删掉限定短语后句子出现悬空指代，读者不知道说的是哪一点。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: 这是一条句子层面的安全检查：删短语看起来是最小的改动，但中文的短语常常承担指代和限定，删掉之后句子在语法上还成立、在语义上已经断了。三个判据（完整、可读、无悬空指代）都可以逐句执行。
  existing: 疑似对应 ALL-PROT-020 与 ALL-P-010。"语义独立性检查"这个操作在现有规则里没有。
```

### U-srh-078

```
id: U-srh-078
category: process
language: zh
rule_summary: `in-place` 下遇到整句空话时保留原句并标注「[空句，建议人工确认是否删除]」，不擅自软化成新说法。
positive: 保留原句并在句后加上该标注。（自造）
negative: in-place 下把整句空话改写成另一句意思相近但读着不那么空的话。——违反点：整句空话应保留并标注，不得软化成新说法。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: 与 U-srh-072 是同一条禁令在 in-place 档的落法，区别在于输出形态：bounded 走删除清单，in-place 走行内标注。两处都堵同一个出口——不能删就改写成另一种空话。
  existing: 疑似对应 ALL-PROT-014（在正文里不插入编辑注记，风险写进单独一节）。本单元要求的是行内标注，与 ALL-PROT-014 的做法相反，归并时是冲突项。
```

### U-srh-079

```
id: U-srh-079
category: process
language: zh
rule_summary: `aggressive + in-place` 的组合可以存在，但默认先提醒用户长文在 aggressive 下容易明显缩水，并建议改成 `standard + bounded`；用户明确坚持时再执行，且仍遵守不删整句、不并句、不重排的边界。
positive: 用户要求"狠改但一句别删"，先说明这个组合的风险并建议 standard + bounded，用户坚持后按 in-place 边界执行。（自造）
negative: 用户要求"狠改但一句别删"，直接执行，没有提醒，也在执行中合并了两句。——违反点：既未提醒，也突破了 in-place 的并句边界。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### `in-place`"
notes: |
  intent: 这个组合本身是矛盾的（要大改又不许动结构），上游没有禁止它，而是要求先把矛盾说清楚再执行。这体现了这份 skill 处理冲突需求的一贯方式：把选择权和后果一起交给用户。
  existing: 疑似对应 ALL-PROC-003（信息不明时停下来问）。本单元的做法是先提醒再执行，不是停下来等回答，两者不同。
```

### U-srh-080

```
id: U-srh-080
category: measurement
language: zh
rule_summary: Tier 表示问题命中的强度，不表示改写力度；不得把 Tier 直接当成档位使用。
positive: 判定为 Tier 1 密集，但因为场景是 docs，档位仍停在 minimal。（自造）
negative: 因为判定为 Tier 1，就直接按 aggressive 改写。——违反点：把命中强度当成了改写力度。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 4. Tier severity"
notes: |
  intent: 上游在 Execution order 第 3 步和本节各强调了一次，说明这是个容易犯的错：Tier 高只说明问题多，改多少还要看场景和 scope。把两者分开是这份 skill 能在 docs 场景下既识别问题又不乱改的前提。
  existing: 现有规则里没有（现有规则没有严重度分级机制）。
```

### U-srh-081

```
id: U-srh-081
category: measurement
language: both
rule_summary: Tier 1 是默认要替换的一档，包含开场套话、总结式收尾、谄媚句、明显的商业黑话、自媒体流水线用语、表演性工程师腔、过度接住式共情、替用户做心理判断、郑重预告、身份认证式夸奖，以及英文里的 sycophantic openers、significance inflation、business jargon；局部命中用 minimal 或 standard 处理，密集命中时可升到 aggressive。
positive: 一段里出现「首先要说的是」「你问到了关键」，判定为两处 Tier 1，按 standard 处理。（自造）
negative: 把一处「值得注意的是」判成 Tier 3 只做记录不处理。——违反点：开场套话属于 Tier 1，默认应当替换。（自造）
positive（英文）: Marking "Great question!" and "This truly underscores its significance" as two Tier 1 hits and replacing both. ——按 Tier 1 默认替换处理。（自造）
negative（英文）: Treating "Great question!" as a low-severity item and leaving it in the text. ——违反点：sycophantic opener 属于 Tier 1，默认应当删除。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Tier 1"
notes: |
  intent: Tier 1 的共同特征是"单独出现就已经是问题"，不需要看密度。清单里的中文项（过度接住、身份认证式夸奖、郑重预告）是本来源特有的观察，英文项则与通用词表对齐。
  existing: 疑似对应 EN-M-001（英文高频词按证据强度分三档处理）。本单元的分级对象是模式而不是词，且覆盖中文，与 EN-M-001 是同一机制的两种落法。
```

### U-srh-082

```
id: U-srh-082
category: measurement
language: zh
rule_summary: Tier 2 是单独出现可以放行、同段聚集才算信号的一档（高频连接词扎堆、渲染性修饰词扎堆、同一类姿态词在同段重复）；密度阈值是：短段落（少于 100 字或词）同段出现 2 个以上即标记，长段落（100 字或词以上）同段 3 个以上再标记。
positive: 一个 80 字的段落里出现三个渲染词，判定命中 Tier 2。（自造）
negative: 一个 150 字的段落里出现两个渲染词就标记为命中。——违反点：长段落的阈值是 3 个以上，两个不构成信号。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Tier 2"
notes: |
  intent: 带数值的阈值是这条规则的价值所在：没有阈值，"扎堆"无法判定，执行者要么放行一切要么见到就改。按段落长度分两档，是因为长段落里出现两个连接词本来就正常。
  existing: 疑似对应 ALL-M-002（单一痕迹不算证据，多种痕迹聚集才构成信号）。ALL-M-002 没有给数值阈值，本单元可以补上。
```

### U-srh-083

```
id: U-srh-083
category: process
language: zh
rule_summary: Tier 2 命中后的默认处理是保留最贴切的那一个，其余改写；通常用 minimal 或 standard 档。
positive: 一段里三个渲染词，留下最贴切的那个，另外两个改成具体表述。（自造）
negative: 一段里三个渲染词全部删掉。——违反点：Tier 2 的处理是保留最贴切的一个，不是全删。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Tier 2"
notes: |
  intent: "保留一个"是这条规则的关键：Tier 2 的问题是密度不是词本身，全删会让文字变干。上游在 Tier 3 也用了同样的思路（删掉多余的几次）。
  existing: 疑似对应 EN-M-001 的第二档（同一段出现两次以上才改）。"保留最贴切的一个"这个处理方式在现有规则里没有明写。
```

### U-srh-084

```
id: U-srh-084
category: measurement
language: both
rule_summary: Tier 3 是常见词本身不构成问题、只在全文密度明显过高时才处理的一档（「重要 / 关键 / 核心 / 提升」「significant / innovative / effective」）；处理方式是删掉多余的几次，或把一部分换成具体信息，不换同义词；通常用 minimal，必要时可以不改。
positive: 全文出现十一次「关键」，删掉七次、把两处换成具体说明、保留两处。（自造）
negative: 全文出现三次「关键」，把其中两次换成「至关重要」和「核心」。——违反点：密度未达到过高，且处理方式用了同义词替换。（自造）
positive（英文）: Cutting seven of eleven occurrences of "significant" and turning two into concrete numbers, leaving two. ——密度过高时删掉多余的几次并换成具体信息。（自造）
negative（英文）: Replacing two of three occurrences of "effective" with "efficacious" and "impactful". ——违反点：Tier 3 的处理方式明确排除同义词替换。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Tier 3"
notes: |
  intent: Tier 3 的存在本身是一条防误杀规则：这些词是正常中文的一部分，把它们放进禁用词表会让改写变成同义词游戏。"不换同义词"这个限定与 Core stance 的第五条呼应。
  existing: 疑似对应 EN-M-001 的第三档（单独出现不动）与 ALL-PROT-009。中文的「重要/关键/核心/提升」四词在现有中文词表里没有单独分档。
```

### U-srh-085

```
id: U-srh-085
category: process
language: zh
rule_summary: 用户当前的要求，以及项目已有的 style guide 和术语表，优先于本 skill 的默认规则。
positive: 项目术语表规定某个说法必须保留，即使它命中通用词表也不动。（自造）
negative: 用户说这次要保留所有「我们」开头的句子，改写时仍按默认规则把它们换成主动主语。——违反点：默认规则覆盖了用户当前的明确要求。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 5. No-touch and keep rules"
notes: |
  intent: 把 skill 的默认规则定位成"没有别的约定时才生效"，与 ai-zixun 的 Repo Overrides 是同一思路。它承认通用词表必然与具体项目的约定冲突，且冲突时项目是对的。
  existing: 疑似对应 ALL-PROC-025（用户或项目提供的词表优先于默认词表）。
```

### U-srh-086

```
id: U-srh-086
category: protection
language: zh
rule_summary: 项目的正式术语和稳定的团队表达，不得仅仅因为命中通用词表就改写。
positive: 团队一直把某个流程叫「过闸」，虽然像黑话，保留。（自造）
negative: 把团队固定使用的「过闸」改成「审批通过」，理由是它命中了黑话词表。——违反点：仅因命中通用词表就改掉了稳定的团队表达。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 5. No-touch and keep rules"
notes: |
  intent: 团队内部的固定说法在外人看来就是黑话，但它在团队内部是精确的、有共识的。上游把"仅因命中词表"这个理由单独否掉，要求执行者给出词表之外的理由才能改。
  existing: 疑似对应 ALL-PROT-009（行业固定表述属于例外）与 ALL-PROC-025。
```

### U-srh-087

```
id: U-srh-087
category: protection
language: zh
rule_summary: 保护的依据是这个词在当前句子里的具体含义，或者用户和项目明确给出的约定；不得只因为文本是 README、发布说明、评测报告，或者带有命令和数字，就把周围的包装表达一起放行。原文用了某个说法，也不等于项目要求保留它。
positive: 一份评测报告里的指标名保留，但同一段里「本次评测充分验证了方案的优越性」照常清理。（自造）
negative: 因为这是一份带命令和数字的评测报告，就把整段包括「充分验证了优越性」在内全部保留。——违反点：用文本类型给周围的包装表达做了整体豁免。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "保护依据是词在当前句子里的具体含义"
notes: |
  intent: 这条堵的是防误杀规则被滥用：执行者一旦发现"技术文本要保护"，容易把整段技术文本当成免检区。上游要求保护落在词一级，且要有依据（当前句子的语义，或明确约定）。最后一句"原文用了某个说法也不等于项目要求保留"堵的是另一个滥用——把现状当成规范。
  existing: 疑似对应 ALL-PROT-009。"不得按文本类型整体豁免"这一层在现有规则里没有。
```

### U-srh-088

```
id: U-srh-088
category: process
language: zh
rule_summary: 不得自行假定存在术语表、团队约定或未提供的提交记录。
positive: 没有拿到术语表时，按词在当前句子里的语义判断，不假设"团队大概有个约定"。（自造）
negative: 保留某个黑话，理由写成「这可能是团队的固定说法」。——违反点：假定了一个未提供的团队约定作为保护依据。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "保护依据是词在当前句子里的具体含义"
notes: |
  intent: 与 U-srh-087 是一对：那条讲不能凭文本类型豁免，这条讲不能凭想象出来的约定豁免。两条一起把"保护"限制在有据可依的范围内。
  existing: 疑似对应 ALL-PROT-001（不得编造）与 ALL-PROC-025。
```

### U-srh-089

```
id: U-srh-089
category: protection
language: zh
rule_summary: 数值和正式指标名按字面保护，逐字不动。
positive: 「P99 延迟 240ms」逐字保留。（自造）
negative: 把「P99 延迟 240ms」写成「P99 大约 240 毫秒」。——违反点：正式指标名与数值的字面写法被改动。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "数值、正式指标名、字段名、命令和引用原文按字面保护"
notes: |
  intent: 上游把保护分成"按字面"和"按含义"两类，数值和指标名属于前者：它们的价值就在于精确的写法，改写等于改数据。这是本 skill 保护对象里最硬的一类。
  existing: 疑似对应 ALL-PROT-002（数字不得改写成概括说法）与 ALL-PROT-008（正文默认逐字不动）。
```

### U-srh-090

```
id: U-srh-090
category: protection
language: zh
rule_summary: 命令按字面保护，逐字不动。
positive: `kubectl rollout undo deploy/api` 逐字保留。（自造）
negative: 把 `kubectl rollout undo deploy/api` 写成「用 kubectl 回滚 api 这个 deployment」。——违反点：可执行的命令被改写成了叙述，读者无法复制执行。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "数值、正式指标名、字段名、命令和引用原文按字面保护"
notes: |
  intent: 命令是文档里唯一会被直接复制粘贴执行的内容，任何改写都可能让它跑不起来或跑出别的结果。按对象拆条是任务要求，本条与字段名、日志、引用原文各自成条。
  existing: 疑似对应 ALL-PROT-008 与 ALL-PROC-016（代码块整体跳过）。ALL-PROC-016 的做法是跳过代码块，本单元保护的是散文里内联出现的命令，两者互补。
```

### U-srh-091

```
id: U-srh-091
category: protection
language: zh
rule_summary: 接口名、参数名、字段名和配置项按字面保护，逐字不动，包括大小写、下划线和连字符的写法。
positive: `retry_max_attempts` 逐字保留。（自造）
negative: 把 `retry_max_attempts` 写成「最大重试次数配置项」或写成 `retryMaxAttempts`。——违反点：字段名被改成了叙述或改了命名写法，读者据此去查代码会查不到。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错"
notes: |
  intent: 这是本来源被登记时点名的保护对象之一。字段名的特殊之处在于它同时是标识符和词：模型看到 `key`、`status`、`level` 这类字段名时很容易把它当普通词处理，而字段名改了就对不上代码。api-reference 子场景里"字段与约束零漂移"讲的是同一件事。
  existing: 疑似对应 ALL-PROT-008（专有名词逐字不动）。接口名、参数名、字段名、配置项作为一类保护对象在现有规则里没有点名，是中文技术写作场景的缺口。
```

### U-srh-092

```
id: U-srh-092
category: protection
language: zh
rule_summary: 日志和报错按字面保护，逐字不动。
positive: `ERROR: connection reset by peer` 逐字保留。（自造）
negative: 把 `ERROR: connection reset by peer` 写成「报了一个连接被对端重置的错」。——违反点：报错原文被改写成叙述，读者无法用它去搜索或匹配。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错"
notes: |
  intent: 报错和日志的用途是被搜索和被匹配——改一个字就搜不到了。这也是 When to use 里"文本主要是代码、日志、命令、配置、接口名、报错"时不适用本 skill 的原因：这类内容整体不该被风格改写。
  existing: 疑似对应 ALL-PROT-008 与 U-srh-001。
```

### U-srh-093

```
id: U-srh-093
category: protection
language: zh
rule_summary: 引用原文按字面保护，逐字不动。
positive: 引号里的原话保持原样，只调整引号外的衔接。（自造）
negative: 把引用里的「我们当时没有意识到这一点」改成「他们当时没意识到」。——违反点：引语内部被改写，引号却仍在，读者会以为这是原话。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错"
notes: |
  intent: 引语被改写是最严重的一类失真：它把模型写的话署到了别人名下。上游把它和命令、字段名并列在同一条按字面保护的清单里。
  existing: 疑似对应 ALL-PROT-008（真实引语默认逐字不动，真伪无法确认的引语一律不改）。
```

### U-srh-094

```
id: U-srh-094
category: protection
language: zh
rule_summary: 技术文档里的系统行为主语要保留，不得为了「像人写的」而换成人称主语或去掉。
positive: 「调度器会在超时后重新入队」——保留"调度器"作主语。（自造）
negative: 把「调度器会在超时后重新入队」改成「我们会在超时后重新把它放回队列」。——违反点：系统行为的主语被换成了人称主语，读者会以为这是人工操作。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 技术文档里的系统行为主语"
notes: |
  intent: 这条是本 skill 与通用去 AI 味规则冲突最明显的地方：通用规则要求"指名动作的执行者、多用人称主语"，但技术文档里动作的执行者就是系统。把系统主语换成人称是事实错误，不是风格改进。
  existing: 与 ALL-P-004（指名动作的执行者，不让抽象事物做只有人能做的动作）是潜在冲突：ALL-P-004 禁止的是"市场奖励""数据告诉我们"这类拟人化，本单元保护的是"调度器重新入队"这类真实的系统行为。归并时两条都要保留，并在 rationale 里写清边界。
```

### U-srh-095

```
id: U-srh-095
category: protection
language: zh
rule_summary: 实验结果和完成状态按含义保护，不要求照抄表达它的全部措辞；非正式叙述里的包装动词仍然可以等义改写。
positive: 「完成了三个模块中的两个」改成「三个模块做完了两个」——含义不变，措辞可以换。（自造）
negative: 「完成了三个模块中的两个」改成「模块开发已推进」。——违反点：完成状态的含义（三个里的两个）没有保住。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "数值、正式指标名、字段名、命令和引用原文按字面保护"
notes: |
  intent: 上游把保护分成两级，这一级是"按含义"：完成状态的价值在于它说清了做到哪一步，措辞可以换。区分两级是为了不让保护规则把所有技术相关的句子都冻住。
  existing: 疑似对应 ALL-PROT-002 与 ALL-PROT-020。"按字面保护"与"按含义保护"这个二分在现有规则里没有，是一个有用的操作区分。
```

### U-srh-096

```
id: U-srh-096
category: protection
language: zh
rule_summary: 不得把带数字的整条叙述自行认定为正式指标名而整体冻结。
positive: 「这一周处理了大概两千单」判定为普通叙述，包装动词可以改，数字不动。（自造）
negative: 把「本周实现了两千单的处理量突破」整条当成指标表述原样保留，理由是它带数字。——违反点：把带数字的普通叙述误判成正式指标名，连"实现了……突破"这样的包装一起冻结了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "数值、正式指标名、字段名、命令和引用原文按字面保护"
notes: |
  intent: 与 U-srh-087 同一动机：防止保护规则被用来豁免整句。判据是"这是不是一个正式指标名"，不是"这句话里有没有数字"。
  existing: 现有规则里没有。
```

### U-srh-097

```
id: U-srh-097
category: protection
language: zh
rule_summary: 一个词正在被定义、被讨论，或属于引用原文时，保留这个词；同一个词被用来包装进展或结论时，按实际语义判断要不要改写。上游给的判例是：「闭环反馈 / 闭环控制」指反馈机制，保留；把完成工作说成「闭环」时，还原为完成了什么。
positive: 「这是一个闭环控制系统」保留；「这块已经闭环了」改成「这块的三步都做完了」。（自造）
negative: 因为"闭环"在黑话词表里，就把「闭环控制系统」也改成「反馈控制系统」。——违反点：词正在作为术语被使用，却按词表改掉了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "词本身正在被定义、讨论"
notes: |
  intent: 这是全篇最清楚的一条"同形词按语义分流"的规则，并且给了判例。它解决的是词表方法的根本缺陷：同一个字符串在不同句子里可能是术语也可能是黑话，只有看语义才能分开。
  existing: 疑似对应 ALL-PROT-008（词被讨论而不是被使用时不改）与 ALL-PROT-009。上游给的"闭环"判例在归并时值得作为例子写进 skill 正文。
```

### U-srh-098

```
id: U-srh-098
category: protection
language: zh
rule_summary: 把「闭环」这类包装说法还原成具体完成情况时，要保留原文的「未 / 只 / 部分」等完成范围，不得写成全流程已完成。
positive: 「这块只闭环了前两步」改成「前两步做完了，第三步还没」。（自造）
negative: 「这块只闭环了前两步」改成「这块的流程已经跑通了」。——违反点：把"只有前两步"的部分完成写成了全流程完成。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "例如 `闭环反馈 / 闭环控制` 是反馈机制"
notes: |
  intent: 还原黑话时最容易丢的就是范围限定词——因为黑话本身模糊，还原时模型会补一个"听起来完整"的说法。这条要求还原的方向只能是更具体，不能是更完整。
  existing: 疑似对应 ALL-PROT-004（不得把不确定说成确定）与 U-srh-047（完成态属于关系）。
```

### U-srh-099

```
id: U-srh-099
category: protection
language: zh
rule_summary: 没有附术语表的正常技术词仍然保留，不要求用户额外证明它是术语；也不得机械替换同形词。
positive: 文中出现「熔断」，没有术语表，仍按技术词保留。（自造）
negative: 把「熔断」改掉，理由是"用户没有提供术语表证明这是术语"。——违反点：把举证责任推给用户，对正常技术词做了默认改写。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "词本身正在被定义、讨论"
notes: |
  intent: 这条把举证责任放在改写一侧：默认保留，要改需要理由。它与 U-srh-088（不得假定存在术语表）不矛盾——那条说不能拿想象的约定当保护理由，这条说不需要约定也能保护正常技术词。
  existing: 疑似对应 ALL-PROT-009。
```

### U-srh-100

```
id: U-srh-100
category: protection
language: zh
rule_summary: 承载关键事实的抽象句要保留，即使它读起来「有点像 AI」。
positive: 「这套机制只在写多读少的场景下成立」——抽象但承载关键限定，保留。（自造）
negative: 删掉「这套机制只在写多读少的场景下成立」，理由是这句话很抽象、像 AI 写的。——违反点：删掉了承载适用条件的抽象句。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "- 承载关键事实的抽象句，即使它"
notes: |
  intent: 这条是对"抽象即空洞"这个反射最直接的纠正：抽象是一种表达层级，不是信息量的指标。上游把它放在保留清单的最后一项，与 U-srh-050 呼应。
  existing: 疑似对应 ALL-P-010 与 U-srh-050。
```

### U-srh-101

```
id: U-srh-101
category: style-opinion
language: zh
rule_summary: 不得为了「像人」把文本改得更假；专业文本可以保持专业，要处理的是模板化和表演化。
positive: 一份技术说明改完仍然是技术说明的口吻，只是不再模板化。（自造）
negative: 把一份技术说明改成带口头禅和感叹的口语，理由是这样更像真人。——违反点：为了"像人"给专业文本换了不属于它的语域。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "不要为了"
notes: |
  intent: 这是 Core stance 第一段那句"不反技术、不反抽象、不反专业"的收尾重申，位置在保护清单末尾，等于给整节做了个总结：保护清单的目的不是保守，是不让"像人"这个目标反过来制造失真。
  existing: 疑似对应 ALL-PROT-018（自然不等于口语化）与 ALL-PROC-018（给本该平实的文字硬注入个性同样算 AI 味）。
```

### U-srh-102

```
id: U-srh-102
category: style-opinion
language: zh
rule_summary: 改写后的文本应当有具体信息，不靠空洞总括撑气势。
positive: 「这一版把重试从五次降到两次，超时从 30 秒降到 5 秒。」（自造）
negative: 「这一版在稳定性方面做了全面的优化和提升。」——违反点：整句是空洞总括，没有一项具体信息。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 6. Positive style targets"
notes: |
  intent: Positive style targets 一节列的是改完之后应该达到的样子，与前面的禁令互补——只有禁令的话，执行者知道不该写什么，不知道该写成什么。这条是七项里最可判定的一条。
  existing: 疑似对应 ALL-P-007 与 ALL-M-001。
```

### U-srh-103

```
id: U-srh-103
category: style-opinion
language: zh
rule_summary: 改写后的文本应当语域统一，不在技术腔、商业腔、自媒体腔之间跳。
positive: 全文保持一种语域。（自造）
negative: 「这个模块的 P99 稳定在 200ms 以内，真的是天花板级的表现，家人们冲就完了。」——违反点：一句里从技术腔跳到自媒体腔。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 6. Positive style targets"
notes: |
  intent: 语域混搭是这份 skill 开篇点名的四大病灶之一，也是它设计"先判场景"这一步的原因。它比用词问题更难察觉，因为每一句单独看都成立。
  existing: 疑似对应 EN-P-040（同一篇里的语域断裂提示拼接）与 ALL-G-002。中文侧的三种腔（技术腔、商业腔、自媒体腔）的点名在现有规则里没有。
```

### U-srh-104

```
id: U-srh-104
category: process
language: zh
rule_summary: 以「改完能直接发」为终点，不为了更像人继续抛光到失真。
positive: 达到可以直接发的状态就停手，不再为了"更有人味"加东西。（自造）
negative: 稿子已经可以直接发，仍继续加口语化的插入语和个人化的感叹，直到语气和作者本人不一样了。——违反点：越过了"可直接发"这个终点，抛光到失真。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 6. Positive style targets"
notes: |
  intent: 给改写定了一个明确的停止条件。没有停止条件的话，"更像人"是一个可以无限追求的目标，而每多改一轮，偏离原文的风险就多一分。这条与 op7418 那种"注入灵魂"的取向正好相反。
  existing: 疑似对应 ALL-PROC-029（如果这次改动没有带来可以说出来的改善就原样返回）与 ALL-PROC-019（最多三轮）。"可直接发"作为终点的提法在现有规则里没有。
```

### U-srh-105

```
id: U-srh-105
category: style-opinion
language: zh
rule_summary: 文章的节奏应当来自删掉冗余和保留重点，不来自硬造金句。
positive: 删掉三句铺垫，剩下的两句自然形成快慢对比。（自造）
negative: 为了让段落有节奏，在段末加一句「而这，才是真正的答案」。——违反点：节奏靠硬造的金句制造，而不是靠删冗余。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 6. Positive style targets"
notes: |
  intent: 上游区分了节奏的两种来源。这条针对的是执行 "句长要有变化" 这类规则时的典型走样：模型不会删，只会加，于是用短促的金句制造节奏差。
  existing: 疑似对应 EN-P-024（删掉故作深刻的收尾金句）与 ZH-P-002。
```

### U-srh-106

```
id: U-srh-106
category: style-opinion
language: zh
rule_summary: 文章的立场应当来自判断或事实，不来自故作洞见。
positive: 「我不建议现在上这套，因为回滚路径还没验证过。」（自造）
negative: 「很多人没有意识到的是，真正的问题从来都不在技术本身。」——违反点：用"很多人没意识到"制造洞见感，句子本身没有给出判断依据。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 6. Positive style targets"
notes: |
  intent: 与 public-writing 场景的"不要装有洞见"是同一条要求在正向目标一侧的表述。判据是立场后面有没有依据，不是立场强不强。
  existing: 疑似对应 EN-P-008（删掉故作洞见的铺垫）与 ALL-S-002（reference-only）。中文侧对应的说法在现有中文词表里没有。
```

### U-srh-107

```
id: U-srh-107
category: process
language: zh
rule_summary: 默认输出一个推荐版本，不默认输出审稿过程、多版本比稿或逐条点评。
positive: 用户只说"帮我去下 AI 味"，交付一份改写稿。（自造）
negative: 用户只说"帮我去下 AI 味"，交付了三个版本和一份逐条点评。——违反点：默认输出应为单一推荐版本。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 7. Output contract"
notes: |
  intent: 三项排除（审稿过程、多版本、逐条点评）各对应一种常见的过度交付。上游把默认值定成最省用户力气的形态，其余形态都要显式触发。
  existing: 与 ALL-PROC-008（改动说明不得省略）方向相反，是冲突项；与 ai-zixun 的 U-azh-060 是同一条规则，两个独立来源支持同一结论，归并时证据强度值得注意。
```

### U-srh-108

```
id: U-srh-108
category: process
language: zh
rule_summary: 只有用户明确要求「先别改，先标问题」「这段哪里像 AI」「只做诊断 / 审稿 / 标注」「先告诉我该不该改」时，才启用 annotation mode。
positive: 用户说"先别改，告诉我哪里像 AI"，切到 annotation mode。（自造）
negative: 用户说"帮我看看这段"，就切到 annotation mode 只给诊断不给改写。——违反点："看看"不属于四类明确要求，触发条件不成立。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 审稿模式与改写模式交付的东西完全不同，猜错会让用户拿到一份自己不要的东西。上游给了四类明确措辞作为触发条件，避免靠推测。
  existing: 疑似对应 ALL-PROC-007（审稿与改写两种工作模式）。触发条件的具体措辞清单在现有规则里没有。
```

### U-srh-109

```
id: U-srh-109
category: process
language: zh
rule_summary: annotation mode 不直接给整段改写稿，默认只输出最重要的 1 到 5 个问题点。
positive: 一段文字标出三个最要紧的问题点。（自造）
negative: annotation mode 下逐句标出十七个问题。——违反点：超出 1 到 5 个的上限。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 上限逼出取舍：审稿的价值在于指出最要紧的几处，全列出来等于没有排序。这一点与 ai-zixun 的"3 到 6 个最明显的问题"是同一思路。
  existing: 疑似对应 ALL-PROC-007。条数上限在现有规则里没有。
```

### U-srh-110

```
id: U-srh-110
category: process
language: zh
rule_summary: annotation mode 的每个问题点固定包含四个字段：问题族、触发点、建议动作、是否建议改写。
positive: 「问题族：无源引用；触发点：『研究表明』；建议动作：补来源或删掉整条；是否建议改写：是」。（自造）
negative: 「这里读着有点像 AI，建议改一下。」——违反点：四个字段一个都没有，触发点和建议动作都不明确。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 四个字段把"哪里有问题"变成可核对的：问题族给分类、触发点给证据、建议动作给出路、是否建议改写给结论。缺任何一个，用户都要回来追问。
  existing: 疑似对应 ALL-PROC-007（审稿逐条点出命中的规则 id、引用原句、给出改法）。四字段结构与现有规则的三要素接近，可以对齐。
```

### U-srh-111

```
id: U-srh-111
category: process
language: zh
rule_summary: 文本的主要问题是缺来源时，可以只建议补来源，不强行给改写稿。
positive: 「这段的问题是三处判断都没有来源，先补来源再谈改写。」（自造）
negative: 明知问题是缺来源，仍给出一份把无源判断改得更流畅的改写稿。——违反点：把缺来源当成风格问题处理，改写让它显得更可信了。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 有些问题不是改写能解决的。上游允许在这种情况下不交改写稿，防的是"必须交付点什么"的压力导致把不该改写的东西改写了。
  existing: 疑似对应 ALL-PROC-004（缺失部分影响事实时先问）。
```

### U-srh-112

```
id: U-srh-112
category: measurement
language: zh
rule_summary: 判断文本是不是「材料不足」用压缩试验：删光姿态层、拔高和套话之后，剩下的事实、动作、数字和判断撑不起原文的篇幅，就是材料不足，而不是话说得不对。
positive: 一篇 800 字的稿子删完套话只剩三句实话，判定为材料不足。（自造）
negative: 一篇稿子读着空，直接标注「材料不足」，没有做压缩试验。——违反点：未按压缩试验的判据判定，只凭印象。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 这是一条把"这篇文章其实没东西"变成可判定的规则：压缩后剩多少，是能数出来的。它区分了两种不同的问题——表达有问题（能改）和材料不足（改不了），而模型默认会把后者当成前者来处理，结果是换一套说法把篇幅填回去。
  existing: 疑似对应 ALL-M-001（可移植性测试）。压缩试验是一个独立的判据，现有规则里没有。
```

### U-srh-113

```
id: U-srh-113
category: process
language: zh
rule_summary: 标注「材料不足」时，建议动作要写清删完之后还剩什么、缺的是哪一类材料；不替作者设计怎么去补，也不用换说法把篇幅填回去；材料不足不等于不用改，该清理的姿态照常清理，但要同时说明改完会短很多。
positive: 「删完剩三句：一个数字、一个动作、一条判断。缺的是案例和对照数据。清理后大约会短一半。」（自造）
negative: 标注材料不足，同时给出「建议补充三个客户案例和一段行业数据」的补写方案。——违反点：替作者设计了怎么补材料。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 三条限制各堵一个出口：不替作者设计补法（那是作者的活，也容易变成编内容）、不用换说法填篇幅（那是把问题藏起来）、不能因为材料不足就不清理（否则等于放弃改写）。最后一句"要同时说明改完会短很多"是对用户的预期管理。
  existing: 疑似对应 ALL-PROT-001 与 ALL-P-007（原文里找不到就标出缺口去问）。"不替作者设计怎么补"这条限制在现有规则里没有明写。
```

### U-srh-114

```
id: U-srh-114
category: process
language: zh
rule_summary: 「材料不足」这个标注只在 annotation mode 下出现；默认改写模式仍然只交改写结果，不评价作者手里有没有东西可写。
positive: 改写模式下发现材料很薄，仍只交改写稿，不加评语。（自造）
negative: 改写模式下在交付稿后面加一句「这篇的问题其实是没什么可写的」。——违反点：材料不足只在 annotation mode 出，改写模式下不评价材料。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: "材料不足"是一句关于作者的评价，说出来是有代价的。上游把它限制在用户明确要诊断时才给，改写模式下即使看出来也不说——用户要的是改好的稿子，不是评语。
  existing: 疑似对应 ALL-PROT-012（不得据文本评价作者）。
```

### U-srh-115

```
id: U-srh-115
category: process
language: zh
rule_summary: 文本落在误杀防护边界内（属于受保护对象或专业表达）时，annotation mode 下直接写「是否建议改写：否」。
positive: 一段全是命令和字段名，问题点写"是否建议改写：否"。（自造）
negative: 一段全是命令和字段名，仍列出五个"可以更自然"的改写建议。——违反点：落在误杀防护边界内的内容应直接给出不建议改写的结论。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 审稿模式有一种压力：既然被叫来审，就得挑出点什么。这条明确允许给出"不用改"的结论，防的是为了交付而制造建议。
  existing: 疑似对应 ALL-PROC-029（本来就好的句子不动）与 ALL-PROC-024（审稿结论的四种判定）。
```

### U-srh-116

```
id: U-srh-116
category: process
language: zh
rule_summary: 不得一边声明只标问题、一边输出完整的重写版；用户没有要求 annotation mode 时，仍按默认改写合同输出单一推荐版本。
positive: annotation mode 下只给问题点，末尾问一句要不要接着改。（自造）
negative: annotation mode 下先列了三个问题点，接着附上一份完整重写稿。——违反点：声明只标问题却输出了完整重写版。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 用户说"先别改"时，看到一份改好的稿子会直接影响他的判断——他很难再回到"要不要改"这个问题上。上游用"不要偷偷输出"这个措辞，说明这是个常见的越界。
  existing: 疑似对应 ALL-PROC-007（审稿模式不重写全文，给完报告就停下）。
```

### U-srh-117

```
id: U-srh-117
category: process
language: zh
rule_summary: 只有在高风险误杀的情况下，才在输出末尾额外补一行极短说明（例如「保留了系统主语和术语，避免失真」「这里只做轻改，避免把正式公告写成口语贴」）。
positive: 一份公告只做了轻改，末尾补一行说明为什么没多改。（自造）
negative: 每次交付都在末尾附三段说明改写思路。——违反点：说明只在高风险误杀时补一行，不是每次都写。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Annotation mode"
notes: |
  intent: 这是对默认"只给一个版本"的唯一例外：当改写幅度明显低于用户预期时，不说明会让用户以为没干活。限定"极短"和"高风险"两个条件，防的是例外变成常态。
  existing: 与 ALL-PROC-008（改动说明不得省略）冲突，冲突方式与 U-srh-107 相同：本来源把说明当成例外，现有规则把它当成必选。
```

### U-srh-118

```
id: U-srh-118
category: process
language: zh
rule_summary: 提交改写前把回读固定拆成两步先后进行：先做保真回读（Pass 1），再按需做残留味回读（Pass 2），不得混着做。
positive: 先只查事实和信息是否漂移，确认无误后再单独查残留 AI 味。（自造）
negative: 通读一遍，一边看事实一边顺手改语感。——违反点：两遍回读混着做，保真检查没有独立完成。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "## 8. Required reread checks"
notes: |
  intent: 混着做的问题是两个目标会互相干扰：改语感的动作会引入新的事实漂移，而这时保真检查已经过去了。分开做保证保真检查的结果在第二遍开始时是有效的，第二遍又只允许轻量修正（见 U-srh-133）。
  existing: 疑似对应 ALL-PROC-014（交付前逐项自查）。"两遍分开、先保真后风格"这个顺序在现有规则里没有。
```

### U-srh-119

```
id: U-srh-119
category: process
language: zh
rule_summary: Pass 1 保真回读固定检查五项：protected spans 有没有漂、信息有没有丢（范围、条件、否定、情态、完成态、方向、强度逐项可追溯）、语域是否统一、术语是否失真、删改后是否出现生硬断裂。
positive: 五项逐项过一遍，发现一处否定被删掉，补回去。（自造）
negative: 只检查了字段名和数字有没有改，没有检查语域和断裂。——违反点：五项检查漏掉两项。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 五项覆盖了这份 skill 全部保护对象的四个维度：受保护片段（不能碰的）、信息（不能丢的）、语域和术语（不能漂的）、断裂（改动带来的新问题）。最后一项是唯一一条检查"改动本身造成的伤害"而不是"原文有没有被保住"的。
  existing: 疑似对应 ALL-PROC-014 与 ALL-PROT-019。七项条件关系的列举与 U-srh-041 相同，是同一条要求在回读环节的重复。
```

### U-srh-120

```
id: U-srh-120
category: process
language: zh
rule_summary: Pass 1 里再做一次分析与输出的一致性检查：如果前面的判断是「原文没有具体对象、能力、实现或依据」，最终结果里就不得出现新的工具、产品、平台、功能、实现关系或指标。
positive: 前面判定原文没有具体产品，回读时确认改写稿里也没有出现任何产品名。（自造）
negative: 前面判定原文只提到抽象的"方案"，改写稿里却出现了一个具体的平台名。——违反点：分析结论与输出不一致，输出里出现了判定为不存在的对象。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 这条检查的是模型自己前后是否一致：分析阶段判定"原文没有说这个"，生成阶段却写出来了。这种不一致在长文里很常见，因为分析和生成是两个独立的过程。把它写成检查项，等于让分析结论对输出产生约束。
  existing: 疑似对应 ALL-PROT-001 与 U-srh-049（共现不等于能力关系）。"分析结论必须约束输出"这个检查方式在现有规则里没有。
```

### U-srh-121

```
id: U-srh-121
category: protection
language: zh
rule_summary: 删掉一句之后段落突然没了落点时，用原文已有的信息重组一条事实句，不得补口号句；原文里找不到可用信息就不补，宁可让段落短一点。
positive: 删掉段末的空总结后，把段中一条具体数字提到末尾做落点。（自造）
negative: 删掉段末空总结后，补一句「这也是我们一直在坚持的方向」。——违反点：用口号句补落点，且这句在原文里不存在。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 删掉空总结之后段落会"塌"，这时补一句是最自然的反应，而最容易补出来的正是另一句空话。上游给了三级处理：先从原文找、找不到就不补、宁可短——把"段落要有落点"这个审美需求排在保真之后。
  existing: 疑似对应 ALL-PROT-001 与 ALL-P-007。"删完不补落点，宁可短"这条在现有规则里没有明写。
```

### U-srh-122

```
id: U-srh-122
category: protection
language: zh
rule_summary: 在 `bounded` 和 `in-place` scope 下，信息留存是硬指标：原文的每一个信息点（事实、数字、判断、动作）在输出里都要能追溯到。
positive: bounded 下逐条核对，确认原文十四个信息点在输出里都能找到。（自造）
negative: bounded 下为了句子更顺，把一条判断和一个动作合并成一句概括表述。——违反点：两个独立信息点合并后无法逐一追溯。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 受限 scope 的存在前提就是用户不希望内容变少，所以这两档下信息留存被提升为硬指标（其他档位下是一般要求）。"可追溯"是比"没丢"更强的判据：要能指出输出里的哪一句对应原文的哪一点。
  existing: 疑似对应 ALL-PROT-003 与 ALL-PROT-019。按 scope 区分硬指标与一般要求在现有规则里没有。
```

### U-srh-123

```
id: U-srh-123
category: measurement
language: zh
rule_summary: `in-place` 下输出字数低于原文 85% 时，回退检查是否误删了整句、并了句或压了段落（in-place 不该删任何整句）。
positive: in-place 输出为原文的 82%，回退检查发现误删了两句，补回。（自造）
negative: in-place 输出为原文的 70%，直接交付。——违反点：低于 85% 的阈值却没有回退检查。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 字数比例是一个廉价但有效的自动检查：in-place 只做句内清洗，正常缩水幅度有限，掉到 85% 以下几乎一定是删了整句。上游用它作为触发回退检查的信号，而不是直接判定失败。
  existing: 现有规则里没有（现有规则没有任何篇幅口径的自查指标）。
```

### U-srh-124

```
id: U-srh-124
category: measurement
language: zh
rule_summary: `bounded` 下字数会因删掉整句空话而下降，不设硬下限；但要确认删除清单里每一条都是「删了不丢信息」的纯空句，没有混进实句或承担节奏的重复句。
positive: bounded 输出比原文短 20%，逐条核对删除清单，确认九条都是纯空句。（自造）
negative: bounded 下用字数比例来判断删多了没有，没有逐条核对清单。——违反点：bounded 不设字数下限，检查对象是清单里的每一条。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: bounded 的机制决定了它必然缩水，所以字数指标在这一档没有意义，检查必须落在"删的每一条是不是真的空"。上游为两档设了两种不同的检查方式，说明它清楚同一个指标不能通用。
  existing: 现有规则里没有。
```

### U-srh-125

```
id: U-srh-125
category: measurement
language: zh
rule_summary: 句数变化超过约 10% 时，回退检查是否在用户没有确认的情况下做了 structural 改写。
positive: 输出句数比原文少了 14%，回退检查发现三处并句是未经确认的，撤回。（自造）
negative: 输出句数比原文少了 20%，未做任何回退检查就交付。——违反点：句数变化超出阈值却没有回退检查。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 句数是比字数更直接的结构指标：并句和删句都会改变句数，而句内清洗不会。10% 这个阈值给了正常波动的余量，超出就说明动了结构。
  existing: 现有规则里没有。
```

### U-srh-126

```
id: U-srh-126
category: protection
language: zh
rule_summary: 关键事实句、转场句，以及承担节奏的重复句，不得因为「看起来像模板」就默认删除。
positive: 保留作者刻意重复的那句短句，因为它承担节奏。（自造）
negative: 删掉一句「还是这个问题」，理由是它和前面重复、像模板。——违反点：删掉了承担节奏的重复句。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 1 | 保真回读"
notes: |
  intent: 三类句子有一个共同点：单独看都像可以删的。事实句可能很短很平，转场句本来就没有信息，重复句看起来是冗余。上游把它们并列列为不得默认删除，要求删之前先判断它承担的是什么功能。
  existing: 疑似对应 ALL-PROT-017（作者的节奏属于作者）与 U-srh-069（唯一过渡不得进删除清单）。
```

### U-srh-127

```
id: U-srh-127
category: process
language: zh
rule_summary: 只有在第一遍已经保住事实、但读起来还有轻微 AI 味时，才做第二遍（Residual Audit）。
positive: Pass 1 通过后读一遍，发现还有两处开场残留，做第二遍。（自造）
negative: Pass 1 里发现两处信息漂移还没修，就先做第二遍处理语感。——违反点：第一遍尚未保住事实就进入了第二遍。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 第二遍是可选的，且有前提。上游把"事实已保住"设成进入条件，是为了防止执行者在事实还没核完的时候就去追求语感——那样第二遍的改动会建立在一个可能已经漂了的稿子上。
  existing: 疑似对应 ALL-PROC-019（改完可以重跑一遍检查再改一轮）。"第二遍有进入条件"在现有规则里没有。
```

### U-srh-128

```
id: U-srh-128
category: pattern
language: zh
rule_summary: Pass 2 查开场残留：还在用「结论先说」「直接说结论」「值得注意的是」这类提示层。
positive: 删掉「直接说结论：」，让结论本身开头。（自造）
negative: 「结论先说：这个方案不合适。」——违反点：「结论先说」是提示层，删掉后句子信息不变。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 这类提示层的特点是它在第一轮改写中常常被当成"结构清晰"的表现留下来，所以要在第二遍专门查一次。「结论先说」尤其容易漏，因为它看起来是在执行好的写作建议。
  existing: 疑似对应 ZH-P-001（含"值得注意的是"）与 EN-P-007（删掉清嗓子式开场）。「结论先说」「直接说结论」在现有中文词表里没有。
```

### U-srh-129

```
id: U-srh-129
category: pattern
language: zh
rule_summary: Pass 2 查总结残留：还在用「总的来说」「归根结底」「最终来看」这类空收尾。
positive: 删掉「总的来说」，让最后一条事实成为结尾。（自造）
negative: 「总的来说，这次改动是值得的。」——违反点：「总的来说」引出的整句是空收尾，没有新增信息。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 空收尾在第一遍被删掉之后，改写过程本身会再生成新的——因为模型在结束一段时倾向于收束。第二遍专门查一次，是承认这个再生成的存在。
  existing: 疑似对应 ZH-P-001、ZH-P-006 与 U-srh-032（同一类问题在兜底规则里已有一条，本条是复扫环节的检查项）。
```

### U-srh-130

```
id: U-srh-130
category: pattern
language: zh
rule_summary: Pass 2 查 narrator 残留：还在解释「这说明了什么」，而不是直接说事实或判断。
positive: 「重试次数从五次降到两次。」（自造）
negative: 「重试次数从五次降到了两次，这说明团队在稳定性上的思路发生了转变。」——违反点：后半句是 narrator 式解说，替读者总结这件事的意义。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: narrator 腔是本 skill 在 standard 档点名要处理的三种腔之一，它的特征是文本在叙述之外还要说明这段叙述的意义。第二遍再查一次，是因为它常常以"补充说明"的面目留在稿子里。
  existing: 疑似对应 EN-P-022（删掉告诉读者该怎么理解的旁白）。中文侧对应规则在现有中文词表里没有。
```

### U-srh-131

```
id: U-srh-131
category: pattern
language: zh
rule_summary: Pass 2 查空泛判断残留：还在写「方向是对的」「意义重大」「真正理解了用户」这类句子。
positive: 删掉「方向是对的」，或换成具体的判断依据。（自造）
negative: 「这次尝试意义重大，说明我们真正理解了用户。」——违反点：「意义重大」「真正理解了用户」两处空泛判断，都没有依据。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 与 U-srh-036（方向/进度认证）同源：这类句子是在替别人下没有依据的结论。放在第二遍再查，是因为它们常常是第一遍删掉空总结之后新补上去的落点。
  existing: 疑似对应 ZH-P-006 与 ALL-M-001（可移植性测试）。
```

### U-srh-132

```
id: U-srh-132
category: pattern
language: zh
rule_summary: Pass 2 查节奏过匀：每句都差不多长、差不多抬手、差不多落点，像被统一抛光过；同一种句式骨架（尤其二元对比「不是 X，是 Y」）反复到能预判下一句形状时，按结构反模式的密度判据处理。
positive: 发现连续四句都是"不是 X，是 Y"，把其中三处换成直接陈述。（自造）
negative: 全段六句都是同一个骨架，读者能预判下一句形状，交付前未处理。——违反点：同型句式骨架的密度已经到了可预判的程度。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: "能预判下一句形状"是一个可执行的判据，比"节奏不好"具体得多。这条同时点名了两件事：句子层的均匀（长度、抬手、落点）和骨架层的重复（同一句式反复），后者尤其指向二元对比——这是本 skill 最关注的中文句式病灶。上游把密度判据放在 references 的结构反模式里，本清单未追踪该文件，此处只记规则和它的指向。
  existing: 疑似对应 ALL-P-001（句长与段落结构要有变化）与 ALL-P-005（对称骨架）。"能预判下一句形状"这个判据与 ai-zixun 的 U-azh-064（连续三节可预测）是同一思路，两个独立来源支持同一判据。
```

### U-srh-133

```
id: U-srh-133
category: process
language: zh
rule_summary: Pass 2 只允许四类轻量修正：删一个残留的开场或收尾、合并两句过匀的事实句或拆一处过满的句子、把一句 narrator 或空泛判断压回直接表达、把超出密度阈值的同型句式骨架换成中性连接或直接陈述（换之前先剔除豁免项）。
positive: 第二遍只删了一处收尾、拆了一个长句。（自造）
negative: 第二遍里顺手把一段的顺序调了。——违反点：调整段落顺序不在四类允许的轻量修正之内。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 给第二遍设动作白名单，是因为这一遍发生在保真检查之后——任何超出白名单的改动都可能引入新的漂移，而不会再有一遍保真检查去接住它。
  existing: 疑似对应 ALL-PROC-019（最多三轮）。"最后一轮只允许白名单动作"在现有规则里没有。
```

### U-srh-134

```
id: U-srh-134
category: process
language: zh
rule_summary: Pass 2 不做三件事：不重写全文、不补原文没有的事实、不为了「更像人」改掉术语、参数、命令、报错或责任归属。
positive: 第二遍只做局部修正，术语和字段一个没动。（自造）
negative: 第二遍觉得整段还是不够自然，重写了整段。——违反点：第二遍不重写全文。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 三条禁令对应三种在最后一轮最容易发生的破坏。第三条把术语、参数、命令、报错、责任归属再点了一遍，说明上游认为"更像人"这个动机在收尾阶段最危险——事实已经检查过了，执行者的注意力全在语感上。
  existing: 疑似对应 ALL-PROT-001、U-srh-005（责任主体）、U-srh-090 至 U-srh-093（各类按字面保护的对象）。
```

### U-srh-135

```
id: U-srh-135
category: genre
language: zh
rule_summary: Pass 2 的场景保守策略：`public-writing` 和 AI 味偏重的 `chat` 更常需要第二遍；`docs`、`status`、`code-context` 默认更保守，如果第二遍会让语气变口语、变广告或影响保真，就停在第一遍。
positive: 一份操作文档做完 Pass 1 后判断第二遍会让语气变口语，停在第一遍。（自造）
negative: 一份操作文档做完 Pass 1 后仍做第二遍，把「执行该命令后系统将重建索引」改成「跑完这条命令，索引就重新建好啦」。——违反点：docs 场景做了第二遍并让语气变成口语。（自造）
source:
  type: upstream
  source_id: upstream-mrgediao-shuorenhua
  path: SKILL.md
  commit: d2d0ce27da295581c3cf87a30ab65deb7d0ddfb8
  anchor: "### Pass 2 | Residual Audit"
notes: |
  intent: 第二遍处理的是"味道"，而味道正是文档场景最不该被优化的东西——文档不需要读起来像人写的，需要读起来准确。上游给了明确的停止条件（会变口语、变广告、影响保真），让"要不要做第二遍"可判定。
  existing: 疑似对应 ALL-G-002（体裁叠加限制）与 ALL-PROC-010（体裁只调整触发门槛，不得整组跳过）。本单元允许整个跳过第二遍，与 ALL-PROC-010 的"不得整组跳过"有张力，归并时需要辨析：Pass 2 是可选环节，不属于必查的四组。
```

## 3 覆盖表

| 来源小节 | 归属单元 / 说明 |
|---|---|
| frontmatter：`name` | 非规则内容（skill 标识符） |
| frontmatter：`description` | U-srh-001（触发场景与保护对象的声明，与 When to use 同一内容） |
| 标题「# 说人话」与开篇两段 | U-srh-002（第二段）；第一段「把文本从像模型在表演写作拉回像具体人在当前场景下表达」为目标陈述，非可判定规则 |
| ## When to use | U-srh-001 |
| ## Core stance：第 1 条（去 AI 味主要处理什么） | 非规则内容（对处理对象的定义，不构成可判定要求；具体病灶由后面各节承担） |
| ## Core stance：第 2 条（保留技术性） | U-srh-003 |
| ## Core stance：第 3 条（优先保信息） | U-srh-004、U-srh-005 |
| ## Core stance：第 4 条（量化表述有歧义） | U-srh-006、U-srh-007 |
| ## Core stance：第 5 条（不用同义词替换表） | U-srh-008、U-srh-009 |
| ## Core stance：第 6 条（短语表只列代表项） | U-srh-010 |
| ## Execution order：八步列表 | U-srh-011；第 2 步 U-srh-012；第 3 步 U-srh-080（主锚点在 §4）；第 6 步的 references 补看要求 U-srh-030（主锚点在 §2 末段）；第 7 步 U-srh-118（主锚点在 §8）；第 8 步 U-srh-107、U-srh-108（主锚点在 §7） |
| ## Execution order：末尾「执行第 6 步时」两条 | U-srh-013、U-srh-010（补词门槛，主锚点在 Core stance） |
| ## 1. Scene detection 引言 | U-srh-014 |
| ### `chat` | U-srh-015 |
| ### `status` | U-srh-016 |
| ### `docs` | U-srh-017 |
| ### `public-writing` | U-srh-018 |
| ### `public-writing` 末句（更细的下限限制见场景禁改表） | 非规则内容（references 导航） |
| ### Scene Packs：触发说明 | U-srh-019 |
| ### Scene Packs：README | U-srh-020 |
| ### Scene Packs：release-note | U-srh-021 |
| ### Scene Packs：forum-post | U-srh-022 |
| ### Scene Packs：issue-reply | U-srh-023 |
| ### Scene Packs：api-reference | U-srh-024；其中 method / path / 字段 / 约束 / 字面量零漂移的要求由 U-srh-089 至 U-srh-093 承担 |
| ### Scene Packs：faq | U-srh-025、U-srh-026、U-srh-027、U-srh-028 |
| ### Scene Packs：末段（子场景的作用范围） | U-srh-029 |
| ## 2. Single-file fallback rules：引言与末段 | U-srh-030 |
| ## 2：删开场套话、谄媚和元评论 | U-srh-031 |
| ## 2：删空总结和收尾腔 | U-srh-032 |
| ## 2：处理二元对比骨架 | U-srh-033 |
| ## 2：处理无源引用 | U-srh-053（主锚点在 Unsourced citation modes） |
| ## 2：把商业黑话和表演性技术腔改回普通动作 | U-srh-034 |
| ## 2：遇到过度接住、替用户做心理判断或身份认证式夸奖 | U-srh-035、U-srh-036 |
| ## 2：发现翻译腔时 | U-srh-037 |
| ## 2：把名词化还原成动词 | U-srh-038 |
| ## 2：同一个对象不要在相邻几句里换三种说法 | U-srh-039 |
| ## 2：误杀防护优先 | U-srh-089 至 U-srh-094（按保护对象逐条拆分，主锚点在 §5 的保留清单） |
| ## 2：清理姿态层时按子句和事实要素判断 | U-srh-040、U-srh-041 |
| ## 2：`code-context` 里的真实运行行为 | U-srh-042、U-srh-043 |
| ## 2：抽象信息、实体类型和关系不能擅自具体化 | U-srh-044、U-srh-045、U-srh-046、U-srh-047、U-srh-048、U-srh-049、U-srh-050、U-srh-051 |
| ## 2：中英混排句中的英文词 | U-srh-052 |
| ### Unsourced citation modes：引言与 `rewrite-safe` | U-srh-053、U-srh-054、U-srh-055 |
| ### Unsourced citation modes：`audit-only` | U-srh-056、U-srh-057 |
| ### Unsourced citation modes：`rewrite-with-placeholder` | U-srh-058 |
| ### Unsourced citation modes：末段（没指定模式怎么办） | U-srh-059 |
| ## 3. Rewrite level（分节标题） | 非规则内容（章节标题，三档的内容在下面三个小节） |
| ### `minimal` | U-srh-060 |
| ### `standard` | U-srh-061 |
| ### `aggressive` | U-srh-062、U-srh-063、U-srh-064 |
| ## 3.5 Edit scope 引言 | U-srh-065 |
| ### `structural` | U-srh-066 |
| ### `bounded`：定位与理由 | U-srh-067 |
| ### `bounded`：和另两档的关系 | U-srh-068 |
| ### `bounded`：进删除清单的三条 | U-srh-069、U-srh-070 |
| ### `bounded`：两类动作分开走 | U-srh-071、U-srh-072 |
| ### `bounded`：输出 | U-srh-073 |
| ### `in-place`：触发条件 | U-srh-074 |
| ### `in-place`：禁止动作 | U-srh-075 |
| ### `in-place`：允许动作 | U-srh-076 |
| ### `in-place`：语义独立性检查与空句标注 | U-srh-077、U-srh-078 |
| ### `in-place`：末段（aggressive + in-place） | U-srh-079 |
| ## 4. Tier severity 引言 | U-srh-080 |
| ### Tier 1 | U-srh-081 |
| ### Tier 2 | U-srh-082、U-srh-083 |
| ### Tier 3 | U-srh-084 |
| ## 5. No-touch and keep rules（分节标题） | 非规则内容（章节标题，本节各段见下列各行） |
| ## 5：用户当前要求与项目 style guide 优先 | U-srh-085、U-srh-086 |
| ## 5：保护依据是词在当前句子里的具体含义 | U-srh-087、U-srh-088 |
| ## 5：数值、正式指标名、字段名、命令和引用原文按字面保护 | U-srh-089、U-srh-095、U-srh-096 |
| ## 5：词本身正在被定义、讨论 | U-srh-097、U-srh-099 |
| ## 5：闭环的判例 | U-srh-098 |
| ## 5：默认优先保留清单（引用原文、命令、接口名、参数名、字段名、配置项、日志、报错） | U-srh-090、U-srh-091、U-srh-092、U-srh-093 |
| ## 5：默认优先保留清单（技术文档里的系统行为主语） | U-srh-094 |
| ## 5：默认优先保留清单（postmortem / incident / PRD / release note 术语） | U-srh-003（主锚点在 Core stance） |
| ## 5：默认优先保留清单（承载关键事实的抽象句） | U-srh-100 |
| ## 5：末句（不要为了像人把文本改得更假） | U-srh-101 |
| ## 5：末行（完整保护清单见 Protected Spans） | 非规则内容（references 导航） |
| ## 6. Positive style targets：有具体信息 | U-srh-102 |
| ## 6：有主语和动作 | U-srh-037、U-srh-094 的重复表述（正向表述，主锚点在 §2 与 §5） |
| ## 6：有统一语域 | U-srh-103 |
| ## 6：以可直接发为终点 | U-srh-104 |
| ## 6：有节奏 | U-srh-105 |
| ## 6：有立场 | U-srh-106 |
| ## 6：有边界（没把握就直说，不替对方做心理判断） | U-srh-035、U-srh-036 的重复表述（正向表述） |
| ## 6：末行（更完整的正向目标见 Positive Style Contract） | 非规则内容（references 导航） |
| ## 7. Output contract 首句 | U-srh-107 |
| ### Annotation mode：触发条件 | U-srh-108 |
| ### Annotation mode：1-5 个问题点与四个字段 | U-srh-109、U-srh-110 |
| ### Annotation mode：额外约束（缺来源） | U-srh-111 |
| ### Annotation mode：额外约束（材料不足） | U-srh-112、U-srh-113、U-srh-114 |
| ### Annotation mode：额外约束（误杀边界、不偷偷重写、默认合同） | U-srh-115、U-srh-116 |
| ### Annotation mode：无源引用在两种模式下的输出 | U-srh-053 至 U-srh-058 的重复表述（主锚点在 Unsourced citation modes） |
| ### Annotation mode：末段（高风险误杀时补一行说明） | U-srh-117 |
| ## 8. Required reread checks 引言 | U-srh-118 |
| ### Pass 1 \| 保真回读（分节标题） | 非规则内容（章节标题，本节各段见下列各行） |
| ### Pass 1：五项检查 | U-srh-119 |
| ### Pass 1：分析—输出一致性检查 | U-srh-120；其中"每个 X 做 Y / X 基于 Y 关系要能回指原文"与"同义改写不得改变谓词方向、完成态、强度、效果类型"是 U-srh-049、U-srh-047 的重复表述 |
| ### Pass 1：删句后没落点怎么办 | U-srh-121 |
| ### Pass 1：`bounded / in-place` 额外检查 | U-srh-122、U-srh-123、U-srh-124、U-srh-125、U-srh-126 |
| ### Pass 2 \| Residual Audit（分节标题） | 非规则内容（章节标题，本节各段见下列各行） |
| ### Pass 2：进入条件 | U-srh-127 |
| ### Pass 2：固定只查五件事 | U-srh-128、U-srh-129、U-srh-130、U-srh-131、U-srh-132 |
| ### Pass 2：只允许做的轻量修正 | U-srh-133 |
| ### Pass 2：不要做的事 | U-srh-134 |
| ### Pass 2：场景保守策略 | U-srh-135 |
| ## Reference navigation | 非规则内容（十二条 references 与 evals 文件的索引说明，本身不是可判定规则；这些文件不在 sources.yaml 的 paths 里，快照中没有） |

## 4 拆分时拿不准的地方

1. **保护对象逐条拆开是按任务要求做的，可能过碎。** U-srh-089 至 U-srh-094（数值与指标名、命令、接口与字段与配置项、日志与报错、引用原文、系统行为主语）在上游原文里是一份清单里的几个并列项，共用"默认优先保留"这一条判定逻辑，按 extraction.md 的判据本可以合成一个单元。本清单按任务要求"一条对象一个单元"拆开，理由是这些对象在归并时的裁决可能不同（例如系统行为主语与 ALL-P-004 冲突，其余不冲突）。如果归并阶段认为它们应当合成一条 protection 规则，可以直接合并。
2. **U-srh-003（专业术语保留）在 Core stance 和 §5 各出现一次，本清单只出一个单元、主锚点放在 Core stance。** 两处的措辞不同（Core stance 说"专业词、系统主语、事故复盘用语、PRD/发布说明术语"，§5 说"postmortem / incident / PRD / release note 中的专业术语"），如果归并阶段认为两处有实质差异，可能要拆回两条。
3. **档位（rewrite level）与 scope 两套机制是否要整体引入本仓库的 skill，本清单不预判。** 它们各自内部一致、可判定，但引入之后与现有 ALL-PROC-005 的三档授权会形成两套并行的力度控制。三种可能的处理（整体采纳并替换 ALL-PROC-005、只采纳 scope 这一条轴、整体记 reference-only）都成立。
4. **U-srh-078（in-place 下给整句空话加行内标注）与 ALL-PROT-014（不得在正文里插入编辑注记）直接冲突。** 上游的做法在 in-place 这个特定档位下有其道理（不能删又不能改写，只剩标注这一个出口），但它确实往正文里写了东西。归并时需要在"另起一节写风险"和"行内标注"之间选一个。
5. **U-srh-107、U-srh-117（默认只给一个版本、只在高风险时补一行说明）与 ALL-PROC-008（改动说明不得省略）冲突。** 值得注意的是 ai-zixun 来源的 U-azh-060 给出了同样的结论，两个独立来源支持"默认不附说明"，而现有规则的来源是 qu-ai-wei 一系。归并时这是一个证据分布值得重新审视的点。
6. **U-srh-030（单文件兜底与 references 补看）涉及上游自己的目录结构，本仓库的 skill 未必有对应的分层。** 本清单照拆，是因为它规定了确定的执行行为；归并时大概率只作为流程参考，不进 skill 正文。
7. **数值型阈值（U-srh-082 的 100 字 / 2 个 / 3 个、U-srh-123 的 85%、U-srh-125 的 10%、U-srh-067 的 1000 字）都是上游给的，未标注来源。** 其中 U-srh-067 附了实测区间（同一篇长文缩水 18% 到 39%），其余三条没有说明依据。按 criteria.md 第 3 条第 2 项（准确性）裁决时，这些数值需要用本仓库自己的样本核一遍，否则采纳的是别人的经验值。
8. **U-srh-002、U-srh-101、U-srh-102 至 U-srh-106 这一组的可判定性弱于其余单元。** 它们是态度声明和正向目标，判定要靠对整段的判断而不是圈出某个词。按 criteria.md 第 2 条，归并阶段可能记 rejected 或 reference-only；本清单照拆是为了覆盖表不留空白，并保留它们作为其他规则的理由说明。
9. **U-srh-132 指向的密度判据在 references 的结构反模式文件里，本清单未追踪该文件。** 因此这条单元只记了规则本身和它的指向，没有具体阈值。归并时如果要采纳这条，需要自己定阈值，或者先把该文件加进 sources.yaml 的 paths（这需要改 tracking_revision，不在本次拆规则的范围内）。

## 5 疑似与现有规则或别的来源重合的单元

- **与现有规则高度重合、估计会聚成一簇**：U-srh-004（≈ALL-PROT-001）、U-srh-007（≈ALL-PROT-001）、U-srh-008/039（≈ALL-PROT-009 + EN-P-019/020）、U-srh-031（≈EN-P-028 + ZH-P-001）、U-srh-032（≈ZH-P-001 + EN-P-023）、U-srh-033（≈EN-P-006 + ALL-P-005）、U-srh-034（≈ZH-P-001 + EN-P-001）、U-srh-037（≈ZH-P-008/011）、U-srh-038（≈ZH-P-011 + EN-P-016）、U-srh-051（≈ALL-P-007）、U-srh-085/086（≈ALL-PROC-025）、U-srh-089/090/093（≈ALL-PROT-008）、U-srh-119（≈ALL-PROC-014）
- **与现有规则冲突、需按 criteria.md 第 8 条双记**：U-srh-094（vs ALL-P-004，系统行为主语 vs 指名执行者）、U-srh-078（vs ALL-PROT-014，行内标注 vs 单独一节）、U-srh-107/117（vs ALL-PROC-008，默认不附说明）、U-srh-042（vs ALL-PROC-016/017，允许改注释 vs 整体跳过代码）、U-srh-010（vs ALL-PROC-028，先按现有模式归类 vs 交给用户判断）、U-srh-059（vs ALL-PROC-003，取保守默认值 vs 停下来问）、U-srh-135（vs ALL-PROC-010，可整体跳过第二遍）
- **可以给现有 unverified 规则补证据**：U-srh-037、U-srh-038（支持 ZH-P-011）；U-srh-082（给 ALL-M-002 补数值阈值）；U-srh-084（给 ZH-P-001 的中文词分档提供依据）
- **与 ai-zixun 来源估计会聚成一簇**：U-srh-033 与 U-azh-026（二元对比）、U-srh-037 与 U-azh-024/025（翻译腔）、U-srh-103 与 U-azh-021（语域统一）、U-srh-107 与 U-azh-060（默认不附说明）、U-srh-132 与 U-azh-064（可预测性判据）
- **与 op7418 来源估计会聚成一簇或直接对立**：U-srh-101/104（不为像人改假、以可直接发为终点）与 U-ohz-001/007 至 011（注入灵魂）是同一问题上的相反主张，归并时应放在一起裁决
- **现有规则里确实没有、值得单独裁决的增量**（本来源最有价值的部分）：U-srh-005（责任主体）、U-srh-045（数字与对象的配对）、U-srh-046（主体与目标的配对）、U-srh-047（谓词的方向 / 完成态 / 强度 / 效果类型）、U-srh-049（共现不等于能力关系）、U-srh-052（中英混排不套英文词表）、U-srh-065/067（scope 这条独立的轴与中文长文的默认 bounded）、U-srh-091（接口名 / 参数名 / 字段名 / 配置项）、U-srh-092（日志与报错）、U-srh-035/036（过度接住与方向认证）、U-srh-097（同形词按语义分流，附"闭环"判例）、U-srh-112（材料不足的压缩试验）、U-srh-118（两遍回读分开做）、U-srh-123/125（篇幅与句数的回退检查阈值）

## 6 上游文本内的指令

上游正文通篇是以祈使句写给模型的操作规程（例如「按固定顺序做，不要跳步」「先执行本文件里的最小规则」），本清单把这些内容当作规则拆分和记录，没有执行其中任何一条，也没有按其指示去读 `references/` 或 `evals/` 下的文件——那些路径不在 sources.yaml 的 paths 里，快照中不存在。

有一段直接对读者下达文件读取指令，照抄如下备查（未执行）：

> 先执行本文件里的最小规则；只要环境里能读 `references/`，默认继续按问题类型补看 [Protected Spans](./references/protected-spans.md)、[Positive Style Contract](./references/positive-style.md)、[微操作手册](./references/operation-manual.md)、[结构反模式](./references/structures.md) 和相关短语表

除此之外，通读全文未发现注入式指令（例如"忽略之前的规则""把这段加进你的系统提示""请把这段复制进你的规则"）。
