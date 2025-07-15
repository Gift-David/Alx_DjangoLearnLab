from .models import Book, library

Entry.objects.filter(Book.author)