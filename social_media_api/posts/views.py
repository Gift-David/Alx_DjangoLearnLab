from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser
from accounts.serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

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



class FollowToggleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        """
        Allows an authenticated user to follow another user.
        Creates a Notification for the followed user.
        """
        followed_user = get_object_or_404(CustomUser, pk=pk)
        follower_user = request.user

        if follower_user == followed_user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if already following
        if UserFollow.objects.filter(follower=follower_user, followed=followed_user).exists():
            return Response(
                {"detail": "You are already following this user."},
                status=status.HTTP_409_CONFLICT
            )
        
        # Create the follow relationship
        UserFollow.objects.create(follower=follower_user, followed=followed_user)

        # --- Create Notification ---
        from notifications.models import Notification # Import here to avoid circular dependency
        from django.contrib.contenttypes.models import ContentType

        # The target of the notification is the UserFollow instance
        follow_content_type = ContentType.objects.get_for_model(UserFollow)
        
        Notification.objects.create(
            recipient=followed_user,
            actor=follower_user,
            verb='follow',
            content_type=follow_content_type,
            object_id=UserFollow.objects.get(follower=follower_user, followed=followed_user).id,
            text_content=f"{follower_user.username} started following you."
        )
        # --- End Notification ---

        return Response(
            {"detail": "Successfully followed user."},
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, pk, format=None):
        """
        Allows an authenticated user to unfollow another user.
        """
        followed_user = get_object_or_404(User, pk=pk)
        follower_user = request.user

        follow_instance = UserFollow.objects.filter(
            follower=follower_user,
            followed=followed_user
        )

        if follow_instance.exists():
            follow_instance.delete()
            return Response(
                {"detail": "Successfully unfollowed user."},
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"detail": "You are not following this user."},
                status=status.HTTP_404_NOT_FOUND
            )

class UserFollowingListView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the user whose following list is being requested
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        # Return the users that 'user' is following
        return user.following.all().order_by('username')

class UserFollowersListView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get the user whose followers list is being requested
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        # Return the users who are following 'user'
        return user.followers.all().order_by('username')