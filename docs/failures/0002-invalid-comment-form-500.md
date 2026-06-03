# 0002: Empty Comment Submission Rendered A 500

## Date Observed

2026-05-30

## Failure Type

User-visible runtime failure and 5xx path.

## Goal

Submitting an invalid comment should return the post detail page with form
validation errors instead of raising a server error.

## What Happened Or Was Tried

Comment creation uses a dedicated `CommentCreateView`, while the comment form is
displayed on the post detail page. Submitting an empty comment as a logged-in
user could trigger a server error instead of returning to the post detail page
with form validation errors.

## Why It Failed

`CommentCreateView` relied on Django's default invalid-form rendering behavior.
Because the view did not define a template for invalid submissions, Django tried
to render the default comment form template instead of the existing post detail
template.

## Current Replacement

Invalid comment submissions render
`harness_starter_kit_django/templates/harness_starter_kit_django/post_detail.html`
and pass the bound comment form back as `comment_form`.

## Detection Or Prevention Check

`harness_starter_kit_django/tests.py` includes
`CommentViewTests.test_invalid_comment_rerenders_post_detail`, and
`scripts/check_harness.py` runs the Django test suite before completion and in
CI.

## Agent Guidance

When a form is submitted from a page that is not the model form's default
template, define the invalid-form rendering path explicitly. Preserve the
invalid comment submission behavior before changing comment create views.
