# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `b291ae74eb7ae80415f277ac99c37a818ef21200`
- Current commit: `f03a3384d280e2d32bab0fb782110ae4af069d45`
- Reference clone state: Clean and fast-forwarded from `b291ae7` to `f03a338`.

## Target State

- Branch/status before update: main tracking origin/main, clean.
- Existing harness files reviewed: `AGENTS.md`, `README.md`,
  `docs/harness/adoption-report.md`, `docs/conventions/coding.md`,
  `scripts/check_harness.py`, `scripts/check_docs_drift.py`,
  `scripts/check_structure.py`, and current Django tests.

## Applied

- Updated `.harness/source.json` from the previous starter-kit commit to
  `f03a3384d280e2d32bab0fb782110ae4af069d45`.
- Added an explicit failure-memory rule to `AGENTS.md` for failed CI runs,
  failed harness checks, repeated agent mistakes, and cross-environment
  mismatches.
- Recorded the prior CI docs-drift failure in
  `docs/failures/0001-docs-drift-windows-venv-command.md`.
- Updated `scripts/check_docs_drift.py` to align with the latest starter-kit
  command detection approach for virtual-environment Python commands.

## Skipped

- Did not copy starter-kit templates wholesale; the current Django project
  already has tailored `AGENTS.md`, docs, and scripts.
- Did not add Ruff, mypy, pre-commit, import-linter, or vulture. Those remain
  useful future candidates but would introduce new tools beyond this refresh.
- Did not copy the starter-kit internal GitHub Actions workflow because it is
  for testing the kit itself, not this Django project.
- Did not copy the starter kit validation page. This target already
  documents local validation in README and harness reports; a target-specific
  validation page can be added later if the workflow grows.

## Manual Review

- Decide later whether to add Ruff or mypy as explicit project tooling.
- Add architecture-boundary checks after the app grows beyond one small CRUD
  surface.
- Add real failure records under `docs/failures/` when repeated mistakes or
  rejected approaches appear.

## Checks Run

- `wsl bash -lc "cd /mnt/c/Users/SSAFY/Desktop/django && python3 scripts/check_docs_drift.py"`:
  Passed.
- `.\.venv\Scripts\python.exe scripts\check_docs_drift.py`: Passed.
- `.\.venv\Scripts\python.exe scripts\check_harness.py`: Passed.
- `.\.venv\Scripts\python.exe harness-starter-kit\scripts\harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.

## Failure Memory

- Recorded: `docs/failures/0001-docs-drift-windows-venv-command.md`
- Skipped: None. This update was directly motivated by a failed CI run and a
  cross-environment docs drift mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `f03a3384d280e2d32bab0fb782110ae4af069d45`.
