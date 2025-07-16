from django.shortcuts import render
from .models import Book, library
from django.views.generic import ListView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, '', books)

class ViewLibrary(ListView):
    pass