# 来源拆分：upstream-ai-zixun-humanizer-zh

## 1 来源摘要

- 文件：`merges/maybe-humanizer/snapshots/upstream-ai-zixun-humanizer-zh/SKILL.source.md`
- 上游原路径：`SKILL.md`（仓库 `ai-zixun/humanizer-zh`，branch `main`）
- commit（sources.lock.json 的 last_seen_commit）：`f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3`
- 许可证：MIT，license_status 为 known，snapshot_policy 为 full-text，允许在本清单中引用原文短句。
- 上游自述的定位：中文长文改写 skill，与 op7418/Humanizer-zh 同名但不同项目、不同谱系。frontmatter 声明用于中文博客、随笔、newsletter、非虚构书稿章节、产品分析和长评论的改写、编辑与审阅，触发语包括「去 AI 味」「润色成中文母语表达」「改得像博客或书里写的」「减少翻译腔」。正文结构是 Workflow（六步）＋ Core Rules（八节）＋ Repo Overrides ＋ Output ＋ Final Check，另有一节可选的 Voice Adoption（套用八位中文作者的声音）。它的关注点是「中文母语表达」而不是「事实保真」：翻译腔、文章级结构、段落节奏、标点排版、术语与日期写法占了规则的大半，保真类规则只有 Workflow 第 5 步的三条。
- 总单元数：66（U-azh-001 至 U-azh-066）
- 按 category 计数：
  - process：28
  - pattern：15
  - style-opinion：10
  - protection：8
  - measurement：3
  - genre：2
- 按 language 计数：zh 66，en 0，both 0。（上游全部规则都限定中文正文；涉及英文的几条管的是中文正文里的英文术语写法，判定对象仍是中文文本，记 zh。）

## 2 单元清单

### U-azh-001

```
id: U-azh-001
category: genre
language: zh
rule_summary: 适用于中文博客、专栏、newsletter、非虚构书稿章节、产品分析、长篇评论的改写、编辑与审阅，触发语包括「去 AI 味」「润色成中文母语表达」「改得像博客或书里写的」「减少翻译腔」；处理对象是已有的中文文本。
positive: "帮我把这篇产品分析润色成中文母语表达" —— 属于中文长文改写请求，适用。（自造）
negative: "帮我写一篇关于这个产品的分析" —— 违反点："写一篇"是从零创作，不是改写已有中文文本，不在适用范围内。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "description: Remove signs of AI-generated"
notes: |
  intent: 上游把适用面收在「中文长文写作」而不是所有中文文本，是为了让后面 Core Rules 里那些偏文章级的规则（文章主线、段落功能、结尾回应开头）有成立的前提——这些规则在一条微信回复或一段接口说明上没有意义。触发语列表针对的现象是用户提需求时不会说"请执行 humanizer-zh"，只会说"去 AI 味""减少翻译腔"。
  existing: 疑似对应 ALL-G-001（适用与不适用范围）。本单元的体裁清单比 ALL-G-001 更窄（只到长文），归并时是收窄还是并入需要裁决。
```

### U-azh-002

```
id: U-azh-002
category: process
language: zh
rule_summary: 改写时按固定优先级先处理四类问题：翻译腔、结构腔、排版腔、判断腔；这四类之外的问题排在它们之后。
positive: 一段文字既有「基于……」的翻译腔连接，又有一处标点不统一，先改翻译腔，再处理标点。（自造）
negative: 拿到稿子先逐句统一全角标点，翻译腔句式一句没动就交稿。——违反点：把排版腔放在翻译腔之前处理，颠倒了固定优先级。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Overview"
notes: |
  intent: 上游未说明理由。推断（标明是推断）：这四类的排序是按"改了之后读感改善最大"排的，翻译腔影响每一句，排版腔只影响观感；先做影响面大的可以避免在一段马上要被重写的文字上做标点微调。
  existing: 现有规则里没有（现有的 ALL-PROC-010 讲"四组检查都要过一遍"，不规定顺序；本条规定的是处理顺序）。
```

### U-azh-003

```
id: U-azh-003
category: protection
language: zh
rule_summary: 改写中文时保留原文的事实、立场和信息密度，不得为了读起来自然而降低信息密度。
positive: 原文一段里有三个论据，改写后句式全变，三个论据仍然都在。（自造）
negative: 原文一段列了三个论据，改写后为了段落更顺只留下最有力的一个。——违反点：删掉两个论据，降低了信息密度。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Overview"
notes: |
  intent: 上游把"信息密度"和"事实""立场"并列成保护对象，针对的现象是：中文改写为了追求"读着舒服"，容易把密集的论述稀释成流畅但空的段落。它防的不是改错事实，而是改稀。
  existing: 疑似对应 ALL-PROT-003（不得默认做摘要式压缩）。"信息密度"这个提法在现有规则里没有对应，是本单元的增量。
```

### U-azh-004

```
id: U-azh-004
category: genre
language: zh
rule_summary: 动手前先判文本类型并据此定尺度：博客、专栏、书稿、评论、产品分析允许更强的节奏和作者判断；公告、说明文、技术文档优先保准确和克制。
positive: 判定这是一份接口说明，改写时不加入作者判断，只清理套话。（自造）
negative: 一份系统公告，改写时按博客的做法加上"我一直觉得这类改动早就该做了"。——违反点：给公告类文本注入了只有博客类文本才允许的作者判断。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "1. 先判断文本类型"
notes: |
  intent: 上游把"允许多少作者个性"绑定在体裁上，针对的现象是去 AI 味被理解成"一律加人味"，结果给公告和说明文也加上口语和判断，让正式文本失真。
  existing: 疑似对应 ALL-G-002（体裁在语体之上叠加限制）。
```

### U-azh-005

```
id: U-azh-005
category: process
language: zh
rule_summary: 动手改句子之前先判定文章主线：第一段在立什么题、主体每段各自承担什么功能、最后一段是不是在收同一件事。
positive: 先写下"首段立题：中文写作的翻译腔来源；二段：证据；三段：反例；末段：回到翻译腔来源"，再开始改。（自造）
negative: 拿到长文直接从第一句开始逐句润色，没有判断过每段承担什么功能。——违反点：跳过主线判定，直接进入句子级改写。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "2. 先看文章主线"
notes: |
  intent: 上游针对的现象是逐句润色出来的长文每句都通顺、整篇却散：因为句子级改写看不见"这一段是干什么用的"。先建立主线是为了让后面的删、并、挪有依据。
  existing: 疑似对应 ALL-PROC-009（先通读全文再动手）和 ALL-PROC-011（重建结构前先写下每段真正要完成的工作）。本单元多了"结尾是否收同一件事"这一项。
```

### U-azh-006

```
id: U-azh-006
category: process
language: zh
rule_summary: 主线判定完先扫最显眼的 AI 痕迹，扫描对象固定为：英文句法直译、机械对照句、空泛结论、列表堆砌、连环冒号、破折号、过度工整的段落节奏。
positive: 通读一遍先标出全文四处「不是……而是……」和两处连环冒号，再决定改哪些。（自造）
negative: 通读后只标了几个用词问题，没有检查段落节奏是不是过度工整。——违反点：漏掉扫描清单里的"过度工整的段落节奏"一项。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "3. 先找最显眼的 AI 痕迹"
notes: |
  intent: 上游给出的是一份"先看哪几处"的固定清单，针对的现象是模型自查时容易只盯用词，看不见结构和排版层的痕迹。七项里有四项（对照句、列表、冒号、破折号）是结构和排版，不是词。
  existing: 疑似对应 ALL-PROC-010（每次改写把四组检查过一遍）。本单元是它在中文长文上的具体扫描清单。
```

### U-azh-007

```
id: U-azh-007
category: process
language: zh
rule_summary: 改写力度分两档并各有边界：轻度润色只清理措辞和标点；深度改写才可以重排句子顺序、合并弱句、补足主语或因果关系。
positive: 用户说"轻润一下"，只换掉几个翻译腔连接词和统一标点，段落顺序不动。（自造）
negative: 用户说"轻润一下"，改写时把三段合并成两段并调换了顺序。——违反点：在轻度润色档位做了只有深度改写才允许的合并和重排。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "4. 再决定改写力度"
notes: |
  intent: 上游给"改到什么程度"设了两个离散档位，针对的现象是同一句"帮我改改"，模型可能只换词也可能整篇重写，用户无法预期。"补足主语或因果关系"被放在深度档，说明上游认为补主语已经属于结构改动。
  existing: 疑似对应 ALL-PROC-005（改动幅度按用户措辞定三档）。本单元只有两档，且档位的划分依据是动作而不是用户措辞，归并时需要对齐。
```

