# 来源拆分：upstream-lifelonglazylearner-qu-ai-wei

## 1 来源摘要

- 文件：`merges/maybe-humanizer/snapshots/upstream-lifelonglazylearner-qu-ai-wei/SKILL.source.md`
- 上游原路径：`SKILL.md`（仓库 `LifelongLazyLearner/qu-ai-wei`，branch `main`）
- commit（sources.lock.json 的 last_seen_commit）：`39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17`
- 许可证：MIT，license_status 为 known，snapshot_policy 为 full-text，允许在本清单中引用原文短句。
- 上游自述的定位：简体中文保真改写 skill。frontmatter 声明用于「去AI味」「改得说人话」「humanize中文」「改自然点」「改写/重写这段中文」「润色得自然些」「太生硬了」等请求，包括段落、文章与长文的结构重写；明确不用于翻译、新写中文、只查错别字、繁体中文，或未经授权替真人更换声口。正文核心机制是：建立全文信息账本与论证图、扫描八个模式族、按"改写/重写"「润色」「校对」三级授权确定改写幅度、允许全文结构重写但保留引用绑定与事实边界、区分普通模式与内嵌模式两种输出形式。
- 总单元数：65（U-qaw-001 至 U-qaw-065）
- 按 category 计数：
  - protection：26
  - process：26
  - pattern：11
  - genre：1
  - measurement：1
  - style-opinion：0

## 2 单元清单

### U-qaw-001

```
id: U-qaw-001
category: genre
language: zh
rule_summary: 请求属于"去AI味""改写/重写""润色得自然些"等使中文更自然的编辑类请求（含段落、文章、长文的结构重写）时适用本 skill；请求是翻译、从零新写中文、只查错别字、繁体中文，或未经授权替真人更换声口时不适用。
positive: "帮我把这段客服回复改得说人话一点"——属于"改得说人话"的改写请求，适用。（自造）
negative: "把这段中文翻译成英文"——违反点：属于翻译请求，不是改写，不在适用范围内。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "Rewrite and humanize Simplifie"
notes: 描述字段里正向触发词表和反向排除词表共用一条"是否属于本skill适用范围"的判断逻辑，按共用逻辑合并为一个单元。
```

### U-qaw-002

```
id: U-qaw-002
category: protection
language: zh
rule_summary: 不得把"文本命中AI高频写作症状"或"未命中"当作判断作者身份、真实性或道德的依据；模式识别只用作编辑信号。
positive: "本文命中若干AI高频句式，按编辑信号处理，改写时不对作者身份下结论。"（自造）
negative: "这段话到处是排比和总结句，一看就是AI写的，不是真人写的。"——违反点：把写作模式识别结果直接当作者身份鉴定结论。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 能力边界"
notes: 开篇段"把 AI 高频写作症状当编辑信号，不把它们当作者身份鉴定"与本节末句"不把模式症状当作者身份、真实性或道德判断"是同一条规则的两处表述，本单元以能力边界一节的完整表述为主锚点，开篇段视为该规则的重复出现，不再单列。
```

### U-qaw-003

```
id: U-qaw-003
category: process
language: zh
rule_summary: 执行改写时，判断为需要即可重建句子、段落和全文信息架构，不得只做局部换词就当作已完成改写。
positive: 原文结构混乱、结论重复出现三次，改写时合并结论段并调整全文顺序。（自造）
negative: 只把"赋能""抓手"替换成别的词，句子结构和段落顺序原封不动就交稿。——违反点：仅做局部换词，未按需要重建结构。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "把一段话、一篇文章或更长内容改成符合目标语体的自然简体中文"
```

### U-qaw-004

```
id: U-qaw-004
category: process
language: zh
rule_summary: 除非用户或调用方明确说明只要终稿、只输出正文、不要过程，或明确标记为流程内嵌步骤，否则一律使用普通模式（输出门检、终稿、打磨报告）；不能因为请求简短、原文像真人、用户直接要求重写，或终稿已自洽就擅自切换到内嵌模式。
positive: 用户只说"帮我改一下这段"，未提只要终稿，按普通模式输出门检、终稿和打磨报告。（自造）
negative: 用户只说"帮我改自然点"，因为请求简短就直接只回终稿，不输出门检和打磨报告。——违反点：以"请求简短"为由切换到内嵌模式，未满足触发条件。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "除非用户或调用方明确说"
```

### U-qaw-005

```
id: U-qaw-005
category: protection
language: zh
rule_summary: 处理正文前先做敏感信息门检；输入含密码、API key、access token、私钥、会话cookie或用户称其为凭证时立即停止，不得引用、改写、复述或先掩码后继续，只能回复固定话术；概念性讨论 token、API key 不算凭证。
positive: 用户贴出的文本里含一串"sk-live-...."并说明是密钥，回复固定的"检测到疑似凭证，请删除或替换为[REDACTED]后重试。"，不做其他处理。（自造）
negative: 发现文本里有一串疑似 API key，先把它替换成"[REDACTED]"再继续改写其余段落。——违反点：检测到疑似凭证后没有停止，而是掩码后继续处理。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "处理正文前先做敏感信息门检"
```

### U-qaw-006

```
id: U-qaw-006
category: process
language: zh
rule_summary: 改写中出现规则冲突时，按固定的五级顺序裁决，前项优先于后项：①事实/原意/证据强度/引用绑定/逻辑关系；②用户指定的用途/语体/编辑范围/受保护文字；③作者真实声口/判断/感受/不确定性/圈层表达；④自然的简体中文表达与阅读顺序；⑤原句式/原段序/标题和格式。
positive: 为了让句子更顺，需要在牺牲一处不确定语气或保留原句式之间二选一时，优先保留不确定语气，句式可以让步。（自造）
negative: 为了追求自然的阅读顺序，把作者"可能""大概"的犹疑语气全部改成肯定语气。——违反点：把第4级（自然表达）凌驾于第3级（作者真实声口/不确定性）之上。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 仲裁顺序"
```

