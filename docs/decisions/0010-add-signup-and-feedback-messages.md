# 0010: Add Signup And Feedback Messages

## Status

Accepted

## Context

The board required login for post and comment writes, but users could only be
created through Django admin. Post and comment workflows also redirected after
successful changes without visible confirmation.

## Decision

Add account registration and feedback messages within the existing
server-rendered Django app:

- Add `/accounts/signup/` with a `UserCreationForm`-based signup form.
- Log new users in automatically after successful registration and redirect to
  the post list.
- Show signup links from the anonymous header and login page.
- Render Django messages in the shared base template.
- Show success messages after post and comment create, update, and delete
  flows.
- Show a generic validation failure message when form submissions are invalid,
  while preserving field-level form errors.

## Consequences

- Users can join and immediately create posts or comments without admin setup.
- Redirecting write flows now provide visible confirmation.
- Form validation failures have both field-level errors and page-level feedback.
- Future profile management, password reset, email verification, or account
  moderation remain separate decisions.
