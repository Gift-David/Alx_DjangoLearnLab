from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User

# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = ''

class UserProfileView(DetailView):
    model = User
    template_name = ''