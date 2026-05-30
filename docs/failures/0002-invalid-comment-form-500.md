# 0002: Empty Comment Submission Rendered A 500

## Status

Resolved

## Context

Comment creation uses a dedicated `CommentCreateView`, while the comment form is
displayed on the post detail page.

## Symptoms

Submitting an empty comment as a logged-in user could trigger a server error
instead of returning to the post detail page with form validation errors.

## Root Cause

`CommentCreateView` relied on Django's default invalid-form rendering behavior.
Because the view did not define a template for invalid submissions, Django tried
to render the default comment form template instead of the existing post detail
template.

## Resolution

Render `harness_starter_kit_django/templates/harness_starter_kit_django/post_detail.html`
for invalid comment submissions and pass the bound comment form back as
`comment_form`.

## Prevention

- Keep a regression test for invalid comment submissions.
- When a form is submitted from a page that is not the model form's default
  template, define the invalid-form rendering path explicitly.
- Record fixed user-visible 500 paths in `docs/failures/`.
