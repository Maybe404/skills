# 示例：一段规则文本的英译中

## 示例 1：定义加规则的段落

### 英文原文

> Mannered prose substitutes metaphor and flourish for direct statement. Instead of "a parameter worth varying," the mannered writer produces "a dial worth turning." Instead of "this point still matters," they write "this point earns its keep." The phrases exist to display the writer, not to convey the idea, and readers can tell. That is why mannered prose irritates: it makes the reader work harder so the writer can perform. It is also imprecise. Metaphors drag in connotations the writer did not choose and cannot control. The fix is to say what you mean. When a literal phrase is available, use it.

### 错误译法 A：省主语，定义句变祈使句

> 矫饰的文字用比喻和修辞替代直白的陈述。不写"一个值得调整的参数"，而写成"一个值得拧动的旋钮"；不写"这一点仍然重要"，而写成"这一点没有白占位置"。……

问题：
- 第一句没有定义标记，"用……替代……"可以读成对读者的要求。
- 第二句丢了主语 "the mannered writer"，"不写 A 而写成 B"变成了让读者写 B——和原意相反。
- 整段没有一句祈使句，放进规则文件后没有"不要"。

### 错误译法 B：译文自己矫饰

> 矫揉造作的文风，本质上就是拿隐喻和花哨修辞取代了直白的陈述。矫饰的作者不会老老实实写"一个值得调整的参数"，非要写成"一个值得转动的旋钮"；……这正是矫饰文风令人反感的地方：作者在台上表演，读者却要在台下受罪。……解决办法其实很简单：有话直说。

问题：
- "本质上""老老实实""非要""其实很简单"都是原文没有的强调词。
- "作者在台上表演，读者却要在台下受罪"是译者加的舞台比喻，原文只有 perform 一个词。
- 一段禁止比喻的规则用比喻来写，模型会把它当成风格样本。

### 正确译法

> 你输出的所有文字（回复、报告、规则、文档）都不矫饰。所谓矫饰的文字，就是该直说的地方偏要用比喻和修辞。写这种文字的人不写"一个值得调整的参数"，而要写"一个值得拧动的旋钮"；不写"这一点仍然重要"，而要写"这一点没有白占位置"。这类说法存在的意义是展示作者本人，不是传达想法，而读者是看得出来的。矫饰的文字让人烦躁，原因就在这里：它让读者更费力，好让作者有机会表演。它同时也不精确——比喻会带进作者没有挑选、也控制不了的言外之意。解决办法是把意思直接说出来。有字面表达可用时，就用字面表达。

做对的地方：
- 段首补了一句祈使句，情态和范围都写明。
- "所谓……就是……"把定义句钉死。
- "写这种文字的人"补回主语。
- "earns its keep" 没有直译，换成中文里同样矫饰的"没有白占位置"，例子的功能保住了。
- 原文的六个论点（定义、例子、目的是展示、读者看得出、为什么烦躁、不精确）一个不少；没有加任何原文没有的词。

## 示例 2：四句规则

### "Already know the fix? Offer it as a suggestion, acceptance separate: 'I'd lean towards X, but the bar is Y.'"

错：已知修法作为建议给出，验收另写。
对：你已经知道怎么修时，把修法作为建议写进去，验收标准另写（"建议用 X，但标准是 Y"）。
原因：条件从名词短语展开成分句；设问改成条件句；示例里的 "I" 按人称表改掉，避免文件里出现"我"。

### "Escalate, don't retry: one re-prompt at the same tier, then move it up — or into the main loop if it was already Opus."

错：同一问题打回两次未解决，换更高一级模型；已是 Opus 的自己做。
对：同档打回一次仍未解决，换更高一档模型新开，不要反复重试；已经是 Opus 的，你自己做。
原因：原文是一次，译文写成两次是静默改数；"自己做"可读成"让那个 agent 自己做"，补"你"。

### "Matching both lists: keep."

错：两边都命中：留下。
对：两边都符合：留在主循环。
原因："命中"是半比喻；"留下"没说留在哪里。

### "Say it is available in every subagent prompt."

错：在每个 subagent 的 prompt 里注明。
对：在每个 subagent 的 prompt 里注明 codegraph 可用。
原因：it 指代的东西要写成名词，否则"注明"没有宾语。
