from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Comment, Post


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            "username": "아이디",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "autocomplete": "username",
                    "placeholder": "아이디를 입력하세요",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "비밀번호"
        self.fields["password1"].widget.attrs.update(
            {
                "autocomplete": "new-password",
                "placeholder": "비밀번호를 입력하세요",
            }
        )
        self.fields["password2"].label = "비밀번호 확인"
        self.fields["password2"].widget.attrs.update(
            {
                "autocomplete": "new-password",
                "placeholder": "비밀번호를 한 번 더 입력하세요",
            }
        )


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
