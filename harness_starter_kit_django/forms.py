from django import forms

from .models import Post


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
