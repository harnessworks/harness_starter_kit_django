# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `a8f98842a414f058c19d29ef945bce8237c7eb0d`
- Current commit: `08513edf7455815312175f5a88f161cb42405305`
- Reference clone state: Clean and fast-forwarded from `a8f9884` to
  `08513ed`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, local harness scripts,
  `.github/workflows/harness-check.yml`, `.gitattributes`, and `.gitignore`.
- New kit guidance reviewed: `/harness review sub-agent` invocation mode,
  `/harness review` fallback clarification, review report invocation field,
  starter-kit README prompt updates, component map updates, site updates, and
  starter-kit repository hygiene tests.

## Applied

- Added target command routing for `/harness review sub-agent` to `AGENTS.md`
  so explicit subagent review requests are distinguished from ordinary
  `/harness review` requests.
- Updated `.harness/source.json` to track
  `08513edf7455815312175f5a88f161cb42405305`.
- Refreshed this update report with the latest applied, skipped, and manual
  review items.
- Added a Harness task outcome record for this workflow update.

## Skipped

- Did not copy starter-kit `/harness review` templates, example reports,
  localized README text, site updates, or repository hygiene tests. They remain
  reference material in the ignored `harness-starter-kit/` clone.
- Did not replace this target's `AGENTS.md` with the generic template. The
  local file contains Django-specific commands, directory rules, migration
  policy, and commit rules that should remain the source of truth.
- Did not add new CI, pre-commit hooks, package scripts, dependencies, or
  architecture checks because the upstream changes were command documentation
  and starter-kit repository hygiene changes, not target Django workflow
  changes.
- Did not duplicate the full `/harness review` invocation-mode procedure into
  `AGENTS.md` because `AGENTS.md` routes the command to the refreshed reference
  command file.
- Did not add a new failure note because this was a proactive kit refresh and
  did not fix a user-visible runtime failure, high-risk bug path, failed CI run,
  failed harness check, repeated agent mistake, or cross-environment mismatch.

## Manual Review

- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether to keep an ignored local `harness-starter-kit/` clone
  between updates or remove it after each update. It must not be committed.
- Decide later whether the target README should document
  `/harness review sub-agent` directly for human readers, or whether command
  routing in `AGENTS.md` is sufficient.

## Checks Run

- `git diff --check`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh and did not fix a
  user-visible runtime failure, high-risk bug path, failed CI run, failed
  harness check, repeated agent mistake, or cross-environment mismatch.

## Source Tracking

- `.harness/source.json`: Updated to
  `08513edf7455815312175f5a88f161cb42405305`.
