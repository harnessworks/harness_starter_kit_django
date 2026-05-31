# 0011: Adopt Harness Task Outcome Records

## Status

Accepted

## Context

The Harness adoption and update reports left an open follow-up to decide
whether future comparable agent tasks should record per-task outcome notes under
`docs/effectiveness/task-outcomes/`.

This repository is a Harness dogfood project, so comparable evidence is useful.
At the same time, requiring a record for every small application change would
add noise and maintenance overhead.

## Decision

Adopt lightweight task outcome records for Harness-relevant work. Add a record
when a task changes architecture, app boundaries, project commands,
verification, CI, durable project guidance, Harness workflows, known failure
paths, or explicit analysis/review/onboarding behavior.

Do not require task outcome records for ordinary small application changes
unless they affect one of those areas.

Use files under `docs/effectiveness/task-outcomes/` named with a date and short
slug, such as `2026-05-31-adopt-task-outcome-records.md`. Keep each record
short, with sections for task type, request, change surface, verification, and
outcome.

## Consequences

- Future Harness effectiveness reports can cite comparable per-task evidence.
- Agents have a clear trigger for when outcome notes are useful.
- Routine feature work avoids unnecessary documentation overhead.