### U-azh-008

```
id: U-azh-008
category: protection
language: zh
rule_summary: 不得擅自补充原文没有的事实。
positive: 原文只说"这个功能上线后投诉变少"，改写后仍只说投诉变少，不补具体降幅。（自造）
negative: 原文说"投诉变少"，改写成"投诉量下降了约三成"。——违反点：补写了原文没有的数字事实。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "5. 保留作者原意"
notes: |
  intent: 上游把这条放在"保留作者原意"下，针对的现象是中文改写为了让句子有落点，顺手把模糊表述补成具体表述。
  existing: 疑似对应 ALL-PROT-001（不得新增原文没有的事实）。
```

### U-azh-009

```
id: U-azh-009
category: protection
language: zh
rule_summary: 不得把原文的谨慎判断改写成绝对论断。
positive: 原文说"这条路径也许更省事"，改写后保留"也许"。（自造）
negative: 原文说"这条路径也许更省事"，改写成"这条路径显然更省事"。——违反点：把"也许"换成"显然"，谨慎判断变成绝对论断。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "5. 保留作者原意"
notes: |
  intent: 上游针对的现象是"去 AI 味"常被执行成"写得更有力"，而更有力的中文往往靠去掉限定词得到，代价是作者原本的判断强度被抬高。
  existing: 疑似对应 ALL-PROT-004（不得把不确定说成确定）。
```

### U-azh-010

```
id: U-azh-010
category: protection
language: zh
rule_summary: 不得把原文的普通结论拔高成时代宣言。
positive: 原文说"这套做法在我们团队里比之前顺"，改写后仍限定在"我们团队"。（自造）
negative: 原文说"这套做法在我们团队里比之前顺"，改写成"这套做法正在改变团队协作的方式"。——违反点：把限定在一个团队的结论扩大成行业级判断。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "5. 保留作者原意"
notes: |
  intent: 中文 AI 文本最稳定的特征之一是段末自动升格，把一个具体观察写成时代判断。上游把"拔高"单列成一条保真规则，说明它认为这不是风格问题而是改变了主张的范围。
  existing: 疑似对应 ALL-PROT-014（不得静默替作者改强结论）与 ZH-P-004/ZH-P-006（空话开场与空洞乐观结尾）。本单元管的是句子层的范围扩大，不只是开头结尾的套话。
```

### U-azh-011

```
id: U-azh-011
category: measurement
language: zh
rule_summary: 交付前做一遍朗读检查，判据是读起来像中文母语者写的文章，而不是英文思路换成中文词汇。
positive: 改完通读一遍，发现"在……的情况下，我们可以观察到"读着仍像译文，改成"这时候会看到"。（自造）
negative: 改完直接交付，没有整篇读一遍。——违反点：跳过朗读检查这一步。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "6. 做最后一遍朗读检查"
notes: |
  intent: 上游用"朗读"当最后一道判据，针对的现象是逐条规则都过了、整篇仍像译文——因为翻译腔常常不在任何单条规则的词表里，只在语流里能听出来。
  existing: 疑似对应 ALL-PROC-014（交付前逐项自查）。本单元的判据是"整篇语感"，可判定性弱于 ALL-PROC-014 的逐项清单，归并时要按 criteria.md 第 2 条重新评估。
```

### U-azh-012

```
id: U-azh-012
category: process
language: zh
rule_summary: 默认走中立路径：不套任何作者的腔调，只按通用规则去 AI 味。
positive: 用户只说"去 AI 味"，按通用规则改写，不模仿任何作者。（自造）
negative: 用户只说"去 AI 味"，改写时按某位专栏作者的句式模板重写全文。——违反点：未经用户选择就套用了某位作者的腔调。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 上游给"声音模仿"这个功能加了一个默认关闭的开关，针对的现象是风格化改写很容易越权——用户要的是去 AI 味，拿回来的是别人的文风。
  existing: 疑似对应 ALL-PROT-017（获得改写授权不等于获得更换声口的授权）。
```

### U-azh-013

```
id: U-azh-013
category: process
language: zh
rule_summary: 只有在三个条件同时满足时才可以主动问用户要不要套用某位作者的声音：本次会话还没问过、当前任务是深度改写或长篇润色或重写或风格化创作、用户没有说过「保持中性」「不要改风格」；且每次会话最多问一次。
positive: 用户要求重写一篇长文且没说保持中性，本会话第一次问："要不要顺便套上某位中文作者的声音？"（自造）
negative: 用户请求只是"帮我把这条公告的错别字改一下"，仍然问了一句要不要套作者声音。——违反点：任务是短句修订，不满足"深度改写或长篇润色"这个条件。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 三个条件加"每会话一次"的上限，是为了让这个可选功能不变成骚扰：上游明确写了"机会性地"，说明它知道主动提问本身有成本。
  existing: 现有规则里没有（现有的 ALL-PROC-003 讲的是信息不足时必须问，本条讲的是可选功能什么时候才允许主动问）。
```

### U-azh-014

```
id: U-azh-014
category: process
language: zh
rule_summary: 询问是否套用作者声音时，先读作者索引文件拿到每位作者的一句话简介，再把八位作者的名单贴给用户，不凭记忆罗列。
positive: 先读 references/voices/index.md，再把八位作者连同各自一句话简介贴给用户选。（自造）
negative: 直接凭印象给用户列出几位中文作者的名字和风格描述，没有读索引文件。——违反点：跳过读索引文件，简介来自模型自己的印象。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 上游要求先读文件再贴名单，防的是模型凭训练记忆描述真实作者的文风——那种描述既可能不准，也会让用户按一个不存在的画像做选择。
  existing: 疑似对应 ALL-PROC-028（判断以本 skill 的 references 为准，不凭语感另立标准）。
```

### U-azh-015

```
id: U-azh-015
category: process
language: zh
rule_summary: 用户拒绝或忽略套用作者声音的提议后，本会话剩余轮次不再追问，全部走中立路径。
positive: 用户对"要不要套作者声音"没有回应，后续所有改写都按中立路径做，不再提这件事。（自造）
negative: 用户第一次没理会，隔了两轮又问一次"要不要试试某位作者的写法？"——违反点：用户已忽略过一次，仍在同一会话里追问。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 把"忽略"和"拒绝"同等对待，是因为用户不回答一个可选提议本身就是回答。这条防的是模型把沉默当成"还没决定"反复推销。
  existing: 现有规则里没有。
```

### U-azh-016

```
id: U-azh-016
category: process
language: zh
rule_summary: 用户主动指名某位作者时跳过询问步骤，直接进入该作者档案的加载流程。
positive: 用户说"用某位作者的口气重写"，不再反问要不要套声音，直接加载对应档案。（自造）
negative: 用户已经点名要某位作者的写法，仍先问一句"要不要套上某位中文作者的声音？"——违反点：用户已指名，仍执行了询问步骤。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 针对的现象是把确认流程机械执行成"每次都要问一遍"，用户已经给出的信息被再问一次。
  existing: 现有规则里没有。
```

### U-azh-017

```
id: U-azh-017
category: process
language: zh
rule_summary: 加载作者档案后，把该档案的人格、句法模板、节奏规则和反模式叠加在通用规则之上，不是替换掉通用规则。
positive: 套用某位作者声音时，通用规则里的保真要求照常执行，只在句法和节奏上叠加档案的要求。（自造）
negative: 加载作者档案后，只按档案里的句法模板重写，通用规则里的翻译腔和标点规则不再执行。——违反点：把叠加执行成了替换。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 上游用"叠加"这个词界定作者档案的作用范围，防的是一加载风格档案就整套规则失效。
  existing: 现有规则里没有（现有规则里没有"可选风格档案"这个机制）。
```

### U-azh-018

