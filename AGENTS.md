# AGENTS.md

## Project Overview

This repository is a Django project. The root entrypoint is `manage.py`, and
the Django project package is `config`. The first app package is
`harness_starter_kit_django`.

Treat the current repository root as the project root. Treat
`harness-starter-kit/` as local reference material only; do not edit it as part
of normal project work.

## Commands

Use the project virtual environment when running local commands:

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe scripts\check_harness.py
```

For first-time local database setup:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

If the project later standardizes on a task runner, update this section instead
of adding parallel command docs.

## Directory Rules

- Keep Django project settings, root URL configuration, ASGI, and WSGI files in
  `config/`.
- Keep app-specific models, views, admin registration, tests, and migrations in
  `harness_starter_kit_django/` unless a later decision adds more apps.
- Keep durable project guidance in `AGENTS.md` and `docs/`.
- Keep local harness checks in `scripts/`.
- Keep architecture decisions in `docs/decisions/`.
- Keep known failed approaches in `docs/failures/`.
- Keep implementation conventions in `docs/conventions/`.
- Keep domain vocabulary and invariants in `docs/domain/`.
- Do not treat `harness-starter-kit/` as application source.

## Django Rules

- Keep Django project settings, ASGI/WSGI, and root URL configuration in
  `config/`.
- Use `harness_starter_kit_django` for Python imports. Use
  `harness-starter-kit-django` only as a display name in prose.
- Keep domain behavior inside Django apps, not in ad hoc scripts at the root.
- Treat migrations as source when they represent intentional model changes.
  Do not delete or rewrite existing migrations without an explicit request.
- Do not commit local virtual environments, `db.sqlite3`, `__pycache__/`,
  coverage output, or the local `harness-starter-kit/` clone.
- Keep dependency versions in `requirements.txt` until a different dependency
  manager is adopted.
- Add pytest, Ruff, mypy, pre-commit, or other tools only when the project
  chooses them explicitly.

## Coding Rules

- Preserve the existing architecture and conventions once application code
  exists.
- Prefer nearby patterns and standard Django extension points over new
  abstractions.
- Keep changes scoped to the requested behavior.
- Add or update tests for behavior changes.
- Remove temporary debugging files before finishing.

## Knowledge Store

Before making architecture, command, or framework changes, inspect:

- `.harness/source.json`
- `docs/decisions/`
- `docs/failures/`
- `docs/conventions/`
- `docs/domain/`

Add a short decision record when changing the Django project layout, database
policy, test runner, formatter, linter, CI provider, or deployment assumptions.
Add a failure note only when an attempted approach should not be repeated.
If a change fixes a failed CI run, failed harness check, repeated agent mistake,
or cross-environment mismatch, add a `docs/failures/*.md` record unless the
failure is purely transient.

When refreshing this repository against a newer `harness-starter-kit`, update
`.harness/source.json` and add a short update report under `docs/harness/`.

## Commit And PR Rules

- Keep each commit focused on one logical change.
- Before committing, inspect `git status` and the staged diff.
- Do not commit local reference clones, virtual environments, dependency
  directories, caches, local databases, secrets, credentials, or
  machine-specific config.
- Run `.\.venv\Scripts\python.exe scripts\check_harness.py` before committing
  when Python and the virtual environment are available.
- Use Conventional Commits for commit subjects, such as `feat:`, `fix:`,
  `docs:`, `test:`, `refactor:`, or `chore:`.
- PR descriptions should summarize changed files, checks run, assumptions,
  remaining risks, and any manual follow-up.

## Forbidden Actions

- Do not overwrite or delete existing project files without a clear task reason.
- Do not edit files under `harness-starter-kit/` unless the user asks to change
  the starter kit itself.
- Do not add package managers, services, or frameworks just to satisfy a harness
  template.
- Do not leave files matching `temp_*`, `*_new.*`, `*_old.*`, `*_backup.*`,
  `*_fix.*`, or `*.bak`.

## Completion Criteria

Before reporting completion:

- Run `python scripts\check_harness.py` when Python is available.
- Run any stack-specific checks documented here once the stack exists.
- Update docs when commands, architecture, conventions, or known failures
  change.
- Report assumptions, checks run, and remaining manual steps.
