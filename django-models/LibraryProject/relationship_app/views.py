from django.shortcuts import render
from .models import Book, library
from django.views.generic import ListView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    set = {'books': books}
    return render(request, 'relationship_app/list_books.html', books)

class ViewLibrary(ListView):
    pass