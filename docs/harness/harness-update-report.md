# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `aa32432dd70759d9a822fdbdf4593a622cc1d37e`
- Current commit: `026920b5fd3884960764e3196ead389961db41b6`
- Reference clone state: Clean and fast-forwarded from `aa32432` to `026920b`.

## Target State

- Branch/status before update: main tracking origin/main, clean.
- Existing harness files reviewed: `AGENTS.md`, `README.md`,
  `docs/harness/adoption-report.md`, `docs/conventions/coding.md`,
  `docs/domain/glossary.md`, `docs/failures/`,
  `.github/workflows/harness-check.yml`, `scripts/check_harness.py`,
  `scripts/check_docs_drift.py`, `scripts/check_structure.py`, and current
  Django tests. New kit guidance reviewed: encoding hygiene check, Django
  profile priority notes, commit convention guidance, Android profile, and
  broader adoption workflow notes.

## Applied

- Updated `.harness/source.json` from the previous starter-kit commit to
  `026920b5fd3884960764e3196ead389961db41b6`.
- Added `scripts/check_encoding_hygiene.py` and wired it into
  `scripts/check_harness.py` to detect invalid UTF-8 and common mojibake
  markers in localized project text files.
- Updated `scripts/check_docs_drift.py` with the latest optional generated path
  references from the starter kit.
- Updated `AGENTS.md` to make Conventional Commits the explicit commit subject
  rule for this repository.
- Updated `README.md` to include the encoding hygiene check in the harness
  artifact map.

## Skipped

- Did not copy starter-kit templates wholesale; the current Django project
  already has tailored `AGENTS.md`, docs, and scripts.
- Did not copy starter-kit `harness_doctor.py` into this target. The doctor is
  run from the local reference clone and remains reference tooling rather than
  application source.
- Did not copy starter-kit test files for the kit itself; this target keeps its
  own Django tests and local harness wrapper.
- Did not adopt Android profile files, mobile checklists, site assets, or
  starter-kit website changes because they are reference-only for this Django
  target.
- Did not add a new failure note because this update was proactive and did not
  fix a failed local check or CI run.

## Manual Review

- Decide later whether to add Ruff or mypy as explicit project tooling.
- Add architecture-boundary checks only if the app grows beyond the current
  small CRUD surface.
- Add real failure records under `docs/failures/` when repeated mistakes or
  rejected approaches appear.

## Checks Run

- `.\.venv\Scripts\python.exe scripts\check_encoding_hygiene.py`: Passed.
- `.\.venv\Scripts\python.exe scripts\check_docs_drift.py`: Passed.
- `.\.venv\Scripts\python.exe scripts\check_harness.py`: Passed.
- `.\.venv\Scripts\python.exe harness-starter-kit\scripts\harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh, not a response to a failed
  CI run, failed harness check, repeated agent mistake, or new
  cross-environment mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `026920b5fd3884960764e3196ead389961db41b6`.
