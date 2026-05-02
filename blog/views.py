from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)

        query = self.request.GET.get("q")
        category = self.request.GET.get("category")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__icontains=query)
            )

        if category:
            queryset = queryset.filter(category=category)

        return queryset


@login_required
def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    comments = post.comments.filter(is_active=True)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

            messages.success(request, "Comment added successfully.")
            return redirect("blog:post_detail", slug=post.slug)

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
    })


@login_required
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, "Post created successfully.")
            return redirect("blog:post_detail", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form, "title": "Create Post"})


@login_required
def post_update_view(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("blog:post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form, "title": "Update Post"})


@login_required
def post_delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {"post": post})


@login_required
def like_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("blog:post_detail", slug=post.slug)