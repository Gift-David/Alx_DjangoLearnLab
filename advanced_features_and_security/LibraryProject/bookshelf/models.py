from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.base_user import BaseUserManager
# from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=False)
    profile_photo = models.ImageField(upload_to='static/profile_pics', blank=True)
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):
        pass

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        pass

class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=200),
    publication_year = models.IntegerField(),

    def __str__(self):
        return self.title