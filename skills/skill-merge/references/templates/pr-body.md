# sync 时追加进 PR 正文的判断一节

upstream-monitor 开的 PR 正文已经有上游 diff 和元数据。sync 处理完后在正文末尾追加下面这一节。PR 标题不改。

---

## 判断

结论：并 | 部分并 | 不并

上游改了什么（一两句，用自己的话，metadata-only 来源不引原文）。

### 并进来的

- <改了哪个文件哪一段>：<并进来的写法>，理由。

### 没并的

- <上游的写法>：理由（对应 criteria.md 第几条；本仓库已有等价写法的指出在哪）。

### 冲突与留痕

与本仓库现有规则矛盾的写法：选了哪边、为什么、另一边怎么开启。没有写"无"。

### 原文声明

metadata-only 来源：本 PR 不含其原文，判断依据在本地用 `upstream-monitor diff` 查看。没有涉及写"本 PR 不涉及 metadata-only 来源"。

### 检查项

- [ ] `upstream-monitor validate --merge <id>` 通过
- [ ] CHANGELOG.md 已加一节
- [ ] 来源清单有变化时 SOURCES.md 已重新渲染
- [ ] 需要人拍板的已开 issue 并打 needs-decision 标签
