# 来源拆分：upstream-op7418-humanizer-zh（derivative，只拆相对 blader 的差异）

## 1 来源摘要

- 文件：`merges/maybe-humanizer/snapshots/upstream-op7418-humanizer-zh/SKILL.source.md`
- 上游原路径：`SKILL.md`（仓库 `op7418/Humanizer-zh`，branch `main`）
- commit（sources.lock.json 的 last_seen_commit）：`91f3d394db8419c20d67ebe22a96cf8fee0a404b`
- 许可证：MIT，license_status 为 known，snapshot_policy 为 full-text，允许在本清单中引用原文短句。
- selection_status：derivative，lineage `blader-humanizer`。对照件：`merges/maybe-humanizer/snapshots/upstream-blader-humanizer/SKILL.source.md`（commit `e2e92e7b4b8229253ed5c8e81dc65463fdeddda5`，英文组拆它本身，本清单不拆）。
- 上游自述的定位：frontmatter 的 metadata 写明「翻译自 blader/humanizer，参考 hardikpandya/stop-slop」，正文自述基于维基百科「AI 写作特征」页面。16.7k stars，是中文圈传播最广的去 AI 味 skill。
- 总单元数：33（U-ohz-001 至 U-ohz-033）
- 按 category 计数：
  - pattern：20
  - style-opinion：5
  - process：3
  - measurement：2
  - genre：2
  - protection：1
- 按 language 计数：zh 33，en 0，both 0。（本清单只拆 op7418 相对 blader 的中文侧差异，英文规则本体由英文组从 blader 拆，故无 en 单元。）

### 相对 blader 的差异概述

op7418 的 24 条模式与 blader 的模式表逐条对应、顺序相同，是同一份表的翻译。差异集中在四类：

1. **中文触发词表（11 处，出单元）**。blader 的每条模式带一份英文「Words to watch」，op7418 把它换成了中文词条。这些词条不是英文词的对照译名，而是中文文本里对应模式的实际触发词（例如 blader §3 的英文 `-ing` 分词短语，在中文里对应「突出/强调/彰显……」「确保……」这类后置小句），对中文判定有独立价值，故逐节出单元。没有词表、只有译文说明和例句的小节（§9、§10、§11、§12、§13～§18、§21、§23、§24）不出单元。
2. **op7418 新增的整节（出单元）**：`## 核心规则速查`（5 条）、`## 个性与灵魂`（缺乏灵魂的六个迹象、增加语调的六种手法、一组改写前后示例）、`## 快速检查清单`（6 条）、`## 质量评分`（5 维度 50 分制与分档标准）、`## 完整示例`。blader 里没有对应内容。
3. **处理方式与 blader 不同的地方（出单元）**：`## 你的任务` 第 5 项把「注入真实的个性」写成无条件的固定步骤，而 blader 的对应要求带体裁条件；`### 16`、`### 18` 两节加了「此模式在中文中不太适用 / 在中文中表现为英文引号的使用」的适用性说明，blader 没有这类语言适配；`## 输出格式` 用一个统一格式取代了 blader 按输入类型分的三种返回模式。
4. **op7418 相对 blader 删掉的内容（不出单元，逐条记在下面，归并时需要知道这些不是 op7418 的主张，而是它没有译）**：
   - blader `## Match the writer's voice`（有写作样本时先分析样本、样本优先于风格规则、样本用破折号就不套用禁令）整节未译。
   - blader `## Add personality only when it fits` 的体裁限制段（参考类、技术类、法律类、事实类文本保持中性；绝不为了显得有人味而编造事实）未译，只保留了「避免 AI 模式只是工作的一半」这一层意思。
   - blader §13「Passive voice and missing subjects」（被动语态与省略主语）整条未译，op7418 的编号从 §12 直接跳到风格模式的破折号。
   - blader §9 的后半（clipped negative endings，`no guessing` 式的截断否定收尾）未译。
   - blader §11 的后半（重复句首的处理，以及「不要禁用这个重复的词，要改的是重复的句式」这条防误杀说明）未译。
   - blader §14 的两条执行细节未译：写作样本使用破折号时按样本的频率保留、提交前逐个搜索 `—` 和 `–`。
   - blader §21 的后半（用似是而非的猜测填补信息缺口）未译，只留了知识截止免责声明这一半。
   - blader §26～§35（连字符词对、假装揭示深层真相、预告下一个要点、标题被首句复述、叙述上一个版本、强行的金句与戏剧化碎片、格言化套话、假坦诚开场、反驳没人提出的反对、否决虚假备选）整块未译。
   - blader `## Check for false positives` 整节未译，包括「What not to flag」的 15 条误杀防护和「Human details to keep」的 7 条作者痕迹保留清单。这是本次比对里最重要的缺口：op7418 有全套命中规则，没有任何一条防误杀规则。
   - blader `## How to return the result`（按输入类型分 pasted / file / embedded 三种返回模式）未译。
   - blader `## Rewrite process` 第 3 步的两个自检问题未译，其中包括「这次改写有没有增加或删除任何事实、姓名、数字、日期、引语、引用或排序」以及「任何未经支持的新增或丢失的主张都算错误」。

## 2 单元清单

### U-ohz-001

```
id: U-ohz-001
category: process
language: zh
rule_summary: 处理任何待改写文本时固定执行五步，其中第五步「注入真实的个性」无条件适用，不因文本体裁而跳过。
positive: 一篇个人博客改完之后，除了删掉套话，还加入了作者的态度和一处自我修正。（自造）
negative: 一份接口变更说明改完之后，加了一句「说实话我一开始也没搞懂这个字段是干嘛的」。——违反点：把无条件的「注入个性」执行到了技术说明文本上。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 你的任务"
notes: |
  intent: 上游作者认为「去掉 AI 模式」只完成了一半工作，剩下一半是让文字有人写的痕迹，所以把它提升成任务清单里与「识别模式」「保留含义」并列的固定步骤。它针对的现象是：删完套话的稿子干净但没有声音，读起来像新闻稿。
  existing: 疑似对应 ALL-PROT-018（不得为了显得像真人而添加原文没有的第一人称、幽默、感受或个人经历）——两条方向相反。blader 的对应要求写作「Add personality only when it fits」，并明确参考类、技术类、法律类、事实类文本保持中性；op7418 把条件删掉了。归并时是明确的冲突项，按 criteria.md 第 1 条（保真优先于风格）与第 8 条（冲突双记）处理。
```

### U-ohz-002

