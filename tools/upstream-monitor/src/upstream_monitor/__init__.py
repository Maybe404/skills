"""upstream_monitor：Maybe404/skills 仓库的上游监控与流转工具。

职责边界见 ``docs/design.md`` 第 5 节：这个包只做机械的事——拉取、hash、
比对、渲染、开 PR；语义判断（是否重复、是否采用、怎么改写）由
``skills/skill-merge`` 这个 skill 做，不在这个包里。
"""

__version__ = "0.1.0"