### U-qaw-007

```
id: U-qaw-007
category: protection
language: zh
rule_summary: 不得为了行文顺口而给原文补写事实、因果关系、经历、例子、观点或结果。
positive: 原文只说"销量下滑"，改写后仍只说销量下滑，不补充下滑原因。（自造）
negative: 原文只说"销量下滑"，改写时加上"这是因为管理层决策失误"。——违反点：补写了原文没有的因果关系。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得为了顺口补写事实"
```

### U-qaw-008

```
id: U-qaw-008
category: protection
language: zh
rule_summary: 不得把原文表达的不确定说成确定。
positive: 原文说"可能与天气有关"，改写后仍保留"可能"。（自造）
negative: 原文说"可能与天气有关"，改写成"与天气有关"。——违反点：去掉"可能"，把不确定表述为确定。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得把不确定说成确定"
notes: 与 U-qaw-007、U-qaw-009 同在一句话内，按"两个'并且'连接的独立要求拆成两个单元"的判据拆开。
```

### U-qaw-009

```
id: U-qaw-009
category: protection
language: zh
rule_summary: 不得把原文表达的相关性升级成因果关系。
positive: 原文说"两者同期上升"，改写后仍表述为同期上升，不称因果。（自造）
negative: 原文说"两者同期上升"，改写成"上升是因为另一者带动"。——违反点：把相关性表述改成了因果表述。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "也不得把相关性升级成因果"
```

### U-qaw-010

```
id: U-qaw-010
category: protection
language: zh
rule_summary: 不得把原文的排除关系改写成更强的正面事实；排除某种归因不等于确认另一种正面结论。
positive: 引自上游——"问题不能归因于大家不够努力"，改写后仍保持"这不是因为不够努力"这一排除表述。
negative: 引自上游——把"问题不能归因于大家不够努力"改写成"大家一直很努力"。违反点：把排除一种归因偷换成了肯定另一种正面事实。
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得把排除关系改成更强的正面事实"
```

### U-qaw-011

```
id: U-qaw-011
category: protection
language: zh
rule_summary: 不得从原文描述的症状自行推出具体解决方案；原文只给出方向性表述时，不得替换成具体动作项。
positive: 引自上游——原文说"完善协同机制"，改写后仍保留"完善协同机制"这一方向性表述。
negative: 引自上游——把"完善协同机制"改写成"形成明确结论、设负责人、规定时限"。违反点：把方向性表述换成了原文没有的具体动作项。
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得从症状自行推出解决方案"
```

### U-qaw-012

```
id: U-qaw-012
category: protection
language: zh
rule_summary: 编辑幅度按用户请求的关键词确定授权范围：说"改写/重写/去AI味/更有人味"允许重建语言和全文信息架构；说"润色"默认只能调整句序、拆并句和必要的段落安排，保留篇幅、段落职责与声口；说"校对"只处理错字、病句和明确错误，不做结构重写。
positive: 用户说"帮我润色一下"，只调整句序和拆并句，篇幅和段落职责不变。（自造）
negative: 用户说"帮我校对一下"，结果重新组织了段落结构。——违反点：校对请求超出了"只处理错字、病句和明确错误"的授权范围，做了结构重写。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 确定授权与幅度"
notes: 三级授权共用同一条"关键词→授权范围"判定逻辑，按共用逻辑合并为一个单元；归并阶段如需按级单独裁决可再拆，已记入"拆分时拿不准的地方"。
```

### U-qaw-013

```
id: U-qaw-013
category: protection
language: zh
rule_summary: 用户给出的具体编辑范围优先于上述默认幅度设定。
positive: 用户说"帮我润色，但可以调整段落顺序"，按用户给出的范围执行段落调整，即使"润色"默认不含大幅结构调整。（自造）
negative: 用户明确说"只改错字，不要动结构"，但仍按默认校对幅度之外做了段落合并。——违反点：无视用户明确给出的范围，套用了默认幅度。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "用户给出的具体范围高于上述默认值"
```

### U-qaw-014

```
id: U-qaw-014
category: protection
language: zh
rule_summary: 用户明确要求改写、重写、润色、去AI味或"用qu-ai-wei处理"这份文字，即视为已授权编辑，即使文本读起来像真人所写；授权编辑不等于要求全面更换作者声口。
positive: 文本带有明显的口语化个人表达，用户明确说"帮我用qu-ai-wei改一下"，据此判断已获授权，正常进入改写流程。（自造）
negative: 文本读起来像真人写的，用户已经明确要求"帮我改写"，仍以"像真人写的"为由拒绝处理。——违反点：忽视用户已给出的明确授权指令，仅凭文本像真人写就停手。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "先检查自纠、犹疑、自嘲、方言"
```

### U-qaw-015

```
id: U-qaw-015
category: protection
language: zh
rule_summary: 用户只提供文本、没有给出任何编辑指令时，判断为真人所写的文本保持原样，不主动改写。
positive: 用户只贴了一段文字，没有提出任何要求，文本带有明显个人声口，判断后原样返回并说明保留原因。（自造）
negative: 用户只贴了一段文字，没提要求，文本像真人写的，仍主动重写并输出终稿。——违反点：用户未给出任何编辑指令，仍主动改写真人文本。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "只有用户仅提供文本、没有给出任何编辑指令时"
```

### U-qaw-016

```
id: U-qaw-016
category: protection
language: zh
rule_summary: 获得改写授权不等于获得全面更换作者声口的授权。
positive: 用户要求改写一篇带方言表达的文章，改写中保留原有的方言用词习惯，只调整句法和结构。（自造）
negative: 用户只要求"改写得更自然"，结果把原本口语化、带方言的声口全部换成书面正式腔。——违反点：把改写授权当成了更换整体声口的授权。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "授权编辑不等于全面换声口"
```

### U-qaw-017

