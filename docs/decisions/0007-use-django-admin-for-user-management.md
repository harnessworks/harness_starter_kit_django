# 0007: Use Django Admin For User Management

## Status

Accepted

## Context

The project needs an admin page where maintainers can manage users and posts.
The project already uses Django's built-in authentication and has the default
admin route mounted at `/admin/`.

## Decision

Use Django's built-in admin as the project admin page. Keep Django's default
User and Group admin registrations for user management, and customize the
project admin branding and `Post` admin options for owner-aware post
management.

## Consequences

- Superusers can manage users, groups, and posts at `/admin/`.
- No custom user-management UI or extra admin package is introduced.
- Future custom roles, staff workflows, or non-admin user management screens
  should be added only when the product needs them.
