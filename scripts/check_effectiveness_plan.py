#!/usr/bin/env python3
"""Validate adoption and Harness effectiveness measurement reports."""

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
    "node_modules",
    "dist",
    "build",
    "target",
    "out",
    ".next",
    ".turbo",
    ".gradle",
    "__pycache__",
    "harness-starter-kit",
}
TEMPLATE_PARTS = {"templates"}

ADOPTION_FIELDS = (
    "Baseline available",
    "Comparable tasks to repeat or track",
    "Primary metric",
    "Review window",
    "Results location",
    "Task outcome records location",
)
GATE_PLACEMENT_FIELDS = (
    "Normal completion gate",
    "Deterministic behavior checks included in the normal gate",
    "Focused or manual checks outside the normal gate",
    "Reasons for focused/manual placement",
)
FAILURE_MEMORY_FIELDS = (
    "Recorded",
    "Detection or prevention check",
    "Skipped",
)
EFFECTIVENESS_SECTIONS = (
    "## Target",
    "## Task Set",
    "## Results",
    "## Interpretation",
)

TODO_RE = re.compile(r"\bTODO\b", flags=re.IGNORECASE)
SECTION_RE = re.compile(r"^##\s+", flags=re.MULTILINE)
FAILURE_RECORD_RE = re.compile(
    r"`?(docs/failures/[^\s,;)`]+)`?",
    flags=re.IGNORECASE,
)
PATH_REFERENCE_RE = re.compile(
    r"`?((?:tests?|specs?|fixtures?|scripts?|docs/checklists)/[^\s,;)`]+"
    r"|\.github/workflows/[^\s,;)`]+)`?",
    flags=re.IGNORECASE,
)
CONCRETE_CHECK_PATTERNS = (
    re.compile(r"\b(?:tests?|specs?|fixtures?|scripts?)/[^\s,.;)]+"),
    re.compile(r"`?\.github/workflows/[^\s,.;)`]+`?"),
    re.compile(r"\bpython3?\s+(?:-m\s+[\w.:-]+|scripts?/[^\s,.;)]+)"),
    re.compile(r"\bmanual review point\s+`?docs/checklists/[^\s,.;)`]+"),
)
NO_FAILURE_RECORD_PHRASES = (
    "no failure record",
    "no failure note",
    "no recurring failure",
    "no user-visible runtime failure",
)


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate adoption reports, gate placement, failure-memory linkage, "
            "and Harness effectiveness reports."
        )
    )
    parser.add_argument("--require-report", action="store_true")
    return parser.parse_args()


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRECTORIES for part in path.parts)


def is_template(path: Path) -> bool:
    return any(part in TEMPLATE_PARTS for part in path.parts)


def is_report(path: Path) -> bool:
    name = path.name.lower()
    return name.endswith(".md") and (
        "adoption-report" in name or "effectiveness-report" in name
    )


def iter_reports(root: Path) -> list[Path]:
    return [
        path
        for path in sorted(root.rglob("*.md"))
        if is_report(path.relative_to(root))
        and not is_ignored(path.relative_to(root))
        and not is_template(path.relative_to(root))
    ]


def field_value(text: str, field: str) -> str | None:
    pattern = re.compile(rf"^(\s*)-\s*{re.escape(field)}:\s*(.*)$")
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = pattern.match(line)
        if match is None:
            continue

        base_indent = len(match.group(1))
        parts = [match.group(2).strip()]
        for continuation in lines[index + 1 :]:
            stripped = continuation.strip()
            if not stripped:
                break
            indent = len(continuation) - len(continuation.lstrip())
            if indent <= base_indent:
                break
            parts.append(stripped)

        return " ".join(part for part in parts if part).strip()

    return None


def section_text(text: str, heading: str) -> str | None:
    lines = text.splitlines()
    start_index = next(
        (index for index, line in enumerate(lines) if line.strip() == heading),
        None,
    )
    if start_index is None:
        return None

    section_lines = [lines[start_index]]
    for line in lines[start_index + 1 :]:
        if SECTION_RE.match(line):
            break
        section_lines.append(line)

    return "\n".join(section_lines)


def is_placeholder(value: str | None) -> bool:
    return value is None or not value or bool(TODO_RE.search(value))


def records_no_failure(value: str | None) -> bool:
    if value is None:
        return False
    return value.strip().lower().startswith("none")


def recorded_failure_exists(value: str | None) -> bool:
    if value is None:
        return False
    normalized = value.strip().lower()
    return "docs/failures/" in normalized and not normalized.startswith("none")


