# Domain Glossary

## Post

A public board entry with a title, body content, optional owner, creation
timestamp, update timestamp, and zero or more comments.

## Comment

A login-required reply on a post. Comments have an owner, body content, creation
timestamp, and update timestamp. Only the comment owner can update or delete a
comment. A comment is deleted when its post or owner is deleted.

## Account

A Django user account that can create posts and comments after logging in. New
users can register through the public signup page and are logged in
automatically after successful registration. Logged-in users can open a my page
to review their own recent posts and comments.

## 게시판

The public read surface for posts. Creating posts requires login, and updating
or deleting posts is limited to the post owner. The board list supports search
and pagination, while post details show comments. Comment creation requires
login, and comment updates or deletes are limited to the comment owner. Create,
update, delete, and validation failure flows show user feedback messages.
