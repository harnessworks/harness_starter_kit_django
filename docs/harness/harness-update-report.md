# Harness Update Report

## Kit Source

- URL: `https://github.com/harnessworks/harness-starter-kit`
- Previous commit: `7d6fac27d69229bfc954b662d24dea9984b1bc50`
- Current commit: `de0737abf3808ecbd7eae50fcc7fab119594bd0d`
- Reference clone state: Clean and fast-forwarded from `7d6fac2` to
  `de0737a` after confirming the local `baskduf` remote. The refreshed kit now
  uses `harnessworks` as the canonical source URL; both remotes were verified to
  resolve `main` to `de0737abf3808ecbd7eae50fcc7fab119594bd0d`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, `docs/evaluation.md`,
  `docs/validation.md`, `docs/templates/`, `docs/effectiveness/`, local
  harness scripts, `.github/workflows/harness-check.yml`, and
  `requirements.txt`.
- Pre-existing target changes: none.
- Dirty target handling: Latest confirmed kit source was used; no pre-existing
  dirty target files required deferral or manual review.

## Applied

- Updated `.harness/source.json` to the canonical starter-kit URL and commit
  `de0737abf3808ecbd7eae50fcc7fab119594bd0d`.
- Added the refreshed task-outcome evidence rule to `AGENTS.md`.
- Added `vendor/` to the local docs-drift optional references.
- Hardened `scripts/check_failure_memory.py` so failure-note detection sections
  validate package-script, Make, Just, Maven, Gradle, and Go command references
  when those command families are named.
- Added contradictory completion-language detection to
  `scripts/check_effectiveness_plan.py`.
- Updated `docs/harness/adoption-report.md` and
  `docs/effectiveness/task-outcomes/README.md` for the refreshed task-outcome
  and validation guidance.
- Added `docs/validation.md` to bind local check scripts to the normal Harness
  gate and focused validation commands.
- Added `docs/evaluation.md`,
  `docs/effectiveness/effectiveness-report-harness-maintenance.md`, and
  `docs/templates/effectiveness-report.md` to separate harness health from
  effectiveness evidence and preserve non-comparable maintenance outcomes.
- Updated `README.md` to include the new validation and evaluation artifacts in
  the Harness artifact map.
- Added task outcome record
  `docs/effectiveness/task-outcomes/2026-06-10-refresh-harness-source-and-memory-checks.md`.
- Refreshed this update report.

## Skipped

- Did not replace this target's `AGENTS.md` with the generic template. The
  local file contains Django-specific commands, directory rules, migration
  policy, and commit rules that remain the source of truth.
- Did not copy starter-kit profiles, localized READMEs, release notes, roadmap,
  repository tests, site content, or example dogfood reports. They remain
  reference material in the ignored `harness-starter-kit/` clone.
- Did not add the kit's YAML task-outcome template or validator wholesale. This
  target already uses Markdown task-outcome records, so the update adapted the
  inclusion guidance to the existing convention and added an effectiveness
  report template instead of migrating formats.
- Did not add pre-commit hooks, package scripts, new dependencies, formatters,
  linters, type checkers, CI providers, or services.
- Did not change the local reference clone remote URL; it remains on the older
  `baskduf` remote alias even though source tracking now records the canonical
  `harnessworks` URL.

## Manual Review

- Decide later whether to update the local `harness-starter-kit` clone remote
  from `https://github.com/baskduf/harness-starter-kit` to
  `https://github.com/harnessworks/harness-starter-kit`.
- Decide later whether this repository should migrate Markdown task-outcome
  records to the starter kit's YAML evidence schema.
- Decide later whether additional architecture-boundary checks are useful as
  the Django app grows.

## Checks Run

- `git diff --check`: Passed.
- `.venv/bin/python -m py_compile scripts/check_docs_drift.py scripts/check_effectiveness_plan.py scripts/check_failure_memory.py scripts/check_harness.py`:
  Passed.
- `.venv/bin/python scripts/check_docs_drift.py`: Passed.
- `.venv/bin/python scripts/check_effectiveness_plan.py --require-report`:
  Passed.
- `.venv/bin/python scripts/check_failure_memory.py`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed; ran 44 Django tests.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with score 96/100, grade A, and no coupling findings detected.

## Failure Memory

- Recorded: none for this update; it did not fix a newly observed
  user-visible runtime failure, failed CI run, data-loss risk, permission bug,
  5xx path, or repeated agent mistake.
- Detection/prevention check: `scripts/check_failure_memory.py` validates all
  structured failure notes; `scripts/check_harness.py` runs it locally and in
  CI.
- Skipped: No new failure record was added because this update adopted
  preventative Harness validation hardening rather than documenting a newly
  observed recurring failure path.

## Source Tracking

- `.harness/source.json`: Updated to
  `de0737abf3808ecbd7eae50fcc7fab119594bd0d` with canonical URL
  `https://github.com/harnessworks/harness-starter-kit`.
- Deferred target patches: none.

## Decision Memory

- Covered by existing ADRs:
  `docs/decisions/0005-track-harness-source-and-ci.md` covers source tracking,
  and `docs/decisions/0013-adopt-decision-and-failure-memory-checks.md` covers
  local memory-check validation.
- New ADR: none. The update hardens existing Harness validation and reporting
  behavior without changing the Django project layout, database policy, test
  runner, dependency manager, CI provider, deployment assumptions, API surface,
  or durable data model.
