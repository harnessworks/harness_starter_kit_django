# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `832ede6c368c3d929a20c7e429ac3ad83ea84408`
- Current commit: `7d6fac27d69229bfc954b662d24dea9984b1bc50`
- Reference clone state: Clean and fast-forwarded from local `28adced` to
  `7d6fac2` after confirming the expected GitHub remote.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, local harness scripts,
  `.github/workflows/harness-check.yml`, `.gitattributes`, and `.gitignore`.
- Pre-existing target changes: none.
- Dirty target handling: Latest confirmed kit source was used; target file
  patches were applied only after review; no pre-existing dirty-file patches
  were deferred.
- New kit guidance reviewed: dirty-worktree source-tracking rules, decision
  memory warnings, verification gate-placement guidance, concrete failure-memory
  validation, updated adoption-report requirements, generic CI decision-memory
  checks, maintenance checklists, profile guidance, templates, examples, and
  starter-kit repository tests.

## Applied

- Added `.harness/decision-memory-rules.json` with Django-specific watched paths
  and ignored tests/migrations/docs/script paths.
- Added `scripts/check_decision_memory.py` and wired it into
  `scripts/check_harness.py`.
- Added `scripts/check_failure_memory.py`, a failure-note template, and a
  Harness maintenance checklist.
- Migrated existing `docs/failures/*.md` records into the structured
  detection/prevention format.
- Expanded `scripts/check_effectiveness_plan.py` to validate gate-placement and
  failure-memory linkage in adoption reports.
- Updated `.github/workflows/harness-check.yml` with `fetch-depth: 0` and a
  pull-request-only decision-memory check against the PR base SHA.
- Updated `AGENTS.md`, `README.md`, `docs/failures/README.md`, and
  `docs/harness/adoption-report.md` for the new memory checks and gate
  placement.
- Added decision record
  `docs/decisions/0013-adopt-decision-and-failure-memory-checks.md`.
- Added Harness task outcome record
  `docs/effectiveness/task-outcomes/2026-06-03-adopt-memory-checks.md`.
- Updated `.harness/source.json` to track
  `7d6fac27d69229bfc954b662d24dea9984b1bc50`.
- Refreshed this update report.

## Skipped

- Did not replace this target's `AGENTS.md` with the generic template. The local
  file contains Django-specific commands, directory rules, migration policy, and
  commit rules that remain the source of truth.
- Did not copy starter-kit profiles, examples, localized READMEs, release
  notes, roadmap, repository tests, or site content. They remain reference
  material in the ignored `harness-starter-kit/` clone.
- Did not add pre-commit hooks, package scripts, new dependencies, formatters,
  linters, type checkers, or services.
- Did not adopt the generic scheduled CI workflow wholesale. The target kept
  its existing GitHub Actions wrapper gate and added only the PR-base
  decision-memory step that fits the new check.
- Did not add broad import-boundary or service-layer checks because this Django
  app remains small and current Django tests cover active behavior boundaries.

## Manual Review

- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether `/harness doctor` should influence target-specific
  adoption-clarity work; the score remains a baseline scan, not a required
  quality gate.
- Decide later whether additional architecture-boundary checks are useful as
  the Django app grows.

## Checks Run

- `git diff --check`: Passed.
- `.venv/bin/python -m py_compile scripts/check_effectiveness_plan.py scripts/check_decision_memory.py scripts/check_failure_memory.py scripts/check_harness.py`:
  Passed.
- `.venv/bin/python scripts/check_effectiveness_plan.py --require-report`:
  Passed.
- `.venv/bin/python scripts/check_failure_memory.py`: Passed.
- `.venv/bin/python scripts/check_decision_memory.py`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed; ran 44 Django tests.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with automated baseline score 83/100, grade B+.

## Failure Memory

- Recorded: none for this update; it adopted preventative Harness checks and did
  not fix a new user-visible runtime failure, failed CI run, data-loss risk,
  permission bug, 5xx path, or newly observed repeated mistake.
- Detection/prevention check: `scripts/check_failure_memory.py` validates all
  structured failure notes; `scripts/check_harness.py` runs it locally and in
  CI.
- Skipped: No new failure record was added because this update did not discover
  a new recurring failure path. Existing records were migrated and validated.

## Source Tracking

- `.harness/source.json`: Updated to
  `7d6fac27d69229bfc954b662d24dea9984b1bc50`.
- Deferred target patches: none.
