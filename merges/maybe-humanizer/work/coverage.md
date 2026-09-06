# 单元到规则的映射（覆盖检查）

804 条单元，每条恰好归入一条规则，无遗漏、无重复引用。其中前 254 条来自首次合并，中间 234 条来自中文批（op7418-humanizer-zh、ai-zixun-humanizer-zh、shuorenhua），接着 112 条来自英文批一（blader-humanizer 77 条、hardikpandya-stop-slop 35 条），末尾 204 条来自英文批二（conorbronsdon-avoid-ai-writing）。

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
| U-abh-003 | aboudjem-humanizer | ### Voice Profiles / casual | EN-S-001 | adopted-with-modification |
| U-abh-004 | aboudjem-humanizer | ### Voice Profiles / professional | EN-S-001 | adopted-with-modification |
| U-abh-005 | aboudjem-humanizer | ### Voice Profiles / technical | EN-S-001 | adopted-with-modification |
| U-abh-006 | aboudjem-humanizer | ### Voice Profiles / warm | EN-S-001 | adopted-with-modification |
| U-abh-007 | aboudjem-humanizer | ### Voice Profiles / blunt | EN-S-001 | adopted-with-modification |
| U-abh-008 | aboudjem-humanizer | ## Quick reference / Flags / --score | ALL-M-005 | rejected |
| U-abh-009 | aboudjem-humanizer | ## Step 1: Parse Arguments / --aggressive | ALL-PROC-027 | rejected |
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
| U-srh-101 | shuorenhua | 不要为了“像人”把文本改得更假 | ALL-PROT-018 | adopted |
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
| U-bld-001 | blader-humanizer | ## What to do / 1. **Find AI patterns.** | ALL-PROC-009 | adopted |
| U-bld-002 | blader-humanizer | ## What to do / 2. **Keep every claim.** | ALL-PROT-003 | adopted |
| U-bld-003 | blader-humanizer | ## What to do / 3. **Do not invent facts.** | ALL-PROT-001 | adopted |
| U-bld-004 | blader-humanizer | ## What to do / 3. **Do not invent facts.** | ALL-PROC-047 | adopted |
| U-bld-005 | blader-humanizer | ## What to do / 3. **Do not invent facts.** | ALL-PROT-035 | rejected |
| U-bld-006 | blader-humanizer | ## What to do / 3. **Do not invent facts.** | ALL-G-005 | rejected |
| U-bld-007 | blader-humanizer | ## What to do / 4. **Match the voice.** | ALL-G-002 | adopted-with-modification |
| U-bld-008 | blader-humanizer | ## Match the writer's voice | ALL-PROC-048 | adopted |
| U-bld-009 | blader-humanizer | ## Match the writer's voice / 2. Match those habits. | ALL-PROT-017 | adopted |
| U-bld-010 | blader-humanizer | A writing sample takes priority over these style rules. | ALL-PROC-049 | adopted-with-modification |
| U-bld-011 | blader-humanizer | ## Add personality only when it fits | ALL-PROC-014 | adopted-with-modification |
| U-bld-012 | blader-humanizer | Use personality in blog posts, essays, opinions, and personal writing | ALL-G-006 | adopted-with-modification |
| U-bld-013 | blader-humanizer | When personality fits, keep the writer's opinions | ALL-PROT-017 | adopted |
| U-bld-014 | blader-humanizer | Never invent facts to make the text feel personal. | ALL-PROT-018 | adopted |
| U-bld-015 | blader-humanizer | ### 1. Inflated claims about importance and legacy | EN-P-014 | adopted |
| U-bld-016 | blader-humanizer | ### 2. Name-dropping to prove importance | EN-P-018 | adopted |
| U-bld-017 | blader-humanizer | If the source explains what the person said and where | EN-P-018 | adopted |
| U-bld-018 | blader-humanizer | ### 3. Shallow analysis with -ing phrases | EN-P-013 | adopted |
| U-bld-019 | blader-humanizer | ### 4. Sales language | EN-P-002 | adopted |
| U-bld-020 | blader-humanizer | ### 5. Vague sources | EN-P-017 | adopted |
| U-bld-021 | blader-humanizer | Name a real source when the source text provides one. | EN-P-017 | adopted |
| U-bld-022 | blader-humanizer | ### 6. Formulaic challenges and outlook sections | EN-P-031 | adopted |
| U-bld-023 | blader-humanizer | Add details such as dates or public actions only when they come from the source or the user. | ALL-PROT-001 | adopted |
| U-bld-024 | blader-humanizer | ### 7. Overused AI words | EN-P-001 | adopted |
| U-bld-025 | blader-humanizer | ### 8. Avoiding is and are | EN-P-015 | adopted |
| U-bld-026 | blader-humanizer | ### 9. Not X but Y and clipped negative endings | EN-P-006 | adopted |
| U-bld-027 | blader-humanizer | ### 9. Not X but Y and clipped negative endings | EN-P-043 | adopted |
| U-bld-028 | blader-humanizer | ### 10. Forced groups of three | ALL-P-005 | adopted |
| U-bld-029 | blader-humanizer | ### 11. Changing names and repeating sentence openings | EN-P-020 | adopted |
| U-bld-030 | blader-humanizer | ### 11. Changing names and repeating sentence openings | ALL-P-001 | adopted-with-modification |
| U-bld-031 | blader-humanizer | Do not ban the repeated word. Fix the repeated sentence pattern. | ALL-PROT-009 | adopted |
| U-bld-032 | blader-humanizer | ### 12. False from X to Y ranges | EN-P-021 | adopted |
| U-bld-033 | blader-humanizer | ### 13. Passive voice and missing subjects | ALL-P-004 | adopted |
| U-bld-034 | blader-humanizer | ### 14. Em and en dashes | EN-S-004 | rejected |
| U-bld-035 | blader-humanizer | Before returning the rewrite, search for | EN-PROC-001 | adopted |
| U-bld-036 | blader-humanizer | ### 15. Too much bold text | ALL-P-002 | adopted |
| U-bld-037 | blader-humanizer | ### 16. Lists with bold mini-headings | ALL-P-002 | adopted |
| U-bld-038 | blader-humanizer | ### 17. Title case in headings | EN-P-012 | adopted |
| U-bld-039 | blader-humanizer | ### 18. Emojis | ALL-P-002 | adopted |
| U-bld-040 | blader-humanizer | ### 19. Curly quotation marks | EN-P-044 | adopted-with-modification |
| U-bld-041 | blader-humanizer | ### 20. Chatbot text left in the answer | EN-P-028 | adopted |
| U-bld-042 | blader-humanizer | ### 21. Knowledge-limit disclaimers and guesses | EN-P-028 | adopted |
| U-bld-043 | blader-humanizer | ### 21. Knowledge-limit disclaimers and guesses | EN-P-045 | adopted |
| U-bld-044 | blader-humanizer | ### 22. Overly agreeable tone | EN-P-028 | adopted |
| U-bld-045 | blader-humanizer | ### 23. Filler phrases | EN-P-004 | adopted |
| U-bld-046 | blader-humanizer | ### 24. Too many qualifiers | EN-P-029 | adopted |
| U-bld-047 | blader-humanizer | ### 25. Generic positive endings | EN-P-023 | adopted |
| U-bld-048 | blader-humanizer | ### 26. Too many hyphenated word pairs | EN-P-036 | adopted |
| U-bld-049 | blader-humanizer | ### 27. Pretending to reveal a deeper truth | EN-P-008 | adopted |
| U-bld-050 | blader-humanizer | ### 28. Announcing the next point | EN-P-007 | adopted |
| U-bld-051 | blader-humanizer | ### 29. A heading repeated in the first sentence | EN-P-033 | adopted |
| U-bld-052 | blader-humanizer | ### 30. Writing about the previous version | EN-P-035 | adopted-with-modification |
| U-bld-053 | blader-humanizer | ### 31. Forced punchlines and dramatic fragments | EN-P-025 | adopted |
| U-bld-054 | blader-humanizer | ### 32. Formulaic sayings | EN-P-024 | adopted |
| U-bld-055 | blader-humanizer | ### 33. Fake-candid openings | EN-P-007 | adopted |
| U-bld-056 | blader-humanizer | ### 34. Answering objections no one raised | EN-P-041 | adopted |
| U-bld-057 | blader-humanizer | Remove only the unsupported defense. | ALL-PROT-020 | adopted |
| U-bld-058 | blader-humanizer | ### 35. Rejecting fake alternatives | EN-P-046 | adopted |
| U-bld-059 | blader-humanizer | One rejected option may be valid. | EN-P-046 | adopted |
| U-bld-060 | blader-humanizer | ### What not to flag | ALL-M-002 | adopted |
| U-bld-061 | blader-humanizer | - **Useful limits and disclaimers.** | ALL-PROT-036 | adopted |
| U-bld-062 | blader-humanizer | - **Secondhand text.** | ALL-PROT-008 | adopted |
| U-bld-063 | blader-humanizer | - **Real alternatives.** | EN-P-046 | adopted |
| U-bld-064 | blader-humanizer | When unsure, look for several patterns together. | ALL-M-002 | adopted |
| U-bld-065 | blader-humanizer | ### Human details to keep | ALL-PROT-017 | adopted |
| U-bld-066 | blader-humanizer | - **Edits made before November 30, 2022.** | ALL-M-020 | adopted-with-modification |
| U-bld-067 | blader-humanizer | **Pasted text (default).** | ALL-PROC-050 | adopted-with-modification |
| U-bld-068 | blader-humanizer | **File mode.** | ALL-PROC-021 | adopted-with-modification |
| U-bld-069 | blader-humanizer | **File mode.** | ALL-PROT-037 | adopted |
| U-bld-070 | blader-humanizer | **Embedded mode.** | ALL-PROC-021 | adopted-with-modification |
| U-bld-071 | blader-humanizer | ## Rewrite process / 1. Read the source and mark each AI pattern. | ALL-PROC-009 | adopted |
| U-bld-072 | blader-humanizer | ## Rewrite process / 2. Write a draft. Read it aloud. | ALL-PROC-051 | adopted-with-modification |
| U-bld-073 | blader-humanizer | ## Rewrite process / 3. Ask two questions: | ALL-PROC-014 | adopted-with-modification |
| U-bld-074 | blader-humanizer | ## Rewrite process / 3. Ask two questions: | ALL-PROT-019 | adopted-with-modification |
| U-bld-075 | blader-humanizer | ## Rewrite process / 4. Write the final version. | ALL-PROC-012 | adopted-with-modification |
| U-bld-076 | blader-humanizer | ## Rewrite process / 4. Write the final version. | ALL-PROC-011 | adopted |
| U-bld-077 | blader-humanizer | ## Rewrite process / 4. Write the final version. | EN-PROC-001 | adopted |
| U-ssl-001 | hardikpandya-stop-slop | ## Throat-Clearing Openers | EN-P-007 | adopted |
| U-ssl-002 | hardikpandya-stop-slop | ## Emphasis Crutches | EN-P-022 | adopted |
| U-ssl-003 | hardikpandya-stop-slop | ## Adverbs / Kill all adverbs. No -ly words. | EN-S-005 | rejected |
| U-ssl-004 | hardikpandya-stop-slop | ## Binary Contrasts | EN-P-006 | adopted |
| U-ssl-005 | hardikpandya-stop-slop | ## Negative Listing | EN-P-006 | adopted |
| U-ssl-006 | hardikpandya-stop-slop | ## Dramatic Fragmentation | EN-P-025 | adopted |
| U-ssl-007 | hardikpandya-stop-slop | ## Rhetorical Setups | EN-P-009 | adopted |
| U-ssl-008 | hardikpandya-stop-slop | ## False Agency | ALL-P-004 | adopted |
| U-ssl-009 | hardikpandya-stop-slop | ## Core Rules / 3. **Use active voice.** | EN-S-006 | rejected |
| U-ssl-010 | hardikpandya-stop-slop | ## Passive Voice | EN-S-007 | rejected |
| U-ssl-011 | hardikpandya-stop-slop | ## Vague Declaratives | ALL-P-007 | adopted |
| U-ssl-012 | hardikpandya-stop-slop | ## Word Patterns / \| Lazy extremes (every, always, never, everyone, everybody, nobody) \| | EN-P-047 | adopted-with-modification |
| U-ssl-013 | hardikpandya-stop-slop | ## Narrator-from-a-Distance | EN-P-034 | reference-only |
| U-ssl-014 | hardikpandya-stop-slop | ## Core Rules / 6. **Vary rhythm.** | ALL-P-001 | adopted-with-modification |
| U-ssl-015 | hardikpandya-stop-slop | ## Rhythm Patterns / \| Three-item lists \| Use two items or one \| | EN-S-008 | rejected |
| U-ssl-016 | hardikpandya-stop-slop | ## Rhythm Patterns / \| Every paragraph ends punchily \| Vary endings \| | EN-P-048 | adopted |
| U-ssl-017 | hardikpandya-stop-slop | ## Rhythm Patterns / \| Em-dashes \| Remove. Use commas or periods. No em dashes at all. \| | EN-S-009 | rejected |
| U-ssl-018 | hardikpandya-stop-slop | ## Core Rules / 7. **Trust readers.** | EN-P-049 | adopted-with-modification |
| U-ssl-019 | hardikpandya-stop-slop | ## Core Rules / 8. **Cut quotables.** | EN-P-024 | adopted |
| U-ssl-020 | hardikpandya-stop-slop | ## Sentence Starters to Avoid / \| Sentences starting with What, When, Where, Which, Who, Why, How \| Restructure. Lead with the subject or the verb. \| | EN-S-010 | reference-only |
| U-ssl-021 | hardikpandya-stop-slop | ## Meta-Commentary | EN-P-050 | adopted-with-modification |
| U-ssl-022 | hardikpandya-stop-slop | ## Quick Checks / Before delivering prose: | ALL-PROC-014 | adopted-with-modification |
| U-ssl-023 | hardikpandya-stop-slop | ## Scoring / Rate 1-10 on each dimension: | ALL-M-017 | reference-only |
| U-ssl-024 | hardikpandya-stop-slop | ## Scoring / Below 35/50: revise. | ALL-M-017 | reference-only |
| U-ssl-025 | hardikpandya-stop-slop | ## Business Jargon | EN-P-051 | adopted-with-modification |
| U-ssl-026 | hardikpandya-stop-slop | ## Adverbs / No softeners, no intensifiers, no hedges. | EN-S-011 | rejected |
| U-ssl-027 | hardikpandya-stop-slop | ## Adverbs / Also cut these filler phrases: | EN-P-004 | adopted |
| U-ssl-028 | hardikpandya-stop-slop | ## Performative Emphasis | EN-P-052 | adopted-with-modification |
| U-ssl-029 | hardikpandya-stop-slop | ## Telling Instead of Showing | EN-P-022 | adopted |
| U-ssl-030 | hardikpandya-stop-slop | ## Formulaic Constructions / \| "By the time X, I was Y." \| Narrative template \| | EN-P-053 | rejected |
| U-ssl-031 | hardikpandya-stop-slop | ## Formulaic Constructions / \| "X that isn't Y" \| Indirect. Say "X is broken" \| | EN-P-054 | rejected |
| U-ssl-032 | hardikpandya-stop-slop | ## Sentence Starters to Avoid / \| Paragraphs starting with "So" \| Start with content \| | EN-S-012 | reference-only |
| U-ssl-033 | hardikpandya-stop-slop | ## Sentence Starters to Avoid / \| Sentences starting with "Look," \| Remove \| | EN-P-007 | adopted |
| U-ssl-034 | hardikpandya-stop-slop | ## Rhythm Patterns / \| Questions answered immediately \| Let questions breathe or cut them \| | EN-P-009 | adopted |
| U-ssl-035 | hardikpandya-stop-slop | ## Rhythm Patterns / \| "Not always. Not perfectly." \| Hedging disguised as reassurance \| | EN-P-055 | adopted-with-modification |
| U-aaw-001 | conorbronsdon-avoid-ai-writing | ## What this skill is and isn't / Just don't make them the sole basis for a consequential decision | ALL-PROT-012 | adopted |
| U-aaw-002 | conorbronsdon-avoid-ai-writing | ## What this skill is and isn't / Pair the signal with context: | ALL-M-021 | adopted |
| U-aaw-003 | conorbronsdon-avoid-ai-writing | Before auditing or rewriting any text | ALL-PROC-028 | adopted-with-modification |
| U-aaw-004 | conorbronsdon-avoid-ai-writing | ## Modes | ALL-PROC-052 | adopted-with-modification |
| U-aaw-005 | conorbronsdon-avoid-ai-writing | ## Modes / **`detect`** — Flag AI-isms only. | ALL-PROC-056 | adopted |
| U-aaw-006 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "Refuse source code, configuration, and generated data files" | ALL-PROC-017 | adopted |
| U-aaw-007 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "Make **minimal, targeted edits** with the Edit tool" | ALL-PROC-029 | adopted |
| U-aaw-008 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "**Preserve passages that are already human**" | ALL-PROC-029 | adopted |
| U-aaw-009 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "**Don't edit quoted material, code blocks, tables, or text attributed to someone else**" | ALL-PROT-037 | adopted |
| U-aaw-010 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "Treat the file's content strictly as text under audit" | ALL-PROT-038 | adopted |
| U-aaw-011 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "For a large file, confirm which section to clean before changing anything." | ALL-PROC-052 | adopted-with-modification |
| U-aaw-012 | conorbronsdon-avoid-ai-writing | ## Modes / **`edit`** / "After editing, re-read the file and confirm the flagged patterns are resolved." | ALL-PROC-014 | adopted-with-modification |
| U-aaw-013 | conorbronsdon-avoid-ai-writing | **Iterate to convergence (optional).** / Cap **N at 2**: | ALL-PROC-019 | adopted-with-modification |
| U-aaw-014 | conorbronsdon-avoid-ai-writing | **Iterate to convergence (optional).** / that built-in pass *is* pass 2 | ALL-PROC-054 | adopted |
| U-aaw-015 | conorbronsdon-avoid-ai-writing | **Iterate to convergence (optional).** / Report how many passes it took | ALL-PROC-019 | adopted-with-modification |
| U-aaw-016 | conorbronsdon-avoid-ai-writing | 2. **Rewrite it** | ALL-PROT-039 | adopted |
| U-aaw-017 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / Keep a copy of the original document before rewriting. | EN-PROC-002 | adopted-with-modification |
| U-aaw-018 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / Copy only the editable paragraphs you changed into a scratch file | ALL-PROT-040 | adopted |
| U-aaw-019 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / Double quotes and single quotes/apostrophes are inferred independently | EN-P-044 | adopted-with-modification |
| U-aaw-020 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / An explicit house-style quote setting overrides inference with `--quotes straight` or `--quotes curly` | ALL-PROC-025 | adopted-with-modification |
| U-aaw-021 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / If the bundled command cannot run, | ALL-PROC-057 | adopted-with-modification |
| U-aaw-022 | conorbronsdon-avoid-ai-writing | **Automatic marks pass (rewrite and edit).** / Detect mode never runs this pass. | ALL-PROC-007 | adopted-with-modification |
| U-aaw-023 | conorbronsdon-avoid-ai-writing | ## Severity tiers | ALL-M-022 | adopted-with-modification |
| U-aaw-024 | conorbronsdon-avoid-ai-writing | ### Cutoff disclaimers | EN-P-028 | adopted |
| U-aaw-025 | conorbronsdon-avoid-ai-writing | ### Chatbot artifacts | EN-P-028 | adopted |
| U-aaw-026 | conorbronsdon-avoid-ai-writing | ### Vague attributions | EN-P-017 | adopted |
| U-aaw-027 | conorbronsdon-avoid-ai-writing | ### Significance inflation | EN-P-014 | adopted |
| U-aaw-028 | conorbronsdon-avoid-ai-writing | ### Hashtag stuffing | EN-P-056 | adopted-with-modification |
| U-aaw-029 | conorbronsdon-avoid-ai-writing | ### Words and phrases to replace / Words are organized into three tiers based on how reliably | EN-M-001 | adopted-with-modification |
| U-aaw-030 | conorbronsdon-avoid-ai-writing | ### Template phrases (avoid) | ALL-M-001 | adopted |
| U-aaw-031 | conorbronsdon-avoid-ai-writing | ### "Let's" constructions | EN-P-007 | adopted |
| U-aaw-032 | conorbronsdon-avoid-ai-writing | ### Synonym cycling | EN-P-019 | adopted |
| U-aaw-033 | conorbronsdon-avoid-ai-writing | ### Structural issues / - **Formulaic openings**: | EN-P-007 | adopted |
| U-aaw-034 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Bold overuse**: | ALL-P-002 | adopted |
| U-aaw-035 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Em dashes (— and --)**: | EN-P-026 | adopted-with-modification |
| U-aaw-036 | conorbronsdon-avoid-ai-writing | ### Generic future-narrative closers | EN-P-023 | adopted |
| U-aaw-037 | conorbronsdon-avoid-ai-writing | ### Social endorsement closers | EN-P-057 | adopted |
| U-aaw-038 | conorbronsdon-avoid-ai-writing | ### Lingering-attention claims | EN-P-058 | adopted |
| U-aaw-039 | conorbronsdon-avoid-ai-writing | ### Narrated candor | EN-P-059 | adopted |
| U-aaw-040 | conorbronsdon-avoid-ai-writing | ### Hedge-stacked predictions | EN-P-029 | adopted |
| U-aaw-041 | conorbronsdon-avoid-ai-writing | ### "Real/actual" adjective inflation | EN-P-060 | adopted |
| U-aaw-042 | conorbronsdon-avoid-ai-writing | ### Moral-adjective category errors / - AI glues moral or character adjectives | EN-P-061 | adopted |
| U-aaw-043 | conorbronsdon-avoid-ai-writing | ### Invented contrast-pair mirroring | EN-P-062 | adopted |
| U-aaw-044 | conorbronsdon-avoid-ai-writing | ### Bullet lists of bare noun phrases | ALL-P-013 | adopted-with-modification |
| U-aaw-045 | conorbronsdon-avoid-ai-writing | #### Tier 3 phrases — Flag at density or in clusters | EN-P-063 | adopted-with-modification |
| U-aaw-046 | conorbronsdon-avoid-ai-writing | ### Generic conclusions | EN-P-023 | adopted |
| U-aaw-047 | conorbronsdon-avoid-ai-writing | ### Manufactured punchlines and staccato drama / - **Repeated setup/reversal punchlines (P2, judgment-only).** | EN-P-064 | adopted-with-modification |
| U-aaw-048 | conorbronsdon-avoid-ai-writing | ### P2 — Stylistic polish (fix when time allows) / - Judgment-only clarity checks | ALL-M-023 | adopted |
| U-aaw-049 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **Compulsive rule of three**: | ALL-P-005 | adopted |
| U-aaw-050 | conorbronsdon-avoid-ai-writing | ### Structural issues / - **Uniform paragraph length**: | ALL-P-001 | adopted-with-modification |
| U-aaw-051 | conorbronsdon-avoid-ai-writing | ### Copula avoidance | EN-P-015 | adopted |
| U-aaw-052 | conorbronsdon-avoid-ai-writing | ### Transition phrases to remove or rewrite | EN-P-004 | adopted |
| U-aaw-053 | conorbronsdon-avoid-ai-writing | ### P2 — Stylistic polish (fix when time allows) / - Tier 3 phrase repetition | EN-P-063 | adopted-with-modification |
| U-aaw-054 | conorbronsdon-avoid-ai-writing | ### Unnecessary hyphenation | EN-P-036 | adopted |
| U-aaw-055 | conorbronsdon-avoid-ai-writing | ## Self-reference escape hatch | ALL-PROT-041 | adopted |
| U-aaw-056 | conorbronsdon-avoid-ai-writing | ## House style (optional): `--style <config-or-guide>` | ALL-PROC-025 | adopted-with-modification |
| U-aaw-057 | conorbronsdon-avoid-ai-writing | **Preferred: a config file.** / A config is JSON: | ALL-PROC-057 | adopted-with-modification |
| U-aaw-058 | conorbronsdon-avoid-ai-writing | **Preferred: a config file.** / Open the output by naming the resolved config | ALL-PROC-057 | adopted-with-modification |
| U-aaw-059 | conorbronsdon-avoid-ai-writing | **How `--style` composes.** | ALL-PROC-058 | adopted-with-modification |
| U-aaw-060 | conorbronsdon-avoid-ai-writing | **Fallback: a named guide from memory.** / you may apply it from general knowledge as best-effort, not as a feature | ALL-PROC-057 | adopted-with-modification |
| U-aaw-061 | conorbronsdon-avoid-ai-writing | **Fallback: a named guide from memory.** / Do **not** reproduce the guide's copyrighted text | ALL-PROT-042 | adopted |
| U-aaw-062 | conorbronsdon-avoid-ai-writing | **Resolving `--style <arg>`.** / A path, or a bare name matching `examples/<name>.json`, loads that config | ALL-PROC-059 | rejected |
| U-aaw-063 | conorbronsdon-avoid-ai-writing | **Resolving `--style <arg>`.** / When a guide's mechanics conflict with the AI-ism catalog | ALL-PROC-025 | adopted-with-modification |
| U-aaw-064 | conorbronsdon-avoid-ai-writing | **Resolving `--style <arg>`.** / don't apply a guide to a genre it wasn't written for | ALL-G-002 | adopted-with-modification |
| U-aaw-065 | conorbronsdon-avoid-ai-writing | ### Rewrite mode (default) | ALL-PROC-007 | adopted-with-modification |
| U-aaw-066 | conorbronsdon-avoid-ai-writing | **2. Rewritten version** | ALL-PROT-002 | adopted |
| U-aaw-067 | conorbronsdon-avoid-ai-writing | **3. What changed** | ALL-PROC-008 | adopted-with-modification |
| U-aaw-068 | conorbronsdon-avoid-ai-writing | **4. Second-pass audit** / Re-read the rewritten version from section 2. | ALL-PROC-014 | adopted-with-modification |
| U-aaw-069 | conorbronsdon-avoid-ai-writing | **4. Second-pass audit** / When this pass changed anything, the corrected text here is the deliverable | ALL-PROC-060 | adopted |
| U-aaw-070 | conorbronsdon-avoid-ai-writing | ### Detect mode | ALL-PROC-024 | adopted-with-modification |
| U-aaw-071 | conorbronsdon-avoid-ai-writing | ### Detect mode / **1. Issues found** | ALL-M-023 | adopted |
| U-aaw-072 | conorbronsdon-avoid-ai-writing | **2. Assessment** | ALL-PROC-024 | adopted-with-modification |
| U-aaw-073 | conorbronsdon-avoid-ai-writing | ### Edit mode | ALL-PROC-052 | adopted-with-modification |
| U-aaw-074 | conorbronsdon-avoid-ai-writing | **2. Verification** | ALL-PROC-052 | adopted-with-modification |
| U-aaw-075 | conorbronsdon-avoid-ai-writing | **Mechanical check (optional, recommended for edit mode).** | ALL-M-025 | adopted-with-modification |
| U-aaw-076 | conorbronsdon-avoid-ai-writing | ## Tone calibration | EN-P-022 | adopted |
| U-aaw-077 | conorbronsdon-avoid-ai-writing | ## Tone calibration / 1. **Vary sentence length** | ALL-P-001 | adopted-with-modification |
| U-aaw-078 | conorbronsdon-avoid-ai-writing | ## Tone calibration / 2. **Be concrete** | ALL-P-007 | adopted |
| U-aaw-079 | conorbronsdon-avoid-ai-writing | ## Tone calibration / 3. **Have a voice** | EN-S-002 | reference-only |
| U-aaw-080 | conorbronsdon-avoid-ai-writing | ## Tone calibration / 4. **Cut the neutrality** | ALL-S-002 | reference-only |
| U-aaw-081 | conorbronsdon-avoid-ai-writing | ## Tone calibration / 5. **Earn your emphasis** | EN-P-022 | adopted |
| U-aaw-082 | conorbronsdon-avoid-ai-writing | Removal is half the job. / When the genre carries a voice (essays, posts, personal writing), put voice back on purpose | ALL-PROC-018 | adopted |
| U-aaw-083 | conorbronsdon-avoid-ai-writing | Removal is half the job. / For encyclopedic, technical, or legal text | ALL-G-006 | adopted-with-modification |
| U-aaw-084 | conorbronsdon-avoid-ai-writing | If the original writing is already strong | ALL-PROC-029 | adopted |
| U-aaw-085 | conorbronsdon-avoid-ai-writing | The replacement table provides defaults, not mandates. | ALL-PROC-056 | adopted |
| U-aaw-086 | conorbronsdon-avoid-ai-writing | ### Never inject these | ALL-PROT-018 | adopted |
| U-aaw-087 | conorbronsdon-avoid-ai-writing | - **Fake first person.** | ALL-PROT-018 | adopted |
| U-aaw-088 | conorbronsdon-avoid-ai-writing | - **Manufactured stakes.** | EN-PROT-001 | adopted |
| U-aaw-089 | conorbronsdon-avoid-ai-writing | - **Forced contrarianism.** | ALL-PROT-001 | adopted |
| U-aaw-090 | conorbronsdon-avoid-ai-writing | - **Performed candor.** | EN-PROT-001 | adopted |
| U-aaw-091 | conorbronsdon-avoid-ai-writing | - **Em-dash theatrics.** | EN-PROT-001 | adopted |
| U-aaw-092 | conorbronsdon-avoid-ai-writing | - **Staccato conversion.** | EN-PROT-001 | adopted |
| U-aaw-093 | conorbronsdon-avoid-ai-writing | - **Invented specifics.** | ALL-PROT-001 | adopted |
| U-aaw-094 | conorbronsdon-avoid-ai-writing | **The test.** | ALL-PROT-019 | adopted-with-modification |
| U-aaw-095 | conorbronsdon-avoid-ai-writing | **Why it belongs here rather than in the pattern catalog.** | ALL-PROT-043 | adopted |
| U-aaw-096 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Emoji in headers**: | ALL-P-002 | adopted |
| U-aaw-097 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Excessive bullet lists**: | ALL-P-002 | adopted |
| U-aaw-098 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Curly quotation marks (“ ” ‘ ’) and apostrophes**: | ALL-M-002 | adopted |
| U-aaw-099 | conorbronsdon-avoid-ai-writing | ### Formatting / - **Immaculate typography in casual registers**: | ALL-M-002 | adopted |
| U-aaw-100 | conorbronsdon-avoid-ai-writing | ### Formatting / Inverse case worth flagging the other direction: | ALL-PROT-017 | adopted |
| U-aaw-101 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **"It's not X — it's Y" / "This isn't about X, it's about Y"**: | EN-P-006 | adopted |
| U-aaw-102 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **Hollow intensifiers**: | EN-P-003 | adopted |
| U-aaw-103 | conorbronsdon-avoid-ai-writing | ### Sentence structure / The default fix for `actually` is deletion | EN-P-003 | adopted |
| U-aaw-104 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **Vague endorsement ("worth [verb]ing")**: | EN-P-022 | adopted |
| U-aaw-105 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **Hedging**: | EN-P-065 | rejected |
| U-aaw-106 | conorbronsdon-avoid-ai-writing | ### Sentence structure / - **Missing bridge sentences**: | ALL-P-008 | adopted |
| U-aaw-107 | conorbronsdon-avoid-ai-writing | ### Words and phrases to replace / **Match inflected forms.** | ALL-PROC-039 | adopted-with-modification |
| U-aaw-108 | conorbronsdon-avoid-ai-writing | #### Tier 1 — Always replace / **1B — Clarity edits.** | ALL-M-023 | adopted |
| U-aaw-109 | conorbronsdon-avoid-ai-writing | #### Tier 1 — Always replace / Caveat worth keeping visible: | ALL-M-024 | adopted |
| U-aaw-110 | conorbronsdon-avoid-ai-writing | ##### Tier 1A — AI frequency markers / \| delve / delve into \| explore, dig into, look at \| | EN-P-001 | adopted |
| U-aaw-111 | conorbronsdon-avoid-ai-writing | ##### Tier 1A — AI frequency markers / **Hyphen required:** | EN-P-066 | adopted |
| U-aaw-112 | conorbronsdon-avoid-ai-writing | ##### Tier 1A — AI frequency markers / **Abstract-noun boundary:** | EN-P-066 | adopted |
| U-aaw-113 | conorbronsdon-avoid-ai-writing | ##### Tier 1B — Clarity edits | EN-P-005 | adopted |
| U-aaw-114 | conorbronsdon-avoid-ai-writing | #### Tier 2 — Flag when 2+ appear in the same paragraph / These words are legitimate on their own. | EN-M-001 | adopted-with-modification |
| U-aaw-115 | conorbronsdon-avoid-ai-writing | #### Tier 2 — Flag when 2+ appear in the same paragraph / \| deeply *(significance collocations only | EN-P-003 | adopted |
| U-aaw-116 | conorbronsdon-avoid-ai-writing | #### Tier 3 — Flag only at high density / These are normal words. | EN-M-001 | adopted-with-modification |
| U-aaw-117 | conorbronsdon-avoid-ai-writing | #### Tier 3 — Flag only at high density / \| verbatim \| Usually redundant with the verb | ALL-PROT-009 | adopted |
| U-aaw-118 | conorbronsdon-avoid-ai-writing | #### Tier 3 phrases — Flag at density or in clusters / \| community-driven \| Name what the community does. | EN-P-063 | adopted-with-modification |
| U-aaw-119 | conorbronsdon-avoid-ai-writing | #### Audience-fit note: domain-term collision (judgment only) | ALL-PROT-009 | adopted |
| U-aaw-120 | conorbronsdon-avoid-ai-writing | ### Structural issues / - **Suspiciously clean grammar**: | ALL-PROT-017 | adopted |
| U-aaw-121 | conorbronsdon-avoid-ai-writing | ### Aphorism formulas | EN-P-024 | adopted |
| U-aaw-122 | conorbronsdon-avoid-ai-writing | ### Moral-adjective category errors / - **Related — ontological slop on assumptions:** | EN-P-067 | adopted |
| U-aaw-123 | conorbronsdon-avoid-ai-writing | ### Moral-adjective category errors / - **Related — gratuitous universal quantifiers:** | EN-P-047 | adopted-with-modification |
| U-aaw-124 | conorbronsdon-avoid-ai-writing | ### Transformation crutch | EN-P-068 | adopted-with-modification |
| U-aaw-125 | conorbronsdon-avoid-ai-writing | ### Hashtag stuffing / - **What doesn't count.** | EN-P-056 | adopted-with-modification |
| U-aaw-126 | conorbronsdon-avoid-ai-writing | ### Subjectless fragments and agentless passives | ALL-P-004 | adopted |
| U-aaw-127 | conorbronsdon-avoid-ai-writing | ### False agency | ALL-P-004 | adopted |
| U-aaw-128 | conorbronsdon-avoid-ai-writing | ### Filler phrases | EN-P-004 | adopted |
| U-aaw-129 | conorbronsdon-avoid-ai-writing | ### Notability name-dropping / - AI text piles on prestigious citations | EN-P-018 | adopted |
| U-aaw-130 | conorbronsdon-avoid-ai-writing | ### Notability name-dropping / - Related — **historical analogy stacking**: | EN-P-069 | adopted |
| U-aaw-131 | conorbronsdon-avoid-ai-writing | ### Vague third-party validation | EN-P-017 | adopted |
| U-aaw-132 | conorbronsdon-avoid-ai-writing | ### Superficial -ing analyses | EN-P-013 | adopted |
| U-aaw-133 | conorbronsdon-avoid-ai-writing | ### Promotional language | EN-P-002 | adopted |
| U-aaw-134 | conorbronsdon-avoid-ai-writing | ### Formulaic challenges | EN-P-031 | adopted |
| U-aaw-135 | conorbronsdon-avoid-ai-writing | ### Speculative scenario openers | EN-P-007 | adopted |
| U-aaw-136 | conorbronsdon-avoid-ai-writing | ### False ranges | EN-P-021 | adopted |
| U-aaw-137 | conorbronsdon-avoid-ai-writing | ### Inline-header lists | EN-P-070 | adopted |
| U-aaw-138 | conorbronsdon-avoid-ai-writing | ### List-label periods | EN-P-071 | adopted-with-modification |
| U-aaw-139 | conorbronsdon-avoid-ai-writing | ### Title case headings | EN-P-012 | adopted |
| U-aaw-140 | conorbronsdon-avoid-ai-writing | ### Hyphenated modifier stacking | EN-P-072 | adopted |
| U-aaw-141 | conorbronsdon-avoid-ai-writing | ### Speculative gap-filling | EN-P-045 | adopted |
| U-aaw-142 | conorbronsdon-avoid-ai-writing | ### Unfilled placeholders | EN-P-038 | adopted |
| U-aaw-143 | conorbronsdon-avoid-ai-writing | ### Chatbot citation markup leaks | EN-P-038 | adopted |
| U-aaw-144 | conorbronsdon-avoid-ai-writing | ### AI-tool URL parameters | EN-P-038 | adopted |
| U-aaw-145 | conorbronsdon-avoid-ai-writing | ### Novelty inflation / - AI text treats established concepts | EN-P-008 | adopted |
| U-aaw-146 | conorbronsdon-avoid-ai-writing | ### Novelty inflation / - Also flag invented labels: | EN-P-073 | adopted |
| U-aaw-147 | conorbronsdon-avoid-ai-writing | ### Infomercial engagement hooks / - Punchy fragment-hooks that tee up a reveal: | EN-P-009 | adopted |
| U-aaw-148 | conorbronsdon-avoid-ai-writing | ### Infomercial engagement hooks / - The same move in a fake-candid register: | EN-P-007 | adopted |
| U-aaw-149 | conorbronsdon-avoid-ai-writing | ### Launch-copy dramatic introductions / - "Enter Flowdesk." | EN-P-074 | adopted-with-modification |
| U-aaw-150 | conorbronsdon-avoid-ai-writing | ### Launch-copy dramatic introductions / - What the detector actually matches, stated exactly: | EN-P-074 | adopted-with-modification |
| U-aaw-151 | conorbronsdon-avoid-ai-writing | ### Fake-casual register | EN-P-075 | adopted-with-modification |
| U-aaw-152 | conorbronsdon-avoid-ai-writing | ### Emotional flatline | EN-P-076 | adopted |
| U-aaw-153 | conorbronsdon-avoid-ai-writing | ### False concession structure | EN-P-031 | adopted |
| U-aaw-154 | conorbronsdon-avoid-ai-writing | ### Rhetorical question openers | EN-P-009 | adopted |
| U-aaw-155 | conorbronsdon-avoid-ai-writing | ### Parenthetical hedging | EN-P-029 | adopted |
| U-aaw-156 | conorbronsdon-avoid-ai-writing | ### Numbered list inflation | ALL-P-005 | adopted |
| U-aaw-157 | conorbronsdon-avoid-ai-writing | ### Reasoning chain artifacts | EN-P-038 | adopted |
| U-aaw-158 | conorbronsdon-avoid-ai-writing | ### Sycophantic tone | EN-P-028 | adopted |
| U-aaw-159 | conorbronsdon-avoid-ai-writing | ### Acknowledgment loops | ALL-PROC-018 | adopted |
| U-aaw-160 | conorbronsdon-avoid-ai-writing | ### Confidence calibration phrases / - "It's worth noting that," "Interestingly," | EN-P-003 | adopted |
| U-aaw-161 | conorbronsdon-avoid-ai-writing | ### Confidence calibration phrases / - Related — **persuasive-authority tropes**: | EN-P-008 | adopted |
| U-aaw-162 | conorbronsdon-avoid-ai-writing | ### Confidence calibration phrases / - **Consequence-free explanation:** | EN-P-022 | adopted |
| U-aaw-163 | conorbronsdon-avoid-ai-writing | ### Self-labeling significance | EN-P-077 | adopted |
| U-aaw-164 | conorbronsdon-avoid-ai-writing | ### Dramatized contrast against the crowd | EN-P-078 | adopted |
| U-aaw-165 | conorbronsdon-avoid-ai-writing | ### Wall-of-text replies (missing line breaks) | EN-P-079 | adopted-with-modification |
| U-aaw-166 | conorbronsdon-avoid-ai-writing | ### Recap-flattery opener | ALL-PROC-018 | adopted |
| U-aaw-167 | conorbronsdon-avoid-ai-writing | ### Excessive structure / - Too many headers in short text: | EN-P-080 | adopted |
| U-aaw-168 | conorbronsdon-avoid-ai-writing | ### Excessive structure / - Too many list items: | EN-P-080 | adopted |
| U-aaw-169 | conorbronsdon-avoid-ai-writing | ### Excessive structure / - Formulaic section headers: | EN-P-081 | adopted |
| U-aaw-170 | conorbronsdon-avoid-ai-writing | ### Excessive structure / - Fragmented headers: | EN-P-033 | adopted |
| U-aaw-171 | conorbronsdon-avoid-ai-writing | ### Diff-anchored writing | EN-P-035 | adopted-with-modification |
| U-aaw-172 | conorbronsdon-avoid-ai-writing | ### Performed-insight phrases | EN-P-008 | adopted |
| U-aaw-173 | conorbronsdon-avoid-ai-writing | ### Negation chains | EN-P-082 | adopted-with-modification |
| U-aaw-174 | conorbronsdon-avoid-ai-writing | ### Dev-blog boilerplate | EN-P-002 | adopted |
| U-aaw-175 | conorbronsdon-avoid-ai-writing | ### Stacked rhetorical questions | EN-P-009 | adopted |
| U-aaw-176 | conorbronsdon-avoid-ai-writing | ### Same-opener sentence runs | ALL-P-001 | adopted-with-modification |
| U-aaw-177 | conorbronsdon-avoid-ai-writing | ### Stranded auxiliary contrast | EN-P-083 | reference-only |
| U-aaw-178 | conorbronsdon-avoid-ai-writing | ### Colon into a triple | ALL-P-005 | adopted |
| U-aaw-179 | conorbronsdon-avoid-ai-writing | ### Manufactured punchlines and staccato drama / - A run of clipped fragments engineered | EN-P-025 | adopted |
| U-aaw-180 | conorbronsdon-avoid-ai-writing | ### Manufactured punchlines and staccato drama / - **Repeated empty concessions:** | EN-P-055 | adopted-with-modification |
| U-aaw-181 | conorbronsdon-avoid-ai-writing | ### Rhythm and uniformity / **Structure is the #1 detection signal.** | ALL-M-026 | adopted-with-modification |
| U-aaw-182 | conorbronsdon-avoid-ai-writing | ### Rhythm and uniformity / - **Sentence length uniformity**: | ALL-P-001 | adopted-with-modification |
| U-aaw-183 | conorbronsdon-avoid-ai-writing | ### Rhythm and uniformity / - **Read-aloud test**: | ALL-PROC-051 | adopted-with-modification |
| U-aaw-184 | conorbronsdon-avoid-ai-writing | ### Rhythm and uniformity / - **Missing first-person perspective**: | EN-S-013 | reference-only |
| U-aaw-185 | conorbronsdon-avoid-ai-writing | ### Rhythm and uniformity / - **Over-polishing**: | ALL-PROC-056 | adopted |
| U-aaw-186 | conorbronsdon-avoid-ai-writing | ### Vocabulary diversity (stylometric) | EN-M-002 | deferred |
| U-aaw-187 | conorbronsdon-avoid-ai-writing | ### Paragraph-reshuffle immunity (structure test) | ALL-P-008 | adopted |
| U-aaw-188 | conorbronsdon-avoid-ai-writing | ### Treadmill effect / low information density (content test) | ALL-M-018 | adopted |
| U-aaw-189 | conorbronsdon-avoid-ai-writing | ### When to rewrite from scratch vs. patch | ALL-PROC-055 | adopted-with-modification |
| U-aaw-190 | conorbronsdon-avoid-ai-writing | ## Context profiles / Pass an optional context hint to adjust rule strictness. | ALL-PROC-053 | adopted-with-modification |
| U-aaw-191 | conorbronsdon-avoid-ai-writing | ### Profile definitions | ALL-G-007 | adopted-with-modification |
| U-aaw-192 | conorbronsdon-avoid-ai-writing | ### Tolerance matrix / Rules not listed in the table apply at full strength across all profiles. | ALL-G-008 | adopted-with-modification |
| U-aaw-193 | conorbronsdon-avoid-ai-writing | ### Tolerance matrix / **Technical-blog word table exceptions:** | EN-P-084 | adopted-with-modification |
| U-aaw-194 | conorbronsdon-avoid-ai-writing | ### Auto-detection cues | ALL-PROC-053 | adopted-with-modification |
| U-aaw-195 | conorbronsdon-avoid-ai-writing | ### Auto-detection cues / If auto-detection feels wrong, say which profile you're using and why. | ALL-PROC-057 | adopted-with-modification |
| U-aaw-196 | conorbronsdon-avoid-ai-writing | ## Voice profiles / Context profiles (above) set *how strict* | ALL-PROC-058 | adopted-with-modification |
| U-aaw-197 | conorbronsdon-avoid-ai-writing | ## Voice profiles / Every target below is bounded by the Never-inject guardrails: | EN-S-001 | adopted-with-modification |
| U-aaw-198 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **`casual`** — Contractions throughout; | EN-S-001 | adopted-with-modification |
| U-aaw-199 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **`professional`** — Active voice for most sentences. | EN-S-001 | adopted-with-modification |
| U-aaw-200 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **`technical`** — Prefer plain copulatives | EN-S-001 | adopted-with-modification |
| U-aaw-201 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **`warm`** — Address the reader directly | EN-S-001 | adopted-with-modification |
| U-aaw-202 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **`blunt`** — Lead with the claim; | EN-S-001 | adopted-with-modification |
| U-aaw-203 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **Calibrate to a sample (optional).** | ALL-PROC-037 | adopted |
| U-aaw-204 | conorbronsdon-avoid-ai-writing | ## Voice profiles / **How voice composes with context.** | ALL-PROC-058 | adopted-with-modification |
