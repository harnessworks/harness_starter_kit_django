from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "harness_starter_kit_django/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "harness_starter_kit_django/post_detail.html"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "harness_starter_kit_django/post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("posts:list")
    template_name = "harness_starter_kit_django/post_confirm_delete.html"
