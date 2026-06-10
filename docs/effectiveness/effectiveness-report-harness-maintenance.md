# Harness Maintenance Effectiveness Report

## Target

- Repository: `harness_starter_kit_django`
- Stack and framework: Django with local Harness verification scripts.
- Evaluation date or window: 2026-05-31 through 2026-06-10.
- Agent or model: Codex task runs in this target repository.
- Evaluation mode: harnessed-only-maintenance-evidence.

## Task Set

| Task ID | Scenario | Expected boundary | Common failure |
| --- | --- | --- | --- |
| `2026-05-31-refresh-harness-review-subagent-mode` | Refresh Harness review routing from the starter kit | Harness docs, source tracking, and update report | Copying starter-kit-only repository material into the Django target |
| `2026-05-31-refresh-subagent-reviewer-mode-ownership` | Refresh subagent reviewer-mode ownership guidance | Harness command routing, update report, and failure memory | Trusting reviewer-mode fields copied from subagent output |
| `2026-06-03-adopt-memory-checks` | Adopt decision-memory and failure-memory checks | Local Harness scripts, failure notes, CI, and adoption docs | Adding checks without durable decision or failure-memory guidance |
| `2026-06-10-refresh-harness-source-and-memory-checks` | Refresh source tracking and validation hardening | Local Harness scripts, source tracking, evaluation docs, and update report | Treating maintenance evidence as comparable product-task improvement |

## Results

| Metric | Baseline | Harnessed | Delta |
| --- | ---: | ---: | ---: |
| Wrong-file edits | Not measured | 0 recorded in these maintenance notes | Not claimed |
| Repeated mistakes | Not measured | 0 recorded repeats after related guidance | Not claimed |
| First-pass verification success | Not measured | Mixed; one maintenance run recorded an initial docs-drift failure before final pass | Not claimed |
| Drift violations detected | Not measured | Docs drift detected stale inline path guidance in maintenance work | Not claimed |
| Human rework minutes | Unknown | Unknown | Not claimed |
| Reverted files | Not measured | 0 recorded in these maintenance notes | Not claimed |

## Non-Comparable Setup Runs

| Run | Reason excluded | Use in metrics |
| --- | --- | --- |
| `2026-05-31-refresh-harness-review-subagent-mode` | Harness-maintenance refresh, not a product-feature task | Excluded from comparable product-task count |
| `2026-05-31-refresh-subagent-reviewer-mode-ownership` | Harness-maintenance refresh, not a product-feature task | Excluded from comparable product-task count |
| `2026-06-03-adopt-memory-checks` | Harness-check adoption, not a product-feature task | Excluded from comparable product-task count |
| `2026-06-10-refresh-harness-source-and-memory-checks` | Harness validation update, not a product-feature task | Excluded from comparable product-task count |

## Run Log

| Condition | Task ID | Run | Verification result | Notes |
| --- | --- | ---: | --- | --- |
| Harnessed maintenance | `2026-05-31-refresh-harness-review-subagent-mode` | 1 | Passed `scripts/check_harness.py` and Harness Doctor | Excluded from comparable product-task count |
| Harnessed maintenance | `2026-05-31-refresh-subagent-reviewer-mode-ownership` | 1 | Passed `scripts/check_harness.py` and Harness Doctor | Excluded from comparable product-task count |
| Harnessed maintenance | `2026-06-03-adopt-memory-checks` | 1 | Passed focused memory checks, `scripts/check_harness.py`, and Harness Doctor | Excluded from comparable product-task count |
| Harnessed maintenance | `2026-06-10-refresh-harness-source-and-memory-checks` | 1 | Passed focused checks, `scripts/check_harness.py`, and Harness Doctor | Excluded from comparable product-task count |

## Changed-Files Consistency

| Task ID | Expected boundary | Actual changed files | Wrong-file edit result |
| --- | --- | --- | --- |
| `2026-05-31-refresh-harness-review-subagent-mode` | Harness docs, source tracking, and update report | Harness docs and source tracking | No wrong-file edit recorded |
| `2026-05-31-refresh-subagent-reviewer-mode-ownership` | Harness command routing, update report, and failure memory | Harness docs, source tracking, and failure memory | No wrong-file edit recorded |
| `2026-06-03-adopt-memory-checks` | Local Harness scripts, failure notes, CI, and adoption docs | Harness scripts, memory docs, CI, and reporting docs | No wrong-file edit recorded |
| `2026-06-10-refresh-harness-source-and-memory-checks` | Local Harness scripts, source tracking, evaluation docs, and update report | Harness scripts, source tracking, evaluation docs, task outcome docs, and report docs | No wrong-file edit recorded |

## Source Records

- Task outcome records reviewed:
  [2026-05-31 refresh review sub-agent mode](task-outcomes/2026-05-31-refresh-harness-review-subagent-mode.md),
  [2026-05-31 refresh reviewer-mode ownership](task-outcomes/2026-05-31-refresh-subagent-reviewer-mode-ownership.md),
  [2026-06-03 adopt memory checks](task-outcomes/2026-06-03-adopt-memory-checks.md), and
  [2026-06-10 refresh source and memory checks](task-outcomes/2026-06-10-refresh-harness-source-and-memory-checks.md).
- Repository refs compared: not a baseline comparison; source records are this
  target's recorded maintenance notes.
- Prompt refs compared: not recorded for these maintenance runs.
- Verification commands compared: `scripts/check_harness.py`, focused Harness
  validators, and Harness Doctor runs named in the task records.

## Interpretation

- Observed benchmark: Harness-maintenance records are now visible as
  operational evidence, but they do not prove effectiveness improvement.
- What improved: no improvement claim; no comparable baseline exists for these
  maintenance runs.
- What did not improve: product-task effectiveness remains unmeasured.
- Confounders or limitations: the records are maintenance tasks, not repeated
  product-feature scenarios, and some human rework data is unknown.
- Harness changes to make next: record future product-facing Django tasks with
  comparable inclusion decisions.
- Human rework interpretation: unknown means not recorded, not 0 minutes.

## Follow-Up

- Next review window: after the next 3 to 5 product-facing Django agent tasks.
- Owner or reviewer: repository maintainer.
- Related decision or failure records:
  `docs/decisions/0011-adopt-task-outcome-records.md`,
  `docs/decisions/0013-adopt-decision-and-failure-memory-checks.md`, and
  `docs/failures/0005-subagent-reviewer-mode-ownership.md`.
