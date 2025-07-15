from .models import Book, library

Library = library
Library.objects.get(name=library_name)
books = Book
books.all()