```
id: U-ohz-002
category: pattern
language: zh
rule_summary: 并列项默认取两项而不是三项；已经写成三项列举的，改成两项或四项。
positive: 「活动包括演讲和小组讨论。」（自造）
negative: 「活动包括演讲、小组讨论和社交环节。」——违反点：三项并列，未按规则改成两项或四项。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 核心规则速查"
notes: |
  intent: blader §10 只说不要为了显得完整而强行凑三项，没有给替代值。op7418 把它变成一条可以直接照做的数量规则（两项优于三项，清单里补充「或四项」），针对的现象是模型写中文时无论内容有几项都凑成三项。上游未说明为什么两项和四项可以、三项不行，推断（标明是推断）：三项是最像"刻意排比"的数量，两项和四项读起来更像自然清点。
  existing: 疑似对应 ALL-P-005（不为凑气势用对称骨架，该用几项就用几项）。ALL-P-005 的判据是"内容有几项就写几项"，本单元的判据是"避开三这个数量"，两者在原文确实只有三项时会冲突。
```

### U-ohz-003

```
id: U-ohz-003
category: pattern
language: zh
rule_summary: 段落的结尾方式要有变化，不得整篇每段都用同一种收尾形状。
positive: 一段停在具体数字上，下一段停在一个没解决的问题上。（自造）
negative: 五个段落全部以一句简短有力的独立短句收尾。——违反点：段落结尾方式在全文范围内没有变化。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 核心规则速查"
notes: |
  intent: blader 把"句长有变化"列在「Human details to keep」里当作要保留的人写痕迹，op7418 把它翻转成一条改写要求，并且把对象从句子扩展到段落结尾。针对的现象是中文 AI 长文里每段都以一句短促的判断句收束，读到第三段就能预判。
  existing: 疑似对应 ALL-P-001（段落结构要有变化，整篇不得段落长度、开头句式雷同）。ALL-P-001 管开头，本单元管结尾。也与 U-azh-035、U-azh-064（ai-zixun 来源）同一主题。
```

### U-ohz-004

```
id: U-ohz-004
category: pattern
language: zh
rule_summary: 直接陈述事实，删掉软化、辩解和手把手引导式的铺垫。
positive: 「这个字段默认关闭。」（自造）
negative: 「需要说明的是，这里可能会稍微有点绕，不过别担心，我们一步一步来看：这个字段默认是关闭的。」——违反点：一句事实前面套了软化（可能有点绕）、辩解（不过别担心）和手把手引导（一步一步来看）三层铺垫。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 核心规则速查"
notes: |
  intent: 上游把这条命名为「信任读者」，针对的现象是模型默认把读者当成需要被安抚和牵引的人，于是每个事实前都加缓冲层。blader 把这类问题拆在 §24（过度限定）和 §28（预告下一个要点）里，op7418 把它们收成一条统一判据：这句话是不是在替读者降低难度。
  existing: 疑似对应 EN-P-029（不堆叠多层保留语）与 EN-P-007（删掉清嗓子式开场）。中文侧的「手把手引导」（我们一步一步来看、别担心）在现有中文词表 ZH-P-001 里没有对应条目。
```

### U-ohz-005

```
id: U-ohz-005
category: pattern
language: zh
rule_summary: 一句话听起来像可以被单独摘出来引用的金句时，重写它。
positive: 「对称的布局让用户更容易预测下一步。」（自造）
negative: 「对称，是信任的语言。」——违反点：整句是可摘抄的格言形式，没有给出具体主张。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 核心规则速查"
notes: |
  intent: blader §32 用一份英文格言模板表（X is the Y of Z、the currency of……）来抓这个问题，op7418 换成一条通用判据：可引用性本身就是信号。针对的现象是中文里格言的形状太多，列不完词表，但"这句话像不像可以印在海报上"是能判的。
  existing: 疑似对应 EN-P-024（删掉故作深刻的收尾金句和格言模板）与 ZH-P-002（不写听着能摘抄、实则没有信息的空心金句）。本单元把判据从词表换成可引用性，是一个可以补进 ZH-P-002 的判据。
```

### U-ohz-006

```
id: U-ohz-006
category: measurement
language: zh
rule_summary: 用六个迹象判断一篇「技术上干净」的稿子是不是没有声音：每句长度和结构都相同、没有观点只有中立报道、不承认不确定或复杂感受、该用第一人称时不用、没有幽默锋芒和个性、读起来像百科条目或新闻稿。
positive: 自查发现全篇没有一处作者判断、句长完全均匀，判定为"干净但无声音"，回到改写环节。（自造）
negative: 稿子里套话已经删光，直接判定为合格交付，没有检查上述六个迹象。——违反点：跳过"无声音"自查，把"没有 AI 词"当成了完成标准。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 缺乏灵魂的写作迹象"
notes: |
  intent: 上游认为「无菌、没有声音的写作和机器生成的内容一样明显」，所以给"干净但无声音"单独立了一组信号。它针对的现象是：按词表清理过的稿子会通过所有命中检查，但读者仍能一眼看出不是人写的。六个迹象共用同一条判定逻辑（判定一篇稿子是否缺乏声音），按 extraction.md 合并为一个单元。
  existing: 现有规则里没有（现有的 ALL-M-002 讲的是不要误判为 AI，本单元讲的是识别"清理过头"）。
```

### U-ohz-007

```
id: U-ohz-007
category: style-opinion
language: zh
rule_summary: 对事实要给出反应而不是只做中立报道，包括直说自己拿不准该怎么看。
positive: 「三百万行代码。我其实不太确定该怎么看这件事。」（自造）
negative: 「实验产生了有趣的结果。一些开发者印象深刻，另一些则持怀疑态度。」——违反点：只中立罗列两方反应，没有作者自己的反应。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 如何增加语调"
notes: |
  intent: 上游明说「我真的不知道该怎么看待这件事」比中立地列出利弊更有人味，针对的现象是模型习惯性地两边各说一句以示平衡，结果整篇没有立场。
  existing: 疑似对应 ALL-S-002（对任何观点逼出一个站得住的立场，decision 为 reference-only）与 ALL-PROC-018（点名拒绝各打五十大板的两边论调）。注意方向差别：ALL-PROC-018 禁止的是"补出"两边论调，本单元要求的是"补出"作者反应——后者在原文没有作者反应时会新增内容，与 ALL-PROT-001 冲突。
```

### U-ohz-008

```
id: U-ohz-008
category: style-opinion
language: zh
rule_summary: 允许并鼓励表达复杂或矛盾的感受，不把复杂感受压成单一评价。
positive: 「这挺让人佩服的，但也有点不安。」（自造）
negative: 「这令人印象深刻。」（原文本身表达的是佩服与不安两种感受）——违反点：把原文的矛盾感受压成了单一评价。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 如何增加语调"
notes: |
  intent: 上游的理由是"真实的人有复杂的感受"，针对的现象是模型倾向于把评价收敛成一个方向。反例按"原文本来就有两种感受"来写，这样它同时是一条保真规则；如果原文只有单一感受而改写补出矛盾，那就落到 ALL-PROT-001 的禁区。
  existing: 疑似对应 ALL-PROT-017（作者的犹疑属于作者，不得为了统一而改掉）。blader 的对应表述是"keep the writer's ... mixed feelings"（保留），op7418 写成"增加"，是同一件事的两个方向。
```

