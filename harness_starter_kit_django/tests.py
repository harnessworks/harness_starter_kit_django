from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTests(TestCase):
    def test_post_string_uses_title(self):
        post = Post.objects.create(title="첫 게시글", content="내용입니다.")

        self.assertEqual(str(post), "첫 게시글")


class PostCrudViewTests(TestCase):
    def test_post_list_shows_posts(self):
        Post.objects.create(title="목록 게시글", content="목록 내용")

        response = self.client.get(reverse("posts:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "목록 게시글")

    def test_create_post(self):
        response = self.client.post(
            reverse("posts:create"),
            {"title": "작성 게시글", "content": "작성 내용"},
        )

        post = Post.objects.get(title="작성 게시글")
        self.assertRedirects(response, post.get_absolute_url())
        self.assertEqual(post.content, "작성 내용")

    def test_update_post(self):
        post = Post.objects.create(title="수정 전", content="이전 내용")

        response = self.client.post(
            reverse("posts:update", kwargs={"pk": post.pk}),
            {"title": "수정 후", "content": "새 내용"},
        )

        post.refresh_from_db()
        self.assertRedirects(response, post.get_absolute_url())
        self.assertEqual(post.title, "수정 후")
        self.assertEqual(post.content, "새 내용")

    def test_delete_post(self):
        post = Post.objects.create(title="삭제 게시글", content="삭제 내용")

        response = self.client.post(reverse("posts:delete", kwargs={"pk": post.pk}))

        self.assertRedirects(response, reverse("posts:list"))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())
