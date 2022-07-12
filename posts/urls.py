from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete, index
from django.contrib.auth.decorators import login_required

app_name = "posts"

urlpatterns = [
    path("", index),
    path("blog", BlogHome.as_view(), name="home"),
    path("blog/create/", login_required(BlogPostCreate.as_view()), name="create"),
    path("blog/<str:slug>/", BlogPostDetail.as_view(), name="detail"),
    path("blog/edit/<str:slug>/", login_required(BlogPostUpdate.as_view()), name="update"),
    path("blog/delete/<str:slug>/", login_required(BlogPostDelete.as_view()), name="delete"),
]