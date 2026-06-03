# Failure Notes

Use this directory for short notes about failures, high-risk bug paths, or
approaches that should not be repeated.

Add a note when a change fixes a user-visible runtime failure, 5xx response,
crash, security or permission bug, data-loss risk, failed CI run, failed harness
check, repeated agent mistake, previously identified bug path, or
cross-environment mismatch unless the issue was purely transient or already
covered by an existing note.

Use `000-template.md` for new records. Each record must name the regression
test, fixture, smoke check, lint rule, drift check, CI gate, or manual review
point that prevents or detects recurrence. If no check is practical, explain the
concrete blocker and what future signal should trigger review.

Run `scripts/check_failure_memory.py` after adding or updating failure notes.
