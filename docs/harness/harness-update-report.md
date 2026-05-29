# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `026920b5fd3884960764e3196ead389961db41b6`
- Current commit: `cffcaece3a662a5737a2bcd5651a61e46c5b5b80`
- Reference clone state: Clean and fast-forwarded from `026920b` to `cffcaec`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `docs/decisions/`, `docs/conventions/`, `docs/domain/`, `docs/failures/`,
  `docs/harness/`, `.github/workflows/harness-check.yml`, and local scripts.
- New kit guidance reviewed: project analysis rule, OSS hygiene files,
  profile README consistency checks, docs drift optional references, and
  updated doctor baseline wording.

## Applied

- Updated `.harness/source.json` to track
  `cffcaece3a662a5737a2bcd5651a61e46c5b5b80`.
- Added the starter kit's project analysis rule to `AGENTS.md` so ordinary
  requests such as "analyze this project" direct agents through `README.md`,
  `.harness/source.json`, decisions, conventions, domain docs, failure notes,
  and local harness scripts before summarizing.
- Added `.gitattributes` with LF text normalization and binary image handling
  from the starter kit's OSS hygiene update.
- Updated `README.md` to describe this repository as a Harness dogfood project,
  include the project analysis rule in the artifact map, and record the recent
  analysis-quality observation.
- Refreshed this update report with the latest applied and skipped items.

## Skipped

- Did not copy issue templates, pull request template, `CONTRIBUTING.md`,
  `CODE_OF_CONDUCT.md`, `SECURITY.md`, or `CHANGELOG.md`. They are useful OSS
  hygiene defaults, but this target has not chosen a public contribution
  workflow yet.
- Did not copy starter-kit profile maintenance docs or profile consistency
  tests because this Django target does not maintain reusable kit profiles.
- Did not copy starter-kit `harness_doctor.py` into this target. The doctor
  remains reference tooling run from the local `harness-starter-kit/` clone.
- Did not overwrite local drift scripts wholesale; the current scripts are
  already tailored to this Django repository.
- Did not add a new failure note because this update was proactive and did not
  fix a failed CI run, failed harness check, repeated agent mistake, or
  cross-environment mismatch.

## Manual Review

- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, and issue/PR templates.
- Decide later whether to rename `evaulation/` to evaluation; that spelling
  cleanup touches documented paths and should be handled as its own change.
- Keep using decision records for architecture, database, test runner,
  formatter, linter, CI, and deployment assumptions.

## Checks Run

- `.\.venv\Scripts\python.exe scripts\check_harness.py`: Passed.
- `.\.venv\Scripts\python.exe harness-starter-kit\scripts\harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.
- `git diff --check`: Passed.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh, not a response to a failed
  CI run, failed harness check, repeated agent mistake, or new
  cross-environment mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `cffcaece3a662a5737a2bcd5651a61e46c5b5b80`.
