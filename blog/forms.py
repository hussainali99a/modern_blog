# from django import forms
# from .models import Post, Comment


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "content", "image", "category", "tags", "is_published"]
#         widgets = {
#             "title": forms.TextInput(attrs={
#                 "class": "input-field",
#                 "placeholder": "Post title"
#             }),
#             "content": forms.Textarea(attrs={
#                 "class": "input-field",
#                 "rows": 8,
#                 "placeholder": "Share your thoughts..."
#             }),
#             "category": forms.Select(attrs={
#                 "class": "input-field"
#             }),
#             "tags": forms.TextInput(attrs={
#                 "class": "input-field",
#                 "placeholder": "communication, django, thoughts"
#             }),
#         }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ["body"]
#         widgets = {
#             "body": forms.Textarea(attrs={
#                 "class": "input-field",
#                 "rows": 3,
#                 "placeholder": "Write your comment..."
#             }),
#         }

from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCE(
            attrs={
                "cols": 80,
                "rows": 20,
            }
        )
    )

    class Meta:
        model = Post
        fields = ["title", "content", "image", "category", "tags", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "Post title"
            }),
            "category": forms.Select(attrs={
                "class": "input-field"
            }),
            "tags": forms.TextInput(attrs={
                "class": "input-field",
                "placeholder": "communication, django, thoughts"
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={
                "class": "input-field",
                "rows": 3,
                "placeholder": "Write your comment..."
            }),
        }