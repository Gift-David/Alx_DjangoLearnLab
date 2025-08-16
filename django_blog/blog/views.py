from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import PostCreationForm
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
    template_name = 'blog/user_profile.html'
    context_object_name = 'user'
    # posts = Post.objects.all().filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.all().filter(author=self.request.user).order_by('-published_date')
        return context


'''
    CRUD operations for blog posts
'''

class PostCreateView(CreateView):
    form_class = PostCreationForm
    success_url = reverse_lazy('list_posts')
    template_name = 'blog/create_post.html'
    context_object_name = 'form'

    def form_valid(self, post):
        post.instance.author = self.request.user
        return super().form_valid(post)

# To get an individual blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_post.html'
    context_object_name = 'post'

class PostListView(ListView):
    model = Post
    template_name = 'blog/list_posts.html'
    context_object_name = 'posts'
    ordering = '-published_date'

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreationForm
    success_url = reverse_lazy('list_posts')
    template_name = 'blog/create_post.html'
    context_object_name = 'form'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/blog_post.html'

# "POST", "method", "save()"