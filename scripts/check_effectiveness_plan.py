#!/usr/bin/env python3
"""Validate adoption-time harness effectiveness measurement reports."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "harness-starter-kit",
}
ADOPTION_FIELDS = (
    "Baseline available",
    "Comparable tasks to repeat or track",
    "Primary metric",
    "Review window",
    "Results location",
    "Task outcome records location",
)
TODO_RE = re.compile(r"\bTODO\b", flags=re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-report", action="store_true")
    return parser.parse_args()


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRECTORIES for part in path.parts)


def iter_reports(root: Path) -> list[Path]:
    return [
        path
        for path in sorted(root.rglob("*.md"))
        if path.name.lower().endswith(".md")
        and "adoption-report" in path.name.lower()
        and not is_ignored(path.relative_to(root))
    ]


def field_value(text: str, field: str) -> str | None:
    pattern = re.compile(rf"^\s*-\s*{re.escape(field)}:\s*(.*)$", re.MULTILINE)
    match = pattern.search(text)
    if match is None:
        return None
    return match.group(1).strip()


def is_placeholder(value: str | None) -> bool:
    return value is None or not value or bool(TODO_RE.search(value))


def validate_report(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    if "## Effectiveness Measurement Plan" not in text:
        findings.append(Finding(path, "missing ## Effectiveness Measurement Plan section"))
        return findings

    for field in ADOPTION_FIELDS:
        if is_placeholder(field_value(text, field)):
            findings.append(Finding(path, f"incomplete measurement field: {field}"))
    return findings


def check_effectiveness_plan(root: Path, require_report: bool) -> int:
    reports = iter_reports(root)
    if require_report and not reports:
        print("No adoption report found.")
        return 1

    findings: list[Finding] = []
    for path in reports:
        findings.extend(validate_report(path, path.read_text(encoding="utf-8")))

    for finding in findings:
        print(f"{finding.path.relative_to(root)}: {finding.message}")

    return 1 if findings else 0


def main() -> int:
    args = parse_args()
    return check_effectiveness_plan(Path.cwd(), args.require_report)


if __name__ == "__main__":
    raise SystemExit(main())