### U-ohz-009

```
id: U-ohz-009
category: style-opinion
language: zh
rule_summary: 该用第一人称的地方就用第一人称，不把「我一直在想的是……」这类表述当作不专业而回避。
positive: 「我一直在想那些通宵跑着的进程。」（自造）
negative: 一篇个人随笔里把所有「我觉得」改写成「可以认为」。——违反点：把作者原有的第一人称改成了无人称表述。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 如何增加语调"
notes: |
  intent: 上游的理由是"第一人称不是不专业，而是诚实"，针对的现象是模型把"正式"等同于"无人称"，于是把作者的第一人称洗掉。反例按"原文本来就有第一人称"来写，避免与不得新增第一人称的规则打架。
  existing: 疑似对应 ALL-PROT-017（保留作者的声口）与 ALL-PROT-018（不得为了像真人而添加原文没有的第一人称）。本单元如果按"补出第一人称"理解，与 ALL-PROT-018 冲突；按"不要删掉作者已有的第一人称"理解则与 ALL-PROT-017 一致。上游原文写的是"适当使用"，两种理解都读得出来，归并时需要择一并写明。
```

### U-ohz-010

```
id: U-ohz-010
category: style-opinion
language: zh
rule_summary: 允许文章里存在跑题、题外话和没有完全成型的想法，不把结构修得完全整齐。
positive: 「（这里其实还有一个我没想清楚的问题：如果两边同时改，谁来合？）」（自造）
negative: 把原文括号里那句「我到现在也没想明白」删掉，让段落干净。——违反点：删掉了作者的题外话与未成形的想法，为了结构整齐。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 如何增加语调"
notes: |
  intent: 上游的理由是"完美的结构感觉像算法"，针对的现象是模型的润色会把作者的旁逸斜出全部修掉，剩下一个结构完整但没有呼吸的稿子。
  existing: 疑似对应 ALL-PROT-017（跑题和自我纠正属于作者）与 ALL-PROC-030（不为整齐而统一结构）。
```

### U-ohz-011

```
id: U-ohz-011
category: style-opinion
language: zh
rule_summary: 描写感受时要具体到场景，不用「令人担忧」「令人印象深刻」这类概括性评价词。
positive: 「凌晨三点没人看着的时候，任务还在一轮一轮地跑。」（自造）
negative: 「这种情况令人担忧。」——违反点：用概括性评价词代替具体场景，换任何主语都成立。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 如何增加语调"
notes: |
  intent: 这是"写具体"这条老规则在感受层的落法：概括性的情绪词和概括性的事实词一样可移植。上游给的对照例子把"这令人担忧"换成一个带时间和动作的场景。
  existing: 疑似对应 ALL-P-007（能给具体内容的地方不用抽象词）与 ALL-M-001（可移植性测试）。注意：如果原文只写了"令人担忧"而改写补出"凌晨三点"这个细节，就违反 ALL-PROT-001；本单元只在原文已有场景素材时成立。
```

### U-ohz-012

```
id: U-ohz-012
category: protection
language: zh
rule_summary: （上游未以规则形式写出，只由六组示例演示）改写时允许用原文之外的具体事实替换掉被删掉的空话，例如补出具体年份、机构、数据或计划。
positive: 原文「专家认为它在区域生态系统中发挥着至关重要的作用」，改写后只保留可独立成立的部分：「研究人员在关注这条河的特殊之处。」（自造，按 blader 的处理方式）
negative: 引自上游示例——把「专家认为它在区域生态系统中发挥着至关重要的作用」改写成「根据中国科学院 2019 年的调查，浩来河支持多种特有鱼类」。违反点：改写稿里的机构名、年份和结论在原文里都不存在，是被补出来的。
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 5. 模糊归因和含糊措辞"
notes: |
  intent: 上游未说明；正文里没有任何一句允许补写事实，但六组「改写后」示例都这么做了（§2 补出「在 2024 年《纽约时报》的采访中」、§4 补出「以其每周集市和 18 世纪教堂而闻名」、§5 补出「中国科学院 2019 年的调查」、§6 补出「2015 年三个新 IT 园区开业」、§20 补出「根据注册文件，该公司成立于 1994 年」、§24 补出「计划明年再开设两个地点」）。同一位置 blader 的示例只做删除，不补内容。推断（标明是推断）：这不是上游有意立的规则，而是翻译时为了让中文例句读起来"更好"而重写了 After 段，加上 blader 原文里那句「Never invent a source」和 Rewrite process 的事实自检问题都没有被译出，于是防线整体缺失。示例在 skill 里是被模仿的对象，效果等同于规则，故按可判定规则的形式记录，供归并阶段裁决。
  existing: 疑似对应 ALL-PROT-001（不得新增原文没有的事实、数字、日期、来源）——本单元与它直接冲突，按 criteria.md 第 1 条应保 ALL-PROT-001。归并时建议在 ALL-PROT-001 的 rationale 里点名这组示例作为反例证据。
```

### U-ohz-013

```
id: U-ohz-013
category: pattern
language: zh
rule_summary: 中文文本里以下夸大意义的说法要删掉或换成具体事实：作为/充当、标志着、见证了、是……的体现/证明/提醒、极其重要的/重要的/至关重要的/核心的/关键性的作用/时刻、凸显/强调/彰显了其重要性/意义、反映了更广泛的、象征着其持续的/永恒的/持久的、为……做出贡献、为……奠定基础、标志着/塑造着、代表/标志着一个转变、关键转折点、不断演变的格局、焦点、不可磨灭的印记、深深植根于。
positive: 「统计局成立于 1989 年，负责收集和发布区域统计数据。」（自造）
negative: 「统计局于 1989 年正式成立，标志着区域统计演变史上的关键时刻。」——违反点：「标志着」「关键时刻」把一次机构成立说成历史转折。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 1. 过度强调意义、遗产和更广泛的趋势"
notes: |
  intent: 规则本身对应 blader §1（LLM 通过声称某个细节代表更广泛的趋势来夸大重要性）。op7418 的增量是这份中文词表：它不是英文词的译名对照，而是中文文本里这一模式的实际触发词，其中「彰显」「深深植根于」「不断演变的格局」在中文自媒体里的密度远高于英文对应词。词表照录自上游，说明文字为重写（license-policy.md 允许词条本身逐条照录）。
  existing: 疑似对应 ZH-P-001（中文高频词与企业黑话词表，已含"彰显""标志着""凸显"）与 EN-P-014（不把普通事实吹成有时代意义）。本词表可以给 ZH-P-001 补十余个词条。
```

### U-ohz-014

