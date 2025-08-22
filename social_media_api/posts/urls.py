from django.urls import path
from . import views

urlpatterns = [
    # Endpoints for posts
    path('create/', views.PostCreateAPIView.as_view(), name='create_post'),
    path('edit/', views.PostUpdateAPIView.as_view(), name='update_post'),
    path('', views.PostListAPIView.as_view(), name='list_post'),
    path('<int:pk>/', views.PostRetrieveAPIView.as_view(), name='retreive_post'),
    path('<int:pk>/', views.PostDeleteAPIView.as_view(), name='delete_post'),

    # Endpoints for comments
]