```
id: U-azh-018
category: process
language: zh
rule_summary: 作者档案与通用规则冲突时，作者档案优先；上游点名的冲突例子是某些作者允许长破折号（覆盖标点规则）、某些作者鼓励短句独立成段、某些作者接受「首先……其次……最后」。
positive: 加载了允许长破折号的作者档案后，正文保留长破折号，不按通用标点规则删掉。（自造）
negative: 加载了明确接受「首先……其次……最后」的作者档案，仍按通用规则把所有序词删光。——违反点：冲突时执行了通用规则，没让作者档案优先。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 上游承认自己的标点和结构规则是通用默认值而不是真理——真实作者确实大量使用被它禁掉的写法。这条冲突裁决说明上游把"像某个真人"排在"符合本 skill 的风格偏好"之上。
  existing: 疑似对应 ALL-PROC-023（仲裁顺序）与 ALL-PROC-025（用户或项目提供的词表优先于默认词表）。本单元的优先项是"作者档案"，与两条的适用对象都不同，归并时要判断是否并入 ALL-PROC-025。
```

### U-azh-019

```
id: U-azh-019
category: process
language: zh
rule_summary: 用户中途说「换成 X」时丢掉当前作者档案并加载新的，说「不要作者声音了」时回到中立路径。
positive: 用户说"换成另一位作者"，卸掉当前档案，只按新档案改写。（自造）
negative: 用户说换一位作者，改写时把两位作者的句法特征都保留着。——违反点：没有丢掉当前档案就加载了新的。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 明确"切换"的语义是替换而不是追加，为下一条（不混多位作者）提供操作层面的保证。
  existing: 现有规则里没有。
```

### U-azh-020

```
id: U-azh-020
category: process
language: zh
rule_summary: 用户没有选定作者时，不得擅自模仿任何作者的口吻。
positive: 用户没选作者，改写用中性的中文，不带任何可辨认的个人腔调。（自造）
negative: 用户没选作者，改写时按某位知名作者的标志性短句节奏重写了全文。——违反点：未经选择就模仿了具体作者的口吻。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 与 U-azh-012 是同一件事的两种表述（默认中立 / 禁止擅自模仿），上游把它单列进反模式清单是为了让违反可判定。这条同时有署名层面的考虑：模仿真人文风而不声明，对被模仿者和读者都不诚实。
  existing: 疑似对应 ALL-PROT-017。与 U-azh-012 同一判定逻辑，归并时可能合并成一条。
```

### U-azh-021

```
id: U-azh-021
category: process
language: zh
rule_summary: 不得把多位作者的声音混在同一篇文章里。
positive: 全文只用一位作者的句法和节奏。（自造）
negative: 前半篇用一位作者的短句节奏，后半篇换成另一位作者的长句和插入语。——违反点：同一篇里混用了两位作者的声音。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 针对的现象是模型加载多份风格档案后按段落轮换使用，结果整篇的语域在几种腔调之间跳——这本身就是 AI 文本的一个特征。
  existing: 疑似对应 EN-P-040（同一篇里出现语域断裂提示拼接）。本单元管的是主动造成的语域跳跃，EN-P-040 管的是识别已有的断裂。
```

### U-azh-022

```
id: U-azh-022
category: protection
language: zh
rule_summary: 不得把作者档案里写给模型看的人格设定原文输出给用户；那是执行指令，不是文章内容。
positive: 加载档案后只输出改写好的中文正文，档案里的英文人格设定一个字都不出现在结果里。（自造）
negative: 改写结果开头带上了档案里那段以「You are a guy from ...」开头的人格设定。——违反点：把写给模型的人格设定当成正文输出了。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 上游明说"那是给你看的，不是文章内容"，针对的现象是模型把加载进来的提示词片段当成待改写的素材，泄漏到交付稿里。
  existing: 疑似对应 EN-P-038（删掉生成过程残留：占位符、工具引用标记、推理链脚手架）。本单元是它在"风格档案"上的具体化。
```

### U-azh-023

```
id: U-azh-023
category: process
language: zh
rule_summary: 作者档案里的反模式只在该作者声音生效的轮次里适用，不得当成通用默认规则沿用到后续的中立改写。
positive: 某位作者的档案禁止使用某种句式，这一轮按档案执行；下一轮用户不要作者声音了，这条禁令不再适用。（自造）
negative: 上一轮用了某位作者的声音，之后中立改写时仍然按那份档案的反模式禁用某种句式。——违反点：把只在该声音生效轮次适用的反模式当成了默认规则。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Voice Adoption（可选）"
notes: |
  intent: 防的是风格档案的规则渗漏——一次风格化改写之后，模型把某个作者的个人偏好当成了普遍的写作规范。上游在 Final Check 末尾又强调了一次"没有把它的口癖泄漏到默认润色里"。
  existing: 现有规则里没有。
```

### U-azh-024

```
id: U-azh-024
category: pattern
language: zh
rule_summary: 把英文句法硬套中文的句子拆开重写，不保留原来的英文句子骨架。
positive: 「这是一个需要被所有参与者所理解的决定」改成「这个决定要让所有参与的人都明白」。（自造）
negative: 「它是一个由多个相互独立的、能够被单独部署的服务所组成的系统」——违反点：定语从句后置结构与「被……所」被动式直接套用英文句法，中文里读不通顺。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 1. 优先改掉翻译腔"
notes: |
  intent: 上游把翻译腔排在 Core Rules 第一条，理由在 Overview 里：中文 AI 文本的底子常常是英文思路。它针对的现象是模型生成中文时沿用英文的句子结构（长定语、被动、从句嵌套），词都是中文词，句子不是中文句子。
  existing: 疑似对应 ZH-P-011（拆掉中文里的英文语法痕迹，decision 为 unverified）。本单元可以给 ZH-P-011 补证据。
```

### U-azh-025

```
id: U-azh-025
category: pattern
language: zh
rule_summary: 少用翻译味重的连接结构：「对于……来说」「基于……」「围绕……展开」「使得……得以……」。
positive: 「对于新用户来说，这个功能很难找」改成「新用户很难找到这个功能」。（自造）
negative: 「基于以上分析，我们可以认为该方案使得团队得以更快地交付。」——违反点：一句里连用「基于……」和「使得……得以……」两个翻译腔连接。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 1. 优先改掉翻译腔"
notes: |
  intent: 这是 U-azh-024 的可判定化：句法层面的"翻译腔"难以逐句判定，上游给了一份具体的连接结构清单当抓手。四个词条共用同一条判定逻辑（出现即视为翻译腔信号），按 extraction.md 合成一个单元。
  existing: 疑似对应 ZH-P-008（前置状语压后主干，含「基于……」）和 ZH-P-011。「对于……来说」「围绕……展开」「使得……得以……」三条在现有词表里没有。
```

### U-azh-026

```
id: U-azh-026
category: pattern
language: zh
rule_summary: 需要表达对比时不默认使用「不是……而是……」，改用转折、递进或重心移动。
positive: 「不是技术问题，而是流程问题」改成「技术上没卡住，卡在流程上」。（自造）
negative: 「这不是一次简单的版本更新，而是一次产品方向的调整。」——违反点：用「不是……而是……」的对照骨架承担对比，是最典型的 AI 中文句式。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 1. 优先改掉翻译腔"
notes: |
  intent: 上游把这个句式归在"翻译腔"下而不是"套话"下，说明它认为这个骨架是从英文 not X but Y 迁移过来的。措辞是"不默认使用"而不是"禁用"，留了余地。
  existing: 疑似对应 ALL-P-005（不为凑气势用对称骨架，含「不仅……而且……更」）与 EN-P-006（英文的二元对比）。中文的「不是……而是……」在现有中文词表里没有单独条目。
```

### U-azh-027

```
id: U-azh-027
category: pattern
language: zh
rule_summary: 少用没有机制解释的大词：「颠覆」「革命」「赋能」「重塑」「深刻改变」「开启新篇章」；要用就得同时给出机制。
positive: 把「这项技术赋能了整个行业」改成「这项技术让小团队也能自己跑完整套流程」。（自造）
negative: 「这次升级重塑了团队的协作方式，开启了新篇章。」——违反点：「重塑」「开启新篇章」两个大词都没有说明具体改变了什么。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 2. 去掉空泛的大词和套话"
notes: |
  intent: 上游给的不是"禁用词"而是"没有机制解释就不许用"，针对的现象是这些词把一件小事说成大事，而且换成任何主语都成立。判据落在"有没有给机制"上，不落在词本身。
  existing: 疑似对应 ZH-P-001（中文高频词与企业黑话词表，已含"赋能""彰显""标志着"）与 ALL-M-001（可移植性测试）。「颠覆」「革命」「重塑」「深刻改变」「开启新篇章」是可补进 ZH-P-001 的词条。
```

