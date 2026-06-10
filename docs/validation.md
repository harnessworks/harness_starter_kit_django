# Validation Coverage

This document names the local validation commands that bind Harness rules to
feedback loops for this Django target.

## Normal Gate

Run the project wrapper before completing implementation or Harness-maintenance
work:

```powershell
.\.venv\Scripts\python.exe scripts\check_harness.py
```

On macOS or Linux, use the project virtual environment Python at
`.venv/bin/python` when available.

`scripts/check_harness.py` runs:

- `scripts/check_docs_drift.py`
- `scripts/check_structure.py`
- `scripts/check_encoding_hygiene.py`
- `scripts/check_effectiveness_plan.py --require-report`
- `scripts/check_failure_memory.py`
- `scripts/check_decision_memory.py`
- `manage.py check`
- `manage.py test`

## Focused Checks

Run these directly when working on their specific surface:

```powershell
.\.venv\Scripts\python.exe scripts\check_docs_drift.py
.\.venv\Scripts\python.exe scripts\check_effectiveness_plan.py --require-report
.\.venv\Scripts\python.exe scripts\check_failure_memory.py
.\.venv\Scripts\python.exe scripts\check_decision_memory.py
```

Use Harness Doctor as a diagnostic, not as proof of agent effectiveness:

```powershell
.\.venv\Scripts\python.exe harness-starter-kit\scripts\harness_doctor.py --target .
```

## What This Does Not Prove

Passing local checks shows that the repository-visible Harness health gate is
clean. It does not prove that agent effectiveness improved. Use
`docs/evaluation.md` and effectiveness reports to record comparable task
outcomes.
