# 0005: Subagent Review Misstated Reviewer Mode

## Date Observed

2026-05-31

## Failure Type

Repeated agent mistake in Harness review reporting.

## Goal

`/harness review sub-agent` should let the parent agent request a read-only
reviewer subagent and then report reviewer mode and fallback reason from the
parent's actual spawn/wait result.

## What Happened Or Was Tried

The parent agent successfully spawned, waited for, and closed a reviewer
subagent. The subagent output nevertheless claimed reviewer mode
`single-agent fallback` with fallback reason `tool unavailable`, which
conflicted with the parent agent's actual spawn/wait result.

## Why It Failed

The reviewer subagent saw the full Harness Review command guidance in forked
context and treated reviewer-mode and fallback reporting as part of its own
responsibility. From inside the subagent runtime, it assessed whether it could
spawn another subagent instead of limiting itself to review findings.

## Current Replacement

The target tracks Harness Starter Kit commit
`832ede6c368c3d929a20c7e429ac3ad83ea84408` or newer, where reviewer-mode and
fallback reporting are explicitly parent/orchestrator-owned. This target's
`AGENTS.md` route for `/harness review sub-agent` carries the same ownership
rule.

## Detection Or Prevention Check

Manual review point `docs/checklists/harness-review.md` checks that
`/harness review sub-agent` reports reviewer mode and fallback reason from the
parent agent's actual spawn/wait result rather than copying subagent output.

## Agent Guidance

Decide `Reviewer mode` and `Fallback reason` from the parent agent's actual
availability check and subagent spawn/wait result. Treat subagent output as
review input only: findings, missing checks, and risks.
