#!/usr/bin/env python3
"""Detect stale file references and broken local Markdown links."""

from __future__ import annotations

from dataclasses import dataclass
import re
import shlex
from pathlib import Path
from urllib.parse import unquote, urlsplit


DOC_FILES = ("AGENTS.md", "README.md", "CONTRIBUTING.md", "CLAUDE.md")
IGNORED_SCHEMES = {"http", "https", "mailto"}
IGNORED_PARTS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "harness-starter-kit",
}
OPTIONAL_REFERENCES = {
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "README.md",
    ".harness/source.json",
    ".venv",
    ".venv/",
    "db.sqlite3",
    "docs/harness/effectiveness-report.md",
    "harness-starter-kit",
    "harness-starter-kit/",
    "manage.py",
}
OPTIONAL_PREFIXES = (
    ".mypy_cache/",
    ".pytest_cache/",
    ".ruff_cache/",
    "__pycache__/",
    "harness-starter-kit/",
)

BACKTICK_RE = re.compile(r"`([^`\n]+)`")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


@dataclass(frozen=True)
class Reference:
    value: str
    source: str


def is_ignored_path(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


def iter_docs(root: Path) -> list[Path]:
    docs = [root / name for name in DOC_FILES if (root / name).exists()]
    if (root / "docs").exists():
        docs.extend(
            path
            for path in sorted((root / "docs").rglob("*.md"))
            if not is_ignored_path(path.relative_to(root))
        )
    return docs


def clean_markdown_link_target(target: str) -> str:
    value = target.strip()
    if value.startswith("<"):
        closing = value.find(">")
        if closing != -1:
            return value[1:closing].strip()

    try:
        parts = shlex.split(value, posix=True)
    except ValueError:
        parts = value.split()
    return parts[0] if parts else ""


def extract_references(text: str) -> set[Reference]:
    references = {
        Reference(value=match, source="inline-code")
        for match in BACKTICK_RE.findall(text)
    }
    references.update(
        Reference(value=target, source="markdown-link")
        for target in (
            clean_markdown_link_target(match)
            for match in MARKDOWN_LINK_RE.findall(text)
        )
        if target
    )
    return references


def is_external(reference: str) -> bool:
    parts = urlsplit(reference.strip())
    return bool(parts.scheme and (parts.scheme in IGNORED_SCHEMES or "://" in reference))


def normalize(reference: str) -> str:
    value = reference.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1].strip()
    path = unquote(urlsplit(value).path).replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def is_ignored_reference(reference: str) -> bool:
    if is_external(reference) or reference.strip().startswith("#"):
        return True
    if any(token in reference for token in ("*", "<", ">", "{{", "}}")):
        return True

    normalized = normalize(reference)
    if not normalized:
        return True
    if normalized.startswith("/"):
        return True
    if normalized in OPTIONAL_REFERENCES:
        return True
    ignored_cache_dirs = {"__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"}
    if any(part in ignored_cache_dirs for part in Path(normalized).parts):
        return True
    return any(normalized.startswith(prefix) for prefix in OPTIONAL_PREFIXES)


def looks_like_command(reference: str) -> bool:
    command_roots = {"python", "pytest", "ruff", "mypy", "pre-commit"}
    try:
        first = shlex.split(reference, posix=False)[0]
    except (IndexError, ValueError):
        return False

    normalized = first.strip("\"'").replace("\\", "/").lower()
    return (
        first in command_roots
        or normalized in {".venv/scripts/python.exe", ".venv/bin/python"}
        or normalized.endswith("/python.exe")
        or normalized.endswith("/python")
    )


def looks_like_path(reference: Reference) -> bool:
    if is_ignored_reference(reference.value):
        return False
    normalized = normalize(reference.value)
    if " " in normalized:
        return False
    if reference.source == "markdown-link":
        return True
    return "/" in normalized or "\\" in reference.value or normalized in DOC_FILES


def referenced_path_exists(root: Path, doc: Path, reference: str) -> bool:
    path = Path(normalize(reference))
    if path.is_absolute():
        return path.exists()
    return (root / path).exists() or (doc.parent / path).exists()


def check_docs(root: Path) -> int:
    missing_paths: list[tuple[Path, str]] = []

    for doc in iter_docs(root):
        text = doc.read_text(encoding="utf-8")
        for reference in sorted(extract_references(text), key=lambda item: item.value):
            if reference.source == "inline-code" and looks_like_command(reference.value):
                continue
            if looks_like_path(reference) and not referenced_path_exists(
                root, doc, reference.value
            ):
                missing_paths.append((doc, reference.value))

    for doc, reference in missing_paths:
        print(f"Missing referenced path in {doc.relative_to(root)}: {reference}")

    return 1 if missing_paths else 0


def main() -> int:
    return check_docs(Path.cwd())


if __name__ == "__main__":
    raise SystemExit(main())
