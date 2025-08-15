from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

def home_view(request):
    posts = Post.objects.all().order_by('-published_date')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = ''

class UserProfileView(DetailView):
    model = User
    template_name = ''


'''
    CRUD operations for blog posts
'''

class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('posts/')
    template_name = ''

# To get an individual blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

class PostUpdateView(UpdateView):
    model = Post
    template_name = ''

class PostDeleteView(DeleteView):
    model = Post
    template_name = ''