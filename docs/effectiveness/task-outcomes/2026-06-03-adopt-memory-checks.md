# 2026-06-03: Adopt Memory Checks

## Task Type

Harness process.

## Request

Run `/harness update` against the refreshed local `harness-starter-kit`
reference.

## Change Surface

- Added decision-memory and failure-memory harness checks.
- Migrated failure notes to the structured detection/prevention format.
- Updated Harness guidance, source tracking, adoption reporting, and the update
  report.

## Verification

- `.venv/bin/python scripts/check_effectiveness_plan.py --require-report`:
  Passed.
- `.venv/bin/python scripts/check_failure_memory.py`: Passed.
- `.venv/bin/python scripts/check_decision_memory.py`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed; ran 44 Django tests.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with baseline score 83/100, grade B+.

## Outcome

The target adopted the kit's new memory-check guidance in a Django-specific
form while keeping `scripts/check_harness.py` as the normal local verification
gate.
