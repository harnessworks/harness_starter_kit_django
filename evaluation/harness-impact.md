# Harness Impact Evaluation

## Summary

The Harness Starter Kit is producing meaningful results for this project. Its
main value is not direct feature generation, but a durable collaboration and
verification system around the Django application.

## Evidence Of Value

- `AGENTS.md` defines project-specific working rules, commands, boundaries, and
  forbidden actions.
- `docs/decisions/` records architectural and product decisions such as Django
  initialization, public CRUD, and post ownership permissions.
- `docs/failures/` stores known failed approaches so future work avoids
  repeating them.
- `scripts/check_harness.py` gives the project one local verification command
  for docs drift, structure drift, Django system checks, and tests.
- `.github/workflows/harness-check.yml` runs the same harness checks in CI.
- `.harness/source.json` and `docs/harness/harness-update-report.md` track
  which starter-kit commit informed the repository and what was selectively
  adopted.
- `harness_doctor.py` currently reports a baseline score of 83/100, grade B+.

## Observed Project Effect

The post ownership permission work showed the harness operating as intended.
The change included model updates, migration, view permissions, templates,
tests, documentation, and a decision record. The full harness check then
verified the resulting state.

This is a concrete example of the kit shaping work quality: behavior changes
were implemented together with verification and durable project memory.

## Limits

- The kit does not automatically guarantee application quality.
- It does not replace product judgment or security review.
- The current app is still small, so stronger architecture-boundary checks
  would be premature.
- The doctor score is based on file and text evidence, so humans still need to
  review whether the content is useful and current.

## Conclusion

The kit is meaningful for this repository because it keeps project rules,
verification, decisions, failures, and update history inside the repository.
That value should increase as the Django app grows and more contributors or
agents touch the code.