```
id: U-ohz-014
category: pattern
language: zh
rule_summary: 不用「独立报道」「地方/区域/国家媒体」「由知名专家撰写」「活跃的社交媒体账号」这类知名度陈述证明重要性；保留一条说清具体报道了什么的引用，其余删掉。
positive: 「她在一次采访里说，监管应该盯结果而不是盯做法。」（自造）
negative: 「她的观点被多家国家媒体引用，并在社交媒体上拥有活跃的存在。」——违反点：用媒体清单和粉丝规模代替具体内容，读者读完不知道她说了什么。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 2. 过度强调知名度和媒体报道"
notes: |
  intent: 规则本身对应 blader §2。中文侧的增量是「活跃的社交媒体账号」「独立报道」这几个在中文人物介绍、公司简介里高频出现的固定说法。上游的问题描述指出这类罗列"通常不提供上下文"，即它占了篇幅却没有信息。
  existing: 疑似对应 EN-P-018（不用媒体清单证明重要性）。中文触发词在现有中文词表里没有。
```

### U-ohz-015

```
id: U-ohz-015
category: pattern
language: zh
rule_summary: 删掉在句末追加的「突出/强调/彰显……」「确保……」「反映/象征……」「为……做出贡献」「培养/促进……」「涵盖……」「展示……」这类后置小句；它们制造深度，不增加信息。
positive: 「寺庙用了蓝、绿、金三色，建筑师说是为了呼应当地的花和海。」（自造）
negative: 「寺庙的色调与该地区的自然美景产生共鸣，象征着当地的花与海，反映了社区与土地的深厚联系。」——违反点：句末连挂「象征着……」「反映了……」两个后置小句，两句都没有新增事实。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 3. 以 -ing 结尾的肤浅分析"
notes: |
  intent: 规则本身对应 blader §3，但 blader 的判定抓手是英文的 `-ing` 分词形态，中文没有这个形态。op7418 给出的这组中文后置小句是这一模式在中文里的实际形状，判定对象从"词尾"变成了"句末追加的评论性小句"。这是一处真正的语言适配，不是词表对译。
  existing: 疑似对应 EN-P-013（删掉假装在解释意义的现在分词从句）。中文侧没有对应规则，本单元是 EN-P-013 的中文版，值得单独立条。
```

### U-ohz-016

```
id: U-ohz-016
category: pattern
language: zh
rule_summary: 不用以下宣传式词语代替事实：拥有（夸张用法）、充满活力的、丰富的（比喻）、深刻的、增强其、展示、体现、致力于、自然之美、坐落于、位于……的中心、开创性的（比喻）、著名的、令人叹为观止的、必游之地、迷人的。
positive: 「这是贡德尔地区的一座小城。」（自造）
negative: 「坐落在令人叹为观止的贡德尔地区，这座充满活力的城镇拥有丰富的文化遗产。」——违反点：「坐落在」「令人叹为观止」「充满活力」「拥有丰富的」四处宣传词，没有一处说明这座城具体是什么样。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 4. 宣传和广告式语言"
notes: |
  intent: 规则本身对应 blader §4。上游点名这个模式在"文化遗产"类话题上最严重。中文词表的增量在于「坐落于」「令人叹为观止」「必游之地」这一组，在中文旅游与城市宣传语料里密度极高，模型写中文城市介绍时几乎必然出现。
  existing: 疑似对应 ZH-P-001（已含"令人叹为观止""坐落于"）与 EN-P-002（英文旅游宣传册式形容词）。中文词表里「必游之地」「充满活力的」「开创性的」等条目可补。
```

### U-ohz-017

```
id: U-ohz-017
category: pattern
language: zh
rule_summary: 「行业报告显示」「观察者指出」「专家认为」「一些批评者认为」「多个来源/出版物」这类模糊归因，要么点名具体来源，要么删掉整条论断。
positive: 「这条河的鱼种情况目前没有公开的调查数据。」（自造）
negative: 「专家认为它在区域生态系统中发挥着至关重要的作用。」——违反点：把结论挂在没有名字的"专家"身上。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 5. 模糊归因和含糊措辞"
notes: |
  intent: 规则本身对应 blader §5。中文词表的增量是「行业报告显示」「一些批评者认为」这组在中文资讯稿里的固定说法。要特别注意：blader 在这一节末尾写了「Name a real source when the source text provides one. Otherwise, remove the unsupported claim. Never invent a source.」，op7418 没有译这三句，而它的示例正是补了一个来源出来（见 U-ohz-012）。
  existing: 疑似对应 EN-P-017（模糊归因要点名具体来源或删掉整个论断）。中文触发词在现有中文词表里没有。
```

### U-ohz-018

```
id: U-ohz-018
category: pattern
language: zh
rule_summary: 不写「尽管其……面临若干挑战……」「尽管存在这些挑战」「挑战与遗产」「未来展望」这类提纲式小节；写具体问题，或整段删掉。
positive: 「2015 年之后这一带的早高峰堵得更厉害了。」（自造）
negative: 「尽管工业繁荣，该地也面临城市地区典型的挑战。尽管存在这些挑战，凭借其战略位置，它仍在持续发展。」——违反点：「尽管……」「尽管存在这些挑战」构成的套路小节，两句都没有具体问题。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 6. 提纲式的"
notes: |
  intent: 规则本身对应 blader §6。中文词表的增量是「挑战与遗产」「未来展望」这两个在中文长文里被当成固定小节标题的说法——它们不只是句子，还是结构模板，模型写完主体后会自动补上这么一节。
  existing: 疑似对应 EN-P-031（不用"Despite ... challenges"式挑战小节套路）。中文侧没有对应规则。
```

### U-ohz-019

```
id: U-ohz-019
category: pattern
language: zh
rule_summary: 中文高频 AI 词汇表，这些词出现（尤其是扎堆出现）时删掉或换成大白话：此外、与……保持一致、至关重要、深入探讨、强调、持久的、增强、培养、获得、突出（动词）、相互作用、复杂/复杂性、关键（形容词）、格局（抽象名词）、关键性的、展示、织锦（抽象名词）、证明、强调（动词）、宝贵的、充满活力的。
positive: 「索马里菜里也有骆驼肉。意大利面是殖民时期传进来的，南部现在还常吃。」（自造）
negative: 「此外，一个显著特征是加入骆驼肉。意大利殖民影响的持久证明是当地烹饪格局中广泛采用意大利面，展示了这些菜肴如何融入传统饮食。」——违反点：「此外」「持久证明」「格局」「展示」四个高频词集中在两句里。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 7. 过度使用的"
notes: |
  intent: 规则本身对应 blader §7，判据也一样（这些词在 2023 年之后的文本里频率高得多，而且常常成群出现）。中文词表是逐条译过来的，其中「织锦」是 tapestry 的直译，在中文里几乎不出现，属于翻译痕迹而不是中文触发词——归并时应剔除。真正在中文里成立的是「此外」「至关重要」「深入探讨」「格局」「赋予/增强」这一组。
  existing: 疑似对应 ZH-P-001（中文高频词表，已含"此外""值得注意的是""至关重要""深入探讨"）与 EN-M-001（英文高频词分三档处理）。本单元可给 ZH-P-001 补「相互作用」「宝贵的」「持久的」等条目，同时应把「织锦」剔除。
```

