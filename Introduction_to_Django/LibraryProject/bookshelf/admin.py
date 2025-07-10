from django.contrib import admin
from .models import Book

# Register your models here.

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'published_date')
    publication_years = ('title', 'author')

admin.site.register(Book, BookAdmin)