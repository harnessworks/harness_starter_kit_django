# 0003: Owner Required Views Returned 403 For Anonymous Users

## Date Observed

2026-05-30

## Failure Type

Permission bug and user-visible auth-flow regression.

## Goal

Anonymous users requesting owner-only edit views should be redirected to login
with a `next` parameter, while authenticated non-owners should receive 403.

## What Happened Or Was Tried

Owner-only post and comment views combine Django's `LoginRequiredMixin` with a
local `OwnerRequiredMixin`. Anonymous users requesting an owner-only edit view
could receive a 403 response instead of being redirected to the login page.

## Why It Failed

`OwnerRequiredMixin` set `raise_exception = True` so authenticated non-owners
would receive 403 responses. Because the same instance is also used by
`LoginRequiredMixin`, the flag also affected anonymous users before the login
redirect path could run.

## Current Replacement

`OwnerRequiredMixin.handle_no_permission()` returns 403 for authenticated users
and redirects anonymous users to the configured login URL with `next`.

## Detection Or Prevention Check

`harness_starter_kit_django/tests.py` includes anonymous access tests for
owner-only post and comment update views, and `scripts/check_harness.py` runs
the Django test suite before completion and in CI.

## Agent Guidance

When stacking Django auth mixins, check how shared `AccessMixin` attributes
affect each mixin in the method resolution order. Preserve the distinct
anonymous redirect and authenticated non-owner 403 behavior.
