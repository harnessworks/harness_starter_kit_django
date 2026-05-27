# Harness Adoption Report

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
- `scripts/check_harness.py`: Added the local verification wrapper.
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
- Target-specific architecture checks: `scripts/check_harness.py` now runs
  Django system checks and tests when `manage.py` exists.
- Not added: Import-boundary, model, view, or service-layer checks would be
  speculative before any Django app exists.

## Effectiveness Measurement Plan

- Baseline available: No baseline agent-task data exists for this empty target
  repository.
- Comparable tasks to repeat or track: Track the next 3 to 5 agent tasks that
  add or modify the Django project layout, app boundaries, test command,
  migration policy, or verification tooling.
- Primary metric: First-pass verification with `python scripts\check_harness.py`
  and count of wrong-file edits outside the intended task boundary.
- Review window: Review after the next 5 agent changes or after the first
  Django app and test command are committed, whichever comes first.
- Results location: Record observations in a future
  `docs/harness/effectiveness-report.md`.

## Assumptions

- The working directory itself is the target repository, even though no `.git`
  directory was present.
- Django was initialized with project package `config`.
- Python is available locally for stdlib harness checks.
- No CI or package manager should be introduced until the application stack
  exists.

## Remaining Manual Steps

- Run `python scripts\check_harness.py` after adoption.
- Decide whether to remove or keep ignoring `harness-starter-kit/` before
  committing. The recommended action is to remove it before commit; keeping the
  `.gitignore` entry is still useful protection during future harness reviews.
- Add real models, views, URLs, templates, or tests to
  `harness_starter_kit_django/` when the app's domain responsibility is known.
- Add CI after the repository has settled on where it will be hosted.

## Notes For Future Agents

- Do not infer architecture from the starter kit. Use it as reference material.
- Replace conditional Django guidance with concrete project commands once
  `manage.py` exists.
- Add project-specific drift checks only after there are real boundaries to
  enforce.
