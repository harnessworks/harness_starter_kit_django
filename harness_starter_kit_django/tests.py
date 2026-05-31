from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .views import MY_PAGE_ACTIVITY_LIMIT
from .models import Comment, Post


User = get_user_model()


class AuthenticationViewTests(TestCase):
    def test_signup_page_is_available(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertContains(response, "회원가입")

    def test_signup_creates_user_and_logs_in(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newuser",
                "password1": "S3cure-Test-Pass-987",
                "password2": "S3cure-Test-Pass-987",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("posts:list"))
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.wsgi_request.user.username, "newuser")
        self.assertContains(response, "회원가입이 완료되었습니다.")

    def test_invalid_signup_shows_feedback_message(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newuser",
                "password1": "S3cure-Test-Pass-987",
                "password2": "different-pass-987",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "입력 내용을 확인하세요.")
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_authenticated_user_is_redirected_from_signup(self):
        user = User.objects.create_user(username="writer", password="password123")
        self.client.force_login(user)

        response = self.client.get(reverse("signup"))

        self.assertRedirects(response, reverse("posts:list"))


class MyPageViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="writer", password="password123")
        self.other_user = User.objects.create_user(
            username="other",
            password="password123",
        )

    def test_anonymous_user_is_redirected_from_my_page(self):
        response = self.client.get(reverse("my_page"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('my_page')}",
            fetch_redirect_response=False,
        )

    def test_authenticated_header_links_to_my_page(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("posts:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "마이페이지")
        self.assertContains(response, reverse("my_page"))

    def test_my_page_shows_only_current_user_activity(self):
        self.client.force_login(self.user)
        my_post = Post.objects.create(
            title="내 게시글",
            content="내 본문",
            owner=self.user,
        )
        commented_post = Post.objects.create(
            title="댓글 단 게시글",
            content="다른 본문",
            owner=self.other_user,
        )
        Post.objects.create(
            title="다른 사용자만의 글",
            content="다른 사용자만의 본문",
            owner=self.other_user,
        )
        my_comment = Comment.objects.create(
            post=commented_post,
            owner=self.user,
            content="내 댓글",
        )
        Comment.objects.create(
            post=my_post,
            owner=self.other_user,
            content="다른 사용자 댓글",
        )

        response = self.client.get(reverse("my_page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/my_page.html")
        self.assertContains(response, self.user.username)
        self.assertContains(response, "내 게시글")
        self.assertContains(response, "내 댓글")
        self.assertContains(response, reverse("posts:update", kwargs={"pk": my_post.pk}))
        self.assertContains(
            response,
            reverse("posts:comment_update", kwargs={"pk": my_comment.pk}),
        )
        self.assertNotContains(
            response,
            reverse("posts:comment_delete", kwargs={"pk": my_comment.pk}),
        )
        self.assertContains(response, "댓글 단 게시글")
        self.assertNotContains(response, "다른 사용자만의 글")
        self.assertNotContains(response, "다른 사용자 댓글")
        self.assertEqual(response.context["post_count"], 1)
        self.assertEqual(response.context["comment_count"], 1)

    def test_my_page_limits_activity_lists_to_recent_items(self):
        self.client.force_login(self.user)
        post = Post.objects.create(
            title="댓글 대상 게시글",
            content="댓글 본문",
            owner=self.other_user,
        )
        for index in range(MY_PAGE_ACTIVITY_LIMIT + 1):
            Post.objects.create(
                title=f"내 게시글 {index}",
                content="내 본문",
                owner=self.user,
            )
            Comment.objects.create(
                post=post,
                owner=self.user,
                content=f"내 댓글 {index}",
            )

        response = self.client.get(reverse("my_page"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["my_posts"]), MY_PAGE_ACTIVITY_LIMIT)
        self.assertEqual(len(response.context["my_comments"]), MY_PAGE_ACTIVITY_LIMIT)
        self.assertEqual(response.context["post_count"], MY_PAGE_ACTIVITY_LIMIT + 1)
        self.assertEqual(response.context["comment_count"], MY_PAGE_ACTIVITY_LIMIT + 1)
        self.assertContains(response, f"최근 {MY_PAGE_ACTIVITY_LIMIT}개만 표시됩니다.")

    def test_my_page_shows_empty_states(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("my_page"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "작성한 게시글이 없습니다.")
        self.assertContains(response, "작성한 댓글이 없습니다.")


class PostModelTests(TestCase):
    def test_post_string_uses_title(self):
        post = Post.objects.create(title="첫 게시글", content="내용입니다.")

        self.assertEqual(str(post), "첫 게시글")

    def test_comment_string_uses_content_preview(self):
        post = Post.objects.create(title="댓글 게시글", content="본문")
        user = User.objects.create_user(username="commenter", password="password123")
        comment = Comment.objects.create(
            post=post,
            owner=user,
            content="댓글 내용입니다.",
        )

        self.assertEqual(str(comment), "댓글 내용입니다.")


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

    def test_post_list_filters_by_query(self):
        Post.objects.create(title="검색 대상", content="목록 내용", owner=self.user)
        Post.objects.create(title="다른 게시글", content="다른 내용", owner=self.user)

        response = self.client.get(reverse("posts:list"), {"q": "검색"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "검색 대상")
        self.assertNotContains(response, "다른 게시글")

    def test_post_list_is_paginated(self):
        for index in range(6):
            Post.objects.create(
                title=f"페이지 게시글 {index}",
                content="페이지 내용",
                owner=self.user,
            )

        response = self.client.get(reverse("posts:list"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_paginated"])
        self.assertEqual(len(response.context["posts"]), 5)
        self.assertContains(response, "다음")

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

    def test_anonymous_user_is_redirected_from_update(self):
        post = Post.objects.create(title="수정 전", content="이전 내용", owner=self.user)
        url = reverse("posts:update", kwargs={"pk": post.pk})

        response = self.client.get(url)

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={url}",
            fetch_redirect_response=False,
        )

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


class CommentViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="writer", password="password123")
        self.other_user = User.objects.create_user(
            username="other",
            password="password123",
        )
        self.post = Post.objects.create(
            title="댓글 게시글",
            content="댓글 본문",
            owner=self.user,
        )

    def test_post_detail_shows_comments(self):
        Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="보이는 댓글",
        )

        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "보이는 댓글")
        self.assertContains(response, self.other_user.username)

    def test_comment_owner_sees_update_link(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="수정 링크 댓글",
        )

        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "댓글 수정")
        self.assertContains(
            response,
            reverse("posts:comment_update", kwargs={"pk": comment.pk}),
        )

    def test_anonymous_user_is_redirected_from_comment_create(self):
        url = reverse("posts:comment_create", kwargs={"post_pk": self.post.pk})

        response = self.client.post(url, {"content": "익명 댓글"})

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={url}",
            fetch_redirect_response=False,
        )
        self.assertFalse(Comment.objects.filter(content="익명 댓글").exists())

    def test_create_comment_assigns_owner_and_post(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("posts:comment_create", kwargs={"post_pk": self.post.pk}),
            {"content": "새 댓글"},
        )

        comment = Comment.objects.get(content="새 댓글")
        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.owner, self.other_user)

    def test_invalid_comment_rerenders_post_detail(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("posts:comment_create", kwargs={"post_pk": self.post.pk}),
            {"content": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "harness_starter_kit_django/post_detail.html",
        )
        self.assertContains(response, self.post.title)
        self.assertContains(response, "This field is required.")
        self.assertFalse(Comment.objects.filter(post=self.post).exists())

    def test_anonymous_user_is_redirected_from_comment_update(self):
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="수정 전 댓글",
        )
        url = reverse("posts:comment_update", kwargs={"pk": comment.pk})

        response = self.client.get(url)

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={url}",
            fetch_redirect_response=False,
        )

    def test_owner_can_update_comment(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="수정 전 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_update", kwargs={"pk": comment.pk}),
            {"content": "수정 후 댓글"},
        )

        comment.refresh_from_db()
        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertEqual(comment.content, "수정 후 댓글")
        self.assertEqual(comment.owner, self.other_user)
        self.assertEqual(comment.post, self.post)

    def test_other_user_cannot_update_comment(self):
        self.client.force_login(self.user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="남의 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_update", kwargs={"pk": comment.pk}),
            {"content": "권한 없는 수정"},
        )

        comment.refresh_from_db()
        self.assertEqual(response.status_code, 403)
        self.assertEqual(comment.content, "남의 댓글")

    def test_invalid_comment_update_rerenders_form(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="수정 전 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_update", kwargs={"pk": comment.pk}),
            {"content": ""},
        )

        comment.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "harness_starter_kit_django/comment_form.html",
        )
        self.assertContains(response, "This field is required.")
        self.assertEqual(comment.content, "수정 전 댓글")

    def test_owner_can_delete_comment(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="삭제할 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_delete", kwargs={"pk": comment.pk})
        )

        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())

    def test_other_user_cannot_delete_comment(self):
        self.client.force_login(self.user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="남의 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_delete", kwargs={"pk": comment.pk})
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Comment.objects.filter(pk=comment.pk).exists())


class FeedbackMessageTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="writer", password="password123")
        self.other_user = User.objects.create_user(
            username="other",
            password="password123",
        )
        self.post = Post.objects.create(
            title="기존 게시글",
            content="기존 본문",
            owner=self.user,
        )

    def test_post_create_shows_success_message(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("posts:create"),
            {"title": "메시지 게시글", "content": "메시지 본문"},
            follow=True,
        )

        self.assertRedirects(
            response,
            Post.objects.get(title="메시지 게시글").get_absolute_url(),
        )
        self.assertContains(response, "게시글이 작성되었습니다.")

    def test_post_update_shows_success_message(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("posts:update", kwargs={"pk": self.post.pk}),
            {"title": "수정된 게시글", "content": "수정된 본문"},
            follow=True,
        )

        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertContains(response, "게시글이 수정되었습니다.")

    def test_post_delete_shows_success_message(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("posts:delete", kwargs={"pk": self.post.pk}),
            follow=True,
        )

        self.assertRedirects(response, reverse("posts:list"))
        self.assertContains(response, "게시글이 삭제되었습니다.")

    def test_invalid_post_create_shows_feedback_message(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("posts:create"),
            {"title": "", "content": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "입력 내용을 확인하세요.")

    def test_comment_create_shows_success_message(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("posts:comment_create", kwargs={"post_pk": self.post.pk}),
            {"content": "메시지 댓글"},
            follow=True,
        )

        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertContains(response, "댓글이 작성되었습니다.")

    def test_comment_update_shows_success_message(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="수정 전 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_update", kwargs={"pk": comment.pk}),
            {"content": "수정 후 댓글"},
            follow=True,
        )

        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertContains(response, "댓글이 수정되었습니다.")

    def test_comment_delete_shows_success_message(self):
        self.client.force_login(self.other_user)
        comment = Comment.objects.create(
            post=self.post,
            owner=self.other_user,
            content="삭제할 댓글",
        )

        response = self.client.post(
            reverse("posts:comment_delete", kwargs={"pk": comment.pk}),
            follow=True,
        )

        self.assertRedirects(response, self.post.get_absolute_url())
        self.assertContains(response, "댓글이 삭제되었습니다.")

    def test_invalid_comment_create_shows_feedback_message(self):
        self.client.force_login(self.other_user)

        response = self.client.post(
            reverse("posts:comment_create", kwargs={"post_pk": self.post.pk}),
            {"content": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "입력 내용을 확인하세요.")


class AdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="password123",
        )
        self.writer = User.objects.create_user(
            username="writer",
            password="password123",
        )
        self.client.force_login(self.admin_user)

    def test_admin_index_uses_project_branding(self):
        response = self.client.get(reverse("admin:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "게시판 관리자")
        self.assertContains(response, "사용자, 게시글 및 댓글 관리")

    def test_builtin_user_admin_is_available(self):
        response = self.client.get(reverse("admin:auth_user_changelist"))

        self.assertTrue(admin.site.is_registered(User))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.admin_user.username)
        self.assertContains(response, self.writer.username)

    def test_post_admin_shows_owner(self):
        Post.objects.create(title="관리 게시글", content="관리 내용", owner=self.writer)

        response = self.client.get(
            reverse("admin:harness_starter_kit_django_post_changelist")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "관리 게시글")
        self.assertContains(response, self.writer.username)

    def test_comment_admin_shows_owner_and_post(self):
        post = Post.objects.create(title="댓글 관리 게시글", content="본문", owner=self.writer)
        Comment.objects.create(post=post, content="관리 댓글", owner=self.writer)

        response = self.client.get(
            reverse("admin:harness_starter_kit_django_comment_changelist")
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "댓글 관리 게시글")
        self.assertContains(response, self.writer.username)