### U-ohz-020

```
id: U-ohz-020
category: pattern
language: zh
rule_summary: 用「是」「有」代替「作为/代表/标志着/充当 [一个]」「拥有/设有/提供 [一个]」这类系动词替身。
positive: 「Gallery 825 是 LAAA 的当代艺术展览空间，有四个房间。」（自造）
negative: 「Gallery 825 作为 LAAA 的当代艺术展览空间。画廊设有四个独立空间，拥有超过 3000 平方英尺。」——违反点：「作为」「设有」「拥有」三处都在回避「是」和「有」。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 8. 避免使用"
notes: |
  intent: 规则本身对应 blader §8。中文侧的增量是这份替身词表：中文的「作为……」当谓语用是明显的书面腔，「设有」「提供」在机构介绍里成群出现。「作为 X」在中文里还有一个副作用——它常常让句子没有谓语（例句里的第一句就不成句）。
  existing: 疑似对应 EN-P-015（用 is/are/has 代替花哨的系动词替身）。中文侧没有对应规则。
```

### U-ohz-021

```
id: U-ohz-021
category: genre
language: zh
rule_summary: 标题大小写模式不适用于中文标题；不得据此改写中文标题的写法。
positive: 遇到中文标题时跳过大小写检查，只看标题本身是不是套话。（自造）
negative: 把中文标题「战略谈判与全球伙伴关系」当成命中"标题大写"模式并做改写。——违反点：把只对英文成立的大小写模式套用到了中文标题上。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 16. 标题中的标题大写"
notes: |
  intent: op7418 保留了 blader §17 的整节，但示例的"改写前"和"改写后"是同一行中文，于是加了一句注说明这个模式在中文里不适用。这条注是它相对 blader 的实质增量：blader 没有语言适配的概念。它针对的现象是照搬英文模式表到中文时会产生空转甚至误改。
  existing: 现有规则里没有（现有 EN-P-012 明确限定 language 为 en，等于隐含了同一结论，但没有把"这条不适用于中文"写成规则）。
```

### U-ohz-022

```
id: U-ohz-022
category: genre
language: zh
rule_summary: 弯引号模式在中文文本上的检查对象是文中英文引号的用法，不是中文引号本身。
positive: 中文正文里的「」和“”照原样保留，只检查夹在其中的英文引文用了哪种引号。（自造）
negative: 把中文正文里的“……”当成命中"弯引号"模式，全部替换成英文直引号。——违反点：把针对英文排版的弯引号规则直接套到中文引号上。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 18. 弯引号"
notes: |
  intent: 与 U-ohz-021 同一动机：这一节译过来之后示例的前后两句在中文里完全相同，上游用一句注把适用对象改掉。它防的是照搬英文排版规则把中文标点改坏。
  existing: 疑似对应 EN-P-037（引号排版跟随作者原稿，language 为 en）。与 ai-zixun 来源的 U-azh-042（中文引号默认全角双引号、两种样式不混用）是同一问题的两种处理：本单元说不管，U-azh-042 说要统一。归并时需要对齐。
```

### U-ohz-023

```
id: U-ohz-023
category: pattern
language: zh
rule_summary: 删掉粘在正文里的聊天残留：希望这对您有帮助、当然！、一定！、您说得完全正确！、您想要……、请告诉我、这是一个……。
positive: 「法国大革命始于 1789 年。」（自造）
negative: 「这是法国大革命的概述。希望这对您有帮助！如果您想让我扩展任何部分，请告诉我。」——违反点：首句的「这是一个……」式引出语与末句的「希望这对您有帮助」「请告诉我」都是对话残留。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 19. 协作交流痕迹"
notes: |
  intent: 规则本身对应 blader §20。中文词表的增量是这组中文助手用语——它们不是英文短语的译文，而是中文对话模型自己会说的话，尤其「希望这对您有帮助」「请告诉我」几乎是固定收尾。
  existing: 疑似对应 EN-P-028（删掉聊天残留，含 I hope this helps、Let me know）。中文侧的对应词条在 ZH-P-001 里没有。
```

### U-ohz-024

```
id: U-ohz-024
category: pattern
language: zh
rule_summary: 删掉知识截止免责声明：截至 [日期]、根据我最后的训练更新、虽然具体细节有限/稀缺……、基于可用信息……。
positive: 「公开资料里没有记载这家公司的成立时间。」（自造）
negative: 「虽然关于公司成立的具体细节在现成资料中没有广泛记录，但它似乎是在 20 世纪 90 年代的某个时候成立的。」——违反点：「虽然具体细节……没有广泛记录」是免责声明，后半句还在此基础上给了一个猜测。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 20. 知识截止日期免责声明"
notes: |
  intent: 规则本身对应 blader §21 的前半。中文词表的增量是这组中文免责说法。要注意 blader §21 还有后半——模型解释自己找不到来源之后，用一个听起来合理的猜测填补空缺（likely、it is believed that、maintains a low profile），并要求"不要把猜测当成事实"。op7418 没有译这一半，它的示例反而演示了用一个补出来的注册文件年份填掉空缺（见 U-ohz-012）。
  existing: 疑似对应 EN-P-028（含知识截止免责声明）与 ALL-PROT-001。中文触发词在现有中文词表里没有。
```

### U-ohz-025

```
id: U-ohz-025
category: pattern
language: zh
rule_summary: 中文填充短语按固定对照缩短：「为了实现这一目标」→「为了实现这一点」、「由于下雨的事实」→「因为下雨」、「在这个时间点」→「现在」、「在您需要帮助的情况下」→「如果您需要帮助」、「系统具有处理的能力」→「系统可以处理」、「值得注意的是数据显示」→「数据显示」。
positive: 「数据显示，投诉在上线后第二周开始下降。」（自造）
negative: 「值得注意的是数据显示，在这个时间点，系统具有处理该类请求的能力。」——违反点：「值得注意的是」「在这个时间点」「具有……的能力」三处填充结构。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "### 22. 填充短语"
notes: |
  intent: 规则本身对应 blader §23。这组中文对照里有真正的中文病灶（「在这个时间点」「具有……的能力」是中文里常见的名词化填充），也有直译痕迹（「由于下雨的事实」是 due to the fact that 的字面译，中文里几乎不会这么写）。归并时应保留前者、剔除后者。
  existing: 疑似对应 EN-P-004（不增加信息的短语与连接词）与 ZH-P-001。中文侧「具有……的能力」「在这个时间点」可补进 ZH-P-001。
```

### U-ohz-026