```
id: U-qaw-017
category: process
language: zh
rule_summary: 同一原文用于品牌官网、自媒体、客服、内部材料等不同场景会产生不同成稿，用户没有提供足以判定用途的信息时，普通模式输出"判断：不确定"并询问发布渠道，不得自行补出品牌主体、发布渠道或叙述身份。
positive: 用户只给了一段介绍性文字，没说发在哪里，输出"判断：不确定 | 证据：[…] | 行动：请问这段会发布在哪个渠道？"（自造）
negative: 用户只给了一段介绍性文字，没说发在哪里，改写时自行假定是"品牌官网文案"并按官网语体处理。——违反点：用途不明时自行补出发布渠道和语体假设，未询问。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "授权编辑也不等于目标语体已经明确"
```

### U-qaw-018

```
id: U-qaw-018
category: process
language: zh
rule_summary: 命中"真人文本（停手）"判断时立即结束：普通模式只输出门检和简短停手说明，不另设终稿或打磨报告；内嵌模式只返回原文；不得先复制全文再包装成"无需改写"的终稿。
positive: 判断为真人文本且未获授权时，普通模式只输出门检结果和一句停手说明，不生成终稿区块。（自造）
negative: 判断为真人文本且未获授权，仍输出一份"终稿"区块，内容是原文照抄，标注"无需改写"。——违反点：命中停手判断后仍生成了终稿区块，只是把原文包装成了"无需改写"。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "命中「真人文本（停手）」时立即结束"
```

### U-qaw-019

```
id: U-qaw-019
category: process
language: zh
rule_summary: 停手说明只写一句授权结论，不得重复门检已经列出的生活细节或声口证据。
positive: 引自上游——「这段已有清楚的个人声口，你没有明确授权改写，我先保留原文。」
negative: 停手说明写成"这段提到了你去年生病住院、和同事吵架、还用了方言词'恁'，这些都是个人声口的证据，你没有授权改写，我先保留原文。"——违反点：重复罗列了门检已经列出的生活细节和声口证据，超出"只写一句授权结论"的要求。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "停手说明只写一句授权结论"
```

### U-qaw-020

```
id: U-qaw-020
category: protection
language: zh
rule_summary: 真实引语、代码、公式、法律条款、标准定义、专名、引用标识和用户明确要求保留的文字属于受保护片段，默认保持正文不变，只调整周边衔接；只有用户明确授权某一类后才能改动该类。
positive: 原文引用了一段法律条款原文，改写时只调整条款前后的衔接句，条款本身逐字保留。（自造）
negative: 原文引用的一段法律条款被改写成了意译版本，用户并未授权改动引用内容。——违反点：改动了受保护片段（法律条款原文），未获用户明确授权。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "真实引语、代码、公式、法律条款、标准定义、专名、引用标识"
notes: 词表内各类受保护对象共用同一条"默认不变，需明确授权才改"的判定逻辑，合并为一个单元。
```

### U-qaw-021

```
id: U-qaw-021
category: protection
language: zh
rule_summary: 无法确认真伪的引语不得擅自改写。
positive: 文中一句引语来源不明，无法核实是否为原话，改写时原样保留该引语。（自造）
negative: 文中一句引语来源不明，改写时把它换了个说法使其"更通顺"。——违反点：对真伪无法确认的引语做了改写。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "无法确认真伪的引语不擅自改写"
```

### U-qaw-022

```
id: U-qaw-022
category: process
language: zh
rule_summary: 普通模式输出门检、终稿和简短打磨报告；存在实质逻辑风险时另加"需作者确认"区块。
positive: 一次常规改写输出了门检、终稿、打磨报告三个区块，未发现逻辑风险，不加需作者确认。（自造）
negative: 改写中发现原文的因果关系可能超出证据，但只输出了门检、终稿和打磨报告，没有加"需作者确认"提示风险。——违反点：存在实质逻辑风险却没有输出"需作者确认"区块。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 选择输出模式"
notes: 与 U-qaw-062（输出契约一节的逐字标签要求）覆盖同一主题的不同层面，前者定内容构成，后者定格式与省略限制，两者互相引用。
```

### U-qaw-023

```
id: U-qaw-023
category: process
language: zh
rule_summary: 内嵌模式只在被另一流程明确标记为内嵌步骤，或用户明确要求"只给终稿/只输出正文/不要过程"时使用，此时只输出终稿正文，不输出门检、标题、报告或摘要。
positive: 用户明确说"只要终稿，别的都不要"，只输出终稿正文，不输出门检和报告。（自造）
negative: 上游流程调用本skill时没有标记为内嵌步骤，用户也没提只要终稿，仍只输出终稿正文。——违反点：不满足内嵌模式的触发条件，却按内嵌模式只输出正文。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "内嵌模式（embedded mode）"
notes: 输出契约一节末句"内嵌模式只输出终稿正文，不输出门检、标题、报告或摘要"是本条的重复表述，已并入本单元，不单列。
```

### U-qaw-024

```
id: U-qaw-024
category: protection
language: zh
rule_summary: 内嵌模式不降低任何约束，也不增加写文件、发布或发送的权限；无法安全完成改写时应提问或返回阻塞说明，不得凭空猜测终稿。
positive: 内嵌模式下遇到无法判断是否为受保护引语的情况，返回阻塞说明而不是猜测处理。（自造）
negative: 内嵌模式下遇到敏感信息判断不清的情况，直接按自己的猜测生成终稿并输出。——违反点：无法安全完成时没有提问或返回阻塞说明，而是猜测生成了终稿。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "内嵌模式不降低约束"
```

### U-qaw-025

```
id: U-qaw-025
category: process
language: zh
rule_summary: 普通模式的门检必须使用固定的四种判定格式之一（AI高频写作症状 / 真人文本（停手）/ 真人文本（已授权改写）/ 不确定），且只说明编辑状态，不对作者身份下结论；证据用具体结构描述。
positive: 引自上游——【门检】判断：AI 高频写作症状 | 证据：[至多两条具体结构]
negative: 门检写成"【门检】判断：这段是AI写的 | 证据：读起来很生硬"。——违反点：判断措辞对作者身份下了结论（"这段是AI写的"），且证据不是具体结构描述。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "普通模式的门检只说明编辑状态，不鉴定作者"
```

