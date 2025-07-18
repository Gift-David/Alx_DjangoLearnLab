from django.urls import path
from .models import Book
from . import views
from .views import list_books, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books , name='book'),
    # path('', views.current_datetime , name='time'),
    path('', views.ViewLibrary.as_view(template_name='relationship_app/library_detail'), name='view_library' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', UserCreationForm.as_view(template_name='relationship_app/register.html'), name='register')
]


# views.register
# LibraryDetailView