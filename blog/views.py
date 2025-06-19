from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = '/templates/blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = '/templates/blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = '/templates/blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog/'  # 성공 후 리다이렉트할 URL

class PostUpdateView(UpdateView):
    model = Post
    template_name = '/templates/blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog/'  # 성공 후 리다이렉트할 URL

class PostDeleteView(DeleteView):
    model = Post
    template_name = '/templates/blog/post_confirm_delete.html'
    context_object_name = 'post'
    success_url = '/blog/'  # 성공 후 리다이렉트할 URL