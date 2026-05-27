# 0004: Add Public Post CRUD

## Status

Accepted

## Context

The first application feature is a simple 게시판. The project does not yet have
authentication, user ownership, API requirements, or frontend framework choices.

## Decision

Implement a small server-rendered CRUD using Django's model, `ModelForm`, class
based generic views, app-local URL configuration, templates, and tests.

The `Post` model stores `title`, `content`, `created_at`, and `updated_at`.
Routes live under the `posts` namespace, with the list view mounted at `/`.

## Consequences

- The board is public until authentication requirements are introduced.
- Templates remain Django-rendered HTML for now.
- Future ownership, permissions, pagination, search, or rich text support should
  be added as explicit follow-up decisions.
