from django.shortcuts import render
from rest_framework import generics
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


class PostCreateAPIView(generics.CreateAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostUpdateAPIView(generics.UpdateAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostListAPIView(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostRetrieveAPIView(generics.RetrieveAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class PostDeleteAPIView(generics.DestroyAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

'''
CRUD operations for Comments
'''
class CommentViewStets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateAPIView(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentUpdateAPIView(generics.UpdateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentListAPIView(generics.ListAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentRetrieveAPIView(generics.RetrieveAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDeleteAPIView(generics.DestroyAPIView):
    model = Comment
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
