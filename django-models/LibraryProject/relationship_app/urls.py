from django.urls import path
from .models import Book
from . import views
from .views import list_books #, LibraryDetailView

urlpatterns = [
    path('', views.list_books , name='book'),
    path('', views.current_datetime , name='time'),
    # path('', views.ViewLibrary.as_view(), name='view_library' )
]
