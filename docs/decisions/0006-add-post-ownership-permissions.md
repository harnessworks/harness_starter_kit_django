# 0006: Add Post Ownership Permissions

## Status

Accepted

## Context

The public board allowed anyone to create, update, and delete posts. The next
step is to introduce authentication and owner-based permissions without
changing the server-rendered Django architecture.

## Decision

Add an optional `owner` foreign key from `Post` to Django's configured user
model. Public list and detail views remain readable without login. Creating a
post requires login and assigns the current user as owner. Updating and deleting
a post require login and are allowed only for the post owner.

Use Django's built-in auth views for login and logout instead of introducing a
separate authentication package.

## Consequences

- Existing local posts can have no owner after migration; they remain readable
  but cannot be edited or deleted through the public CRUD views.
- Future posts created through the app have an owner.
- Future registration, profile, password reset, group permission, or moderator
  workflows should be added as explicit follow-up decisions.
