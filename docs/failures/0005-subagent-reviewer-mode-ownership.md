# 0005: Subagent Review Misstated Reviewer Mode

## Status

Resolved

## Context

`/harness review sub-agent` should let the parent agent request a read-only
reviewer subagent and then report whether a subagent was actually used.

## Symptoms

The parent agent successfully spawned, waited for, and closed a reviewer
subagent. The subagent output nevertheless claimed reviewer mode
`single-agent fallback` with fallback reason `tool unavailable`, which
conflicted with the parent agent's actual spawn/wait result.

## Root Cause

The reviewer subagent saw the full Harness Review command guidance in forked
context and treated reviewer-mode and fallback reporting as part of its own
responsibility. From inside the subagent runtime, it assessed whether it could
spawn another subagent instead of limiting itself to review findings.

## Resolution

Refresh the local `harness-starter-kit/` reference to commit
`832ede6c368c3d929a20c7e429ac3ad83ea84408`, which makes reviewer-mode and
fallback reporting explicitly parent/orchestrator-owned. Clarify this target's
`AGENTS.md` route for `/harness review sub-agent` with the same ownership rule.

## Prevention

- Decide `Reviewer mode` and `Fallback reason` from the parent agent's actual
  availability check and subagent spawn/wait result.
- Treat subagent output as review input only: findings, missing checks, and
  risks.
- Do not copy reviewer-mode, fallback-reason, or tool-availability claims from
  a spawned reviewer subagent.
