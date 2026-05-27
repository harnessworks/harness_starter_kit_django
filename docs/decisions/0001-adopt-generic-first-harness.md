# 0001: Adopt A Generic-First Harness

## Status

Accepted

## Context

The repository root did not contain application source, Django project files,
package metadata, CI, or existing docs when harness adoption began. The working
directory name suggests Django intent, but there is not yet a `manage.py` file
or settings package to inspect.

## Decision

Adopt a generic-first harness with Django-aware guidance. The local checks focus
on documentation integrity, repository structure, and adoption-report
completeness. The verification wrapper will run Django checks only after
`manage.py` exists.

## Consequences

- The harness is useful immediately without inventing project architecture.
- Future Django setup work must update `AGENTS.md` and this knowledge store
  with real commands and boundaries.
- The cloned `harness-starter-kit/` directory remains reference material and
  should be removed or ignored before any commit.
