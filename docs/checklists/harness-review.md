# Harness Maintenance Review Checklist

Use this checklist for periodic Harness maintenance and for manual review
points that are not practical to enforce with an automated local check.

This is separate from `/harness review`, which reviews the current change set.

- [ ] Did an agent repeat a mistake that should become an `AGENTS.md` rule,
      failure note, checklist item, or local check?
- [ ] Does every important `AGENTS.md` rule have a test, drift check, CI gate,
      or manual review point where practical?
- [ ] Do docs reference files or commands that no longer exist?
- [ ] Are temporary, duplicate, backup, or one-off files absent from source
      paths?
- [ ] Does each new or updated failure record name a regression test, fixture,
      smoke check, lint rule, drift check, CI gate, or manual review point?
- [ ] Are new architecture, workflow, permission, data-model, or verification
      decisions covered by `docs/decisions/` or by an existing ADR?
- [ ] Are deterministic, local, reasonably fast checks for repeated behavior
      verification included in `scripts/check_harness.py`, or is there a
      recorded reason they remain focused or manual?
- [ ] Are live, credentialed, quota-sensitive, slow, visual, or otherwise
      fragile checks kept outside the normal gate unless this repository
      explicitly expects them?
- [ ] For `/harness review sub-agent`, is reviewer mode and fallback reason
      reported from the parent agent's actual spawn/wait result rather than
      copied from subagent output?
- [ ] If localized text is present, are UTF-8 and mojibake risks covered by
      `scripts/check_encoding_hygiene.py` or an explicit manual audit note?
- [ ] Is the effectiveness measurement plan current, including normal gate
      placement, task outcome records, and failure-memory linkage?