### U-qaw-026

```
id: U-qaw-026
category: process
language: zh
rule_summary: 门检的证据至多列出两条具体结构。
positive: 门检证据栏写"证据：排比句式、总结句重复"（两条）。（自造）
negative: 门检证据栏列出五条具体结构。——违反点：证据条数超过两条的上限。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "至多两条具体结构"
```

### U-qaw-027

```
id: U-qaw-027
category: protection
language: zh
rule_summary: 改写正文前须建立全文信息账本，逐项记录人物、事实、数字、时间、地点、动作、引语、归因、评价、排除项、限定、来源和术语。
positive: 改写前列出信息账本，逐项记下文中出现的人名、日期、数字和引语。（自造）
negative: 直接开始改写，没有先列出信息账本记录文中的人物、数字、引语等内容。——违反点：跳过了建立信息账本这一步，直接局部改写。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 1. 冻结不可丢失内容"
notes: 词表内各类记录对象（人物、事实、数字……）共用"须逐项记入信息账本"这一条判定逻辑，合并为一个单元。
```

### U-qaw-028

```
id: U-qaw-028
category: protection
language: zh
rule_summary: 改写正文前须建立论证图，标出主张、依据、例子、反例、条件、比较、因果和结论。
positive: 改写前梳理出文章的主要主张和支撑它的依据、例子。（自造）
negative: 直接开始改写，没有先梳理文章的主张、依据、条件、结论等论证结构。——违反点：跳过了建立论证图这一步。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 1. 冻结不可丢失内容"
notes: 与 U-qaw-027 同一小节但对象不同（论证结构 vs 事实清单），拆成两个单元。
```

### U-qaw-029

```
id: U-qaw-029
category: process
language: zh
rule_summary: 输入较长时，在建立信息账本和论证图的同时标记段落职责和术语写法。
positive: 处理一篇长文时，除了信息账本和论证图，还标出每段的职责（例如"背景段""论证段"）和术语的统一写法。（自造）
negative: 处理一篇长文时只做了信息账本，没有标记段落职责和术语写法。——违反点：输入较长却没有补做段落职责和术语标记。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 1. 冻结不可丢失内容"
```

### U-qaw-030

```
id: U-qaw-030
category: process
language: zh
rule_summary: 必须先掌握全局约束（信息账本、论证图），才能按章节处理；不得分别润色孤立段落再拼接成全文。
positive: 先完成全文信息账本和论证图，再逐章节改写。（自造）
negative: 跳过全局梳理，直接把文章拆成几段分别润色，再拼接成终稿。——违反点：没有先掌握全局约束就按孤立段落处理，再拼接成全文。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得分别润色孤立段落再拼成全文"
```

### U-qaw-031

```
id: U-qaw-031
category: process
language: zh
rule_summary: 所有语体的改写都要扫描八个模式族：内容真实性与具体性、证据推论与结论强度、篇章组织与信息推进、简体中文句法与语序、词汇搭配与抽象密度与语义复现、修辞节奏与表现形式、受众体裁平台与交互残留、来源引用与事实一致性。
positive: 改写客服文案时，仍按八个模式族逐一扫描，包括来源引用与事实一致性。（自造）
negative: 改写时只检查了句法和修辞两个方面，没有扫描证据强度、事实一致性等其余模式族。——违反点：跳过了八个模式族中的若干项，扫描不完整。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 2. 扫描八个模式族"
notes: 八个模式族共用同一条"每种语体都必须扫描"的判定逻辑，合并为一个单元，词表放进正反例。
```

### U-qaw-032

```
id: U-qaw-032
category: process
language: zh
rule_summary: 语体（如学术、自媒体、客服）只调整八个模式族的触发阈值和改写幅度，不能因为语体不同就关闭整个模式族的扫描。
positive: 处理轻松的自媒体文案时，降低"修辞节奏"这一族的改写幅度，但仍然扫描它。（自造）
negative: 处理轻松的自媒体文案时，认为不需要检查"来源、引用与事实一致性"这一族，直接跳过。——违反点：因语体不同直接关闭了整个模式族，而不是调整阈值。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "语体只调整触发阈值和改写幅度"
```

### U-qaw-033

```
id: U-qaw-033
category: process
language: zh
rule_summary: 重建信息架构前，先确定每段真正要完成的工作，再决定事实、解释、例子和结论的出场顺序。
positive: 先判断某段的职责是"给出结论"，再决定这段里事实和解释谁先谁后。（自造）
negative: 没有先确定段落职责，直接按原文顺序调换事实和结论的位置。——违反点：跳过确定段落职责这一步，直接调整出场顺序。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 3. 重建信息架构"
```

### U-qaw-034

```
id: U-qaw-034
category: process
language: zh
rule_summary: 重建信息架构时允许：改变句子主干、主语和信息重心；拆句、并句及跨句重组；合并、拆分和调换段落；重写标题、列表和层级；删除舞台指令、空洞升华和语义完全重复的内容。
positive: 把两个意思重复的段落合并成一个，删除其中重复的空洞总结句。（自造）
negative: 以"不能动结构"为由拒绝合并两个语义完全重复的段落。——违反点：这类合并属于允许范围内的操作，不应因为过度保守而不做。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "允许："
notes: "允许"清单中的操作共用一条"这些操作不算过度编辑"的判定逻辑，合并为一个单元；其中"移动引用及其支持的陈述"因附带独立的判定条件，拆为 U-qaw-035 单列。
```

### U-qaw-035