### U-azh-028

```
id: U-azh-028
category: pattern
language: zh
rule_summary: 避免自动收束句：「这标志着……」「这意味着……的时代已经到来」。
positive: 「这标志着行业进入新阶段」删掉，直接停在前一句具体事实上。（自造）
negative: 「三家厂商同时宣布支持该协议。这意味着开放互联的时代已经到来。」——违反点：第二句是自动收束句，把一条事实自动升级成时代判断。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 2. 去掉空泛的大词和套话"
notes: |
  intent: "自动"是关键词：上游针对的是这类句子出现的位置固定（在具体事实后面）、内容固定（拔高一级）、与前文没有真实推理关系。它是段落层的口癖，不是用词问题。
  existing: 疑似对应 ZH-P-006（结尾不拉高到空洞乐观）与 EN-P-014（不把普通事实吹成有时代意义）。中文的「这标志着」在 ZH-P-001 词表里已有。
```

### U-azh-029

```
id: U-azh-029
category: pattern
language: zh
rule_summary: 把抽象判断落回具体的动作、约束、成本、分工或结果。
positive: 「协作效率大幅提升」改成「排期表从每周对一次改成每天早上对一次，返工少了」。（自造）
negative: 「新流程显著优化了团队的协作体验。」——违反点：整句是抽象判断，没有落到任何动作、约束、成本、分工或结果上。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 2. 去掉空泛的大词和套话"
notes: |
  intent: 上游给出了五个落点（动作、约束、成本、分工、结果），把"写具体"变成了可检查的事——判据是能不能指出这句落在这五类里的哪一类。
  existing: 疑似对应 ALL-P-007（能给名字、数字、机制、例子的地方不用抽象词）。本单元的五类落点是 ALL-P-007 没有的可判定抓手。
```

### U-azh-030

```
id: U-azh-030
category: pattern
language: zh
rule_summary: 不强行把每段都写成三分句、排比句或工整对照句。
positive: 一段里两个要点就写两句，不硬凑第三句。（自造）
negative: 「它降低了成本，缩短了周期，提升了体验。」全文每段都以这样一组三个动宾短语收尾。——违反点：段落被统一压成三分句排比结构。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 3. 打散机械结构"
notes: |
  intent: 针对的现象是中文 AI 文本的段落形状高度一致，读者读到第三段就能预测第四段的形状。上游把它归到"机械结构"而不是修辞问题。
  existing: 疑似对应 ALL-P-005（不为凑气势用对称骨架）。
```

### U-azh-031

```
id: U-azh-031
category: pattern
language: zh
rule_summary: 不连续使用「首先」「其次」「最后」「与此同时」「值得注意的是」「从某种意义上说」这类连接与元叙述词。
positive: 删掉序词，靠内容本身的顺序推进：「先做的是……做完才发现……」。（自造）
negative: 「首先，成本下降了。其次，周期缩短了。与此同时，值得注意的是体验也有改善。」——违反点：连续使用「首先」「其次」「与此同时」「值得注意的是」四个连接与元叙述词。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 3. 打散机械结构"
notes: |
  intent: 上游的措辞是"不连续使用"，说明它管的是密度而不是单个词——单独一个"其次"不构成问题，连成串就是模板骨架露出来了。
  existing: 疑似对应 ZH-P-003（不用"首先……其次……"搭骨架）与 ZH-P-001（元叙述词表）。本单元的"连续"密度判据在 ZH-P-003 里没有明写。
```

### U-azh-032

```
id: U-azh-032
category: pattern
language: zh
rule_summary: 发现列表可以改成自然叙述时，优先改写成段落。
positive: 三条各只有半句话的要点合成一段连贯叙述。（自造）
negative: 一段本可以连着说完的说明被拆成五条项目符号，每条一句话。——违反点：可以自然叙述的内容被拆成了列表。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 3. 打散机械结构"
notes: |
  intent: 针对的现象是模型把任何多项内容都排成列表，列表在中文长文里造成"提纲感"——看起来清楚，读起来没有推进。上游只说"优先"，不是禁止列表。
  existing: 疑似对应 ALL-P-002（不把本可以两三句说清的内容拆成加粗项目符号列表）。
```

### U-azh-033

```
id: U-azh-033
category: pattern
language: zh
rule_summary: 允许长短句混用，不把每句都写成同样长度。
positive: 「他没解释。第二天所有人都收到了一封两千字的说明邮件，里面提到了三次'流程'。」（自造）
negative: 「这个方案降低了运营成本。这个改动缩短了交付周期。这个决定改善了用户体验。」——违反点：连续三句字数与结构几乎相同，句长没有变化。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 4. 保持中文节奏"
notes: |
  intent: 句长均匀是 AI 文本最稳定的统计特征之一。上游没有给数值阈值，只给方向，判定要靠读。
  existing: 疑似对应 ALL-P-001（句子长度和段落结构要有变化，中文口径见 ZH-M-001）。
```

### U-azh-034

```
id: U-azh-034
category: pattern
language: zh
rule_summary: 句子要有明确的主语和动作，少写无主句串联。
positive: 「运维把配置回滚了，第二天又提了一版新的。」（自造）
negative: 「经过多轮讨论，形成了初步方案，并在会后进行了同步。」——违反点：三个分句都没有主语，读不出是谁讨论、谁形成、谁同步。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 4. 保持中文节奏"
notes: |
  intent: 无主句串联在中文公文里是常态，模型把它当成了"正式"的写法。上游针对的是它带来的后果：读完不知道谁做了什么。
  existing: 疑似对应 ALL-P-004（指名动作的执行者，不用隐藏施事者的无主句和被动式）。
```

### U-azh-035

```
id: U-azh-035
category: pattern
language: zh
rule_summary: 段落结尾不总是落在大而空的价值判断上。
positive: 段落停在最后一个具体事实：「这版上线后，值班群里没再出现过这条报警。」（自造）
negative: 每一段都以「这对整个团队来说都是有意义的一步」这类句子收尾。——违反点：段末固定落在空泛价值判断上。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 4. 保持中文节奏"
notes: |
  intent: 上游关注的是"总是"——段末拔高偶尔出现是修辞，每段都有就是模板。它与 U-azh-028 的差别在于：028 管句子（自动收束句），本条管位置分布（段末固定）。
  existing: 疑似对应 ZH-P-006（结尾不拉高到空洞乐观）。ZH-P-006 管全文结尾，本单元管每个段落的结尾。
```

### U-azh-036

```
id: U-azh-036
category: pattern
language: zh
rule_summary: 开头要尽快立题，不得第一段说 A、后文一路滑到 B。
positive: 第一段就点出全文要谈的是排期方式，后文都在谈排期。（自造）
negative: 第一段从行业趋势谈起，第三段之后全文实际在讲一个内部工具的用法，开头和主体不是一件事。——违反点：首段立的题与主体讨论的题不一致。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 上游针对的是 AI 长文的典型开头：先写一段可以放在任何文章前面的行业背景，真正的题目到第二三段才出现。判据是首段立的题与主体是不是同一件事。
  existing: 疑似对应 ZH-P-004（不用空话开场，从最具体的那句话开始）。ZH-P-004 管开场的措辞，本单元管开场与全文的关系。
```

### U-azh-037

```
id: U-azh-037
category: process
language: zh
rule_summary: 主体段落每段都要承担一个明确功能，常见功能是交代背景、提出判断、展开论据、举例、转折、收束。
positive: 改写前先给每段标一个功能，发现两段都是"展开论据"且论据相同，合并成一段。（自造）
negative: 中间四段都在换着说法重复同一个判断，说不出哪段承担什么功能。——违反点：段落没有各自的功能，是同一内容的重复表述。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 给出六个功能名是为了让"这段有没有用"变成可回答的问题。上游把它放在文章级结构下，与 Workflow 第 2 步的主线判定配套：先判功能，才知道哪段可以删。
  existing: 疑似对应 ALL-PROC-011（重建信息结构前先写下每段真正要完成的工作）。六个功能名是现有规则没有的具体清单。
```

