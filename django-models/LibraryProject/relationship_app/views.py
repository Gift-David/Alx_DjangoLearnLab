from django.shortcuts import render
from .models import Book, library
from django.views.generic import ListView
from .models import Library
from django.http import HttpResponse
import datetime

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    set = {'boks': books}
    # return HttpResponse(books)
    return render(request, 'relationship_app/list_books.html', set)

# class ViewLibrary(ListView):
#     pass

def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body> it is now %s. </body> </html>' % now
    return HttpResponse(html)