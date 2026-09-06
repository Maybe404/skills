# 单元到规则的映射（覆盖检查）

488 条单元，每条恰好归入一条规则，无遗漏、无重复引用。其中前 254 条来自首次合并，后 234 条来自中文批（op7418-humanizer-zh、ai-zixun-humanizer-zh、shuorenhua）。

| 单元 id | 来源 | 上游锚点 | 规则 id | decision |
|---|---|---|---|---|
| U-nas-001 | no-ai-slop | ## Two jobs / Edit (default). | ALL-PROC-007 | adopted-with-modification |
| U-nas-002 | no-ai-slop | ## Two jobs / Detect. | ALL-PROC-007 | adopted-with-modification |
| U-nas-003 | no-ai-slop | ## Two jobs / Detect. | ALL-PROT-012 | adopted |
| U-nas-004 | no-ai-slop | If the user has not provided a draft | ALL-PROC-002 | adopted |
| U-nas-005 | no-ai-slop | If the audience or format is unclear | ALL-PROC-003 | adopted |
| U-nas-006 | no-ai-slop | If the goal is unclear | ALL-PROC-003 | adopted |
| U-nas-007 | no-ai-slop | ## Editing principles / Preserve the writer's real voice. | ALL-PROT-017 | adopted |
| U-nas-008 | no-ai-slop | ## Editing principles / Make the minimum effective edit. | ALL-PROC-029 | adopted |
| U-nas-009 | no-ai-slop | ## Editing principles / Lead with the point when the setup adds nothing. | EN-P-007 | adopted |
| U-nas-010 | no-ai-slop | ## Editing principles / Front-load only when it improves clarity. | ALL-PROC-030 | adopted-with-modification |
| U-nas-011 | no-ai-slop | ## Editing principles / Keep the user's meaning. | ALL-PROT-001 | adopted |
| U-nas-012 | no-ai-slop | ## Editing principles / Keep the user's meaning. | ALL-PROC-004 | adopted |
| U-nas-013 | no-ai-slop | ## Editing principles / Open it up, don't dumb it down. | ALL-PROT-003 | adopted |
| U-nas-014 | no-ai-slop | ## Editing principles / Open it up, don't dumb it down. | ALL-P-010 | adopted |
| U-nas-015 | no-ai-slop | ## Editing principles / Use active voice. | ALL-P-004 | adopted |
| U-nas-016 | no-ai-slop | ## Editing principles / Make every sentence earn its place. | EN-P-003 | adopted |
| U-nas-017 | no-ai-slop | ## Editing principles / Untangle sentences without flattening the cadence. | ALL-P-006 | adopted |
| U-nas-018 | no-ai-slop | ## Editing principles / Be concrete and specific. | ALL-P-007 | adopted |
| U-nas-019 | no-ai-slop | ## Editing principles / Use the portability test. | ALL-M-001 | adopted |
| U-nas-020 | no-ai-slop | ## Editing principles / Always show, don't tell the reader what to think. | EN-P-022 | adopted |
| U-nas-021 | no-ai-slop | ## Editing principles / Protect the specific fact. | ALL-PROT-002 | adopted |
| U-nas-022 | no-ai-slop | ## Editing principles / Make verbs do the work. | EN-P-016 | adopted |
| U-nas-023 | no-ai-slop | ## Editing principles / Know the job. | ALL-PROC-001 | adopted |
| U-nas-024 | no-ai-slop | ## Editing principles / Preserve useful edge and character. | ALL-PROT-017 | adopted |
| U-nas-025 | no-ai-slop | ## Editing principles / Keep structure unless it's hurting the piece. | ALL-PROC-030 | adopted-with-modification |
| U-nas-026 | no-ai-slop | ## Editing principles / Keep structure unless it's hurting the piece. | ALL-PROC-008 | adopted-with-modification |
| U-nas-027 | no-ai-slop | ## Words to cut / Banned outright | EN-P-001 | adopted |
| U-nas-028 | no-ai-slop | ## Words to cut / Often-empty adverbs | EN-P-003 | adopted |
| U-nas-029 | no-ai-slop | ## Words to cut / Often-empty phrases | EN-P-004 | adopted |
| U-nas-030 | no-ai-slop | ## Patterns to cut / Binary contrasts. | EN-P-006 | adopted |
| U-nas-031 | no-ai-slop | ## Patterns to cut / Throat-clearing openers. | EN-P-007 | adopted |
| U-nas-032 | no-ai-slop | ## Patterns to cut / Faux-insight setups. | EN-P-008 | adopted |
| U-nas-033 | no-ai-slop | ## Patterns to cut / Colon reveals. | EN-P-010 | adopted |
| U-nas-034 | no-ai-slop | ## Patterns to cut / Colon reveals. | EN-P-011 | adopted |
| U-nas-035 | no-ai-slop | ## Patterns to cut / Superficial analysis. | EN-P-013 | adopted |
| U-nas-036 | no-ai-slop | ## Patterns to cut / Importance puffery. | EN-P-014 | adopted |
| U-nas-037 | no-ai-slop | ## Patterns to cut / Interpretive metadiscourse. | EN-P-022 | adopted |
| U-nas-038 | no-ai-slop | ## Patterns to cut / Weasel attribution. | EN-P-017 | adopted |
| U-nas-039 | no-ai-slop | ## Patterns to cut / Weasel attribution. | ALL-PROT-001 | adopted |
| U-nas-040 | no-ai-slop | ## Patterns to cut / Fake-strong verbs. | EN-P-015 | adopted |
| U-nas-041 | no-ai-slop | ## Patterns to cut / Synonym cycling. | EN-P-019 | adopted |
| U-nas-042 | no-ai-slop | ## Patterns to cut / Negative listing. | EN-P-006 | adopted |
| U-nas-043 | no-ai-slop | ## Patterns to cut / Dramatic fragmentation. | EN-P-025 | adopted |
| U-nas-044 | no-ai-slop | ## Patterns to cut / Robotic rhythm. | ALL-P-001 | adopted-with-modification |
| U-nas-045 | no-ai-slop | ## Patterns to cut / Rhetorical setups. | EN-P-009 | adopted |
| U-nas-046 | no-ai-slop | ## Patterns to cut / Fake-profound kickers. | EN-P-024 | adopted |
| U-nas-047 | no-ai-slop | ## Patterns to cut / Summary-recap endings. | EN-P-023 | adopted |
| U-nas-048 | no-ai-slop | ## Patterns to cut / Formatting slop. | ALL-P-002 | adopted |
| U-nas-049 | no-ai-slop | ## Patterns to cut / Em dashes. | EN-P-026 | adopted-with-modification |
| U-nas-050 | no-ai-slop | ## Workflow / 1. Read the full draft before editing. | ALL-PROC-009 | adopted |
| U-nas-051 | no-ai-slop | ## Workflow / 2. Identify the core point | ALL-PROC-001 | adopted |
| U-nas-052 | no-ai-slop | ## Workflow / 3. For a detect request | ALL-PROC-007 | adopted-with-modification |
| U-nas-053 | no-ai-slop | ## Workflow / 4. For an edit | ALL-PROC-014 | adopted-with-modification |
| U-nas-054 | no-ai-slop | ## Workflow / 5. If any check fails | ALL-PROC-014 | adopted-with-modification |
| U-nas-055 | no-ai-slop | ## Workflow / 6. Output the full edited draft | ALL-PROC-008 | adopted-with-modification |
| U-qaw-001 | qu-ai-wei | Rewrite and humanize Simplifie | ALL-G-001 | adopted-with-modification |
| U-qaw-002 | qu-ai-wei | ## 能力边界 | ALL-PROT-012 | adopted |
| U-qaw-003 | qu-ai-wei | 把一段话、一篇文章或更长内容改成符合目标语体的自然简体中文 | ALL-PROC-012 | adopted-with-modification |
| U-qaw-004 | qu-ai-wei | 除非用户或调用方明确说 | ALL-PROC-021 | adopted-with-modification |
| U-qaw-005 | qu-ai-wei | 处理正文前先做敏感信息门检 | ALL-PROT-011 | adopted |
| U-qaw-006 | qu-ai-wei | ## 仲裁顺序 | ALL-PROC-023 | adopted |
| U-qaw-007 | qu-ai-wei | 不得为了顺口补写事实 | ALL-PROT-001 | adopted |
| U-qaw-008 | qu-ai-wei | 不得把不确定说成确定 | ALL-PROT-004 | adopted-with-modification |
| U-qaw-009 | qu-ai-wei | 也不得把相关性升级成因果 | ALL-PROT-005 | adopted-with-modification |
| U-qaw-010 | qu-ai-wei | 不得把排除关系改成更强的正面事实 | ALL-PROT-006 | adopted-with-modification |
| U-qaw-011 | qu-ai-wei | 不得从症状自行推出解决方案 | ALL-PROT-007 | adopted-with-modification |
| U-qaw-012 | qu-ai-wei | ## 确定授权与幅度 | ALL-PROC-005 | adopted |
| U-qaw-013 | qu-ai-wei | 用户给出的具体范围高于上述默认值 | ALL-PROC-005 | adopted |
| U-qaw-014 | qu-ai-wei | 先检查自纠、犹疑、自嘲、方言 | ALL-PROC-006 | adopted |
| U-qaw-015 | qu-ai-wei | 只有用户仅提供文本、没有给出任何编辑指令时 | ALL-PROC-006 | adopted |
| U-qaw-016 | qu-ai-wei | 授权编辑不等于全面换声口 | ALL-PROT-017 | adopted |
| U-qaw-017 | qu-ai-wei | 授权编辑也不等于目标语体已经明确 | ALL-PROC-003 | adopted |
| U-qaw-018 | qu-ai-wei | 命中「真人文本（停手）」时立即结束 | ALL-PROC-022 | adopted |
| U-qaw-019 | qu-ai-wei | 停手说明只写一句授权结论 | ALL-PROC-022 | adopted |
| U-qaw-020 | qu-ai-wei | 真实引语、代码、公式、法律条款、标准定义、专名、引用标识 | ALL-PROT-008 | adopted |
| U-qaw-021 | qu-ai-wei | 无法确认真伪的引语不擅自改写 | ALL-PROT-008 | adopted |
| U-qaw-022 | qu-ai-wei | ## 选择输出模式 | ALL-PROC-008 | adopted-with-modification |
| U-qaw-023 | qu-ai-wei | 内嵌模式（embedded mode） | ALL-PROC-021 | adopted-with-modification |
| U-qaw-024 | qu-ai-wei | 内嵌模式不降低约束 | ALL-PROC-021 | adopted-with-modification |
| U-qaw-025 | qu-ai-wei | 普通模式的门检只说明编辑状态，不鉴定作者 | ALL-PROC-024 | adopted-with-modification |
| U-qaw-026 | qu-ai-wei | 至多两条具体结构 | ALL-PROC-024 | adopted-with-modification |
| U-qaw-027 | qu-ai-wei | ### 1. 冻结不可丢失内容 | ALL-PROT-019 | adopted-with-modification |
| U-qaw-028 | qu-ai-wei | ### 1. 冻结不可丢失内容 | ALL-PROT-019 | adopted-with-modification |
| U-qaw-029 | qu-ai-wei | ### 1. 冻结不可丢失内容 | ALL-PROC-009 | adopted |
| U-qaw-030 | qu-ai-wei | 不得分别润色孤立段落再拼成全文 | ALL-PROC-009 | adopted |
| U-qaw-031 | qu-ai-wei | ### 2. 扫描八个模式族 | ALL-PROC-010 | adopted-with-modification |
| U-qaw-032 | qu-ai-wei | 语体只调整触发阈值和改写幅度 | ALL-PROC-010 | adopted-with-modification |
| U-qaw-033 | qu-ai-wei | ### 3. 重建信息架构 | ALL-PROC-011 | adopted |
| U-qaw-034 | qu-ai-wei | 允许： | ALL-PROC-012 | adopted-with-modification |
| U-qaw-035 | qu-ai-wei | 移动引用及其支持的陈述 | ALL-PROT-010 | adopted |
| U-qaw-036 | qu-ai-wei | 不要默认摘要 | ALL-PROT-003 | adopted |
| U-qaw-037 | qu-ai-wei | 显眼的对称骨架要重建，不做同义换壳 | ALL-P-005 | adopted |
| U-qaw-038 | qu-ai-wei | 真实引语、固定表述或改变外壳会造成歧义时保留 | ALL-PROT-009 | adopted |
| U-qaw-039 | qu-ai-wei | 显眼的对称骨架要重建，不做同义换壳 | ALL-PROC-028 | adopted-with-modification |
| U-qaw-040 | qu-ai-wei | ### 4. 按简体中文重写 | ALL-P-004 | adopted |
| U-qaw-041 | qu-ai-wei | ### 4. 按简体中文重写 | ZH-P-009 | adopted-with-modification |
| U-qaw-042 | qu-ai-wei | ### 4. 按简体中文重写 | ZH-P-008 | adopted |
| U-qaw-043 | qu-ai-wei | ### 4. 按简体中文重写 | ALL-P-001 | adopted-with-modification |
| U-qaw-044 | qu-ai-wei | ### 4. 按简体中文重写 | ALL-P-006 | adopted |
| U-qaw-045 | qu-ai-wei | ### 4. 按简体中文重写 | ZH-P-001 | adopted |
| U-qaw-046 | qu-ai-wei | 但保留真实关系、必要术语及正式程度 | ALL-PROT-020 | adopted |
| U-qaw-047 | qu-ai-wei | 不要为了“人味”添加错别字、emoji、网语 | ALL-PROT-018 | adopted |
| U-qaw-048 | qu-ai-wei | ### 5. 处理逻辑风险 | ALL-P-009 | adopted |
| U-qaw-049 | qu-ai-wei | 不静默替作者纠正 | ALL-PROT-014 | adopted |
| U-qaw-050 | qu-ai-wei | 能自然保义：保留原主张 | ALL-PROC-013 | adopted |
| U-qaw-051 | qu-ai-wei | 无法自然保留而不继续误导：暂停并请求作者确认 | ALL-PROC-013 | adopted |
| U-qaw-052 | qu-ai-wei | 默认只检查文内一致性和引用绑定 | ALL-PROT-015 | adopted |
| U-qaw-053 | qu-ai-wei | ### 6. 全文复扫 | ALL-PROC-014 | adopted-with-modification |
| U-qaw-054 | qu-ai-wei | ### 6. 全文复扫 | ALL-PROT-019 | adopted-with-modification |
| U-qaw-055 | qu-ai-wei | ### 6. 全文复扫 | ALL-PROT-010 | adopted |
| U-qaw-056 | qu-ai-wei | ### 6. 全文复扫 | ALL-PROC-014 | adopted-with-modification |
| U-qaw-057 | qu-ai-wei | ### 6. 全文复扫 | ALL-P-001 | adopted-with-modification |
| U-qaw-058 | qu-ai-wei | 改动是否带来可验证改善 | ALL-PROC-029 | adopted |
| U-qaw-059 | qu-ai-wei | ## 长文与不完整输入 | ALL-PROC-015 | adopted |
| U-qaw-060 | qu-ai-wei | 缺失部分会影响事实、指代或论证关系时 | ALL-PROC-004 | adopted |
| U-qaw-061 | qu-ai-wei | 不得把阶段稿称为全文终稿 | ALL-PROT-016 | adopted |
| U-qaw-062 | qu-ai-wei | ## 输出契约 | ALL-PROC-008 | adopted-with-modification |
| U-qaw-063 | qu-ai-wei | ## 能力边界 | ALL-PROC-020 | adopted |
| U-qaw-064 | qu-ai-wei | ## 能力边界 | ALL-PROT-001 | adopted |
| U-qaw-065 | qu-ai-wei | ## 能力边界 | ALL-PROC-029 | adopted |
| U-wss-001 | writing-style-skill | 【0】Voice Dimensions（量化你的风格） | ALL-M-006 | reference-only |
| U-wss-002 | writing-style-skill | 【0】Voice Dimensions（量化你的风格） | ALL-M-007 | reference-only |
| U-wss-003 | writing-style-skill | 【1】角色与读者 | ALL-PROC-001 | adopted |
| U-wss-004 | writing-style-skill | 【2】写作规则 | ALL-PROC-032 | reference-only |
| U-wss-005 | writing-style-skill | 【3】格式规范 / ### 平台适配 | ALL-P-003 | adopted |
| U-wss-006 | writing-style-skill | 🔄 自动学习（内置） / ### 工作原理 | ALL-PROC-033 | deferred |
| U-wss-007 | writing-style-skill | 只需要两个数据点 | ALL-M-008 | deferred |
| U-wss-008 | writing-style-skill | observe.py / record_final 里对 original 与 final 内容是否一致的判断 | ALL-M-009 | deferred |
| U-wss-009 | writing-style-skill | observe.py / compute_hash | ALL-M-010 | rejected |
| U-wss-010 | writing-style-skill | improve.py / extract_improvements 里给提炼环节设定的采纳门槛 | ALL-M-011 | deferred |
| U-wss-011 | writing-style-skill | improve.py / extract_improvements 里给提炼环节设定的采纳门槛 | ALL-M-012 | rejected |
| U-wss-012 | writing-style-skill | improve.py / extract_improvements 里给提炼环节设定的采纳门槛 | ALL-M-013 | duplicate |
| U-wss-013 | writing-style-skill | 规则分级 | ALL-M-014 | rejected |
| U-wss-014 | writing-style-skill | 安全 | ALL-PROC-034 | rejected |
| U-wss-015 | writing-style-skill | observe.py / record_final 里的字数变化百分比计算 | ALL-M-015 | rejected |
| U-wss-016 | writing-style-skill | observe.py / show_stats | ALL-M-016 | rejected |
| U-abh-001 | aboudjem-humanizer | ## Quick reference / Modes | ALL-PROC-007 | adopted-with-modification |
| U-abh-002 | aboudjem-humanizer | ## Step 1: Parse Arguments / --voice | ALL-PROC-031 | duplicate |
| U-abh-003 | aboudjem-humanizer | ### Voice Profiles / casual | EN-S-001 | reference-only |
| U-abh-004 | aboudjem-humanizer | ### Voice Profiles / professional | EN-S-001 | reference-only |
| U-abh-005 | aboudjem-humanizer | ### Voice Profiles / technical | EN-S-001 | reference-only |
| U-abh-006 | aboudjem-humanizer | ### Voice Profiles / warm | EN-S-001 | reference-only |
| U-abh-007 | aboudjem-humanizer | ### Voice Profiles / blunt | EN-S-001 | reference-only |
| U-abh-008 | aboudjem-humanizer | ## Quick reference / Flags / --score | ALL-M-005 | rejected |
| U-abh-009 | aboudjem-humanizer | ## Step 1: Parse Arguments / --aggressive | ALL-PROC-027 | duplicate |
| U-abh-010 | aboudjem-humanizer | ## Step 1: Parse Arguments / --purpose | ALL-G-002 | adopted-with-modification |
| U-abh-011 | aboudjem-humanizer | ## Quick reference / Flags / --ignore-code | ALL-PROC-016 | adopted |
| U-abh-012 | aboudjem-humanizer | ## Step 1: Parse Arguments / Auto-load brand context | ALL-PROC-025 | adopted-with-modification |
| U-abh-013 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / A single em dash, curly quote, or tidy sentence alone means nothing. | ALL-M-002 | adopted |
| U-abh-014 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Perfect grammar is not AI. | ALL-M-002 | adopted |
| U-abh-015 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives) | ALL-PROT-008 | adopted |
| U-abh-016 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives) | ALL-PROT-009 | adopted |
| U-abh-017 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / What NOT to flag (false positives) | ALL-M-003 | adopted-with-modification |
| U-abh-018 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Consistent, formulaic structure alone is not proof of AI. | ALL-M-002 | adopted |
| U-abh-019 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Formal or non-native-English prose is not proof of AI either. | ALL-M-002 | adopted |
| U-abh-020 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these) | ALL-PROT-002 | adopted |
| U-abh-021 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these) | ALL-PROT-017 | adopted |
| U-abh-022 | aboudjem-humanizer | ## Guardrails: what NOT to flag, and what to preserve / Signs of human writing (preserve these) | ALL-PROT-013 | adopted-with-modification |
| U-abh-023 | aboudjem-humanizer | ## Operating principles / No fabrication | ALL-PROT-001 | adopted |
| U-abh-024 | aboudjem-humanizer | ## Operating principles | ALL-S-001 | rejected |
| U-abh-025 | aboudjem-humanizer | ## Step 1: Parse Arguments / Text | ALL-PROC-002 | adopted |
| U-abh-026 | aboudjem-humanizer | ## Step 1: Parse Arguments / --openings N | ALL-PROC-026 | reference-only |
| U-abh-027 | aboudjem-humanizer | ### CONTENT PATTERNS / P1: Significance Inflation | EN-P-014 | adopted |
| U-abh-028 | aboudjem-humanizer | ### CONTENT PATTERNS / P2: Notability Name-Dropping | EN-P-018 | adopted |
| U-abh-029 | aboudjem-humanizer | ### CONTENT PATTERNS / P3: Superficial -ing Phrases | EN-P-013 | adopted |
| U-abh-030 | aboudjem-humanizer | ### CONTENT PATTERNS / P4: Promotional Language | EN-P-002 | adopted |
| U-abh-031 | aboudjem-humanizer | ### CONTENT PATTERNS / P5: Vague Attributions | EN-P-017 | adopted |
| U-abh-032 | aboudjem-humanizer | ### CONTENT PATTERNS / P6: Formulaic Challenges Sections | EN-P-031 | adopted |
| U-abh-033 | aboudjem-humanizer | ### CONTENT PATTERNS / P7: AI Vocabulary Words | EN-P-001 | adopted |
| U-abh-034 | aboudjem-humanizer | ### CONTENT PATTERNS / P8: Copula Avoidance | EN-P-015 | adopted |
| U-abh-035 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P9: Negative Parallelisms | EN-P-006 | adopted |
| U-abh-036 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P10: Rule of Three | ALL-P-005 | adopted |
| U-abh-037 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P11: Synonym Cycling (Elegant Variation) | EN-P-019 | adopted |
| U-abh-038 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P12: False Ranges | EN-P-021 | adopted |
| U-abh-039 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P13: Em Dash Ban | EN-P-026 | adopted-with-modification |
| U-abh-040 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P14: Boldface/Formatting Overuse | ALL-P-002 | adopted |
| U-abh-041 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P15: Structured List Syndrome | ALL-P-002 | adopted |
| U-abh-042 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P16: Title Case in Headings | EN-P-012 | adopted |
| U-abh-043 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P17: Curly Quotes and Typographic Tells | EN-P-037 | adopted-with-modification |
| U-abh-044 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P18: Formal Register Overuse | EN-P-005 | adopted |
| U-abh-045 | aboudjem-humanizer | ### COMMUNICATION PATTERNS / P19: Chatbot Artifacts | EN-P-028 | adopted |
| U-abh-046 | aboudjem-humanizer | ### COMMUNICATION PATTERNS / P20: Knowledge-Cutoff Disclaimers | EN-P-028 | adopted |
| U-abh-047 | aboudjem-humanizer | ### COMMUNICATION PATTERNS / P21: Sycophantic Tone | EN-P-028 | adopted |
| U-abh-048 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P22: Filler Phrases | EN-P-004 | adopted |
| U-abh-049 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P23: Excessive Hedging | EN-P-029 | adopted |
| U-abh-050 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P24: Generic Positive Conclusions | EN-P-023 | adopted |
| U-abh-051 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P25: Hallucination Markers | EN-P-039 | adopted-with-modification |
| U-abh-052 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P26: Perfect/Error Alternation | EN-P-040 | adopted-with-modification |
| U-abh-053 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P27: Question-Format Section Titles | EN-P-032 | adopted |
| U-abh-054 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P28: Markdown Bleeding | ALL-P-003 | adopted |
| U-abh-055 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P29: The "Comprehensive Overview" Opening | EN-P-007 | adopted |
| U-abh-056 | aboudjem-humanizer | ### FILLER & HEDGING PATTERNS / P30: Uniform Sentence Length | ALL-P-001 | adopted-with-modification |
| U-abh-057 | aboudjem-humanizer | ### EMERGING PATTERNS / P31: Elegant Variation (Noun-Phrase Cycling) | EN-P-020 | adopted |
| U-abh-058 | aboudjem-humanizer | ### EMERGING PATTERNS / P32: Collaborative Communication Leaking | EN-P-007 | adopted |
| U-abh-059 | aboudjem-humanizer | ### EMERGING PATTERNS / P33: Placeholder Text / Mad Libs | EN-P-038 | adopted |
| U-abh-060 | aboudjem-humanizer | ### EMERGING PATTERNS / P34: Chatbot Reference Markup Leaking | EN-P-038 | adopted |
| U-abh-061 | aboudjem-humanizer | ### EMERGING PATTERNS / P35: UTM Source Parameters from AI Tools | EN-P-038 | adopted |
| U-abh-062 | aboudjem-humanizer | ### EMERGING PATTERNS / P36: Sudden Style/Register Shift | EN-P-040 | adopted-with-modification |
| U-abh-063 | aboudjem-humanizer | ### EMERGING PATTERNS / P37: Overattribution / Source-Listing as Content | EN-P-018 | adopted |
| U-abh-064 | aboudjem-humanizer | ### EMERGING PATTERNS / P38: Paragraph-Reshuffling Immunity | ALL-P-008 | adopted |
| U-abh-065 | aboudjem-humanizer | ### EMERGING PATTERNS / P39: Paragraph-Closing "Whether" Summaries | EN-P-023 | adopted |
| U-abh-066 | aboudjem-humanizer | ### EMERGING PATTERNS / P40: Symbolic Gloss / Meaning-Telling | EN-P-014 | adopted |
| U-abh-067 | aboudjem-humanizer | ### EMERGING PATTERNS / P41: Infomercial Engagement Hooks | EN-P-009 | adopted |
| U-abh-068 | aboudjem-humanizer | ### EMERGING PATTERNS / P42: Erratic Inline Bolding | ALL-P-002 | adopted |
| U-abh-069 | aboudjem-humanizer | ### EMERGING PATTERNS / P43: The Treadmill Effect (Low Information Density) | ALL-P-011 | adopted |
| U-abh-070 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P44: False Agency | ALL-P-004 | adopted |
| U-abh-071 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P45: Narrator-from-a-Distance | EN-P-034 | reference-only |
| U-abh-072 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P46: Diff-Anchored Writing | EN-P-035 | adopted-with-modification |
| U-abh-073 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P47: Hyphenated-Pair Overuse | EN-P-036 | adopted |
| U-abh-074 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P48: Aphorism Formulas | EN-P-024 | adopted |
| U-abh-075 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P49: Fragmented Headers | EN-P-033 | adopted |
| U-abh-076 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P50: Passive / Subjectless Constructions | ALL-P-004 | adopted |
| U-abh-077 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P51: Reasoning-Chain Artifacts | EN-P-038 | adopted |
| U-abh-078 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P52: Unicode Obfuscation | EN-P-042 | adopted-with-modification |
| U-abh-079 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P53: Hedged-Enumeration Openers | EN-P-007 | adopted |
| U-abh-080 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P54: Argument Residue | EN-P-041 | adopted |
| U-abh-081 | aboudjem-humanizer | ### CRAFT AND FORENSIC PATTERNS / P55: Leftover Hedge Debris | EN-P-030 | adopted-with-modification |
| U-abh-082 | aboudjem-humanizer | ### LANGUAGE & STYLE PATTERNS / P13: Em Dash Ban | EN-P-027 | adopted-with-modification |
| U-abh-083 | aboudjem-humanizer | ### Tiered-confidence vocabulary (refines P7) | EN-M-001 | adopted-with-modification |
| U-abh-084 | aboudjem-humanizer | ### The Burstiness Principle | ALL-P-001 | adopted-with-modification |
| U-abh-085 | aboudjem-humanizer | ### The Perplexity Principle | EN-S-003 | rejected |
| U-abh-086 | aboudjem-humanizer | ## Step 3: Rewrite Craft / Voice Read | ALL-PROC-001 | adopted |
| U-abh-087 | aboudjem-humanizer | ## Step 3: Rewrite Craft / Anti-Default Discipline | ALL-PROC-018 | adopted |
| U-abh-088 | aboudjem-humanizer | ## Step 3: Rewrite Craft / Position engine (give it teeth) | ALL-S-002 | reference-only |
| U-abh-089 | aboudjem-humanizer | ## Step 3: Rewrite Craft / Concretizer pass | ALL-P-007 | adopted |
| U-abh-090 | aboudjem-humanizer | ### Soul Injection Techniques / Have actual opinions. | EN-S-002 | reference-only |
| U-abh-091 | aboudjem-humanizer | ### Soul Injection Techniques / Calibrate certainty on a spectrum, don't just hedge. | EN-S-002 | reference-only |
| U-abh-092 | aboudjem-humanizer | ### Soul Injection Techniques / Reference shared human experiences. | EN-S-002 | reference-only |
| U-abh-093 | aboudjem-humanizer | ### Soul Injection Techniques / Allow tangents and asides. | EN-S-002 | reference-only |
| U-abh-094 | aboudjem-humanizer | ### Soul Injection Techniques / Use the "imperfect start" technique. | EN-S-002 | reference-only |
| U-abh-095 | aboudjem-humanizer | ### Soul Injection Techniques / Use callbacks. | EN-S-002 | reference-only |
| U-abh-096 | aboudjem-humanizer | ### Soul Injection Techniques / Self-correct. | EN-S-002 | reference-only |
| U-abh-097 | aboudjem-humanizer | ### Mode: `detect` | ALL-PROC-007 | adopted-with-modification |
| U-abh-098 | aboudjem-humanizer | ### Mode: `detect` / Severity: HIGH (8+ patterns = heavy AI smell) | ALL-M-005 | rejected |
| U-abh-099 | aboudjem-humanizer | ### Mode: `rewrite` | ALL-PROC-007 | adopted-with-modification |
| U-abh-100 | aboudjem-humanizer | ### Mode: `rewrite` / Verify the rewrite: | ALL-PROC-014 | adopted-with-modification |
| U-abh-101 | aboudjem-humanizer | ### Mode: `edit` / Refuse non-prose targets. | ALL-PROC-017 | adopted |
| U-abh-102 | aboudjem-humanizer | ### Mode: `edit` / If patterns found: apply fixes with the Edit tool | ALL-PROC-029 | adopted |
| U-abh-103 | aboudjem-humanizer | ## Step 5: Final Quality Check | ALL-PROC-014 | adopted-with-modification |
| U-abh-104 | aboudjem-humanizer | ### Draft, self-audit, final (cheap quality pass, distinct from `--iterate`) | ALL-PROC-014 | adopted-with-modification |
| U-abh-105 | aboudjem-humanizer | ### Scoring rubric (used when `--score` is set) | ALL-M-005 | rejected |
| U-abh-106 | aboudjem-humanizer | ### Scoring rubric (used when `--score` is set) / A model grading its own output in the same session | ALL-M-004 | adopted |
| U-abh-107 | aboudjem-humanizer | ### Iterate handling (used when `--iterate N` is set) | ALL-PROC-019 | adopted-with-modification |
| U-abh-108 | aboudjem-humanizer | ## Honest limits of this catalog | ALL-G-003 | adopted |
| U-abh-109 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH1 | ZH-P-002 | adopted |
| U-abh-110 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH2 | ZH-P-003 | adopted |
| U-abh-111 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH3 | ZH-P-004 | adopted |
| U-abh-112 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH4 | ZH-P-001 | adopted |
| U-abh-113 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH5 | ZH-P-007 | adopted |
| U-abh-114 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH6 | ZH-P-005 | adopted |
| U-abh-115 | aboudjem-humanizer | ## 核心原生模式 · Core native tells (ZH1–ZH7) / ZH7 | ZH-P-006 | adopted |
| U-abh-116 | aboudjem-humanizer | ## 未验证假设 · Unverified hypotheses (ZH13–ZH14) / ZH13 | ZH-P-010 | unverified |
| U-abh-117 | aboudjem-humanizer | ## 未验证假设 · Unverified hypotheses (ZH13–ZH14) / ZH14 | ZH-P-011 | adopted-with-modification |
| U-abh-118 | aboudjem-humanizer | ## ⚠️ 实验性 · PROVISIONAL — 请先读这里 | ZH-M-001 | adopted |
| U-azh-001 | ai-zixun-humanizer-zh | description: Remove signs of AI-generated | ALL-G-001 | adopted-with-modification |
| U-azh-002 | ai-zixun-humanizer-zh | ## Overview | ZH-PROC-002 | adopted-with-modification |
| U-azh-003 | ai-zixun-humanizer-zh | ## Overview | ALL-PROT-003 | adopted |
| U-azh-004 | ai-zixun-humanizer-zh | 1. 先判断文本类型 | ALL-G-002 | adopted-with-modification |
| U-azh-005 | ai-zixun-humanizer-zh | 2. 先看文章主线 | ALL-PROC-011 | adopted |
| U-azh-006 | ai-zixun-humanizer-zh | 3. 先找最显眼的 AI 痕迹 | ZH-PROC-002 | adopted-with-modification |
| U-azh-007 | ai-zixun-humanizer-zh | 4. 再决定改写力度 | ALL-PROC-005 | adopted |
| U-azh-008 | ai-zixun-humanizer-zh | 5. 保留作者原意 | ALL-PROT-001 | adopted |
| U-azh-009 | ai-zixun-humanizer-zh | 5. 保留作者原意 | ALL-PROT-004 | adopted-with-modification |
| U-azh-010 | ai-zixun-humanizer-zh | 5. 保留作者原意 | ZH-PROT-001 | adopted |
| U-azh-011 | ai-zixun-humanizer-zh | 6. 做最后一遍朗读检查 | ZH-M-003 | reference-only |
| U-azh-012 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROT-017 | adopted |
| U-azh-013 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-014 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-028 | adopted-with-modification |
| U-azh-015 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-016 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-017 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-018 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-019 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-020 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROT-017 | adopted |
| U-azh-021 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-P-012 | adopted |
| U-azh-022 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROT-021 | adopted |
| U-azh-023 | ai-zixun-humanizer-zh | ## Voice Adoption（可选） | ALL-PROC-036 | rejected |
| U-azh-024 | ai-zixun-humanizer-zh | ### 1. 优先改掉翻译腔 | ZH-P-011 | adopted-with-modification |
| U-azh-025 | ai-zixun-humanizer-zh | ### 1. 优先改掉翻译腔 | ZH-P-011 | adopted-with-modification |
| U-azh-026 | ai-zixun-humanizer-zh | ### 1. 优先改掉翻译腔 | ZH-P-024 | adopted |
| U-azh-027 | ai-zixun-humanizer-zh | ### 2. 去掉空泛的大词和套话 | ZH-P-001 | adopted |
| U-azh-028 | ai-zixun-humanizer-zh | ### 2. 去掉空泛的大词和套话 | ZH-P-015 | adopted |
| U-azh-029 | ai-zixun-humanizer-zh | ### 2. 去掉空泛的大词和套话 | ALL-P-007 | adopted |
| U-azh-030 | ai-zixun-humanizer-zh | ### 3. 打散机械结构 | ALL-P-005 | adopted |
| U-azh-031 | ai-zixun-humanizer-zh | ### 3. 打散机械结构 | ZH-P-003 | adopted |
| U-azh-032 | ai-zixun-humanizer-zh | ### 3. 打散机械结构 | ALL-P-002 | adopted |
| U-azh-033 | ai-zixun-humanizer-zh | ### 4. 保持中文节奏 | ALL-P-001 | adopted-with-modification |
| U-azh-034 | ai-zixun-humanizer-zh | ### 4. 保持中文节奏 | ALL-P-004 | adopted |
| U-azh-035 | ai-zixun-humanizer-zh | ### 4. 保持中文节奏 | ZH-P-006 | adopted |
| U-azh-036 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ZH-PROC-003 | adopted |
| U-azh-037 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ALL-PROC-011 | adopted |
| U-azh-038 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ALL-P-008 | adopted |
| U-azh-039 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ZH-PROC-003 | adopted |
| U-azh-040 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ALL-PROC-030 | adopted-with-modification |
| U-azh-041 | ai-zixun-humanizer-zh | ### 5. 管住文章级结构 | ZH-P-003 | adopted |
| U-azh-042 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-P-025 | adopted-with-modification |
| U-azh-043 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-S-002 | rejected |
| U-azh-044 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-P-026 | adopted-with-modification |
| U-azh-045 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-S-003 | reference-only |
| U-azh-046 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-S-003 | reference-only |
| U-azh-047 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-S-003 | reference-only |
| U-azh-048 | ai-zixun-humanizer-zh | ### 6. 处理标点和排版 | ZH-PROT-002 | adopted-with-modification |
| U-azh-049 | ai-zixun-humanizer-zh | ### 7. 统一常见术语和日期 | ZH-S-004 | reference-only |
| U-azh-050 | ai-zixun-humanizer-zh | ### 7. 统一常见术语和日期 | ZH-S-005 | rejected |
| U-azh-051 | ai-zixun-humanizer-zh | ### 7. 统一常见术语和日期 | ZH-S-004 | reference-only |
| U-azh-052 | ai-zixun-humanizer-zh | ### 7. 统一常见术语和日期 | ZH-S-004 | reference-only |
| U-azh-053 | ai-zixun-humanizer-zh | ### 8. 控制判断强度 | ALL-PROT-014 | adopted |
| U-azh-054 | ai-zixun-humanizer-zh | ### 8. 控制判断强度 | ALL-PROT-001 | adopted |
| U-azh-055 | ai-zixun-humanizer-zh | ### 8. 控制判断强度 | ALL-P-007 | adopted |
| U-azh-056 | ai-zixun-humanizer-zh | ## Repo Overrides | ALL-PROC-025 | adopted-with-modification |
| U-azh-057 | ai-zixun-humanizer-zh | ## Repo Overrides | ALL-PROC-037 | adopted |
| U-azh-058 | ai-zixun-humanizer-zh | ## Repo Overrides | ZH-P-025 | adopted-with-modification |
| U-azh-059 | ai-zixun-humanizer-zh | ## Repo Overrides | ZH-P-025 | adopted-with-modification |
| U-azh-060 | ai-zixun-humanizer-zh | ## Output | ALL-PROC-046 | rejected |
| U-azh-061 | ai-zixun-humanizer-zh | ## Output | ALL-PROC-038 | adopted |
| U-azh-062 | ai-zixun-humanizer-zh | ## Output | ALL-PROC-005 | adopted |
| U-azh-063 | ai-zixun-humanizer-zh | ## Final Check | ZH-PROC-003 | adopted |
| U-azh-064 | ai-zixun-humanizer-zh | ## Final Check | ZH-M-005 | adopted |
| U-azh-065 | ai-zixun-humanizer-zh | ## Final Check | ZH-M-004 | adopted |
| U-azh-066 | ai-zixun-humanizer-zh | ## Final Check | ALL-PROC-036 | rejected |
| U-ohz-001 | op7418-humanizer-zh | ## 你的任务 | ZH-PROC-001 | rejected |
| U-ohz-002 | op7418-humanizer-zh | ## 核心规则速查 | ZH-P-012 | rejected |
| U-ohz-003 | op7418-humanizer-zh | ## 核心规则速查 | ZH-P-013 | adopted |
| U-ohz-004 | op7418-humanizer-zh | ## 核心规则速查 | ZH-P-014 | adopted |
| U-ohz-005 | op7418-humanizer-zh | ## 核心规则速查 | ZH-P-002 | adopted |
| U-ohz-006 | op7418-humanizer-zh | ### 缺乏灵魂的写作迹象 | ZH-M-002 | reference-only |
| U-ohz-007 | op7418-humanizer-zh | ### 如何增加语调 | ZH-S-001 | rejected |
| U-ohz-008 | op7418-humanizer-zh | ### 如何增加语调 | ALL-PROT-017 | adopted |
| U-ohz-009 | op7418-humanizer-zh | ### 如何增加语调 | ALL-PROT-017 | adopted |
| U-ohz-010 | op7418-humanizer-zh | ### 如何增加语调 | ALL-PROC-030 | adopted-with-modification |
| U-ohz-011 | op7418-humanizer-zh | ### 如何增加语调 | ALL-P-007 | adopted |
| U-ohz-012 | op7418-humanizer-zh | ### 5. 模糊归因和含糊措辞 | ALL-PROT-001 | adopted |
| U-ohz-013 | op7418-humanizer-zh | ### 1. 过度强调意义、遗产和更广泛的趋势 | ZH-P-015 | adopted |
| U-ohz-014 | op7418-humanizer-zh | ### 2. 过度强调知名度和媒体报道 | ZH-P-016 | adopted |
| U-ohz-015 | op7418-humanizer-zh | ### 3. 以 -ing 结尾的肤浅分析 | ZH-P-017 | adopted |
| U-ohz-016 | op7418-humanizer-zh | ### 4. 宣传和广告式语言 | ZH-P-018 | adopted |
| U-ohz-017 | op7418-humanizer-zh | ### 5. 模糊归因和含糊措辞 | ZH-P-019 | adopted |
| U-ohz-018 | op7418-humanizer-zh | ### 6. 提纲式的 | ZH-P-020 | adopted |
| U-ohz-019 | op7418-humanizer-zh | ### 7. 过度使用的 | ZH-P-001 | adopted |
| U-ohz-020 | op7418-humanizer-zh | ### 8. 避免使用 | ZH-P-021 | adopted |
| U-ohz-021 | op7418-humanizer-zh | ### 16. 标题中的标题大写 | ZH-G-001 | adopted |
| U-ohz-022 | op7418-humanizer-zh | ### 18. 弯引号 | ZH-G-001 | adopted |
| U-ohz-023 | op7418-humanizer-zh | ### 19. 协作交流痕迹 | ZH-P-022 | adopted |
| U-ohz-024 | op7418-humanizer-zh | ### 20. 知识截止日期免责声明 | ZH-P-022 | adopted |
| U-ohz-025 | op7418-humanizer-zh | ### 22. 填充短语 | ZH-P-023 | adopted |
| U-ohz-026 | op7418-humanizer-zh | ## 快速检查清单 | ALL-P-001 | adopted-with-modification |
| U-ohz-027 | op7418-humanizer-zh | ## 快速检查清单 | ZH-P-013 | adopted |
| U-ohz-028 | op7418-humanizer-zh | ## 快速检查清单 | ZH-P-007 | adopted |
| U-ohz-029 | op7418-humanizer-zh | ## 快速检查清单 | ALL-P-011 | adopted |
| U-ohz-030 | op7418-humanizer-zh | ## 快速检查清单 | ZH-P-001 | adopted |
| U-ohz-031 | op7418-humanizer-zh | ## 输出格式 | ALL-PROC-046 | rejected |
| U-ohz-032 | op7418-humanizer-zh | ## 质量评分 | ALL-M-017 | reference-only |
| U-ohz-033 | op7418-humanizer-zh | ## 质量评分 | ALL-M-017 | reference-only |
| U-srh-001 | shuorenhua | ## When to use | ALL-G-001 | adopted-with-modification |
| U-srh-002 | shuorenhua | 这份 skill 不是敏感词替换器 | ALL-PROC-029 | adopted |
| U-srh-003 | shuorenhua | - 保留技术性。 | ALL-PROT-009 | adopted |
| U-srh-004 | shuorenhua | - 优先保信息，再谈风格。 | ALL-PROT-001 | adopted |
| U-srh-005 | shuorenhua | - 优先保信息，再谈风格。 | ALL-PROT-022 | adopted |
| U-srh-006 | shuorenhua | - 原文的量化表述有歧义时 | ALL-PROT-014 | adopted |
| U-srh-007 | shuorenhua | - 原文的量化表述有歧义时 | ALL-PROT-001 | adopted |
| U-srh-008 | shuorenhua | - 不用机械同义词替换表 | ALL-PROT-009 | adopted |
| U-srh-009 | shuorenhua | - 不用机械同义词替换表 | ALL-PROC-042 | adopted |
| U-srh-010 | shuorenhua | - 短语表默认只列代表项 | ALL-PROC-039 | adopted-with-modification |
| U-srh-011 | shuorenhua | ## Execution order | ALL-PROC-001 | adopted |
| U-srh-012 | shuorenhua | ## Execution order | ALL-PROT-019 | adopted-with-modification |
| U-srh-013 | shuorenhua | 执行第 6 步时 | ALL-PROC-039 | adopted-with-modification |
| U-srh-014 | shuorenhua | ## 1. Scene detection | ALL-P-012 | adopted |
| U-srh-015 | shuorenhua | ### `chat` | ZH-G-002 | adopted-with-modification |
| U-srh-016 | shuorenhua | ### `status` | ZH-G-002 | adopted-with-modification |
| U-srh-017 | shuorenhua | ### `docs` | ZH-G-002 | adopted-with-modification |
| U-srh-018 | shuorenhua | ### `public-writing` | ZH-G-002 | adopted-with-modification |
| U-srh-019 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-020 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-021 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-022 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-023 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-024 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-025 | shuorenhua | ### Scene Packs | ZH-G-003 | adopted |
| U-srh-026 | shuorenhua | ### Scene Packs | ALL-PROT-024 | adopted |
| U-srh-027 | shuorenhua | ### Scene Packs | ALL-PROT-023 | adopted |
| U-srh-028 | shuorenhua | ### Scene Packs | ALL-G-004 | adopted |
| U-srh-029 | shuorenhua | ### Scene Packs | ALL-PROC-010 | adopted-with-modification |
| U-srh-030 | shuorenhua | 单文件模式只是兜底 | ALL-PROC-035 | rejected |
| U-srh-031 | shuorenhua | - 删开场套话、谄媚和元评论 | ZH-P-022 | adopted |
| U-srh-032 | shuorenhua | - 删空总结和收尾腔 | ZH-P-001 | adopted |
| U-srh-033 | shuorenhua | - 处理二元对比骨架 | ZH-P-024 | adopted |
| U-srh-034 | shuorenhua | - 把商业黑话和表演性技术腔改回普通动作 | ZH-P-001 | adopted |
| U-srh-035 | shuorenhua | - 遇到过度接住、替用户做心理判断或身份认证式夸奖 | ZH-P-027 | adopted |
| U-srh-036 | shuorenhua | - 遇到过度接住、替用户做心理判断或身份认证式夸奖 | ZH-P-028 | adopted |
| U-srh-037 | shuorenhua | - 发现翻译腔时 | ZH-P-011 | adopted-with-modification |
| U-srh-038 | shuorenhua | - 把名词化还原成动词 | ZH-P-011 | adopted-with-modification |
| U-srh-039 | shuorenhua | - 同一个对象不要在相邻几句里换三种说法 | ZH-P-029 | adopted |
| U-srh-040 | shuorenhua | - 清理姿态层时按子句和事实要素判断 | ALL-PROT-025 | adopted |
| U-srh-041 | shuorenhua | - 清理姿态层时按子句和事实要素判断 | ALL-PROT-023 | adopted |
| U-srh-042 | shuorenhua | - `code-context` 里的真实运行行为 | ALL-PROT-026 | adopted-with-modification |
| U-srh-043 | shuorenhua | - `code-context` 里的真实运行行为 | ALL-PROT-003 | adopted |
| U-srh-044 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-027 | adopted |
| U-srh-045 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-028 | adopted |
| U-srh-046 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-022 | adopted |
| U-srh-047 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-023 | adopted |
| U-srh-048 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-020 | adopted |
| U-srh-049 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-PROT-029 | adopted |
| U-srh-050 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-P-010 | adopted |
| U-srh-051 | shuorenhua | - 抽象信息、实体类型和关系不能擅自具体化 | ALL-P-007 | adopted |
| U-srh-052 | shuorenhua | - 中英混排句中的英文词 | ZH-PROT-003 | adopted |
| U-srh-053 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-054 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-055 | shuorenhua | ### Unsourced citation modes | ALL-PROT-002 | adopted |
| U-srh-056 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-057 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-058 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-059 | shuorenhua | ### Unsourced citation modes | ALL-PROC-040 | adopted |
| U-srh-060 | shuorenhua | ### `minimal` | ALL-PROC-041 | rejected |
| U-srh-061 | shuorenhua | ### `standard` | ALL-PROC-041 | rejected |
| U-srh-062 | shuorenhua | ### `aggressive` | ALL-PROC-041 | rejected |
| U-srh-063 | shuorenhua | ### `aggressive` | ALL-PROT-019 | adopted-with-modification |
| U-srh-064 | shuorenhua | ### `aggressive` | ZH-G-002 | adopted-with-modification |
| U-srh-065 | shuorenhua | ## 3.5 Edit scope | ALL-PROC-042 | adopted |
| U-srh-066 | shuorenhua | ### `structural` | ALL-PROC-042 | adopted |
| U-srh-067 | shuorenhua | ### `bounded` | ZH-PROC-004 | adopted-with-modification |
| U-srh-068 | shuorenhua | ### `bounded` | ALL-PROC-042 | adopted |
| U-srh-069 | shuorenhua | ### `bounded` | ALL-PROC-043 | adopted |
| U-srh-070 | shuorenhua | ### `bounded` | ALL-PROC-043 | adopted |
| U-srh-071 | shuorenhua | ### `bounded` | ALL-PROC-043 | adopted |
| U-srh-072 | shuorenhua | ### `bounded` | ALL-PROC-044 | adopted-with-modification |
| U-srh-073 | shuorenhua | ### `bounded` | ALL-PROC-043 | adopted |
| U-srh-074 | shuorenhua | ### `in-place` | ALL-PROC-042 | adopted |
| U-srh-075 | shuorenhua | ### `in-place` | ALL-PROC-042 | adopted |
| U-srh-076 | shuorenhua | ### `in-place` | ALL-PROC-042 | adopted |
| U-srh-077 | shuorenhua | ### `in-place` | ALL-PROT-030 | adopted |
| U-srh-078 | shuorenhua | ### `in-place` | ALL-PROC-044 | adopted-with-modification |
| U-srh-079 | shuorenhua | ### `in-place` | ALL-PROC-042 | adopted |
| U-srh-080 | shuorenhua | ## 4. Tier severity | ZH-M-006 | adopted-with-modification |
| U-srh-081 | shuorenhua | ### Tier 1 | ZH-M-006 | adopted-with-modification |
| U-srh-082 | shuorenhua | ### Tier 2 | ZH-M-006 | adopted-with-modification |
| U-srh-083 | shuorenhua | ### Tier 2 | ZH-M-006 | adopted-with-modification |
| U-srh-084 | shuorenhua | ### Tier 3 | ZH-M-006 | adopted-with-modification |
| U-srh-085 | shuorenhua | ## 5. No-touch and keep rules | ALL-PROC-025 | adopted-with-modification |
| U-srh-086 | shuorenhua | ## 5. No-touch and keep rules | ALL-PROT-009 | adopted |
| U-srh-087 | shuorenhua | 保护依据是词在当前句子里的具体含义 | ALL-PROT-031 | adopted |
| U-srh-088 | shuorenhua | 保护依据是词在当前句子里的具体含义 | ALL-PROT-031 | adopted |
| U-srh-089 | shuorenhua | 数值、正式指标名、字段名、命令和引用原文按字面保护 | ALL-PROT-032 | adopted |
| U-srh-090 | shuorenhua | 数值、正式指标名、字段名、命令和引用原文按字面保护 | ALL-PROT-032 | adopted |
| U-srh-091 | shuorenhua | - 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错 | ALL-PROT-032 | adopted |
| U-srh-092 | shuorenhua | - 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错 | ALL-PROT-032 | adopted |
| U-srh-093 | shuorenhua | - 引用原文、命令、接口名、参数名、字段名、配置项、日志、报错 | ALL-PROT-032 | adopted |
| U-srh-094 | shuorenhua | - 技术文档里的系统行为主语 | ALL-PROT-033 | adopted |
| U-srh-095 | shuorenhua | 数值、正式指标名、字段名、命令和引用原文按字面保护 | ALL-PROT-023 | adopted |
| U-srh-096 | shuorenhua | 数值、正式指标名、字段名、命令和引用原文按字面保护 | ALL-PROT-031 | adopted |
| U-srh-097 | shuorenhua | 词本身正在被定义、讨论 | ZH-P-030 | adopted |
| U-srh-098 | shuorenhua | 例如 `闭环反馈 / 闭环控制` 是反馈机制 | ZH-P-030 | adopted |
| U-srh-099 | shuorenhua | 词本身正在被定义、讨论 | ALL-PROT-009 | adopted |
| U-srh-100 | shuorenhua | - 承载关键事实的抽象句，即使它 | ALL-P-010 | adopted |
| U-srh-101 | shuorenhua | 不要为了 | ALL-PROT-018 | adopted |
| U-srh-102 | shuorenhua | ## 6. Positive style targets | ALL-P-007 | adopted |
| U-srh-103 | shuorenhua | ## 6. Positive style targets | ALL-P-012 | adopted |
| U-srh-104 | shuorenhua | ## 6. Positive style targets | ALL-PROC-019 | adopted-with-modification |
| U-srh-105 | shuorenhua | ## 6. Positive style targets | ZH-P-002 | adopted |
| U-srh-106 | shuorenhua | ## 6. Positive style targets | ZH-P-031 | adopted |
| U-srh-107 | shuorenhua | ## 7. Output contract | ALL-PROC-046 | rejected |
| U-srh-108 | shuorenhua | ### Annotation mode | ALL-PROC-007 | adopted-with-modification |
| U-srh-109 | shuorenhua | ### Annotation mode | ALL-PROC-038 | adopted |
| U-srh-110 | shuorenhua | ### Annotation mode | ALL-PROC-007 | adopted-with-modification |
| U-srh-111 | shuorenhua | ### Annotation mode | ALL-PROC-040 | adopted |
| U-srh-112 | shuorenhua | ### Annotation mode | ALL-M-018 | adopted |
| U-srh-113 | shuorenhua | ### Annotation mode | ALL-M-018 | adopted |
| U-srh-114 | shuorenhua | ### Annotation mode | ALL-PROT-012 | adopted |
| U-srh-115 | shuorenhua | ### Annotation mode | ALL-PROC-024 | adopted-with-modification |
| U-srh-116 | shuorenhua | ### Annotation mode | ALL-PROC-007 | adopted-with-modification |
| U-srh-117 | shuorenhua | ### Annotation mode | ALL-PROC-046 | rejected |
| U-srh-118 | shuorenhua | ## 8. Required reread checks | ALL-PROC-045 | adopted |
| U-srh-119 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-PROC-045 | adopted |
| U-srh-120 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-PROT-029 | adopted |
| U-srh-121 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-PROT-034 | adopted |
| U-srh-122 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-PROC-042 | adopted |
| U-srh-123 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-M-019 | adopted-with-modification |
| U-srh-124 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-M-019 | adopted-with-modification |
| U-srh-125 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-M-019 | adopted-with-modification |
| U-srh-126 | shuorenhua | ### Pass 1 \| 保真回读 | ALL-PROC-043 | adopted |
| U-srh-127 | shuorenhua | ### Pass 2 \| Residual Audit | ALL-PROC-045 | adopted |
| U-srh-128 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-P-001 | adopted |
| U-srh-129 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-P-001 | adopted |
| U-srh-130 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-P-032 | adopted |
| U-srh-131 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-P-028 | adopted |
| U-srh-132 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-M-005 | adopted |
| U-srh-133 | shuorenhua | ### Pass 2 \| Residual Audit | ALL-PROC-045 | adopted |
| U-srh-134 | shuorenhua | ### Pass 2 \| Residual Audit | ALL-PROC-045 | adopted |
| U-srh-135 | shuorenhua | ### Pass 2 \| Residual Audit | ZH-G-002 | adopted-with-modification |
