# 0002: Initialize Django With A Config Project Package

## Status

Accepted

## Context

The repository needed a Django development environment. The repository root is
named `django`, so using `django` as the generated project package would be
confusing and could shadow the installed Django package in imports.

## Decision

Create a local Python virtual environment in `.venv`, install Django, add
`requirements.txt`, and initialize the Django project with:

```powershell
.\.venv\Scripts\django-admin.exe startproject config .
```

The generated root entrypoint is `manage.py`, and the Django project package is
`config`.

## Consequences

- Local commands should use `.\.venv\Scripts\python.exe`.
- Project settings, root URLs, ASGI, and WSGI configuration live in `config/`.
- Future Django apps should be created as sibling app packages at the repository
  root unless a different app layout decision is recorded.
