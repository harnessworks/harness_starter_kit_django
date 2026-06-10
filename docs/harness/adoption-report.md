# Harness Adoption Report

## Refresh Note

This report is historical: it records the initial Harness adoption and early
Django setup. As of the latest refresh, Django source, CI, local harness checks,
public board features, authentication, comments, signup, and feedback messages
exist in the target repository.

Completed items that were originally listed as remaining work:

- Django was initialized with `manage.py` and the `config` project package.
- The `harness_starter_kit_django/` app now contains models, views, URLs,
  templates, tests, admin registration, and migrations.
- CI is present in `.github/workflows/harness-check.yml`.
- The local `harness-starter-kit/` clone is ignored and remains reference
  material only.

Follow-up resolved on 2026-05-31: per-task outcome records are now adopted for
Harness-relevant tasks under `docs/effectiveness/task-outcomes/`. See
`docs/decisions/0011-adopt-task-outcome-records.md`.

Follow-up resolved on 2026-06-03: decision-memory and failure-memory checks are
now part of the normal Harness gate. See
`docs/decisions/0013-adopt-decision-and-failure-memory-checks.md`.

Follow-up resolved on 2026-06-10: the Harness update refreshed source tracking
to the canonical starter-kit URL and tightened local memory/effectiveness
validators for command-reference and report-consistency checks. The task
outcome convention now records whether Harness-maintenance work counts as
comparable product-task evidence, and `docs/validation.md` plus
`docs/evaluation.md` now make validation binding and effectiveness boundaries
explicit.

## Target Repository Observed

- Stack and framework: Django was initialized after harness adoption. The root
  entrypoint is `manage.py`, and the project package is `config`.
- Package manager and commands: Python virtual environment with pip and
  `requirements.txt`. Primary commands use `.\.venv\Scripts\python.exe`.
- Existing docs or agent instructions: None detected outside the cloned
  `harness-starter-kit/` reference directory.
- CI or verification path: None detected.
- Monorepo or special layout: None detected.

## Files Added Or Changed

- `AGENTS.md`: Added project-specific agent instructions for the current blank
  workspace and future Django adoption.
- `.gitignore`: Added ignores for the local starter-kit clone and common
  Python/Django local artifacts.
- `docs/decisions/0001-adopt-generic-first-harness.md`: Recorded the choice to
  adopt a generic-first harness until Django source exists.
- `docs/conventions/coding.md`: Added initial coding and future Django
  convention notes.
- `docs/domain/glossary.md`: Added the domain knowledge-store entrypoint.
- `docs/failures/README.md`: Added the failure-memory entrypoint.
- `scripts/check_docs_drift.py`: Added a local Markdown reference drift check.
- `scripts/check_structure.py`: Added a local temporary-file and structure
  drift check.
- `scripts/check_effectiveness_plan.py`: Added adoption-report measurement
  validation.
- `scripts/check_decision_memory.py`: Added Django-specific decision-memory
  review warnings for implementation diffs.
- `scripts/check_failure_memory.py`: Added validation for concrete failure-note
  detection or prevention checks.
- `scripts/check_harness.py`: Added the local verification wrapper.
- `.harness/decision-memory-rules.json`: Added Django path rules for the
  decision-memory check.
- `docs/checklists/harness-review.md`: Added a manual Harness maintenance
  review point.
- `docs/harness/adoption-report.md`: Added this report.
- `requirements.txt`: Added pinned Django environment dependencies.
- `README.md`: Added setup, check, test, migrate, runserver, and harness
  commands.
- `manage.py`: Added by `django-admin startproject config .`.
- `config/`: Added Django settings, root URLs, ASGI, and WSGI modules.
- `docs/decisions/0002-initialize-django-config-project.md`: Recorded the
  Django project package and environment setup decision.
- `harness_starter_kit_django/`: Added the first Django app.
- `docs/decisions/0003-create-harness-starter-kit-django-app.md`: Recorded the
  app naming decision.

## Existing Structures Reused

- No existing docs, CI, package scripts, test commands, lint commands, or agent
  instruction files were present to reuse.
- The Django profile in `harness-starter-kit/templates/profiles/django/` was
  used as reference and adapted into the local verification wrapper.

## Checks Run

```powershell
python scripts\check_harness.py
```

Result: First run failed because the planned future effectiveness-report path
was treated as an existing-file reference. The doc drift check was updated to
allow that planned path, then the full wrapper passed. The wrapper skipped
Django checks because `manage.py` is not present yet.

After Django initialization, the wrapper was rerun and includes Django checks.
It passed `check_docs_drift.py`, `check_structure.py`,
`check_effectiveness_plan.py --require-report`, `manage.py check`, and
`manage.py test`.

Additional Django setup command run:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

Result: Passed. This created the ignored local development database
`db.sqlite3`.

Additional syntax checks run:

```powershell
python -m py_compile scripts\check_docs_drift.py scripts\check_structure.py scripts\check_effectiveness_plan.py scripts\check_harness.py
python -c "import ast, pathlib; [ast.parse(p.read_text(encoding='utf-8'), filename=str(p)) for p in pathlib.Path('scripts').glob('*.py')]"
```

Result: Passed. The generated `scripts\__pycache__` artifact from
`py_compile` was removed after the first syntax check.

## Documentation Updated

- `README.md`: Added project setup and local commands.
- `AGENTS.md`: Added durable agent workflow, rules, and verification commands.
- `docs/conventions/coding.md`: Added Django project conventions.
- `docs/decisions/0001-adopt-generic-first-harness.md`: Added the adoption
  decision.
- `docs/decisions/0002-initialize-django-config-project.md`: Added the Django
  environment decision.
