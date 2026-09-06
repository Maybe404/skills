"""读当前 git 分支名，只读，不做任何写操作。"""
from __future__ import annotations

import subprocess
from pathlib import Path


def current_branch(root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    branch = out.stdout.strip()
    return branch or None
