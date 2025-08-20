from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics
from .models import CustomUser
from .serializers import ProfileSerializer

# Create your views here.

class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer