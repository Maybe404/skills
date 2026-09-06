import shutil
import sys
from pathlib import Path

import pytest

PKG_ROOT = Path(__file__).resolve().parent.parent
SRC = PKG_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from upstream_monitor.paths import RepoPaths  # noqa: E402

FIXTURES_REPO = Path(__file__).parent / "fixtures" / "repo"
SCHEMAS_DIR = PKG_ROOT / "schemas"


@pytest.fixture
def fixture_repo(tmp_path) -> Path:
    dest = tmp_path / "repo"
    shutil.copytree(FIXTURES_REPO, dest)
    return dest


@pytest.fixture
def repo_paths(fixture_repo) -> RepoPaths:
    return RepoPaths.resolve(root=fixture_repo, schemas_dir=SCHEMAS_DIR)
