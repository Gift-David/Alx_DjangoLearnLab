from django.shortcuts import render
from rest_framework import generics, status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

'''
CRUD operations for Posts
'''
class PostViewStets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

'''
CRUD operations for Comments
'''
class CommentViewStets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



