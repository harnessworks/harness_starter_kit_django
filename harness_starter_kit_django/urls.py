from django.urls import path

from .views import (
    CommentCreateView,
    CommentDeleteView,
    CommentUpdateView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)


app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("posts/new/", PostCreateView.as_view(), name="create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="delete"),
    path(
        "posts/<int:post_pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path(
        "comments/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path(
        "comments/<int:pk>/edit/",
        CommentUpdateView.as_view(),
        name="comment_update",
    ),
]
