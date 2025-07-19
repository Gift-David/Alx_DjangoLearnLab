from django import forms
from .models import UserProfile, Book

class RegisterationForm(forms.ModelForm):
    model = UserProfile
    fields = ['name', 'password', 'confirm_password']

class BookForm(forms.ModelForm):
    model = Book
    fields = ['title', 'author']