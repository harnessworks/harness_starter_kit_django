# 0003: Create The Harness Starter Kit Django App

## Status

Accepted

## Context

The project needs its first Django app. The desired human-facing name was
`harness-starter-kit-django`, but Django apps must be importable Python modules,
so hyphens are not valid in the package name.

## Decision

Create the Django app package as `harness_starter_kit_django` and register it in
`INSTALLED_APPS`.

## Consequences

- Use `harness_starter_kit_django` in Python imports and Django settings.
- Use `harness-starter-kit-django` only as a display or documentation name when
  that spelling is useful.
- App-specific models, views, admin registration, tests, and migrations should
  live under `harness_starter_kit_django/`.