```
id: U-qaw-035
category: protection
language: zh
rule_summary: 移动引用及其支持的陈述时必须一起移动；引用标识须紧跟它实际支持的最后一项陈述，若下一句或同句后半新增了来源未支持的内容，须先拆句，不能让引用标识挂在更宽的陈述之后。
positive: 把一句带引用标识的陈述整体移到新位置，标识仍紧跟它原本支持的那句话。（自造）
negative: 把带引用标识的陈述移动后，又在同句后半追加了一条该引用并不支持的新论断，引用标识却留在了整句末尾。——违反点：引用标识挂在了包含未获引用支持内容的更宽陈述之后，没有先拆句。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "移动引用及其支持的陈述"
notes: 这是本来源"引用绑定"特征最集中的规则，归并阶段优先级最高。
```

### U-qaw-036

```
id: U-qaw-036
category: protection
language: zh
rule_summary: 不得默认对内容做摘要式压缩；独立的事实、限定、例子、反例、评价或证据均须保留，只有用户明确要求精简、压缩或缩短时才可实质压缩。
positive: 用户没提压缩要求，改写保留了原文列出的三个例子。（自造）
negative: 用户没提压缩要求，改写时把原文的三个例子合并省略成一个。——违反点：在用户未要求压缩的情况下做了摘要式删减，丢掉了独立的例子。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不要默认摘要"
```

### U-qaw-037

```
id: U-qaw-037
category: pattern
language: zh
rule_summary: 原文中显眼的对称写作骨架（如排比、三段式并列）应重建而非只做同义词替换。
positive: 原文用三个结构完全相同的排比句表达三层意思，改写时打破排比结构，按各自的重要性重新组织。（自造）
negative: 原文的三个排比句只是把其中的形容词换了近义词，句式结构原样保留。——违反点：只做了同义换壳，没有重建对称骨架。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "显眼的对称骨架要重建，不做同义换壳"
```

### U-qaw-038

```
id: U-qaw-038
category: protection
language: zh
rule_summary: 真实引语、固定表述，或改变外壳会造成歧义的表达，即使形式对称也应保留，不因"重建骨架"的要求而改动。
positive: 三句排比中有一句是受访者的真实原话，改写时保留这句原话，只调整其余两句的结构。（自造）
negative: 为了打破排比骨架，把受访者的真实原话也换了说法。——违反点：真实引语不应因重建骨架而被改动。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "真实引语、固定表述或改变外壳会造成歧义时保留"
```

### U-qaw-039

```
id: U-qaw-039
category: process
language: zh
rule_summary: 具体的骨架识别、断言强度判断和拆并规则显眼的对称骨架要重建，不做同义换壳，不得凭经验另立标准。
positive: 判断某个句式是否属于需要打破的对称骨架时，依据 pattern-catalog.md 里的定义。（自造）
negative: 凭自己的语感判定某段是"AI味的对称结构"并改写，没有对照 pattern-catalog.md。——违反点：没有以 pattern-catalog.md 为权威依据，自行判断骨架标准。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "显眼的对称骨架要重建，不做同义换壳"
```

### U-qaw-040

```
id: U-qaw-040
category: pattern
language: zh
rule_summary: 按简体中文重写时优先使用清楚的行动者和直接动词。
positive: "工厂上个月裁员两百人"优于"上个月发生了两百人的裁员行为"。（自造）
negative: 改写后仍写成"相关裁员行为在上个月发生"，没有点明行动者"工厂"，也没用直接动词。——违反点：主语被隐去，用了名词化的"行为发生"代替直接动词。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
```

### U-qaw-041

```
id: U-qaw-041
category: pattern
language: zh
rule_summary: 把条件、时间和范围放到句子里最容易理解的位置，不要让读者需要读完全句才能确定适用范围。
positive: "2023年起，总部员工的年假从10天增加到15天"把时间和适用范围放在句首。（自造）
negative: "年假从10天增加到15天，这一调整仅适用于2023年起入职的总部员工"——违反点：适用范围和时间被放到句尾，读者读到中途以为是普遍调整。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
notes: "最容易理解的位置"缺少客观量化标准，可判定性弱于本节其余句法规则，归并阶段需按 criteria.md 第2条重新评估是否可判定，已记入"拆分时拿不准的地方"。
```

### U-qaw-042

```
id: U-qaw-042
category: pattern
language: zh
rule_summary: 不要让句子主干被"在……背景下""基于……""通过……"这类前置状语结构长期压后。
positive: "公司裁员两百人，原因是订单减少"把主干提前。（自造）
negative: "在订单持续减少的背景下，基于降本增效的考虑，通过内部评估，公司裁员两百人。"——违反点：主干"公司裁员两百人"被三层"在……背景下/基于……/通过……"结构压到句末。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
```

### U-qaw-043

```
id: U-qaw-043
category: pattern
language: zh
rule_summary: 打破全文中长度均等的句子和结构雷同的段落。
positive: 把原文中三段字数、结构几乎相同的段落改写成长短不一、结构各异的段落。（自造）
negative: 改写后仍保留原文三段字数相近、开头句式相同的段落结构。——违反点：没有打破等长句和同构段落。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
```

### U-qaw-044

```
id: U-qaw-044
category: pattern
language: zh
rule_summary: 合并语义破碎的短句，拆开信息过载的长句。
positive: 把"他去了。很晚。很累。"合并为"他很晚才疲惫地赶到"；把一句塞了五个信息点的长句拆成两三句。（自造）
negative: 一句话里塞了时间、地点、原因、结果、评价五个信息点，改写后仍是一句没有拆分。——违反点：没有拆开过载的长句。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
```

### U-qaw-045

```
id: U-qaw-045
category: pattern
language: zh
rule_summary: 删除无功能的连接词、元叙述和结论标签。
positive: 删除"值得注意的是""综上所述，我们可以看到"这类元叙述和结论标签。（自造）
negative: 改写后仍保留"值得一提的是"这种不承载实际信息的元叙述开头。——违反点：保留了无功能的元叙述。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 4. 按简体中文重写"
```

### U-qaw-046

