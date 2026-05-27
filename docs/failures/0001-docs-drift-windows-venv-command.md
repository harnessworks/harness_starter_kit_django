# 0001. Docs Drift Treated Windows Venv Commands As Paths

## Date Tried

2026-05-27

## Goal

Document local verification commands in README and harness docs without causing
cross-platform docs drift failures.

## What Was Tried

Windows virtual-environment commands such as
`.\.venv\Scripts\python.exe manage.py check` and
`.\.venv\Scripts\python.exe scripts\check_harness.py` were documented as inline
code.

## Why It Failed

The docs drift checker can run on non-Windows environments. A Windows venv
Python path can look like a local file reference instead of a command when the
checker only sees inline code, which may create a false missing-path failure.

## Current Replacement

Treat virtual-environment Python paths as commands or ignored local environment
paths in harness docs drift checks. Keep verification commands documented, but
do not rely on local `.venv/` paths existing in CI.

## Agent Guidance

When a check fails because a command is misclassified as a path, fix the checker
and add a regression test. Do not remove useful verification commands from docs
just to silence docs drift.
