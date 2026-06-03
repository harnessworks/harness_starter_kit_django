# 0004: Inline Placeholder Path Broke Docs Drift Check

## Date Observed

2026-05-31

## Failure Type

Failed harness check and documentation drift false positive.

## Goal

The docs drift check should catch stale local references without treating
placeholder filename patterns as required files.

## What Happened Or Was Tried

While adopting task outcome records, a decision record documented the intended
outcome filename pattern as inline code with a directory path and placeholder
filename. `scripts/check_harness.py` failed in `scripts/check_docs_drift.py`
because the placeholder outcome-record path was treated as a real local file
reference.

## Why It Failed

The docs drift checker validates inline-code strings that look like local paths.
A placeholder path with slashes can look like a real repository path even when
it is only meant to describe a naming convention.

## Current Replacement

The decision record keeps inline-code path references limited to real existing
paths and uses a real example filename for the outcome record.

## Detection Or Prevention Check

`scripts/check_docs_drift.py` detects broken inline local path references, and
`scripts/check_harness.py` runs it as part of the normal Harness gate.

## Agent Guidance

Avoid inline-code placeholder paths that contain directory separators. Prefer
fenced examples or prose for filename patterns, and use real existing paths for
inline local path references unless the drift checker explicitly treats them as
optional.
