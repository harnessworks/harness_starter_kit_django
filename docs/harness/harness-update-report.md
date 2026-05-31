# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `d076aa9ff4755e0ea980fd7919c8bd32dc109c03`
- Current commit: `a8f98842a414f058c19d29ef945bce8237c7eb0d`
- Reference clone state: Clean and fast-forwarded from `d076aa9` to
  `a8f9884`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, local harness scripts,
  `.github/workflows/harness-check.yml`, `.gitattributes`, and `.gitignore`.
- New kit guidance reviewed: `/harness review` subagent availability and
  fallback reporting workflow, review report template and example updates,
  starter-kit README image change, and starter-kit repository hygiene tests.

## Applied

- Updated `.harness/source.json` to track
  `a8f98842a414f058c19d29ef945bce8237c7eb0d`.
- Refreshed this update report with the latest applied, skipped, and manual
  review items.

## Skipped

- Did not copy starter-kit `/harness review` templates, example reports,
  starter-kit README media, or repository hygiene tests. They remain reference
  material in the ignored `harness-starter-kit/` clone.
- Did not replace this target's `AGENTS.md` with the generic template. The
  local file contains Django-specific commands, directory rules, migration
  policy, and commit rules that should remain the source of truth.
- Did not add new CI, pre-commit hooks, package scripts, dependencies, or
  architecture checks because the upstream changes were documentation and
  starter-kit repository hygiene changes, not target Django workflow changes.
- Did not duplicate the new `/harness review` subagent fallback text into
  `AGENTS.md` because `AGENTS.md` already routes the command to the refreshed
  reference command file.
- Did not add a new failure note because this was a proactive kit refresh and
  did not fix a user-visible runtime failure, high-risk bug path, failed CI run,
  failed harness check, repeated agent mistake, or cross-environment mismatch.

## Manual Review

- Resolved after the update: per-task records are now adopted for
  Harness-relevant tasks under `docs/effectiveness/task-outcomes/`; see
  `docs/decisions/0011-adopt-task-outcome-records.md`.
- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether to keep an ignored local `harness-starter-kit/` clone
  between updates or remove it after each update. It must not be committed.
- Decide later whether the target README should document `/harness review`
  reviewer-mode reporting directly, or whether command routing in `AGENTS.md`
  is sufficient.

## Checks Run

- `.venv/bin/python scripts/check_harness.py`: Passed.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.
- `git diff --check`: Passed.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh and did not fix a
  user-visible runtime failure, high-risk bug path, failed CI run, failed
  harness check, repeated agent mistake, or cross-environment mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `a8f98842a414f058c19d29ef945bce8237c7eb0d`.
