# 0004: Inline Placeholder Path Broke Docs Drift Check

## Status

Resolved

## Context

While adopting task outcome records, a decision record documented the intended
outcome filename pattern as inline code with a directory path and placeholder
filename.

## Symptoms

`scripts/check_harness.py` failed in `scripts/check_docs_drift.py` because the
placeholder outcome-record path was treated as a real local file reference.

## Root Cause

The docs drift checker validates inline-code strings that look like local paths.
A placeholder path with slashes can look like a real repository path even when
it is only meant to describe a naming convention.

## Resolution

Rewrite the decision record to keep inline-code path references limited to real
existing paths and use a real example filename for the outcome record.

## Prevention

- Avoid inline-code placeholder paths that contain directory separators.
- Prefer fenced examples or prose for filename patterns.
- When documenting a path inline, use a real existing path unless the drift
  checker explicitly treats it as optional.
