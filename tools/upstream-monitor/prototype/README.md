# prototype

`check_merge.py` 和 `render_sources.py` 已经吸收进正式包
`tools/upstream-monitor/src/upstream_monitor/`，两个脚本已删除：

- `check_merge.py` 的 format、anchors、coverage 三项，对应
  `upstream-monitor validate`，实现见 `validate.py`（外加 catalog 与
  skills/、merges/ 的三方一致性校验，以及 main 分支上禁止
  model-proposed 的检查）、`anchors.py`、`coverage.py`。
- `render_sources.py` 对应 `upstream-monitor render`，实现见 `render.py`。

改动直接改正式包，跑 `tools/upstream-monitor/tests/` 里的用例，不再在这
里维护。

`lineage.py` 是仍在用的过渡脚本，处理入围阶段的谱系聚类（同一项目的
fork、翻译版、再适配版归一类），还没有吸收进正式包，继续留在本目录，
按需手工运行。等它的逻辑并入 `upstream_monitor` 之后，本目录连同这份
README 一起删除。
