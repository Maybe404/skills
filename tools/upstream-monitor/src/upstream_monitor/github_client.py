"""GitHub 访问的可注入接口。

上游内容一律当数据：这里只负责取字节和元数据，不解析、不执行、不把内容
拼进 shell 命令。真实实现只用标准库 urllib 调 GitHub REST API 和
raw.githubusercontent.com；token 从环境变量 GITHUB_TOKEN 读，读不到时
尝试本地 `gh auth token`（只读，不把任何上游内容传给它）。

测试用 FakeGitHubClient 注入固定内容，不发真实网络请求。
"""
from __future__ import annotations

import json
import subprocess
import urllib.error
import urllib.request
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


class GitHubError(Exception):
    """GitHub 访问失败的基类。"""


class RepoNotFound(GitHubError):
    """仓库不存在或不可见（含私有但无权访问的情况，GitHub 两者都返回 404）。"""


class RepoPrivate(GitHubError):
    """仓库存在但已知转为私有（元数据里 private 为 true 且可读到）。"""


class FileNotFound(GitHubError):
    """仓库可达，但指定路径在指定 ref 上不存在。"""


class NetworkError(GitHubError):
    """网络层面的失败：超时、DNS、5xx 等，与内容是否存在无关。"""


@dataclass(frozen=True)
class RepoMeta:
    stars: int
    forks: int
    private: bool
    license_spdx: str | None = None


class GitHubClient(Protocol):
    """check / diff / snapshot / pr 命令依赖的最小接口。"""

    def get_head_commit(self, repo: str, branch: str) -> str:
        """返回 repo 在 branch 上的 HEAD commit（40 位小写十六进制）。"""
        ...

    def get_file(self, repo: str, path: str, ref: str) -> bytes:
        """返回 repo 在 ref（分支名或 commit）上 path 的原始字节。"""
        ...

    def get_repo_meta(self, repo: str) -> RepoMeta:
        """返回 repo 的 star、fork 数和是否私有。"""
        ...

    def get_license(self, repo: str, ref: str) -> tuple[str, bytes]:
        """返回 (仓库内许可证文件路径, 原始字节)。没有许可证文件时抛 FileNotFound。"""
        ...


def resolve_token() -> str | None:
    import os

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=5, check=False
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    token = out.stdout.strip()
    return token or None


class RealGitHubClient:
    """标准库 urllib 实现，不依赖第三方 HTTP 库。"""

    API_BASE = "https://api.github.com"
    RAW_BASE = "https://raw.githubusercontent.com"

    def __init__(self, token: str | None = None, timeout: float = 15.0):
        self._token = token if token is not None else resolve_token()
        self._timeout = timeout

    def _headers(self, accept: str = "application/vnd.github+json") -> dict:
        h = {"Accept": accept, "User-Agent": "upstream-monitor"}
        if self._token:
            h["Authorization"] = f"Bearer {self._token}"
        return h

    def _get(self, url: str, accept: str = "application/vnd.github+json") -> bytes:
        req = urllib.request.Request(url, headers=self._headers(accept))
        try:
            with urllib.request.urlopen(req, timeout=self._timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise RepoNotFound(url) from e
            if e.code in (403, 451):
                raise RepoPrivate(url) from e
            raise NetworkError(f"{url}: HTTP {e.code}") from e
        except urllib.error.URLError as e:
            raise NetworkError(f"{url}: {e.reason}") from e

    def get_repo_meta(self, repo: str) -> RepoMeta:
        try:
            data = json.loads(self._get(f"{self.API_BASE}/repos/{repo}"))
        except RepoNotFound:
            raise
        lic = data.get("license") or {}
        spdx = lic.get("spdx_id")
        if spdx in (None, "NOASSERTION"):
            spdx = None
        return RepoMeta(
            stars=data.get("stargazers_count", 0),
            forks=data.get("forks_count", 0),
            private=bool(data.get("private", False)),
            license_spdx=spdx,
        )

    def get_head_commit(self, repo: str, branch: str) -> str:
        try:
            data = json.loads(self._get(f"{self.API_BASE}/repos/{repo}/commits/{branch}"))
        except RepoNotFound as e:
            raise RepoNotFound(f"{repo}@{branch}") from e
        return data["sha"]

    def get_file(self, repo: str, path: str, ref: str) -> bytes:
        url = f"{self.RAW_BASE}/{repo}/{ref}/{path}"
        try:
            return self._get(url, accept="*/*")
        except RepoNotFound as e:
            raise FileNotFound(f"{repo}@{ref}:{path}") from e

    def get_license(self, repo: str, ref: str) -> tuple[str, bytes]:
        import base64

        url = f"{self.API_BASE}/repos/{repo}/license?ref={ref}"
        try:
            data = json.loads(self._get(url))
        except RepoNotFound as e:
            raise FileNotFound(f"{repo}@{ref}: 无 LICENSE") from e
        path = data.get("path", "LICENSE")
        content = base64.b64decode(data.get("content", ""), validate=False)
        return path, content


class FakeGitHubClient:
    """测试用的固定内容客户端，不发真实网络请求。

    data 形如::

        {
            "owner/repo": {
                "meta": {"stars": 10, "forks": 2, "private": False},
                "branches": {"main": "<40位commit>"},
                "files": {("<commit或分支>", "path/in/repo"): b"raw bytes"},
                "missing_files": {("<commit>", "path")},  # 显式声明 404
            }
        }

    repo 不在 data 里时视为仓库不存在（RepoNotFound）。
    """

    def __init__(self, data: dict | None = None):
        self.data = data or {}

    def get_repo_meta(self, repo: str) -> RepoMeta:
        if repo not in self.data:
            raise RepoNotFound(repo)
        m = self.data[repo].get("meta", {})
        if m.get("private"):
            raise RepoPrivate(repo)
        return RepoMeta(
            stars=m.get("stars", 0),
            forks=m.get("forks", 0),
            private=False,
            license_spdx=m.get("license_spdx"),
        )

    def get_head_commit(self, repo: str, branch: str) -> str:
        if repo not in self.data:
            raise RepoNotFound(repo)
        branches = self.data[repo].get("branches", {})
        if branch not in branches:
            raise RepoNotFound(f"{repo}@{branch}")
        return branches[branch]

    def get_file(self, repo: str, path: str, ref: str) -> bytes:
        if repo not in self.data:
            raise RepoNotFound(repo)
        entry = self.data[repo]
        key = (ref, path)
        if key in entry.get("missing_files", set()):
            raise FileNotFound(f"{repo}@{ref}:{path}")
        files = entry.get("files", {})
        if key not in files:
            raise FileNotFound(f"{repo}@{ref}:{path}")
        return files[key]

    def get_license(self, repo: str, ref: str) -> tuple[str, bytes]:
        if repo not in self.data:
            raise RepoNotFound(repo)
        lic = self.data[repo].get("license")
        if lic is None:
            raise FileNotFound(f"{repo}@{ref}: 无 LICENSE")
        return lic["path"], lic["content"]
