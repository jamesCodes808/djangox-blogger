from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post-list-view.html'
    model = Post
    context_object_name = 'post_list'

class PostDetailView(DetailView):
    template_name = 'blog/post-detail-view.html'
    model = Post

class PostCreateView(CreateView):
    template_name = 'blog/post-create-view.html'
    model = Post
    fields = ['title','slug', 'author','content', 'status']

class PostUpdateView(UpdateView):
    template_name = 'blog/post-update-view.html'
    model = Post
    fields = ['title','slug', 'author','content', 'status']


class PostDeleteView(DeleteView):
    template_name = 'blog/post-delete-view.html'
    model = Post
    success_url = reverse_lazy('blog_post_list_view')



