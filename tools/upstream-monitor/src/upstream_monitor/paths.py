"""仓库路径解析。所有命令都通过这里找 catalog/、merges/、skills/、schemas/。"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepoPaths:
    root: Path
    catalog_dir: Path
    merges_dir: Path
    skills_dir: Path
    schemas_dir: Path

    @classmethod
    def resolve(
        cls,
        root: str | Path = ".",
        catalog_dir: str | Path | None = None,
        merges_dir: str | Path | None = None,
        skills_dir: str | Path | None = None,
        schemas_dir: str | Path | None = None,
    ) -> "RepoPaths":
        root_p = Path(root).resolve()
        return cls(
            root=root_p,
            catalog_dir=Path(catalog_dir).resolve() if catalog_dir else root_p / "catalog",
            merges_dir=Path(merges_dir).resolve() if merges_dir else root_p / "merges",
            skills_dir=Path(skills_dir).resolve() if skills_dir else root_p / "skills",
            schemas_dir=Path(schemas_dir).resolve()
            if schemas_dir
            else root_p / "tools" / "upstream-monitor" / "schemas",
        )

    def merge_dir(self, merge_id: str) -> Path:
        return self.merges_dir / merge_id

    def sources_yaml(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "sources.yaml"

    def lock_json(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "sources.lock.json"

    def decisions_yaml(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "decisions.yaml"

    def snapshots_dir(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "snapshots"

    def reports_dir(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "reports"

    def changelog_md(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "CHANGELOG.md"

    def work_dir(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "work"

    def lineage_relations_yaml(self, merge_id: str) -> Path:
        return self.merge_dir(merge_id) / "lineage-relations.yaml"

    def catalog_entries(self) -> list[Path]:
        if not self.catalog_dir.is_dir():
            return []
        return sorted(self.catalog_dir.glob("*.yaml"))

    def catalog_for_merge(self, merge_id: str) -> Path | None:
        target = f"merges/{merge_id}"
        for p in self.catalog_entries():
            from upstream_monitor.yamlio import load_yaml

            doc = load_yaml(p)
            if doc.get("merge_instance") == target:
                return p
        return None

    def merge_ids(self) -> list[str]:
        if not self.merges_dir.is_dir():
            return []
        return sorted(p.name for p in self.merges_dir.iterdir() if p.is_dir())

    def skill_source_path(self, skill_id: str, original_path: str) -> str:
        """决定 snapshots/<source_id>/ 下一个追踪文件的落盘名。

        SKILL.md 存为 SKILL.source.md，避免被 skills CLI 当成本仓库自己的
        skill 加载；其余文件原名不动。
        """
        p = Path(original_path)
        if p.name == "SKILL.md":
            p = p.with_name("SKILL.source.md")
        return str(p)
