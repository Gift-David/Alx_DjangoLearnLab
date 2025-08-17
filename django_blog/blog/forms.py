from django.forms import ModelForm
from .models import Post, Comment

class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