```
id: U-ohz-026
category: pattern
language: zh
rule_summary: 交付前检查是否有连续三个句子长度相同；有就把其中一句改掉。
positive: 发现连续三句都是十四五个字，把中间一句拆成两个短句。（自造）
negative: 连续三句都是「这个改动降低了成本。」这种同长同构的句子，交付时未做处理。——违反点：命中"连续三句长度相同"这个阈值却没有打断。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 快速检查清单"
notes: |
  intent: blader 只在「Human details to keep」里说真人写作会长短交错、AI 倾向于均匀中长句，没有给判定门槛。op7418 把它变成一条带数值的交付检查（连续三句），针对的现象是"句长要有变化"这种说法无法判定，写不进检查清单。
  existing: 疑似对应 ALL-P-001（中文口径：同一段里连续三句以上字数相差在 3 个字以内即命中）。本单元的门槛与 ALL-P-001 的中文口径一致，可以作为独立证据。
```

### U-ohz-027

```
id: U-ohz-027
category: pattern
language: zh
rule_summary: 交付前检查段落是不是以简洁的单行收尾；是就换一种结尾方式。
positive: 发现三段都以一句独立短句结尾，把其中两段的结尾并回上一句。（自造）
negative: 每段末尾都单独留一行「就是这样。」交付时未处理。——违反点：段落固定以简洁单行收尾，命中检查项却未变换。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 快速检查清单"
notes: |
  intent: 这是 U-ohz-003（段落结尾要多样化）在交付环节的可判定形式：把"多样化"具体成一个可以数出来的形状——简洁的单行结尾。blader 的 §31 描述过这种戏剧化收尾，但没有把它写成检查项，也没有译进 op7418 的模式表。
  existing: 疑似对应 EN-P-025（不用戏剧化的碎片句制造节奏）与 ALL-P-001。中文侧没有对应规则。
```

### U-ohz-028

```
id: U-ohz-028
category: pattern
language: zh
rule_summary: 交付前检查是否有用在揭晓前制造停顿的破折号；有就删掉。
positive: 「真正卡住的是排期。」（自造）
negative: 「真正卡住的不是技术——是排期。」——违反点：破折号用在揭晓前制造停顿。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 快速检查清单"
notes: |
  intent: op7418 §13 已经全面反对破折号，这条检查项把最典型的一种用法单列出来：揭晓前的停顿。它比"少用破折号"可判定，因为位置固定。blader §14 的对应要求是提交前逐个搜索 `—` 和 `–`，那句执行细节 op7418 没有译。
  existing: 疑似对应 ZH-P-007（中文破折号只在真正需要时用一次）与 EN-P-026（英文破折号按篇幅分界）。"揭晓前的破折号"这个位置判据现有规则里没有。
```

### U-ohz-029

```
id: U-ohz-029
category: pattern
language: zh
rule_summary: 交付前检查有没有在打完比方之后又解释这个比方；有就删掉解释，让比方自己成立。
positive: 「排期像拼图，缺一块就摆不下去。」（自造）
negative: 「排期像拼图，缺一块就摆不下去——也就是说，只要有一个环节没到位，整件事就推进不了。」——违反点：比方之后又加了一句"也就是说"的解释。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 快速检查清单"
notes: |
  intent: 上游把它归在「信任读者」这条核心规则下，针对的现象是模型不放心读者能接住比喻，于是紧接着用直白语言重说一遍，结果同一个意思出现两次。
  existing: 疑似对应 ALL-P-011（不用"换句话说""也就是说"把同一个意思绕几遍）。本单元的触发位置更具体（紧跟在比喻之后），可作为 ALL-P-011 的补充证据。
```

### U-ohz-030

```
id: U-ohz-030
category: pattern
language: zh
rule_summary: 交付前检查「此外」「然而」这类连接词，逐个判断能不能删掉。
positive: 删掉「此外」，两句直接并列，读起来没有损失。（自造）
negative: 一段里连着用「此外」「然而」「因此」，交付前未逐个检查是否必要。——违反点：命中连接词检查项却未做删除判断。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 快速检查清单"
notes: |
  intent: 与 U-ohz-019 的词表重合（「此外」在词表里），但这里的形态不同：词表是改写时的命中规则，本条是交付前的复查项，且措辞是"考虑删除"而不是"删除"，留了保留真实逻辑关系的余地。
  existing: 疑似对应 ZH-P-001（元叙述与连接词）与 ALL-PROT-020（删连接词时不得连同真实逻辑关系一起删掉）。归并时应与 ALL-PROT-020 配对，否则"考虑删除"会被执行成一律删除。
```

### U-ohz-031

```
id: U-ohz-031
category: process
language: zh
rule_summary: 输出固定为两部分：改写后的文本；以及一份可选的更改摘要，逐条写明删了什么、属于哪个模式。
positive: 交付改写稿，后附「删除了『作为……的证明』（夸大象征意义）」这样的逐条说明。（自造）
negative: 只交付改写稿，用户要求说明时也不给逐条更改。——违反点：更改摘要虽是可选，但用户要求时未提供。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 输出格式"
notes: |
  intent: blader 按输入类型分了三种返回模式（粘贴的文本返回草稿＋剩余问题清单＋终稿；文件模式只写终稿并给简短总结；被别的流程调用时只返回终稿），op7418 把三种合并成一个统一格式，改动说明降级为可选。推断（标明是推断）：简化的动机是中文用户多数是直接粘贴文本，用不上文件与嵌入两种模式；代价是丢掉了"被别的流程调用时只返回正文"这一条，容易在自动化调用里把说明混进正文。`## 完整示例` 一节的「所做更改」演示的就是这份可选摘要的写法。
  existing: 疑似对应 ALL-PROC-008（改动说明不得省略）与 ALL-PROC-021（内嵌模式才只给正文）。本单元把改动说明记为可选，与 ALL-PROC-008 冲突；它没有内嵌模式的概念，与 ALL-PROC-021 是缺口而不是冲突。
```

### U-ohz-032

```
id: U-ohz-032
category: measurement
language: zh
rule_summary: 对改写后的文本按五个维度各打 1 到 10 分并求和（满分 50）：直接性（直接陈述还是绕圈铺垫）、节奏（句长是否变化）、信任度（是否过度解释）、真实性（是否机械生硬）、精炼度（还有没有可删的）。
positive: 改完给出五项分数和总分，总分低的那一项指出具体是哪几句拉低的。（自造）
negative: 改完只写一句「整体读起来自然多了」。——违反点：没有按五个维度分别给分，无法定位是哪一项不合格。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 质量评分"
notes: |
  intent: blader 没有任何评分机制。op7418 加这一节是为了让"改得好不好"有一个可以说出口的结果，五个维度分别对应它自己的五条核心规则（速查里的删填充、变节奏、信任读者、有个性、删金句）。推断（标明是推断）：它的用途是自查而不是对外报告，因为分档标准的落点是"要不要重新修订"。注意这套评分不声称能预测任何 AI 检测器的判定，与 criteria.md 第 5 条第 1 项禁止的那类分数不是一回事。
  existing: 疑似对应 ALL-M-005（按公式给文本算分并按分段给判语，decision 为 rejected）与 ALL-M-004（自己改完自己判分不算验收）。本单元的评分维度与 ALL-M-005 被拒的那套不同（不含"不该被任何检测器标记"这类判语），归并时要区分对待，不要因为同属"打分"就直接沿用 rejected。
