from django.shortcuts import render
from .models import Book, library
# from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class ViewLibrary(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html'


class UserCreationForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

# UserCreationForm()