- `docs/decisions/0003-create-harness-starter-kit-django-app.md`: Added the
  first app naming decision.
- `docs/domain/glossary.md`: Added the domain knowledge-store entrypoint.
- `docs/failures/README.md`: Added the failure-memory entrypoint.

## Failure Memory

- Recorded: `docs/failures/0001-docs-drift-windows-venv-command.md`,
  `docs/failures/0002-invalid-comment-form-500.md`,
  `docs/failures/0003-owner-required-anonymous-403.md`,
  `docs/failures/0004-inline-placeholder-path-docs-drift.md`, and
  `docs/failures/0005-subagent-reviewer-mode-ownership.md`.
- Detection or prevention check: `scripts/check_failure_memory.py` validates
  that structured failure records name a concrete check or manual review point.
  `scripts/check_harness.py` runs that validator locally, and
  `.github/workflows/harness-check.yml` runs the wrapper in CI.
- Skipped: Purely transient command mistakes and one-off diagnostics remain in
  final reports unless they reveal a recurring bug path, failed check,
  permission issue, data-loss risk, 5xx path, or cross-environment mismatch.

## Profile Absorption

- Profile reviewed: Django.
- Snippets adopted: `manage.py check`, `manage.py test`, virtual environment
  usage, SQLite ignore rules, and `scripts/check_harness.py`.
- Snippets adapted: The verification wrapper still runs generic harness checks
  before Django checks.
- Snippets skipped or deferred: Tool-specific lint/type configuration remains
  deferred until the project explicitly adopts those tools.

## Drift Checks Added

- Baseline doc or structure hygiene checks: `scripts/check_docs_drift.py` checks
  local Markdown references; `scripts/check_structure.py` rejects temporary and
  backup files while ignoring the local starter-kit clone.
- Memory checks: `scripts/check_decision_memory.py` warns when watched Django
  implementation diffs lack a decision-record change, and
  `scripts/check_failure_memory.py` validates failure-note detection or
  prevention links, including package-script, Make, Just, Maven, Gradle, and Go
  command references when those command families are named in failure records.
- Effectiveness evidence checks:
  `scripts/check_effectiveness_plan.py --require-report` validates adoption and
  effectiveness report structure and flags contradictory effectiveness-report
  completion language.
- Validation binding: `docs/validation.md` names the normal Harness gate and
  focused checks, while `docs/evaluation.md` separates harness health from
  agent effectiveness evidence.
- Target-specific architecture checks: `scripts/check_harness.py` now runs
  Django system checks and tests when `manage.py` exists.
- Not added: Additional import-boundary or service-layer checks remain deferred
  because the app is still small and current Django tests cover the active
  behavior boundaries directly.

## Verification Gate Placement

- Normal completion gate: `scripts/check_harness.py`, run through the project
  virtual environment when available.
- Deterministic behavior checks included in the normal gate:
  `scripts/check_docs_drift.py`, `scripts/check_structure.py`,
  `scripts/check_encoding_hygiene.py`,
  `scripts/check_effectiveness_plan.py --require-report`,
  `scripts/check_failure_memory.py`, `scripts/check_decision_memory.py`,
  `manage.py check`, and `manage.py test`.
- Focused or manual checks outside the normal gate:
  `scripts/check_decision_memory.py --base <pull-request-base-sha>` in pull
  request CI, `/harness review`, `/harness doctor`, and manual review point
  `docs/checklists/harness-review.md`.
- Reasons for focused/manual placement: The PR-base decision-memory check needs
  CI pull-request context, while the local wrapper checks working-tree diffs.
  `/harness review` and `/harness doctor` are diagnostic review workflows
  rather than required checks for every small task. The checklist covers
  judgment-based maintenance items such as subagent reviewer-mode ownership
  that cannot be proven reliably by a local deterministic script.

## Effectiveness Measurement Plan

- Baseline available: No baseline agent-task data exists for this empty target
  repository.
- Comparable tasks to repeat or track: Track the next 3 to 5 agent tasks that
  add or modify the Django project layout, app boundaries, test command,
  migration policy, or verification tooling.
- Primary metric: First-pass verification with `python scripts\check_harness.py`,
  decision-memory warnings resolved or explained, and count of wrong-file edits
  outside the intended task boundary.
- Review window: Review after the next 5 agent changes or after the first
  Django app and test command are committed, whichever comes first.
- Results location: Record observations in a future
  `docs/harness/effectiveness-report.md`.
- Task outcome records location: Record per-task observations under
  `docs/effectiveness/task-outcomes/`.

## Assumptions

- The working directory itself is the target repository, even though no `.git`
  directory was present.
- Django was initialized with project package `config`.
- Python is available locally for stdlib harness checks.
- No CI or package manager should be introduced until the application stack
  exists.

## Remaining Manual Steps

- Historical item completed: `python scripts\check_harness.py` was run after
  adoption and is now wired into CI.
- Historical item completed: `harness-starter-kit/` is ignored and treated as
  local reference material only.
- Historical item completed: `harness_starter_kit_django/` now contains the
  board application's models, views, URLs, templates, tests, admin
  registration, and migrations.
- Historical item completed: CI exists in `.github/workflows/harness-check.yml`;
  see `docs/harness/harness-update-report.md` for the update record.
- Historical item completed: per-task outcome records are now adopted for
  Harness-relevant tasks under `docs/effectiveness/task-outcomes/`.

## Notes For Future Agents

- Do not infer architecture from the starter kit. Use it as reference material.
- Replace conditional Django guidance with concrete project commands once
  `manage.py` exists.
- Add project-specific drift checks only after there are real boundaries to
  enforce.
