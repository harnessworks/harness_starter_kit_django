# Coding Conventions

## Current State

The Django project package is `config`, the root command entrypoint is
`manage.py`, and the first app package is `harness_starter_kit_django`.

## General Rules

- Follow the style and structure of nearby project files.
- Keep root-level application entrypoints limited and intentional; `manage.py`
  is the established Django entrypoint.
- Prefer standard Django app boundaries before adding custom framework layers.
- Keep generated, cache, database, and environment files out of version control.

## Django Rules

- Keep settings, root URL configuration, ASGI, and WSGI files in `config/`.
- Keep app-specific code in `harness_starter_kit_django/` until another app
  boundary is intentionally added.
- Use `harness_starter_kit_django` in imports and settings.
- Use `.\.venv\Scripts\python.exe manage.py check` for system checks.
- Use `.\.venv\Scripts\python.exe manage.py test` for tests.
- Document migration review expectations before the first model change.
- Document formatter, linter, and type-checker choices only after they are
  actually adopted.
