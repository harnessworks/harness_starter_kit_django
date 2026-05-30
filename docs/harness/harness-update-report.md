# Harness Update Report

## Kit Source

- URL: `https://github.com/baskduf/harness-starter-kit`
- Previous commit: `cf1e288238959ed80e7dd0987afb1af93c3a59e7`
- Current commit: `6ac7e8b287c24f82b8ec99a448dc8b695ecfdd68`
- Reference clone state: Clean and fast-forwarded from `cf1e288` to
  `6ac7e8b`.

## Target State

- Branch/status before update: `main` tracking the origin main branch, clean.
- Existing harness files reviewed: `AGENTS.md`, `.harness/source.json`,
  `README.md`, `docs/decisions/`, `docs/conventions/`, `docs/domain/`,
  `docs/failures/`, `docs/harness/`, local harness scripts,
  `.github/workflows/harness-check.yml`, `.gitattributes`, and `.gitignore`.
- New kit guidance reviewed: clarified failure-memory trigger for user-visible
  runtime failures and high-risk bug paths, task outcome record template,
  effectiveness-report source-record guidance, harness theory document,
  Harness Doctor wording updates, and `/harness update` failure-memory wording.

## Applied

- Updated `.harness/source.json` to track
  `6ac7e8b287c24f82b8ec99a448dc8b695ecfdd68`.
- Updated `AGENTS.md` so failure-memory guidance explicitly covers
  user-visible runtime failures, 5xx errors, crashes, security or permission
  bugs, data-loss risks, and previously identified bug paths.
- Updated `docs/failures/README.md` with the same clarified failure-note
  trigger.
- Updated `scripts/check_effectiveness_plan.py` to require a task outcome
  records location in adoption effectiveness plans.
- Updated `docs/harness/adoption-report.md` with the target task outcome
  records location.
- Added `docs/effectiveness/task-outcomes/README.md` as the target location for
  optional per-task outcome records.
- Refreshed this update report with the latest applied, skipped, and manual
  review items.

## Skipped

- Did not copy starter-kit theory, task-outcome template, localized READMEs,
  site files, installer tests, repository hygiene tests, or public OSS docs.
  They remain reference material in the ignored `harness-starter-kit/` clone.
- Did not replace this target's `AGENTS.md` with the generic template. The
  local file contains Django-specific commands, directory rules, migration
  policy, and commit rules that should remain the source of truth.
- Did not replace local drift scripts wholesale. Only the
  task-outcome-location check was adapted because it fits this repository's
  existing effectiveness measurement plan.
- Did not add a new failure note for this update because the relevant
  user-visible 500 path is already recorded in
  `docs/failures/0002-invalid-comment-form-500.md`.

## Manual Review

- Decide later whether to fill per-task records under
  `docs/effectiveness/task-outcomes/` for future comparable agent tasks.
- Decide later whether this repository should adopt public OSS files such as
  `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, issue templates, or a pull
  request template.
- Decide later whether to keep an ignored local `harness-starter-kit/` clone
  between updates or remove it after each update. It must not be committed.

## Checks Run

- `.venv/bin/python scripts/check_harness.py`: Passed.
- `.venv/bin/python harness-starter-kit/scripts/harness_doctor.py --target .`:
  Passed with an automated baseline score of 83/100, grade B+.
- `git diff --check`: Passed.

## Failure Memory

- Recorded: none.
- Skipped: This update was a proactive kit refresh. The runtime 500 failure
  mode that motivated the clarified upstream guidance is already covered by
  `docs/failures/0002-invalid-comment-form-500.md`.

## Source Tracking

- `.harness/source.json`: Updated to
  `6ac7e8b287c24f82b8ec99a448dc8b695ecfdd68`.
