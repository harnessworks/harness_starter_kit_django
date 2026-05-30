from urllib.parse import urlsplit

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CommentForm, PostForm, SignUpForm
from .models import Comment, Post


FORM_INVALID_MESSAGE = "입력 내용을 확인하세요."


class FeedbackMessageMixin:
    success_message = ""
    invalid_message = FORM_INVALID_MESSAGE

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

    def form_invalid(self, form):
        messages.error(self.request, self.invalid_message)
        return super().form_invalid(form)


class OwnerRequiredMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.get_object().owner == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())

        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        login_scheme, login_netloc = urlsplit(resolved_login_url)[:2]
        current_scheme, current_netloc = urlsplit(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )


class SignUpView(FeedbackMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("posts:list")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("posts:list")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        login(self.request, self.object)
        messages.success(self.request, "회원가입이 완료되었습니다.")
        return redirect(self.get_success_url())


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 5
    template_name = "harness_starter_kit_django/post_list.html"

    def get_queryset(self):
        queryset = (
            Post.objects.select_related("owner")
            .annotate(comment_count=Count("comments"))
            .order_by("-created_at")
        )
        self.query = self.request.GET.get("q", "").strip()
        if self.query:
            queryset = queryset.filter(
                Q(title__icontains=self.query)
                | Q(content__icontains=self.query)
                | Q(owner__username__icontains=self.query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.query
        return context


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "harness_starter_kit_django/post_detail.html"

    def get_queryset(self):
        return Post.objects.select_related("owner").prefetch_related("comments__owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, FeedbackMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"
    success_message = "게시글이 작성되었습니다."

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(
    LoginRequiredMixin,
    OwnerRequiredMixin,
    FeedbackMessageMixin,
    UpdateView,
):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"
    success_message = "게시글이 수정되었습니다."


class PostDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("posts:list")
    template_name = "harness_starter_kit_django/post_confirm_delete.html"

    def form_valid(self, form):
        messages.success(self.request, "게시글이 삭제되었습니다.")
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, FeedbackMessageMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "harness_starter_kit_django/post_detail.html"
    success_message = "댓글이 작성되었습니다."

    def dispatch(self, request, *args, **kwargs):
        self.parent_post = get_object_or_404(Post, pk=kwargs["post_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return redirect(self.parent_post.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = self.parent_post
        context["comment_form"] = context.get("form", CommentForm())
        return context

    def form_valid(self, form):
        form.instance.post = self.parent_post
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.parent_post.get_absolute_url()


class CommentUpdateView(
    LoginRequiredMixin,
    OwnerRequiredMixin,
    FeedbackMessageMixin,
    UpdateView,
):
    model = Comment
    form_class = CommentForm
    context_object_name = "comment"
    template_name = "harness_starter_kit_django/comment_form.html"
    success_message = "댓글이 수정되었습니다."

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "harness_starter_kit_django/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def form_valid(self, form):
        messages.success(self.request, "댓글이 삭제되었습니다.")
        return super().form_valid(form)