### U-azh-038

```
id: U-azh-038
category: process
language: zh
rule_summary: 某一段既不推进主线也不提供必要信息时，优先删、并、挪，不硬留。
positive: 一段只是把上一段的判断换个说法重说一遍，删掉。（自造）
negative: 明知某段既不推进主线也没有新信息，仍保留原位，只把里面的句子改顺。——违反点：对不承担功能的段落只做了句子级润色，没有删、并或挪。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 与 U-azh-037 是一对：037 判功能，本条给处置动作。上游针对的现象是模型的改写只会"改句子"，不会"删段落"，于是没有功能的段落被润色得更漂亮地留在原地。
  existing: 疑似对应 ALL-P-008（段落可任意互换顺序说明是并列堆砌，应当合并、删除或补出真实依赖关系）。
```

### U-azh-039

```
id: U-azh-039
category: pattern
language: zh
rule_summary: 结尾要回应前文真正提出的问题，不得临时拔高到更大的时代命题。
positive: 全文问"这套排期方式值不值得推广"，结尾回答"在我们这种规模的团队里值得，再大就不一定"。（自造）
negative: 全文讨论一个内部工具的取舍，结尾写成「这也许正是这个时代所有团队都要面对的命题」。——违反点：结尾没有回应文中提出的取舍问题，而是升级成了时代命题。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 上游给"结尾拔高"加了一个可判定的判据：不是看结尾有多空，而是看它有没有回到开头提出的那个问题。这比"不要空洞乐观"好判。
  existing: 疑似对应 ZH-P-006 与 EN-P-023（结尾停在最后一个具体事实上）。"回应开头提出的问题"这个判据现有规则里没有。
```

### U-azh-040

```
id: U-azh-040
category: process
language: zh
rule_summary: 深度改写时可以重排段落顺序，但不得为了工整硬凑成三段论。
positive: 把结论段前移，因为读者需要先知道结论；不额外补一段凑成"提出—分析—总结"。（自造）
negative: 原文是四段松散的观察，改写时硬改成"现象—原因—对策"三段，多写了一段对策。——违反点：为凑三段论结构补出了原文没有的对策段。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 上游一边给深度改写放开了重排权限，一边立刻给这个权限设了边界，防的是"结构自由"被执行成"套一个标准结构"。
  existing: 疑似对应 ALL-PROC-030（不为整齐而统一结构）与 ALL-PROT-007（不得从问题自行推出解决方案）。
```

### U-azh-041

```
id: U-azh-041
category: pattern
language: zh
rule_summary: 总结段落之间的关系时，少写成一串「先……再……最后……」，要看它们是不是顺着同一个问题自然往下走。
positive: 「前面在说排期为什么难，后面在说我们试过的两种办法，末尾说哪种留下来了。」（自造）
negative: 「文章先介绍了背景，再分析了原因，最后给出了建议。」——违反点：用「先……再……最后……」的流程式描述代替段落之间真实的问题推进关系。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 5. 管住文章级结构"
notes: |
  intent: 上游要求的是换一种看结构的方式：流程式的"先再最后"能套在任何文章上，看不出这篇是不是在推进一个问题。它防的是用叙述顺序冒充论证结构。
  existing: 疑似对应 ZH-P-003（不用序词搭骨架）。本单元管的是描述结构的方式，ZH-P-003 管正文里的序词，判定对象不同。
```

### U-azh-042

```
id: U-azh-042
category: style-opinion
language: zh
rule_summary: 正文引号默认用全角双引号、嵌套用全角单引号；项目在 CLAUDE.md/AGENTS.md 里声明或用户本轮明确要求时全篇改用「」（嵌套『』）；两种样式不得混用。
positive: 全篇统一用一种引号样式，嵌套时用配套的那一种。（自造）
negative: 同一篇里前半用“……”、后半用「……」。——违反点：两种引号样式在同一篇里混用。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 上游关心的不是哪种引号更好，而是全篇一致——混用是模型拼接痕迹的直接证据。默认值和覆盖顺序是为了让"一致"有一个确定的落点。
  existing: 疑似对应 EN-P-037（引号排版跟随作者原稿）。EN-P-037 管英文直/弯引号，本单元管中文全角双引号与「」，两条的默认值逻辑不同：EN-P-037 跟随原稿，本单元有默认值加覆盖顺序。归并时可能冲突。
```

### U-azh-043

```
id: U-azh-043
category: style-opinion
language: zh
rule_summary: 中文正文不使用长破折号「——」，改成逗号、句号或拆句。
positive: 「这不是技术问题——是排期问题」改成「这不是技术问题。是排期问题。」（自造）
negative: 「我们试过三种办法——都没成——最后还是回到了最笨的那种。」——违反点：一句里用两处长破折号承担停顿。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 破折号是模型中文里最容易过量的标点，用来制造"有力"的停顿。上游的处理是一刀切禁用，同时在 Voice Adoption 一节承认某些真实作者大量使用它、档案可以覆盖这条。
  existing: 疑似对应 ZH-P-007（中文正文里破折号只在真正需要时用一次）。本单元比 ZH-P-007 更严：完全禁用。归并时是冲突项，两条的裁决要互相点名。
```

### U-azh-044

```
id: U-azh-044
category: style-opinion
language: zh
rule_summary: 不密集使用冒号，尤其避免连续多句都靠冒号展开解释。
positive: 「问题只有一个：排期对不上。」全篇只用这一处冒号。（自造）
negative: 「原因有两个：一是排期；二是人手。结论也很清楚：先补人。做法同样明确：从下周开始。」——违反点：连续三句都用冒号展开解释。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 连环冒号在 Workflow 第 3 步的扫描清单里被单列，说明上游把它当成一个显眼的 AI 痕迹：冒号让每句话都变成"标签＋展开"，读起来像幻灯片。
  existing: 疑似对应 EN-P-027（分号和冒号连续三句以上密集出现作为弱信号，decision 为 adopted-with-modification）。EN-P-027 只作弱信号提示复查，本单元要求改写，强度不同。
```

### U-azh-045

```
id: U-azh-045
category: style-opinion
language: zh
rule_summary: 中文正文里的英文多词术语用半角空格分词（写作 `AI Design Agent`）。
positive: 「这套 AI Design Agent 的用法……」（自造）
negative: 「这套 AIDesignAgent 的用法……」——违反点：多词英文术语没有用半角空格分词。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 上游未说明。推断（标明是推断）：这一组排版规则针对的是中文技术博客里英文术语的写法在同一篇内不统一，而不统一本身就是拼接痕迹。
  existing: 现有规则里没有。
```

### U-azh-046

```
id: U-azh-046
category: style-opinion
language: zh
rule_summary: 英文术语与中文括号连写时，不在「（」前加空格，写作 `LLM（大语言模型）`。
positive: 「LLM（大语言模型）在这里的作用是……」（自造）
negative: 「LLM （大语言模型）在这里的作用是……」——违反点：英文术语与中文全角括号之间多了一个空格。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 上游未说明。推断（标明是推断）：全角括号自带留白，再加半角空格会出现双倍间距；这条与 U-azh-045 是一套排版约定的两面（该加空格的地方加、不该加的地方不加）。
  existing: 现有规则里没有。
```

### U-azh-047

```
id: U-azh-047
category: style-opinion
language: zh
rule_summary: 并列英文术语用斜杠连接时，斜杠两侧不加空格，写作 `coworkers/agents`。
positive: 「同事和智能体（coworkers/agents）在这里是同一类角色。」（自造）
negative: 「同事和智能体（coworkers / agents）在这里是同一类角色。」——违反点：斜杠两侧加了空格。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 上游未说明。推断（标明是推断）：与 U-azh-045、U-azh-046 同属一套排版约定，目的是让同一篇里英文与中文混排的间距处理一致。
  existing: 现有规则里没有。
```

### U-azh-048

