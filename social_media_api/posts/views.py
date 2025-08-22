from django.shortcuts import render
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

'''
CRUD operations for Posts
'''

class PostCreateAPIView(generics.CreateAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostUpdateAPIView(generics.UpdateAPIView):
    model = Post
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostListAPIView(generics.ListAPIView):
    model = Post
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostRetrieveAPIView(generics.RetrieveAPIView):
    model = Post
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostDeleteAPIView(generics.DestroyAPIView):
    model = Post
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
