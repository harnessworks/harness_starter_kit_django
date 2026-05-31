# 0012: Add My Page

## Status

Accepted

## Context

The board has account signup and owner-based post and comment permissions.
Users can create and edit their own content, but there is no account-centered
place to find their posts and comments after logging in.

## Decision

Add a login-required my page at `/accounts/me/` using the existing
server-rendered Django architecture.

The page summarizes the current user's username, total post count, and total
comment count. It lists the five most recent posts and five most recent
comments owned by the current user and provides edit links for each item. The
authenticated header links to the page.

## Consequences

- Users can quickly return to their own activity without searching the public
  board.
- The page avoids loading unbounded account activity as the board grows.
- No new model, migration, profile table, or authentication package is needed.
- Future profile fields, password changes, email verification, or public user
  pages remain separate decisions.