```
id: U-azh-048
category: protection
language: zh
rule_summary: 英文品牌名按官方大小写书写，例如 `YouTube`、`OpenAI`、`GitHub`。
positive: 「这段视频发在 YouTube 上。」（自造）
negative: 「这段视频发在 Youtube 上。」——违反点：品牌名 YouTube 的官方大小写被改成了 Youtube。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 6. 处理标点和排版"
notes: |
  intent: 上游未说明。推断（标明是推断）：品牌名的大小写是事实性写法而不是排版偏好，写错在中文技术文章里是明显的失真信号；归 protection 而不是 style-opinion 是因为它有唯一正确答案。
  existing: 疑似对应 ALL-PROT-008（专有名词默认逐字不动）与 ALL-PROT-010（复扫时核对专名写法）。
```

### U-azh-049

```
id: U-azh-049
category: style-opinion
language: zh
rule_summary: `token` 和 `API` 在中文正文里保持英文，不译成中文。
positive: 「这段提示词大概占两千个 token。」（自造）
negative: 「这段提示词大概占两千个词元。」——违反点：把应保持英文的 token 译成了中文。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 7. 统一常见术语和日期"
notes: |
  intent: 上游未说明。推断（标明是推断）：这两个词在中文技术写作里的通行写法就是英文，译成中文反而增加阅读成本；这条属于"术语稳定"而不是"要不要用外来词"的立场。
  existing: 疑似对应 ALL-PROT-009（精确技术术语不得为避免重复而换称）。本单元规定的是具体词条的写法，不是不换称。
```

### U-azh-050

```
id: U-azh-050
category: style-opinion
language: zh
rule_summary: `PR` 在长篇中文叙述里优先写作「代码审查」，除非项目已有别的明确约定。
positive: 「这段逻辑在代码审查里被提出来过。」（自造）
negative: 「这段逻辑在 PR 里被提出来过。」（项目没有相反约定的长文中）——违反点：长篇中文叙述里保留了 PR，未按规则改写。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 7. 统一常见术语和日期"
notes: |
  intent: 上游未说明。推断（标明是推断）：与 U-azh-049 相反的处理说明上游的判据是读者而不是词源——面向一般读者的长文里 PR 是行话，token 已经是通用词。这条的替换结果（PR→代码审查）在语义上并不精确（PR 是拉取请求，代码审查是发生在其中的活动），归并时要留意。
  existing: 现有规则里没有。本单元与 ALL-PROT-009（术语不换称）方向相反，归并时是潜在冲突项。
```

### U-azh-051

```
id: U-azh-051
category: style-opinion
language: zh
rule_summary: 数字日期写作 `2026 年 2 月 26 日`、`2 月 5 日` 这一种格式。
positive: 「改动是 2 月 5 日上线的。」（自造）
negative: 「改动是 2026/02/05 上线的。」——违反点：日期没有按规定的中文数字日期格式书写。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 7. 统一常见术语和日期"
notes: |
  intent: 上游未说明。推断（标明是推断）：日期格式在中文长文里最容易出现同篇不一致（有的写 2 月 5 日、有的写 02/05），统一格式是消除拼接痕迹的低成本手段。
  existing: 现有规则里没有。注意与 ALL-PROT-002（数字日期不得改写成概括说法）不冲突：本单元只改写法，不改值。
```

### U-azh-052

```
id: U-azh-052
category: style-opinion
language: zh
rule_summary: 中文月份叙事写作汉字「一月」「二月」，不与数字日期格式混用。
positive: 「一月还在讨论，三月就上线了。」（自造）
negative: 「1 月还在讨论，三月就上线了。」——违反点：同一句里叙事月份一处用数字、一处用汉字。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 7. 统一常见术语和日期"
notes: |
  intent: 上游未说明。推断（标明是推断）：与 U-azh-051 配套，把"具体日期"和"叙事月份"分成两种写法，避免正文里数字密度过高。
  existing: 现有规则里没有。
```

### U-azh-053

```
id: U-azh-053
category: protection
language: zh
rule_summary: 不轻易下「完全取代」「彻底结束」「只剩一种可能」这类极端结论。
positive: 「这类工具已经能接手一部分排版工作。」（自造）
negative: 「这类工具将完全取代排版岗位。」——违反点：用「完全取代」下了原文证据支撑不了的极端结论。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 8. 控制判断强度"
notes: |
  intent: 与 Workflow 第 5 步的"不把谨慎判断写成绝对论断"呼应，但方向不同：那条管的是不改强原文，这条管的是改写稿自己不要写出极端结论。上游把判断强度当成一个独立维度来控制。
  existing: 疑似对应 ALL-PROT-014（结论超出证据时的处理）与 U-azh-009。本单元管的是输出侧的措辞上限。
```

### U-azh-054

```
id: U-azh-054
category: protection
language: zh
rule_summary: 不做无依据的阴谋论推断、资本市场臆测或人物动机脑补。
positive: 原文只写"该公司当天宣布调整"，改写后仍只写这件事本身。（自造）
negative: 原文只写"该公司当天宣布调整"，改写成「显然是为了在融资前把数据做好看」。——违反点：补出了原文没有的动机推断。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 8. 控制判断强度"
notes: |
  intent: 针对的现象是"写得像人"被理解成"写得更有观点"，而最容易生成的观点就是动机推测。上游把三类（阴谋论、市场臆测、动机脑补）并列，共用"没有依据"这一条判据。
  existing: 疑似对应 ALL-PROT-001（不得新增观点与论据）。三类具体对象在现有规则里没有点名。
```

### U-azh-055

```
id: U-azh-055
category: process
language: zh
rule_summary: 需要强调某件事重要时，先给机制，再给判断，不得只给判断。
positive: 「排期对不上时，联调只能等到最后一周，测试时间被压掉一半——所以排期是这里最要紧的一环。」（自造）
negative: 「排期是这里最要紧的一环。」（全段没有说明为什么）——违反点：只给了重要性判断，没有先给机制。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "### 8. 控制判断强度"
notes: |
  intent: 这条把"重要性"从形容词层拉回论证层：判断本身不禁止，禁止的是判断没有机制托底。与 U-azh-027（大词要有机制解释）是同一套思路在两个层面上的落法。
  existing: 疑似对应 ALL-P-007（抽象换具体）与 ALL-M-001（可移植性测试）。"先机制后判断"的顺序要求现有规则里没有。
```

### U-azh-056

```
id: U-azh-056
category: process
language: zh
rule_summary: 当前项目里存在 CLAUDE.md、AGENTS.md、样例文章或术语表时，先遵守项目内规则，再套用本 skill 的通用规则。
positive: 项目术语表规定某个词固定写法，改写时按项目写法，不按通用词表改。（自造）
negative: 项目 AGENTS.md 里写明保留某个说法，改写时仍按通用词表把它换掉。——违反点：项目内规则被通用规则覆盖，顺序颠倒。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Repo Overrides"
notes: |
  intent: 上游把 skill 的规则定位成"项目没有规定时的默认值"。针对的现象是通用去 AI 味词表与项目自己的文风约定冲突时，模型按词表把项目术语改掉。
  existing: 疑似对应 ALL-PROC-025（用户或项目提供的词表优先于本 skill 的默认词表）。
```

### U-azh-057

```
id: U-azh-057
category: process
language: zh
rule_summary: 项目已有明确文风样本时，模仿它的句长、判断方式、段落推进和术语约定，不额外套用另一套腔调。
positive: 项目已有的文章都是短句直述，改写按这个来，不换成更书面的写法。（自造）
negative: 项目已有文章都是短句直述，改写时按本 skill 偏好的节奏改成长短交错的书面语。——违反点：有项目文风样本时仍套用了另一套腔调。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Repo Overrides"
notes: |
  intent: 上游给出了四个可对齐的维度（句长、判断方式、段落推进、术语约定），把"模仿项目文风"变成可执行的事。它与 Voice Adoption 一节的作者档案是同一机制的两个来源：一个来自项目，一个来自用户选择。
  existing: 疑似对应 ALL-PROT-017（作者的声口属于作者）。"项目文风样本"作为声口来源在现有规则里没有。
```

### U-azh-058

