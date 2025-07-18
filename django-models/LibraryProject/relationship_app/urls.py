from django.urls import path
from .models import Book
from . import views
from .views import list_books #, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books , name='book'),
    # path('', views.current_datetime , name='time'),
    path('', views.ViewLibrary.as_view(template_name='relationship_app/library_detail'), name='view_library' ),
    path('accounts/login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout')
    # path('accounts/register/',),
]
