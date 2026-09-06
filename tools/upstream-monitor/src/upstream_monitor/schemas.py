"""JSON Schema 加载与校验。四份 schema 见 tools/upstream-monitor/schemas/。"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from upstream_monitor.yamlio import load_any

SCHEMA_FILES = {
    "catalog": "catalog.schema.json",
    "sources": "sources.schema.json",
    "lock": "lock.schema.json",
    "decisions": "decisions.schema.json",
}


class SchemaValidationError(Exception):
    """一份文档没有通过对应 schema 的校验。errors 是排序后的错误列表。"""

    def __init__(self, target: str, errors: list[str]):
        self.target = target
        self.errors = errors
        super().__init__(f"{target} 未通过 schema 校验，共 {len(errors)} 处错误")


def load_schema(schemas_dir: Path, name: str) -> dict:
    schema = load_any(schemas_dir / SCHEMA_FILES[name])
    Draft202012Validator.check_schema(schema)
    return schema


def iter_errors(schemas_dir: Path, name: str, doc: Any) -> list[str]:
    schema = load_schema(schemas_dir, name)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errs = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    return [f"/{'/'.join(str(x) for x in e.path)}: {e.message}" for e in errs]


def validate_doc(schemas_dir: Path, name: str, doc: Any, target: str = "<内存文档>") -> None:
    """校验失败时抛 SchemaValidationError，调用方据此决定不写文件。"""
    errs = iter_errors(schemas_dir, name, doc)
    if errs:
        raise SchemaValidationError(target, errs)