```
id: U-azh-058
category: process
language: zh
rule_summary: 引号样式按固定顺序确定：用户在本轮请求里的明确要求 → 项目 CLAUDE.md/AGENTS.md 的声明 → 默认全角双引号。
positive: 用户本轮说要用「」，即使项目声明了别的样式，也按用户的来。（自造）
negative: 用户本轮明确要求用「」，仍按项目声明的样式输出。——违反点：把项目声明排在了用户本轮要求之前。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Repo Overrides"
notes: |
  intent: 上游给一个具体的排版分歧写了完整的优先级链，说明它认为引号样式是这类项目里最常见的反复修改点，值得单独定规矩。
  existing: 疑似对应 ALL-PROC-023（仲裁顺序）与 ALL-PROC-025。本单元是这两条在引号样式上的具体化。
```

### U-azh-059

```
id: U-azh-059
category: process
language: zh
rule_summary: 原文整篇已显著使用「」而项目未作声明时，沿用原文的引号样式，不硬改成默认样式。
positive: 原文全篇用「」、项目没有声明，改写后仍用「」。（自造）
negative: 原文全篇用「」、项目没有声明，改写时全部换成默认的全角双引号。——违反点：在项目未声明的情况下把原文已有的一致样式改掉了。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Repo Overrides"
notes: |
  intent: 这是对默认值的一条例外：原文自己已经一致时，一致本身就是作者的选择，默认值不该覆盖它。上游在意的是"全篇统一"，不是"用哪一种"。
  existing: 疑似对应 EN-P-037（引号排版跟随作者原稿）。两条的思路一致，只是语种不同，归并时可能合成一条。
```

### U-azh-060

```
id: U-azh-060
category: process
language: zh
rule_summary: 默认输出只给改写后的版本，不附解释，也不给多个版本。
positive: 用户只说"帮我改改"，直接给一版改写稿。（自造）
negative: 用户只说"帮我改改"，输出里附了逐条说明和三个候选版本。——违反点：用户没有要求，仍输出了解释和多版本。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Output"
notes: |
  intent: 上游把交付默认值定成"只给结果"，针对的现象是改写工具输出一堆分析，用户还要自己从中挑出正文。
  existing: 与 ALL-PROC-008（改写稿后面附一节改动说明，终稿短也不省略）方向相反，是明确的冲突项。归并时两条都要记，rationale 互相点名。
```

### U-azh-061

```
id: U-azh-061
category: process
language: zh
rule_summary: 用户要求解释时，简短指出 3 到 6 个最明显的问题，不逐句点评。
positive: 用户问"哪里有问题"，列出四条：翻译腔连接、段末拔高、连环冒号、结尾没回应开头。（自造）
negative: 用户要求解释，输出了十七条逐句点评。——违反点：条数超出 3 到 6 条的上限，变成了逐句点评。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Output"
notes: |
  intent: 上下限（3 到 6）是为了逼出取舍：把最明显的问题挑出来，比列全更有用。上游默认用户读解释是为了理解改写方向，不是为了核对每一处改动。
  existing: 疑似对应 ALL-PROC-007（审稿模式逐条点出命中的规则 id）。本单元有条数上限，现有规则没有。
```

### U-azh-062

```
id: U-azh-062
category: process
language: zh
rule_summary: 只有用户要求保留更多原句时，才额外给一个「轻改版」和一个「重写版」。
positive: 用户说"能不能少改一点"，这时给出轻改版和重写版两稿供选。（自造）
negative: 用户没有提出保留原句的要求，主动给了轻改版和重写版两稿。——违反点：在触发条件不成立时输出了双版本。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Output"
notes: |
  intent: 双版本是给"改多了"这个具体反馈准备的补救手段，不是默认交付形态。上游用触发条件把它挡在默认路径之外。
  existing: 现有规则里没有（现有的 ALL-PROC-005 用三档授权解决"改多少"，不用多版本）。
```

### U-azh-063

```
id: U-azh-063
category: measurement
language: zh
rule_summary: 交付前确认第一段提出的问题在最后一段确实有回应。
positive: 交付前回头看首末两段，确认末段回答的正是首段提出的那个问题。（自造）
negative: 交付前只逐段检查了句子，没有把首段和末段放在一起对照。——违反点：漏掉首尾呼应这一项交付检查。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Final Check"
notes: |
  intent: 上游在 Workflow 第 2 步和 Core Rules 第 5 节都提过首尾呼应，Final Check 再列一次，说明它被当成交付门槛而不只是改写方向。
  existing: 疑似对应 ALL-PROC-014（交付前逐项自查）。首尾呼应作为独立检查项在现有规则里没有。与 U-azh-039 是同一件事的两处表述（一处是改写要求，一处是交付检查），主锚点在 Core Rules 第 5 节。
```

### U-azh-064

```
id: U-azh-064
category: measurement
language: zh
rule_summary: 交付前确认全文节奏不总是「先定义、再拆项、最后拔高」，且读者不能连续三节都预测出下一节的写法。
positive: 检查发现三节都是"定义—拆项—拔高"，把其中一节改成先给场景再给判断。（自造）
negative: 全文五节，每节都以一句定义开头、中间三个要点、末尾一句拔高。——违反点：节的写法完全可预测，连续超过三节使用同一骨架。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Final Check"
notes: |
  intent: "可预测性"是上游给结构腔的判据，比"不要模板化"可判定得多：拿三节连起来看，能不能预测第四节的形状。三节这个数值是上游给的门槛。
  existing: 疑似对应 ALL-P-001（段落结构要有变化）与 ALL-P-008（段落可互换说明是堆砌）。"连续三节可预测"这个可判定门槛在现有规则里没有。
```

### U-azh-065

```
id: U-azh-065
category: process
language: zh
rule_summary: 交付前确认标点、术语、日期和品牌大小写在全篇统一。
positive: 交付前搜一遍全文，确认日期格式只有一种写法。（自造）
negative: 交付稿里一处写「2 月 5 日」、另一处写「2/5」，未做统一检查。——违反点：日期写法在同一篇内不统一，交付前未核对。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Final Check"
notes: |
  intent: 这是 Core Rules 第 6、7 节那批排版与术语规则的验收环节：规则本身管单处写法，这条管全篇一致。上游把"不一致"当成拼接痕迹的证据。
  existing: 疑似对应 ALL-PROC-014（交付前逐项自查）。
```

### U-azh-066

```
id: U-azh-066
category: process
language: zh
rule_summary: 本次启用过某位作者的声音时，交付前对照该档案的反模式和测试清单再扫一遍，确认风格没跑偏，也没有把该作者的口癖泄漏到默认润色部分。
positive: 用某作者声音改完后，按档案的反模式清单再扫一遍，删掉两处过头的口癖。（自造）
negative: 启用了作者声音，改完直接交付，没有按该档案的反模式清单复扫。——违反点：跳过启用作者声音后的专项复扫。（自造）
source:
  type: upstream
  source_id: upstream-ai-zixun-humanizer-zh
  path: SKILL.md
  commit: f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3
  anchor: "## Final Check"
notes: |
  intent: 与 U-azh-023 配套：023 规定作者档案的规则不许渗漏到之后的轮次，本条规定同一轮里也要检查有没有把口癖用过头。上游知道风格模仿最容易失控的方向是"用力过猛"。
  existing: 现有规则里没有。
```

## 3 覆盖表

