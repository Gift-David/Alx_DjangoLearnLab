from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistrationView, UserProfileView, PostCreateView, PostDeleteView,PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('posts/', PostListView.as_view(), name='list_posts'),
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='viewing_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view, name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_posts'),
]