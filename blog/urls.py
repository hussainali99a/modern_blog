from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("create/", views.post_create_view, name="post_create"),
    path("<slug:slug>/", views.post_detail_view, name="post_detail"),
    path("<slug:slug>/edit/", views.post_update_view, name="post_update"),
    path("<slug:slug>/delete/", views.post_delete_view, name="post_delete"),
    path("<slug:slug>/like/", views.like_post_view, name="like_post"),
]