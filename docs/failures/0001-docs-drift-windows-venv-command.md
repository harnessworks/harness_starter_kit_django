# 0001: Docs Drift Check Misread Windows Venv Commands

## Date Observed

2026-05-27

## Failure Type

Failed CI run and cross-environment mismatch.

## Goal

Documented local commands should remain valid guidance without making Linux CI
require a Windows virtual-environment path.

## What Happened Or Was Tried

GitHub Actions failed after CI was added for the Harness. The failing command
was:

```powershell
python scripts/check_harness.py
```

The failure happened inside `scripts/check_docs_drift.py`. The CI log reported
missing paths for documented PowerShell commands:

```text
Missing referenced path in docs/decisions/0002-initialize-django-config-project.md: .\.venv\Scripts\python.exe
Missing referenced path in docs/harness/adoption-report.md: .\.venv\Scripts\python.exe
```

## Why It Failed

The docs drift checker treated inline Windows virtual-environment commands as
file references. That passed locally on Windows because
`.\.venv\Scripts\python.exe` existed, but failed in Linux CI where that path is
not present.

## Current Replacement

`scripts/check_docs_drift.py` treats documented Python executable commands such
as `.\.venv\Scripts\python.exe ...` and `.venv/bin/python ...` as commands, not
required file references.

## Detection Or Prevention Check

`scripts/check_docs_drift.py` detects broken local Markdown references while
allowing documented Python executable commands. `scripts/check_harness.py` runs
that drift check locally, and `.github/workflows/harness-check.yml` runs the
same Harness wrapper in CI.

## Agent Guidance

Keep cross-platform command examples in docs. When improving docs drift logic,
recognize commands by executable name rather than by host-specific path
existence.
