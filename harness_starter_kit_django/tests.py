from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


User = get_user_model()


class PostModelTests(TestCase):
    def test_post_string_uses_title(self):
        post = Post.objects.create(title="첫 게시글", content="내용입니다.")

        self.assertEqual(str(post), "첫 게시글")


class PostCrudViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="writer", password="password123")
        self.other_user = User.objects.create_user(
            username="other", password="password123"
        )

    def test_post_list_shows_posts(self):
        Post.objects.create(title="목록 게시글", content="목록 내용", owner=self.user)

        response = self.client.get(reverse("posts:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "목록 게시글")

    def test_anonymous_user_is_redirected_from_create(self):
        response = self.client.get(reverse("posts:create"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('posts:create')}",
            fetch_redirect_response=False,
        )

    def test_create_post_assigns_owner(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("posts:create"),
            {"title": "작성 게시글", "content": "작성 내용"},
        )

        post = Post.objects.get(title="작성 게시글")
        self.assertRedirects(response, post.get_absolute_url())
        self.assertEqual(post.content, "작성 내용")
        self.assertEqual(post.owner, self.user)

    def test_owner_can_update_post(self):
        self.client.force_login(self.user)
        post = Post.objects.create(title="수정 전", content="이전 내용", owner=self.user)

        response = self.client.post(
            reverse("posts:update", kwargs={"pk": post.pk}),
            {"title": "수정 후", "content": "새 내용"},
        )

        post.refresh_from_db()
        self.assertRedirects(response, post.get_absolute_url())
        self.assertEqual(post.title, "수정 후")
        self.assertEqual(post.content, "새 내용")

    def test_other_user_cannot_update_post(self):
        self.client.force_login(self.other_user)
        post = Post.objects.create(title="수정 전", content="이전 내용", owner=self.user)

        response = self.client.post(
            reverse("posts:update", kwargs={"pk": post.pk}),
            {"title": "수정 후", "content": "새 내용"},
        )

        post.refresh_from_db()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(post.title, "수정 전")
        self.assertEqual(post.content, "이전 내용")

    def test_owner_can_delete_post(self):
        self.client.force_login(self.user)
        post = Post.objects.create(title="삭제 게시글", content="삭제 내용", owner=self.user)

        response = self.client.post(reverse("posts:delete", kwargs={"pk": post.pk}))

        self.assertRedirects(response, reverse("posts:list"))
        self.assertFalse(Post.objects.filter(pk=post.pk).exists())

    def test_other_user_cannot_delete_post(self):
        self.client.force_login(self.other_user)
        post = Post.objects.create(title="삭제 게시글", content="삭제 내용", owner=self.user)

        response = self.client.post(reverse("posts:delete", kwargs={"pk": post.pk}))

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Post.objects.filter(pk=post.pk).exists())
