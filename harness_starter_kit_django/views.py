from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CommentForm, PostForm
from .models import Comment, Post


class OwnerRequiredMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.get_object().owner == self.request.user


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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"


class PostDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("posts:list")
    template_name = "harness_starter_kit_django/post_confirm_delete.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "harness_starter_kit_django/post_detail.html"

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


class CommentDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Comment
    context_object_name = "comment"
    template_name = "harness_starter_kit_django/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()