```
id: U-qaw-046
category: protection
language: zh
rule_summary: 删除无功能的连接词、元叙述和结论标签的同时，须保留原文真实的逻辑关系、必要术语及正式程度。
positive: 删除了"综上所述"这个结论标签，但保留了它后面表达的真实因果关系。（自造）
negative: 为了删除"因此"这个连接词，把前后两句的因果关系也一并抹掉，变成两句并列陈述。——违反点：删除连接词的同时丢掉了真实存在的因果关系。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "但保留真实关系、必要术语及正式程度"
```

### U-qaw-047

```
id: U-qaw-047
category: pattern
language: zh
rule_summary: 不得为了制造"人味"而添加错别字、emoji、网络用语、第一人称、幽默、感受或个人经历；自然不等于口语化。
positive: 改写后文字通顺自然，但没有额外添加emoji或网络热词。（自造）
negative: 为了让文字显得像真人写的，改写时加了几个emoji和"绝绝子"这类网络用语。——违反点：为营造人味添加了原文没有的emoji和网络用语。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不要为了“人味”添加错别字、emoji、网语"
notes: 词表内各类禁用手段（错别字、emoji、网语、第一人称、幽默、感受、个人经历）共用同一条"不得为营造人味添加"的判定逻辑，合并为一个单元。
```

### U-qaw-048

```
id: U-qaw-048
category: pattern
language: zh
rule_summary: 由表达外壳（措辞方式）制造的虚假逻辑关系，可以在不改变原意的前提下改写消除。
positive: 原文"由于天气原因，加上大家的努力，项目按时完成"中的"由于……加上……"只是行文习惯，并非真实并列因果，改写为"项目按时完成，期间遇到天气影响，团队也付出了努力"，不再暗示两者共同构成因果。（自造）
negative: 把这句强行拆成"天气原因导致项目延误风险，大家的努力抵消了这一风险，因此项目按时完成"，编出了原文没有的因果链条。——违反点：没有等义重写虚假因果外壳，反而编造了新的因果链条。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 5. 处理逻辑风险"
```

### U-qaw-049

```
id: U-qaw-049
category: protection
language: zh
rule_summary: 原文的因果、权衡、比较或结论可能超过证据支持时，不得静默替作者纠正，也不得在终稿正文里插入编辑标签。
positive: 发现原文的因果表述可能证据不足时，在【需作者确认】区块提示，终稿正文保持原文表述。（自造）
negative: 发现原文因果表述证据不足，直接在终稿正文里把结论改弱，或者在正文里插入"（编者注：此处证据不足）"这样的标签。——违反点：在终稿正文里静默改动了结论或插入了编辑标签。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不静默替作者纠正"
```

### U-qaw-050

```
id: U-qaw-050
category: process
language: zh
rule_summary: 原文的因果、权衡、比较或结论可能超过证据，但能自然保义改写时，保留原主张，在"需作者确认"简短指出风险。
positive: 原表述可以在不改变主张的前提下换一种说法降低误导性，同时在需作者确认里注明"该结论的证据支持力度有限"。（自造）
negative: 能够自然保义处理的情况下，却直接删掉了原主张。——违反点：本可自然保义却删除了原主张，而不是保留主张并标注风险。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "能自然保义：保留原主张"
```

### U-qaw-051

```
id: U-qaw-051
category: process
language: zh
rule_summary: 原文的因果、权衡、比较或结论可能超过证据，且无法自然保留原表述而不继续误导时，应暂停并请求作者确认，不得强行改写下去。
positive: 遇到无法在不误导读者的前提下保留的强因果结论时，暂停改写并向作者提问确认。（自造）
negative: 遇到无法自然保留而不误导的强因果结论，仍继续按原计划完成整篇改写并直接交付终稿。——违反点：应暂停请求确认的情况下继续完成了改写。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "无法自然保留而不继续误导：暂停并请求作者确认"
```

### U-qaw-052

```
id: U-qaw-052
category: process
language: zh
rule_summary: 默认只检查文内一致性和引用绑定，不自动调查外部来源；只有用户要求查证，或任务本身属于研究工作时才做外部核验。
positive: 改写时核对了文中引用与其支持陈述是否一致，没有主动上网查证引用来源的真实性。（自造）
negative: 用户没有要求查证，任务也不是研究工作，改写者却主动去搜索验证原文引用的数据来源。——违反点：在未获授权的情况下做了外部核验，超出默认检查范围。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "默认只检查文内一致性和引用绑定"
```

### U-qaw-053

```
id: U-qaw-053
category: pattern
language: zh
rule_summary: 全文复扫时检查是否仍存在同义重复、机械对称、推论台阶和整齐收尾。
positive: 复扫发现结尾仍是一句空洞的升华式总结，删除处理。（自造）
negative: 复扫时没有检查结尾是否还有整齐的升华式收尾，直接交稿。——违反点：跳过了对机械对称和整齐收尾的复查。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 6. 全文复扫"
```

### U-qaw-054

```
id: U-qaw-054
category: protection
language: zh
rule_summary: 全文复扫时检查是否改变了事实、范围、归因、证据强度或不确定性。
positive: 复扫时对照信息账本，确认所有数字和归因与原文一致。（自造）
negative: 复扫时没有核对数字和归因是否与原文一致，直接交付终稿。——违反点：跳过了对事实、归因、证据强度是否漂移的复查。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 6. 全文复扫"
```

### U-qaw-055

```
id: U-qaw-055
category: protection
language: zh
rule_summary: 全文复扫时检查引用是否仍支持相邻陈述，专名和术语是否一致。
positive: 复扫时发现一处引用因为段落调整已经不再紧邻其支持的陈述，重新调整位置。（自造）
negative: 复扫时没有检查引用位置是否因为段落调整而与原陈述脱节。——违反点：跳过了引用绑定的复查。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 6. 全文复扫"
```

### U-qaw-056

