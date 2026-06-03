# 0013: Adopt Decision And Failure Memory Checks

## Status

Accepted

## Context

The refreshed Harness Starter Kit adds local checks that warn when implementation
diffs may need decision memory and validate that failure notes name concrete
detection or prevention checks.

This repository is a Django dogfood target with existing decision records,
failure notes, task outcomes, and a single local verification wrapper in
`scripts/check_harness.py`.

## Decision

Adopt target-specific decision and failure memory checks. Configure decision
memory to watch Django implementation paths, project settings, `manage.py`, and
`requirements.txt`, while ignoring tests, migrations, docs, and harness scripts.

Add a failure-memory validator and include both checks in
`scripts/check_harness.py` so the normal Harness gate keeps decision and failure
memory visible during local work and CI. In GitHub pull requests, run the
decision-memory check with the pull request base SHA so the warning can inspect
the PR diff rather than an already-clean checkout.

## Consequences

- Implementation changes that alter structure, workflow, contracts, state,
  permissions, dependencies, or project settings prompt an explicit decision
  memory review.
- Failure notes must carry a concrete regression test, drift check, CI gate, or
  manual review point instead of relying on prose alone.
- Pull request CI can surface decision-memory warnings for implementation diffs
  even though the local wrapper still remains the main completion gate.
- The checks remain lightweight and local; no new package manager, linter,
  formatter, or external service is introduced.
