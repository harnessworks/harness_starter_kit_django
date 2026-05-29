# 0008: Add Board Search, Pagination, And Comments

## Status

Accepted

## Context

The board supports public post reading and owner-limited post writing,
updating, and deleting. As the number of posts grows, readers need a way to find
relevant posts and move through the list without loading every post at once.
Posts also need a lightweight discussion surface.

## Decision

Keep the server-rendered Django architecture and extend the existing app with:

- Query-string search on the post list using `q`, matching title, content, and
  owner username.
- Django `ListView` pagination with five posts per page.
- A `Comment` model linked to `Post` and Django's configured user model.
- Login-required comment creation and owner-only comment deletion.
- Admin registration for comments, plus inline comment management on posts.

## Consequences

- Public readers can still view post lists, post details, and comments without
  login.
- Comment writing requires authentication, and comments are removed if their
  post or owner is deleted.
- Future comment editing, moderation, spam controls, or notification workflows
  should be added as explicit follow-up decisions.