def failure_record_references(value: str | None) -> list[str]:
    if value is None:
        return []
    return sorted(
        {match.group(1).rstrip(".") for match in FAILURE_RECORD_RE.finditer(value)}
    )


def references_missing_local_paths(root: Path, value: str | None) -> list[str]:
    if value is None:
        return []
    return [
        reference
        for reference in sorted(
            {match.group(1).rstrip(".") for match in PATH_REFERENCE_RE.finditer(value)}
        )
        if not (root / reference).exists()
    ]


def says_no_failure_record(value: str | None) -> bool:
    if value is None:
        return False
    normalized = " ".join(value.lower().split())
    return any(phrase in normalized for phrase in NO_FAILURE_RECORD_PHRASES)


def has_concrete_check(value: str | None) -> bool:
    if value is None:
        return False
    normalized = " ".join(value.lower().split())
    return any(pattern.search(normalized) for pattern in CONCRETE_CHECK_PATTERNS)


def validate_adoption_report(root: Path, path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []

    effectiveness_section = section_text(text, "## Effectiveness Measurement Plan")
    if effectiveness_section is None:
        findings.append(
            Finding(path, "missing ## Effectiveness Measurement Plan section")
        )
    else:
        for field in ADOPTION_FIELDS:
            if is_placeholder(field_value(effectiveness_section, field)):
                findings.append(Finding(path, f"incomplete measurement field: {field}"))

    gate_section = section_text(text, "## Verification Gate Placement")
    if gate_section is None:
        findings.append(Finding(path, "missing ## Verification Gate Placement section"))
    else:
        for field in GATE_PLACEMENT_FIELDS:
            if is_placeholder(field_value(gate_section, field)):
                findings.append(
                    Finding(path, f"incomplete gate-placement field: {field}")
                )

    failure_section = section_text(text, "## Failure Memory")
    if failure_section is None:
        findings.append(Finding(path, "missing ## Failure Memory section"))
        return findings

    values: dict[str, str | None] = {}
    for field in FAILURE_MEMORY_FIELDS:
        value = field_value(failure_section, field)
        values[field] = value
        if is_placeholder(value):
            findings.append(Finding(path, f"incomplete failure-memory field: {field}"))

    recorded_value = values.get("Recorded")
    detection_value = values.get("Detection or prevention check")
    failure_references = failure_record_references(recorded_value)

    if records_no_failure(recorded_value) and failure_references:
        findings.append(
            Finding(
                path,
                "contradictory failure-memory Recorded: none with docs/failures reference",
            )
        )
    if recorded_value is not None and not records_no_failure(recorded_value):
        if not failure_references:
            findings.append(
                Finding(
                    path,
                    "failure-memory Recorded must list docs/failures/... or none",
                )
            )
        for reference in failure_references:
            if not (root / reference).exists():
                findings.append(
                    Finding(
                        path,
                        f"failure-memory Recorded references missing record: {reference}",
                    )
                )

    if recorded_failure_exists(recorded_value):
        if says_no_failure_record(detection_value):
            findings.append(
                Finding(
                    path,
                    "contradictory failure-memory field: Detection or prevention check",
                )
            )
        if not has_concrete_check(detection_value):
            findings.append(
                Finding(
                    path,
                    "incomplete failure-memory detection link: Detection or prevention check",
                )
            )
        for reference in references_missing_local_paths(root, detection_value):
            findings.append(
                Finding(
                    path,
                    f"failure-memory detection references missing local path: {reference}",
                )
            )

    return findings


def validate_effectiveness_report(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for section in EFFECTIVENESS_SECTIONS:
        if section not in text:
            findings.append(Finding(path, f"missing required section: {section}"))
    if TODO_RE.search(text):
        findings.append(Finding(path, "effectiveness report still contains TODO"))
    return findings


def check_effectiveness_plan(root: Path, require_report: bool) -> int:
    reports = iter_reports(root)
    if require_report and not reports:
        print("No adoption or effectiveness report found.")
        return 1

    findings: list[Finding] = []
    for path in reports:
        text = path.read_text(encoding="utf-8")
        name = path.name.lower()
        if "adoption-report" in name:
            findings.extend(validate_adoption_report(root, path, text))
        if "effectiveness-report" in name:
            findings.extend(validate_effectiveness_report(path, text))

    for finding in findings:
        print(f"{finding.path.relative_to(root)}: {finding.message}")

    return 1 if findings else 0


def main() -> int:
    args = parse_args()
    return check_effectiveness_plan(Path.cwd(), args.require_report)


if __name__ == "__main__":
    raise SystemExit(main())