```
id: U-qaw-056
category: process
language: zh
rule_summary: 全文复扫时检查标题、列表和段落层级是否真的帮助阅读或执行，而不是为了形式好看而设置。
positive: 复扫发现一个不必要的三级列表让内容更难读，改回段落形式。（自造）
negative: 复扫时保留了一个把简单的一句话拆成三条列表项的结构，只是因为列表看起来更规整。——违反点：为形式好看保留了不利于阅读的列表结构，没有做这项检查。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 6. 全文复扫"
```

### U-qaw-057

```
id: U-qaw-057
category: pattern
language: zh
rule_summary: 全文复扫时检查句长、段长和句式是否有自然变化，声口是否前后一致。
positive: 复扫发现连续三句长度几乎相同，调整其中一句的长度。（自造）
negative: 复扫时没有检查句长是否有自然变化，交付的终稿里连续多句长度几乎一致。——违反点：跳过了句长变化和声口一致性的复查。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "### 6. 全文复扫"
```

### U-qaw-058

```
id: U-qaw-058
category: measurement
language: zh
rule_summary: 复扫后须判断改动是否带来可验证的改善；若没有，原样返回原文并说明无需改写。
positive: 复扫后发现改写并未让文字更清楚或更准确，交付时说明"无需改写"并返回原文。（自造）
negative: 复扫后改动其实没有带来任何可验证的改善，仍然交付了改写后的版本而不说明。——违反点：改动没有带来可验证改善却仍然替换了原文，没有原样返回并说明。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "改动是否带来可验证改善"
```

### U-qaw-059

```
id: U-qaw-059
category: process
language: zh
rule_summary: 输入超长或不完整时，可交付阶段稿，但须明确标注已处理范围、未完成范围、尚未通过的全局检查，以及当前稿能否独立使用。
positive: 处理一篇过长文章时先交付前三章的阶段稿，并说明后续章节未处理、全局引用检查尚未完成。（自造）
negative: 处理一篇过长文章时只交付了处理过的部分，没有说明哪些范围未处理、也没说明能否独立使用。——违反点：阶段稿缺少已处理范围、未完成范围和可用性说明。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 长文与不完整输入"
```

### U-qaw-060

```
id: U-qaw-060
category: process
language: zh
rule_summary: 输入缺失的部分会影响事实、指代或论证关系时，应先请求完整文件或明确的拆分边界，不得直接处理不完整输入。
positive: 发现文章缺失的部分包含关键的指代对象，先向用户请求完整文件再处理。（自造）
negative: 明知缺失部分会影响文中的指代关系，仍直接按现有片段改写。——违反点：缺失内容影响指代关系时没有先请求完整文件。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "缺失部分会影响事实、指代或论证关系时"
```

### U-qaw-061

```
id: U-qaw-061
category: protection
language: zh
rule_summary: 不得把阶段稿称为全文终稿。
positive: 阶段性交付的内容标注为"阶段稿"，不使用"终稿"字样。（自造）
negative: 只处理了文章的一部分，却在交付时称之为"终稿"。——违反点：把未完成的阶段稿称为了全文终稿。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "不得把阶段稿称为全文终稿"
```

### U-qaw-062

```
id: U-qaw-062
category: process
language: zh
rule_summary: 普通模式必须逐字使用门检、终稿、打磨报告三个区块标签，不能因为终稿简短而省略门检或报告；"需作者确认"区块只在存在风险时出现。
positive: |
  引自上游——
  【门检】判断：[…]| 证据：[…]

  终稿
  [完整终稿；若无需改写则返回原文]

  【打磨报告】
  · 结构：[最重要的结构变化或"无需改写"]
  · 语言：[最重要的语言变化或"无"]
  · 保留：[关键事实、声口或受保护片段]
negative: 因为原文本来就很自然、终稿只有一句话不变，就只输出终稿这一句，省略了门检和打磨报告区块。——违反点：因终稿简短而省略了门检和打磨报告标签，违反"不能因终稿简短而省略"的要求。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 输出契约"
```

### U-qaw-063

```
id: U-qaw-063
category: process
language: zh
rule_summary: 不得把AI生成的文本伪装成未使用AI，也不协助规避平台或机构的相关政策。
positive: 拒绝按用户要求"把这段AI生成的文字改到查重工具查不出是AI写的"这类请求中涉及伪装的部分。（自造）
negative: 按用户要求专门优化文字使其能规避某平台的AI内容标注政策。——违反点：协助伪装AI文本、规避机构政策。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 能力边界"
```

### U-qaw-064

```
id: U-qaw-064
category: protection
language: zh
rule_summary: 不得替文章重新立论，不得新增原文没有的论据、采访内容或专业判断。
positive: 改写时只调整原有论据的表达方式，不新增任何论据或专业判断。（自造）
negative: 改写时觉得原文论证不够有力，补充了一条原文没有的行业数据作为新论据。——违反点：新增了原文没有的论据。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 能力边界"
notes: 与 U-qaw-007（不得为了顺口补写事实、因果、经历、例子、观点或结果）主题相近但对象不同（本条特指立论、论据、采访、专业判断），保留为独立单元。
```

### U-qaw-065

```
id: U-qaw-065
category: process
language: zh
rule_summary: 不得因为获得了结构重写的权限，就强行改动已经自然、无需改写的文本。
positive: 判断原文已经自然通顺，即使获得了改写授权，也原样返回并说明无需改写。（自造）
negative: 获得改写授权后，即使原文已经很自然，仍然强行调整了句式和段落顺序以显得"做了工作"。——违反点：文本已经自然，却因为有改写权限而强行改动。（自造）
source:
  type: upstream
  source_id: upstream-lifelonglazylearner-qu-ai-wei
  path: SKILL.md
  commit: 39da1cfac4f0e3e4d2b46bc7188a0edc762b8d17
  anchor: "## 能力边界"
notes: 与 U-qaw-058（改动须带来可验证改善否则原样返回）是同一原则在不同小节的呼应：058 是复扫步骤里的执行门检，本条是能力边界里的授权原则声明，保留为两个单元。
```

## 3 覆盖表

