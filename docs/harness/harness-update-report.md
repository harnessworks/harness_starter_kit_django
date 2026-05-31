# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `08513edf7455815312175f5a88f161cb42405305`
- Current commit: `832ede6c368c3d929a20c7e429ac3ad83ea84408`
- Reference clone state: Clean and fast-forwarded from `08513ed` to
  `832ede6`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, local harness scripts,
  `.github/workflows/harness-check.yml`, `.gitattributes`, and `.gitignore`.
- New kit guidance reviewed: parent/orchestrator ownership of `/harness review
  sub-agent` reviewer mode and fallback reason, the restricted reviewer
  subagent prompt, updated review report templates/examples, starter-kit
  failure memory for the subagent reviewer-mode issue, and starter-kit
  repository hygiene tests.

## Applied

- Clarified target command routing for `/harness review sub-agent` in
  `AGENTS.md` so reviewer mode and fallback reason are parent/orchestrator-owned
  and not copied from subagent output.
- Updated `.harness/source.json` to track
  `832ede6c368c3d929a20c7e429ac3ad83ea84408`.
- Refreshed this update report with the latest applied, skipped, and manual
  review items.
- Added target failure memory for the subagent reviewer-mode ownership mistake.
- Added a Harness task outcome record for this workflow update.

## Skipped

- Did not copy starter-kit `/harness review` templates, example reports, or
  repository hygiene tests. They remain reference material in the ignored
  `harness-starter-kit/` clone.
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

## Manual Review

- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether to keep an ignored local `harness-starter-kit/` clone
  between updates or remove it after each update. It must not be committed.
- Decide later whether the target README should document `/harness review`
  commands directly for human readers, or whether command routing in
  `AGENTS.md` is sufficient.

## Checks Run

- `git diff --check`: Passed.
- `.venv/bin/python scripts/check_harness.py`: Passed.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.

## Failure Memory

- Recorded: `docs/failures/0005-subagent-reviewer-mode-ownership.md`.
- Skipped: none.

## Source Tracking

- `.harness/source.json`: Updated to
  `832ede6c368c3d929a20c7e429ac3ad83ea84408`.
