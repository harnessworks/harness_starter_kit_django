# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: Unknown in target tracking; local reference clone was at
  `775f513` before the update.
- Current commit: `b291ae74eb7ae80415f277ac99c37a818ef21200`
- Reference clone state: Clean and fast-forwarded from `775f513` to `b291ae7`.

## Target State

- Branch/status before update: main tracking origin/main, clean.
- Existing harness files reviewed: `AGENTS.md`, `README.md`,
  `docs/harness/adoption-report.md`, `docs/conventions/coding.md`,
  `scripts/check_harness.py`, `scripts/check_docs_drift.py`,
  `scripts/check_structure.py`, and current Django tests.

## Applied

- Created `.harness/source.json` to record the starter-kit source commit.
- Added `.github/workflows/harness-check.yml` to run the existing local harness
  verification command in GitHub Actions.
- Added commit and PR hygiene rules to `AGENTS.md`.
- Updated README harness output map to include source tracking and CI.
- Added decision record
  `docs/decisions/0005-track-harness-source-and-ci.md`.
- Updated `scripts/check_docs_drift.py` so source tracking references are known
  harness metadata.

## Skipped

- Did not copy starter-kit templates wholesale; the current Django project
  already has tailored `AGENTS.md`, docs, and scripts.
- Did not add Ruff, mypy, pre-commit, import-linter, or vulture. Those remain
  useful future candidates but would introduce new tools beyond this refresh.
- Did not copy the starter-kit internal GitHub Actions workflow because it is
  for testing the kit itself, not this Django project.

## Manual Review

- Decide later whether to add Ruff or mypy as explicit project tooling.
- Add architecture-boundary checks after the app grows beyond one small CRUD
  surface.
- Add real failure records under `docs/failures/` when repeated mistakes or
  rejected approaches appear.

## Checks Run

- `.\.venv\Scripts\python.exe scripts\check_harness.py`: Passed after
  adjusting this report so branch tracking text is not mistaken for a file path.
- `.\.venv\Scripts\python.exe harness-starter-kit\scripts\harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.

## Source Tracking

- `.harness/source.json`: Created.
