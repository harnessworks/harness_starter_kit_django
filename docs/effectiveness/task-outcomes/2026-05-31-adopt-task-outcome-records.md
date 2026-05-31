# 2026-05-31: Adopt Task Outcome Records

## Task Type

Harness process.

## Request

Proceed with the recommended follow-up to decide and organize whether this
project should record per-task outcome notes.

## Change Surface

- Added a decision record for task outcome records.
- Expanded `docs/effectiveness/task-outcomes/README.md` with triggers, naming,
  and record format.
- Updated Harness adoption and update reports so this follow-up is no longer
  undecided.

## Verification

- First `scripts/check_harness.py` run failed in the docs drift checker because
  a placeholder outcome-record path was documented as inline code.
- The placeholder path was replaced with a real directory reference and example
  filename, and the failure was recorded in `docs/failures/`.
- `.venv/bin/python scripts/check_harness.py`: Passed.

## Outcome

The repository now records lightweight task outcomes for Harness-relevant work,
while ordinary small application changes remain exempt.
