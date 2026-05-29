from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        labels = {
            "title": "제목",
            "content": "내용",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "autocomplete": "off",
                    "placeholder": "제목을 입력하세요",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "내용을 입력하세요",
                    "rows": 12,
                }
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": "댓글",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "placeholder": "댓글을 입력하세요",
                    "rows": 4,
                }
            ),
        }
