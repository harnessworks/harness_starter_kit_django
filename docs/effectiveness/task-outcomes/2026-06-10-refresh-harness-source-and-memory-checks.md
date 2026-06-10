# 2026-06-10: Refresh Harness Source And Memory Checks

## Task Type

Harness process.

## Request

Run `/harness update` against the refreshed local `harness-starter-kit`
reference.

## Change Surface

- Refreshed `.harness/source.json` to the latest starter-kit commit and
  canonical source URL.
- Updated local Harness validators for docs drift, failure-memory command
  references, and effectiveness-report consistency.
- Added evaluation and validation docs so the refreshed Doctor diagnostic can
  see the target's check bindings and maintenance evidence.
- Updated Harness guidance, adoption reporting, task-outcome guidance, and the
  update report.

## Verification

- `.venv/bin/python -m py_compile scripts/check_docs_drift.py scripts/check_effectiveness_plan.py scripts/check_failure_memory.py scripts/check_harness.py`:
  Passed.
- `.venv/bin/python scripts/check_docs_drift.py`: Passed.
- `.venv/bin/python scripts/check_effectiveness_plan.py --require-report`:
  Passed.
- `.venv/bin/python scripts/check_failure_memory.py`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed; ran 44 Django tests.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with score 96/100, grade A.

## Effectiveness Inclusion

- `include_in_effectiveness_report: true`
- `include_in_comparable_product_task_count: false`
- Reason: this was Harness-maintenance work, not a comparable product-feature
  task.

## Outcome

The target tracks starter-kit commit `de0737abf3808ecbd7eae50fcc7fab119594bd0d`
and adopted the update's target-appropriate validation hardening while keeping
the existing Django project layout and Markdown task-outcome convention.
