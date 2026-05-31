# 2026-05-31: Refresh Harness Review Sub-Agent Mode

## Task Type

Harness process

## Request

Run `/harness update` against the latest local Harness Starter Kit reference.

## Change Surface

Updated Harness command routing, source tracking, and the Harness update
report. The upstream change clarified `/harness review` versus
`/harness review sub-agent` behavior.

## Verification

`git diff --check` passed. `.venv/bin/python scripts/check_harness.py` passed,
including Django's 44 tests. `.venv/bin/python
harness-starter-kit/scripts/harness_doctor.py --target .` passed with an
automated baseline score of 83/100, grade B+.

## Outcome

The target now routes explicit subagent review requests without changing the
Django application workflow or copying starter-kit-only repository hygiene
tests.
