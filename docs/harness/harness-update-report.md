# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `cffcaece3a662a5737a2bcd5651a61e46c5b5b80`
- Current commit: `cf1e288238959ed80e7dd0987afb1af93c3a59e7`
- Reference clone state: Cloned cleanly into ignored local
  `harness-starter-kit/` at `cf1e288`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, `.github/workflows/harness-check.yml`,
  local harness scripts, `.gitattributes`, and `.gitignore`.
- New kit guidance reviewed: `/harness refresh` workflow, compact generic
  agent instructions, Python 3 validation wording, roadmap and contributor
  guidance, release notes, prompt-first adoption ADR, and updated repository
  hygiene tests.

## Applied

- Updated `.harness/source.json` to track
  `cf1e288238959ed80e7dd0987afb1af93c3a59e7`.
- Added Harness command routing to `AGENTS.md` for `/harness doctor`,
  `/harness update`, and `/harness refresh`, adapted to this repository's
  local reference-clone policy.
- Refreshed this update report with the latest applied, skipped, and manual
  review items.

## Skipped

- Did not copy starter-kit `CHANGELOG.md`, `CONTRIBUTING.md`, `ROADMAP.md`,
  localized READMEs, issue templates, pull request template,
  `CODE_OF_CONDUCT.md`, or `SECURITY.md`. They are useful for the public
  starter kit, but this Django target has not chosen a broader public
  contribution workflow.
- Did not copy the refresh command document into this target. It remains
  reference material in the ignored `harness-starter-kit/` clone, while
  `AGENTS.md` now routes future refresh requests to it.
- Did not replace this target's `AGENTS.md` with the compact generic template.
  The local file already contains Django-specific commands, directory rules,
  migration policy, and commit rules that should remain the source of truth.
- Did not overwrite local drift scripts with starter-kit templates. The current
  scripts are already tailored to this Django repository and pass locally.
- Did not adopt starter-kit profile maintenance tests, site files, installer
  tests, or README prompt drift tests because this target does not maintain the
  starter kit itself.
- Did not add a new failure note because this update was proactive and did not
  fix a failed CI run, failed harness check, repeated agent mistake, or
  cross-environment mismatch.

## Manual Review

- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether to keep an ignored local `harness-starter-kit/` clone
  between updates or remove it after each update. It must not be committed.
- Keep using decision records for architecture, database, test runner,
  formatter, linter, CI, and deployment assumptions.

## Checks Run

- `.venv/bin/python scripts/check_harness.py`: Passed.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.
- `git diff --check`: Passed.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh, not a response to a failed
  CI run, failed harness check, repeated agent mistake, or new
  cross-environment mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `cf1e288238959ed80e7dd0987afb1af93c3a59e7`.
