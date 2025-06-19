from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog/'  # 성공 후 리다이렉트할 URL

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    success_url = '/blog/'  # 성공 후 리다이렉트할 URL

class PostDeleteView(DeleteView):
    model = Post  # Specify the model to use
    # 삭제를 시도할때 template_name을 지정 ,get방식으로 호출이 되어야만 해당 html이 렌더링됨
    # post로 요청하면 삭제가 진행됨
    template_name = 'blog/post_confirm_delete.html'  # Specify the template to use
    success_url = '/blog'  # Redirect to the post list after successful deletion