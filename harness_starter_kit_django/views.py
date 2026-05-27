from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class OwnerRequiredMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.get_object().owner == self.request.user


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "harness_starter_kit_django/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "harness_starter_kit_django/post_detail.html"


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