| 来源小节 | 归属单元 / 说明 |
|---|---|
| frontmatter：`name` | 非规则内容（skill 标识符） |
| frontmatter：`description` | U-azh-001 |
| 标题「# 中文去 AI 味」 | 非规则内容（标题） |
| ## Overview | U-azh-002、U-azh-003 |
| ## Workflow：1. 先判断文本类型 | U-azh-004 |
| ## Workflow：2. 先看文章主线 | U-azh-005 |
| ## Workflow：3. 先找最显眼的 AI 痕迹 | U-azh-006 |
| ## Workflow：4. 再决定改写力度 | U-azh-007 |
| ## Workflow：5. 保留作者原意 | U-azh-008、U-azh-009、U-azh-010 |
| ## Workflow：6. 做最后一遍朗读检查 | U-azh-011 |
| ## Voice Adoption：默认中立段 | U-azh-012 |
| ## Voice Adoption：三个询问条件 | U-azh-013 |
| ## Voice Adoption：询问时先读 index 并贴名单 | U-azh-014 |
| ## Voice Adoption：用户拒绝或忽略 | U-azh-015 |
| ## Voice Adoption：用户主动指名 | U-azh-016 |
| ## Voice Adoption：加载流程第 1、2 步 | U-azh-017 |
| ## Voice Adoption：加载流程第 3 步（冲突时档案优先） | U-azh-018 |
| ## Voice Adoption：加载流程第 4 步（换成 X / 不要作者声音） | U-azh-019 |
| ## Voice Adoption：反模式第 1 条 | U-azh-020 |
| ## Voice Adoption：反模式第 2 条 | U-azh-021 |
| ## Voice Adoption：反模式第 3 条 | U-azh-022 |
| ## Voice Adoption：反模式第 4 条 | U-azh-023 |
| ### 1. 优先改掉翻译腔 | U-azh-024、U-azh-025、U-azh-026 |
| ### 2. 去掉空泛的大词和套话 | U-azh-027、U-azh-028、U-azh-029 |
| ### 3. 打散机械结构 | U-azh-030、U-azh-031、U-azh-032 |
| ### 4. 保持中文节奏 | U-azh-033、U-azh-034、U-azh-035 |
| ### 5. 管住文章级结构 | U-azh-036、U-azh-037、U-azh-038、U-azh-039、U-azh-040、U-azh-041 |
| ### 6. 处理标点和排版 | U-azh-042、U-azh-043、U-azh-044、U-azh-045、U-azh-046、U-azh-047、U-azh-048 |
| ### 7. 统一常见术语和日期 | U-azh-049、U-azh-050、U-azh-051、U-azh-052 |
| ### 8. 控制判断强度 | U-azh-053、U-azh-054、U-azh-055 |
| ## Repo Overrides | U-azh-056、U-azh-057、U-azh-058、U-azh-059 |
| ## Deep Review（读 patterns.md / corpus.md / corpus-quickpick.md 的触发条件） | 非规则内容（reference 文件的导航说明，性质与 qu-ai-wei 清单里的「按需参考」相同） |
| ## Deep Review 末段（用户选定作者时额外加载对应档案、冲突时档案优先） | U-azh-017、U-azh-018 的重复表述，主锚点在 Voice Adoption |
| ## Output：第 1 项 | U-azh-060 |
| ## Output：第 2 项 | U-azh-061 |
| ## Output：第 3 项 | U-azh-062 |
| ## Final Check：读起来像中文作者在写 | U-azh-011 的重复表述，主锚点在 Workflow 第 6 步 |
| ## Final Check：第一段的问题最后一段有回应 | U-azh-063（与 U-azh-039 同一要求的交付侧表述） |
| ## Final Check：主体段落都在服务主线 | U-azh-037、U-azh-038 的重复表述 |
| ## Final Check：句子之间有自然推进，不靠模板连接词硬粘 | U-azh-031 的重复表述 |
| ## Final Check：结论不过火，判断和事实强度匹配 | U-azh-053 的重复表述 |
| ## Final Check：全文节奏不总是「先定义、再拆项、最后拔高」 | U-azh-064 |
| ## Final Check：标点、术语、日期和品牌大小写统一 | U-azh-065 |
| ## Final Check：引号样式全篇统一 | U-azh-042 的重复表述 |
| ## Final Check：启用作者声音时对照 anti-patterns 复扫 | U-azh-066 |

## 4 拆分时拿不准的地方

1. U-azh-011（朗读检查）的可判定性弱：「读起来像中文原生写作」没有可圈出的词或结构，按 criteria.md 第 2 条可能记 rejected。本清单仍立为单元，是因为它在上游是一个独立的交付步骤（Workflow 第 6 步），删掉它覆盖表会缺一格；归并阶段可以改判。
2. U-azh-045 至 U-azh-052 这八条排版与术语写法规则，是否要按"共用同一条判定逻辑"合并成一到两个单元，两种拆法都成立。本清单按"每条有各自的取值和例外"拆开（例如 U-azh-050 带例外条款、U-azh-049 没有），归并阶段如果决定整体记 reference-only，可以合并处理。
3. U-azh-042/043/044 三条标点规则的强度与现有规则不一致：U-azh-043 完全禁用长破折号，现有 ZH-P-007 允许一次；U-azh-044 要求改写密集冒号，现有 EN-P-027 只作弱信号。这三条属于 criteria.md 第 4 条说的"单一来源的强风格意见"，且上游自己在 Voice Adoption 里承认真实作者会违反它们，归并阶段大概率不进默认规则。
4. U-azh-060（默认不附解释）与现有 ALL-PROC-008（改动说明不得省略）直接冲突。两条都可以自圆其说：上游面向的是"拿了就发"的中文长文场景，现有规则面向的是需要留痕的合并流程。按 criteria.md 第 8 条，两条都要进 decisions.yaml，不得静默丢弃。
5. Voice Adoption 一整节（U-azh-012 至 U-azh-023，共 12 个单元）是否属于本仓库 skill 的范围，需要归并阶段裁决：它引入的是"模仿指定真人作者"这一功能，与 ALL-PROT-017（不得擅自更换声口）方向相容但目标不同。如果整节判为 out of scope，这 12 个单元会一起落到 rejected 或 reference-only；本清单按"逐条可判定"照拆，不预判。
6. U-azh-050（PR→代码审查）的替换在术语上不精确：PR 指拉取请求，代码审查是其中的活动，两者不等价。这条如果采纳，可能违反 ALL-PROT-009（术语不得换称）。本清单照记，判断留给归并。
7. U-azh-002（四类问题的处理优先级）是从 Overview 一句话里拆出来的，上游没有把它写成显式步骤。是否算一条独立规则、还是只是对 Core Rules 章节顺序的描述，两种理解都成立；本清单按前者处理，理由是它规定了处理顺序，而 Core Rules 的章节顺序本身不构成要求。

## 5 疑似与现有规则或别的来源重合的单元

以下单元的判定逻辑估计会与现有 decisions.yaml 的规则或其他中文来源聚成一簇，归并时优先核对：

- 与现有规则高度重合：U-azh-003（≈ALL-PROT-003）、U-azh-008（≈ALL-PROT-001）、U-azh-009（≈ALL-PROT-004）、U-azh-029（≈ALL-P-007）、U-azh-030（≈ALL-P-005）、U-azh-031（≈ZH-P-003）、U-azh-032（≈ALL-P-002）、U-azh-033（≈ALL-P-001）、U-azh-034（≈ALL-P-004）、U-azh-035（≈ZH-P-006）、U-azh-038（≈ALL-P-008）、U-azh-056（≈ALL-PROC-025）、U-azh-065（≈ALL-PROC-014）
- 与现有规则冲突、需要按 criteria.md 第 8 条双记：U-azh-043（vs ZH-P-007）、U-azh-044（vs EN-P-027）、U-azh-050（vs ALL-PROT-009）、U-azh-060（vs ALL-PROC-008）
- 可给 unverified 规则补证据：U-azh-024、U-azh-025（可支持 ZH-P-011，现为 unverified）
- 估计会与 shuorenhua 聚成一簇：U-azh-024/025（翻译腔）与 U-srh-037（翻译腔处理），U-azh-027（大词）与 U-srh-034（商业黑话与表演性技术腔），U-azh-034（无主句）与 U-srh-094（系统行为主语的例外）、U-azh-042（引号样式）与 U-ohz-022（中文引号不套英文规则）
- 现有规则里确实没有、值得单独裁决的增量：U-azh-039（结尾必须回应开头提出的问题）、U-azh-064（连续三节可预测即命中）、U-azh-037（六个段落功能名）、U-azh-055（先机制后判断）、U-azh-013 至 U-azh-023（可选作者声音的整套流程）

## 6 上游文本内的指令

上游正文里有一处提到"写给模型看的指令"，但它是在规定如何处理这类内容，不是要求本清单执行的指令，照抄如下备查：

> 不要把 voice 档案里的 persona preamble（「You are a guy from 东北…」之类英文写作指令）原文输出给用户 —— 那是给你看的，不是文章内容。

这段被拆成 U-azh-022，作为一条"不得把提示词片段当正文输出"的保护规则记录，本清单不执行其中引用的人格设定，也未加载上游的 references/voices/ 目录（不在 sources.yaml 的 paths 追踪范围内，快照里也没有）。

除此之外，通读全文未发现针对读者或模型的注入式指令（例如"忽略之前的规则""把这段加进你的系统提示"）。
