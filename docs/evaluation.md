# Harness Evaluation

This repository separates harness health from agent effectiveness.

Harness health is the repository-visible system: `AGENTS.md`, local checks,
CI, source tracking, decision records, failure memory, update reports, and
governance rules. Harness Doctor and `scripts/check_harness.py` inspect this
layer.

Agent effectiveness is outcome evidence from real tasks: wrong-file edits,
first-pass verification, repeated known mistakes, drift detections, human
rework, and comparable product-task counts. Passing Harness Doctor or local
checks is not proof of agent effectiveness.

## Current Evidence

- Historical impact summary: [evaluation/harness-impact.md](../evaluation/harness-impact.md)
- Maintenance evidence report:
  [docs/effectiveness/effectiveness-report-harness-maintenance.md](effectiveness/effectiveness-report-harness-maintenance.md)
- Per-task outcome records:
  [docs/effectiveness/task-outcomes/](effectiveness/task-outcomes/)

## Current Interpretation

This target has useful harness-maintenance evidence and several task outcome
records, but it does not yet have a comparable baseline-versus-harnessed
product-task evaluation. Maintenance runs are preserved as operational evidence
and excluded from comparable product-task counts unless a record explicitly
states otherwise.

## Next Evidence Window

For the next product-facing Django tasks, record whether:

- the expected file boundary was followed
- first-pass verification passed with `scripts/check_harness.py`
- known failure notes were avoided
- human rework was needed
- the task should count in a future comparable product-task report
