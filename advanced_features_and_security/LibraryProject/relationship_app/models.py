from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class CustomUser(AbstractUser):
    # email = models.EmailField(unique=True, blank=False)
    date_of_birth = models.DateField(blank=False)
    profile_photo = models.ImageField(upload_to='static/profile_pics', blank=True)
    # USERNAME_FIELD = email

    # def __str__(self):
    #     return f"{self.username}"
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):
        pass

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        pass

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        permissions = (
            ('can_add_book', 'Can Delete Book'),
            ('can_change_book', 'Can Change Book'),
            ('can_delete_book', 'Can Delete Book')
        )

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    Library = models.OneToOneField('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('librarian', 'Librarian'), ('member', 'Member')])

    # def __str__(self):
    #     return self.user
