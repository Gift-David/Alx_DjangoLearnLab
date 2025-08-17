from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostCreationForm, CommentForm
from .models import Post, Comment

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comments'] = self.object.comments.all()
        return context

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
    template_name = 'blog/delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        author_id = self.object.author.pk
        return reverse_lazy('user_profile', kwargs={'pk': author_id})

'''
    CRUD operations for comments
'''
class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'blog/create_comment.html'
    context_object_name = 'form'

    # Makes the user the author
    def form_valid(self, comment):
        post = Post.objects.get(pk=self.kwargs.get('pk'))
        comment.instance.author = self.request.user
        comment.instance.post = post
        return super().form_valid(comment)
    
    def get_success_url(self):
        post_id = self.object.post.pk
        return reverse_lazy('list_comments', kwargs={'pk': post_id})
    

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/list_comments.html'
    context_object_name = 'comments'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['post'] = Post.objects.get(pk=self.kwargs.get('pk'))
        return context

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    form_class = CommentForm
    success_url = reverse_lazy('list_posts')
    template_name = 'blog/create_post.html'
    context_object_name = 'form'
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'blog/delete.html'

    template_name = 'blog/delete.html'
    context_object_name = 'post'
    
    def get_success_url(self):
        post_id = self.object.post.pk
        return reverse_lazy('user_profile', kwargs={'pk': post_id})
    
    


# "POST", "method", "save()"