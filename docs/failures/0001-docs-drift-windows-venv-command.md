# 0001: Docs Drift Check Misread Windows Venv Commands

## Status

Resolved

## Context

GitHub Actions failed after CI was added for the harness. The failing command
was:

```powershell
python scripts/check_harness.py
```

The failure happened inside `scripts/check_docs_drift.py`.

## Symptoms

The CI log reported missing paths for documented PowerShell commands:

```text
Missing referenced path in docs/decisions/0002-initialize-django-config-project.md: .\.venv\Scripts\python.exe
Missing referenced path in docs/harness/adoption-report.md: .\.venv\Scripts\python.exe
```

## Root Cause

The docs drift checker treated inline Windows virtual-environment commands as
file references. That passed locally on Windows because
`.\.venv\Scripts\python.exe` existed, but failed in Linux CI where that path is
not present.

## Resolution

Update `scripts/check_docs_drift.py` so documented Python executable commands
such as `.\.venv\Scripts\python.exe ...` and `.venv/bin/python ...` are treated
as commands, not required file references.

## Prevention

- Keep cross-platform command examples in docs.
- When fixing a failed harness check, add a failure note unless the failure is
  purely transient.
- Prefer drift-check logic that recognizes commands by executable name rather
  than by host-specific path existence.
