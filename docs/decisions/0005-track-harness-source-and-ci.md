# 0005: Track Harness Source And Run Harness Checks In CI

## Status

Accepted

## Context

The upstream `harness-starter-kit` added a `/harness update` workflow that asks
target repositories to record which kit commit informed their local harness.
This repository is now hosted on GitHub and has a stable local verification
entrypoint in `scripts/check_harness.py`.

## Decision

Add `.harness/source.json` to record the latest starter-kit source commit used
for this repository's harness. Add a GitHub Actions workflow that installs the
project dependencies and runs `python scripts/check_harness.py` on pushes,
pull requests, and manual dispatches.

## Consequences

- Future harness refreshes can compare against the recorded kit source.
- The same verification command used locally now runs in GitHub Actions.
- CI is intentionally limited to existing project tools; no new linter,
  type-checker, or package manager is introduced by this change.
