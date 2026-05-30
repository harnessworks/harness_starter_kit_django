# 0009: Add Owner Comment Editing

## Status

Accepted

## Context

The board already supports login-required comment creation and owner-only
comment deletion. Comments have an `updated_at` timestamp, but users could not
correct or revise their own comments after posting.

## Decision

Add owner-only comment editing with the existing server-rendered Django
architecture:

- Add `CommentUpdateView` using `CommentForm`.
- Add `comments/<id>/edit/` under the existing `posts` URL namespace.
- Show a comment edit link only to the comment owner on the post detail page.
- Redirect successful edits back to the parent post detail page.
- Keep authenticated non-owners on a 403 response.
- Redirect anonymous users on owner-only views to login with `next`.

## Consequences

- Comment owners can fix or revise their comments without deleting and
  reposting.
- Comment edit behavior now has tests for anonymous users, owners,
  authenticated non-owners, and invalid form submissions.
- Future moderation, edit history, or notification behavior remains out of
  scope until explicitly chosen.
