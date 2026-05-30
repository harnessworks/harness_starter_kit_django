# 0003: Owner Required Views Returned 403 For Anonymous Users

## Status

Resolved

## Context

Owner-only post and comment views combine Django's `LoginRequiredMixin` with a
local `OwnerRequiredMixin`.

## Symptoms

Anonymous users requesting an owner-only edit view could receive a 403 response
instead of being redirected to the login page with a `next` parameter.

## Root Cause

`OwnerRequiredMixin` set `raise_exception = True` so authenticated non-owners
would receive 403 responses. Because the same instance is also used by
`LoginRequiredMixin`, the flag also affected anonymous users before the login
redirect path could run.

## Resolution

Update `OwnerRequiredMixin.handle_no_permission()` so authenticated users still
receive 403 responses, while anonymous users are redirected to the configured
login URL with `next`.

## Prevention

- Keep tests for anonymous access to owner-only update views.
- When stacking Django auth mixins, check how shared `AccessMixin` attributes
  affect each mixin in the method resolution order.