```

### U-ohz-033

```
id: U-ohz-033
category: process
language: zh
rule_summary: 按质量评分的总分决定是否再改：45 到 50 分算完成，35 到 44 分算还有改进空间，低于 35 分必须重新修订。
positive: 自评 31 分，不交付，回到改写环节再做一轮。（自造）
negative: 自评 28 分，仍然当成终稿交付。——违反点：总分低于 35 分的门槛却没有重新修订。（自造）
source:
  type: upstream
  source_id: upstream-op7418-humanizer-zh
  path: SKILL.md
  commit: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  anchor: "## 质量评分"
notes: |
  intent: 这条把评分和动作挂上钩，否则打分只是装饰。上游没有给重试次数上限，推断（标明是推断）：这是一个疏漏，按字面执行可能在低分文本上反复重写。
  existing: 疑似对应 ALL-PROC-019（改完可以重跑检查再改一轮，最多三轮）。本单元缺少轮次上限，归并时如果采纳需要补上 ALL-PROC-019 的上限。
```

## 3 覆盖表

op7418 的每个小节要么对应 blader 的小节（纯译文，不出单元），要么对应本清单的单元。

| op7418 小节 | 对应 blader 的小节 / 归属单元 |
|---|---|
| frontmatter：`name`、`description` | 对应 blader 的 frontmatter `name`、`description`（译文，术语与模式名一一对应） |
| frontmatter：`allowed-tools`、`metadata` | 非规则内容（工具白名单与来源声明；`metadata.source` 写明翻译自 blader/humanizer） |
| 标题「# Humanizer-zh: 去除 AI 写作痕迹」与开篇段 | 对应 blader 的「# Humanizer: remove AI writing patterns」及其开篇段 |
| ## 你的任务 第 1～4 项 | 对应 blader 的「## What to do」第 1～4 项 |
| ## 你的任务 第 5 项（注入灵魂） | U-ohz-001 |
| ## 核心规则速查 ①删除填充短语 | 对应 blader §23「Filler phrases」 |
| ## 核心规则速查 ②打破公式结构 | 对应 blader §9（二元对比）与 §31（戏剧化碎片）；§31 本身未译进模式表 |
| ## 核心规则速查 ③变化节奏（混合句长、两项优于三项、段落结尾多样化） | 句长部分对应 blader「Human details to keep / Variety in sentence length」；U-ohz-002、U-ohz-003 |
| ## 核心规则速查 ④信任读者 | U-ohz-004 |
| ## 核心规则速查 ⑤删除金句 | U-ohz-005 |
| ## 个性与灵魂 引言段 | 对应 blader「## Add personality only when it fits」前两段；blader 该节的体裁限制段未译（见差异概述） |
| ### 缺乏灵魂的写作迹象 | U-ohz-006 |
| ### 如何增加语调（有观点） | U-ohz-007 |
| ### 如何增加语调（变化节奏） | U-ohz-003 的重复表述 |
| ### 如何增加语调（承认复杂性） | U-ohz-008 |
| ### 如何增加语调（适当使用「我」） | U-ohz-009 |
| ### 如何增加语调（允许一些混乱） | U-ohz-010 |
| ### 如何增加语调（对感受要具体） | U-ohz-011 |
| ### 改写前 / 改写后（干净但无灵魂 → 鲜活） | U-ohz-012（示例补出了原文没有的内容） |
| ## 内容模式（分组标题） | 对应 blader「## Content patterns」 |
| ### 1. 过度强调意义、遗产和更广泛的趋势 | 对应 blader §1；中文词表 U-ohz-013；示例 U-ohz-012 |
| ### 2. 过度强调知名度和媒体报道 | 对应 blader §2；中文词表 U-ohz-014；示例 U-ohz-012 |
| ### 3. 以 -ing 结尾的肤浅分析 | 对应 blader §3；中文后置小句词表 U-ohz-015 |
| ### 4. 宣传和广告式语言 | 对应 blader §4；中文词表 U-ohz-016；示例 U-ohz-012 |
| ### 5. 模糊归因和含糊措辞 | 对应 blader §5（末尾三句防误写未译）；中文词表 U-ohz-017；示例 U-ohz-012 |
| ### 6. 提纲式的「挑战与未来展望」部分 | 对应 blader §6；中文词表 U-ohz-018；示例 U-ohz-012 |
| ## 语言和语法模式（分组标题） | 对应 blader「## Language and grammar patterns」 |
| ### 7. 过度使用的「AI 词汇」 | 对应 blader §7；中文词表 U-ohz-019 |
| ### 8. 避免使用「是」 | 对应 blader §8；中文词表 U-ohz-020 |
| ### 9. 否定式排比 | 对应 blader §9 的前半（后半的截断否定收尾未译） |
| ### 10. 三段式法则过度使用 | 对应 blader §10 |
| ### 11. 刻意换词（同义词循环） | 对应 blader §11 的前半（重复句首与防误杀说明未译） |
| ### 12. 虚假范围 | 对应 blader §12 |
| （无对应小节） | blader §13「Passive voice and missing subjects」整条未译 |
| ## 风格模式（分组标题） | 对应 blader「## Style patterns」 |
| ### 13. 破折号过度使用 | 对应 blader §14（写作样本例外与提交前搜索两条执行细节未译） |
| ### 14. 粗体过度使用 | 对应 blader §15 |
| ### 15. 内联标题垂直列表 | 对应 blader §16 |
| ### 16. 标题中的标题大写 | 对应 blader §17；中文适用性注 U-ohz-021 |
| ### 17. 表情符号 | 对应 blader §18 |
| ### 18. 弯引号 | 对应 blader §19；中文适用性注 U-ohz-022 |
| ## 交流模式（分组标题） | 对应 blader「## Chatbot patterns」 |
| ### 19. 协作交流痕迹 | 对应 blader §20；中文词表 U-ohz-023 |
| ### 20. 知识截止日期免责声明 | 对应 blader §21 的前半（猜测填补空缺的后半未译）；中文词表 U-ohz-024；示例 U-ohz-012 |
| ### 21. 谄媚/卑躬屈膝的语气 | 对应 blader §22 |
| ## 填充词和回避（分组标题） | 对应 blader「## Filler and hedging」 |
| ### 22. 填充短语 | 对应 blader §23；中文对照表 U-ohz-025 |
| ### 23. 过度限定 | 对应 blader §24 |
| ### 24. 通用积极结论 | 对应 blader §25；示例 U-ohz-012 |
| （无对应小节） | blader §26～§35 整块未译 |
| （无对应小节） | blader「## Check for false positives」整节未译（15 条误杀防护 + 7 条作者痕迹保留） |
| （无对应小节） | blader「## Match the writer's voice」整节未译 |
| ## 快速检查清单 第 1 项（连续三句同长） | U-ohz-026 |
| ## 快速检查清单 第 2 项（段落简洁单行收尾） | U-ohz-027 |
| ## 快速检查清单 第 3 项（揭示前的破折号） | U-ohz-028 |
| ## 快速检查清单 第 4 项（解释隐喻或比喻） | U-ohz-029 |
| ## 快速检查清单 第 5 项（「此外」「然而」等连接词） | U-ohz-030 |
| ## 快速检查清单 第 6 项（三段式改为两项或四项） | U-ohz-002 |
| ## 处理流程 | 对应 blader「## Rewrite process」（第 3 步的两个自检问题未译，其中含事实增删自检） |
| ## 输出格式 | U-ohz-031（blader「## How to return the result」的三种返回模式未译） |
| ## 质量评分（评分表） | U-ohz-032 |
| ## 质量评分（标准：45-50 / 35-44 / 低于 35） | U-ohz-033 |
| ## 完整示例（改写前 / 改写后） | 对应 blader 各模式小节的 Before/After 体例；本例的「改写后」同样补出了原文没有的功能与反馈，归 U-ohz-012 |
| ## 完整示例（所做更改清单） | U-ohz-031 里可选更改摘要的示范 |
| ## 参考 | 对应 blader「## Source」（同一段维基百科出处与引语） |

## 4 拆分时拿不准的地方

1. **U-ohz-012 不是上游写出来的规则，是从示例反推的。** 上游正文没有任何一句允许补写事实，但六组「改写后」示例都补了。按 extraction.md，单元必须是"一条可判定的规则"，本清单把它写成规则形式并在 notes 里标明是推断。归并阶段有两种处理都成立：当成一条与 ALL-PROT-001 冲突的规则裁决，或者不当规则、只作为 ALL-PROT-001 的反例证据写进 rationale。本清单倾向后者，但没有替归并做决定。
2. **中文词表要不要逐条采纳，本清单没有裁决。** U-ohz-019 里的「织锦」和 U-ohz-025 里的「由于下雨的事实」明显是直译痕迹，在中文语料里几乎不出现；同一份词表里的其他条目则是真实的中文触发词。词表照录时按 license-policy.md 逐条同序照录，剔除哪几条留给归并。
3. **「注入灵魂」这一整块（U-ohz-001、U-ohz-006 至 U-ohz-011）与本仓库现有的 ALL-PROT-018 是正面冲突。** 上游因为没有译 blader 的体裁限制段和误杀防护节，这一块在它自己的文本里没有任何边界。本清单按原样拆出，没有替它补边界；归并时如果采纳，必须补上体裁条件和"不得为此新增事实"的限制，否则会与 ALL-PROT-001、ALL-PROT-018 直接打架。
4. **U-ohz-002（两项优于三项）与 ALL-P-005（该用几项就用几项）在原文确实有三项时会给出相反的动作。** 两条都可判定，谁优先取决于本仓库是把"三项"当成需要被打散的模板信号，还是当成一个中性的数量。本清单不预判。
5. **op7418 未译的部分数量很大（blader §13、§26～§35、整节误杀防护、写作样本一节），但"未译"不等于"反对"。** 本清单把它们记在差异概述里而不是当作 op7418 的主张，归并时不应据此认为 op7418 与 blader 在这些点上有分歧。它唯一可以支持的结论是：只装了 op7418 的用户拿不到这些规则。
6. **U-ohz-009（适当使用第一人称）有两种读法**：保留作者已有的第一人称（与 ALL-PROT-017 一致），或在改写中补出第一人称（与 ALL-PROT-018 冲突）。上游原文「适当使用『我』。第一人称不是不专业——而是诚实」两种都读得出来。本清单的正反例按前一种读法写，并在 notes 里标明另一种读法存在。

## 5 疑似与现有规则或别的来源重合的单元

- 与现有规则直接冲突、需按 criteria.md 第 8 条双记：U-ohz-001（vs ALL-PROT-018）、U-ohz-012（vs ALL-PROT-001）、U-ohz-031（vs ALL-PROC-008）、U-ohz-002（vs ALL-P-005）、U-ohz-022（vs ai-zixun 的 U-azh-042）
- 与现有规则高度重合、估计会聚成一簇：U-ohz-013（≈ZH-P-001 + EN-P-014）、U-ohz-016（≈ZH-P-001 + EN-P-002）、U-ohz-019（≈ZH-P-001 + EN-M-001）、U-ohz-023（≈EN-P-028）、U-ohz-025（≈EN-P-004）、U-ohz-026（≈ALL-P-001 中文口径）、U-ohz-029（≈ALL-P-011）
- 可以填补现有中文规则缺口的单元（现有规则只有英文版）：U-ohz-015（分词式后置小句的中文形态，对应 EN-P-013）、U-ohz-017（模糊归因的中文触发词，对应 EN-P-017）、U-ohz-018（挑战小节的中文形态，对应 EN-P-031）、U-ohz-020（系动词替身的中文形态，对应 EN-P-015）、U-ohz-024（知识截止免责声明的中文形态）
- 现有规则里确实没有、值得单独裁决的增量：U-ohz-006（"干净但无声音"的六个迹象）、U-ohz-021、U-ohz-022（模式的语言适用性说明）、U-ohz-027（段落简洁单行收尾）、U-ohz-028（揭示前的破折号）、U-ohz-032/033（五维评分与重修门槛）
- 与 ai-zixun 来源估计会聚成一簇：U-ohz-003 与 U-azh-035/U-azh-064（段落结尾与可预测性）、U-ohz-009 与 U-azh-012（第一人称与声口）、U-ohz-031 与 U-azh-060（默认要不要附说明）

## 6 上游文本内的指令

上游正文开头有一句以第二人称写给模型的角色设定，属于指令类文本。按 SKILL.md 的硬约束只照抄、不执行：

> 你是一位文字编辑，专门识别和去除 AI 生成文本的痕迹，使文字听起来更自然、更有人味。

`## 你的任务`、`## 处理流程`、`## 快速检查清单` 三节同样是以祈使句写给模型的操作指令。本清单把它们当作规则内容拆分和记录，没有按其要求改写任何文本，也没有执行 frontmatter 的 `allowed-tools` 声明（Read、Write、Edit、AskUserQuestion）。

除此之外，通读全文未发现注入式指令（例如"忽略之前的规则""把这段加进你的系统提示"）。