| 来源小节 | 归属单元 / 说明 |
|---|---|
| frontmatter：`name` | 非规则内容（skill 标识符） |
| frontmatter：`description` | U-qaw-001 |
| 标题「# 去 AI 味（qu-ai-wei）」 | 非规则内容（标题） |
| 开篇段（"把一段话……"至"……不用局部换词假装完成改写"） | U-qaw-002（与能力边界重复表述，主锚点在能力边界）、U-qaw-003 |
| "除非用户或调用方明确说……"段 | U-qaw-004 |
| "处理正文前先做敏感信息门检……"段 | U-qaw-005 |
| ## 仲裁顺序 | U-qaw-006、U-qaw-007、U-qaw-008、U-qaw-009、U-qaw-010、U-qaw-011 |
| ## 确定授权与幅度 | U-qaw-012、U-qaw-013、U-qaw-014、U-qaw-015、U-qaw-016、U-qaw-017、U-qaw-018、U-qaw-019、U-qaw-020、U-qaw-021 |
| ## 选择输出模式 | U-qaw-022、U-qaw-023、U-qaw-024、U-qaw-025、U-qaw-026 |
| ## 执行完整重写（一级标题本身） | 非规则内容（章节标题） |
| ### 1. 冻结不可丢失内容 | U-qaw-027、U-qaw-028、U-qaw-029、U-qaw-030 |
| ### 2. 扫描八个模式族 | U-qaw-031、U-qaw-032 |
| ### 2 节内"准备诊断或改写时读……""保护条件拿不准时读……"两句 | 非规则内容（指向 references 文件的导航说明，与"按需参考"一节性质相同） |
| ### 3. 重建信息架构 | U-qaw-033、U-qaw-034、U-qaw-035、U-qaw-036、U-qaw-037、U-qaw-038、U-qaw-039 |
| ### 4. 按简体中文重写 | U-qaw-040、U-qaw-041、U-qaw-042、U-qaw-043、U-qaw-044、U-qaw-045、U-qaw-046、U-qaw-047 |
| ### 5. 处理逻辑风险 | U-qaw-048、U-qaw-049、U-qaw-050、U-qaw-051、U-qaw-052 |
| ### 6. 全文复扫 | U-qaw-053、U-qaw-054、U-qaw-055、U-qaw-056、U-qaw-057、U-qaw-058 |
| ## 长文与不完整输入 | U-qaw-059、U-qaw-060、U-qaw-061 |
| ## 按需参考 | 非规则内容（六条 reference 文件的索引说明，本身不是可判定规则） |
| ## 输出契约 | U-qaw-062（含"内嵌模式只输出终稿正文……"一句，并入 U-qaw-023） |
| ## 能力边界 | U-qaw-002（主锚点）、U-qaw-063、U-qaw-064、U-qaw-065 |

## 4 拆分时拿不准的地方

1. U-qaw-002 的锚点选择：开篇段与"能力边界"一节对同一条规则各有一句表述，本清单把主锚点定在"能力边界"（表述更完整），开篇段视为重复出现不再单列。归并阶段如果认为两处措辞有实质差异（开篇段只提"作者身份鉴定"，能力边界多了"真实性或道德判断"），可能需要拆回两条。
2. U-qaw-012（改写/润色/校对三级授权范围）目前按共用的"关键词→授权范围"判定逻辑合并为一个单元。三级各自的具体权限边界不同，归并阶段如果需要对某一级单独裁决（例如只采纳"校对"级的定义、不采纳其余两级），可能需要拆成三条。
3. U-qaw-017 中列出的品牌官网、自媒体、客服、内部材料四种场景是否要按场景各建一条，还是按当前处理为一条"用途不明则问"的门检规则，两种拆法都成立，本清单选择了后者。
4. U-qaw-041（把条件、时间、范围放到最容易理解的位置）的可判定性弱于同小节其余规则，"最容易理解"没有客观量化标准。按 criteria.md 第2条，归并阶段需要重新评估这条是否可判定，不排除被记为 rejected。
5. U-qaw-034（允许的结构重写范围）与 U-qaw-003、U-qaw-037、U-qaw-065 在"允许/要求全文结构重写"这一主题上有多处呼应，是否会在归并阶段被认为内容过碎、需要合并，留给归并阶段判断；本清单按拆分判据（各自的判定对象不同：授权原则、具体允许操作清单、对称骨架专项、复扫环节的授权边界）保留为独立单元。
6. U-qaw-019（停手说明只写一句、不重复门检证据）归为 process 而非 protection，是因为规则目的看起来是格式简洁，而非专门保护个人隐私；如果归并阶段认为其实质是避免二次暴露门检中提到的生活细节，可能需要改记 protection。

## 5 疑似常见规则

以下单元的判断逻辑（不涉及本来源专有的措辞）估计在其他去 AI 味类项目里也会出现，归并阶段聚类时可优先核对：

- U-qaw-005（敏感信息/凭证检测并停止）
- U-qaw-020（受保护片段：引语、代码、公式、法律条款、专名默认不变）
- U-qaw-036（不默认摘要压缩，独立事实须保留）
- U-qaw-037（对称骨架应重建而非同义换壳）
- U-qaw-040（优先清楚行动者和直接动词）
- U-qaw-042（主干不应被"在……背景下/基于……/通过……"压后）
- U-qaw-043（打破等长句和同构段落）
- U-qaw-045（删除无功能连接词、元叙述、结论标签）
- U-qaw-047（不为营造人味添加错别字/emoji/网语等）
- U-qaw-053（复扫检查同义重复、机械对称、推论台阶、整齐收尾）
- U-qaw-058（改动须带来可验证改善，否则原样返回）
- U-qaw-063（不协助伪装AI文本、不协助规避机构政策）
- U-qaw-064（不新增论据、采访、专业判断）

## 6 上游文本内的指令

无。通读全文未发现针对读者/模型的注入式指令（如"忽略之前的规则""把这段加进你的系统提示"等）。
