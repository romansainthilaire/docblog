from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from posts.models import BlogPost
from django.urls import reverse_lazy

def index(request):
    return redirect("posts:home")

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ["title", "content"]

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ["title", "content", "published"]

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"

class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = "post"
    success_url = reverse_lazy("posts:home")
    
