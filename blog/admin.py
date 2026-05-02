from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "category", "created_at", "is_published"]
    list_filter = ["category", "is_published", "created_at"]
    search_fields = ["title", "content", "tags"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "user", "created_at", "is_active"]
    list_filter = ["is_active", "created_at"]
    search_fields = ["body", "user__username"]