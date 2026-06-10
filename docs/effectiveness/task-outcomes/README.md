# Task Outcome Records

Use this directory for lightweight per-task records when comparing agent work
over time. These notes are part of the Harness dogfood evidence, not a
replacement for tests, decision records, failure notes, commits, or PR
descriptions.

## When To Add A Record

Add a record when a task is useful evidence for future Harness evaluation,
especially when it:

- Changes architecture, app boundaries, commands, verification, CI, or project
  guidance.
- Updates Harness adoption, update, refresh, review, analysis, or effectiveness
  workflows.
- Fixes a known failure note or high-risk bug path.
- Is an explicit project analysis, review, or onboarding task whose outcome
  should be compared with future agent work.

Ordinary small application changes do not need a task outcome record unless
they touch one of those areas.

## Naming

Name records with the task date and a short slug:

```text
YYYY-MM-DD-short-task-name.md
```

## Format

Keep each record short. Use this shape:

```markdown
# YYYY-MM-DD: Task Name

## Task Type

Harness process | Application feature | Bug fix | Review | Analysis

## Request

One or two sentences describing what was requested.

## Change Surface

Files or areas changed, at a high level.

## Verification

Commands run and results.

## Effectiveness Inclusion

State whether the record is included in an effectiveness report and whether it
counts as a comparable product-task run. Harness-maintenance work normally uses
`include_in_comparable_product_task_count: false` unless the task is explicitly
part of a comparable product-task evaluation.

## Outcome

What changed, what passed, and any follow-up worth carrying forward.
```
