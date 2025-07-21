from django.contrib import admin
from .models import Author, Book, UserProfile, library, CustomUser

# Register your models here.

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date')
#     search_fields = ('title', 'author')

# admin.site.register(BookAdmin)

class CustomAdmin(admin.ModelAdmin):
    list_display = ['date_of_birth', 'profile_photo']

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(library)
admin.site.register(CustomUser, CustomAdmin)
# admin.site.register()