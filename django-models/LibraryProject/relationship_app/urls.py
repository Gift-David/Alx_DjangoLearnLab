from django.urls import path
from .models import Book
from . import views
from .views import list_books, UserCreationForm, add_book, edit_book, delete_book
from . import admin_view, librarian_view, member_view
from .admin_view import admin_dashboard
# from .librarian_view import librarian_dashboard
from .member_view import member_dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books , name='book'),
    # path('', views.current_datetime , name='time'),
    path('', views.ViewLibrary.as_view(template_name='relationship_app/library_detail'), name='view_library' ),
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('accounts/register/', UserCreationForm.as_view(template_name='relationship_app/register.html'), name='register'),
    path('superadmin/', admin_view.admin_dashboard, name='admin'),
    # path('librarian/', librarian_view.librarian_dashboard, name='librarian'),
    path('member/', member_view.member_dashboard, name='member'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book')
]


# views.register
# LibraryDetailView