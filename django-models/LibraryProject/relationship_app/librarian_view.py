from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, HttpResponse

userprofile = UserProfile

def is_librarian(user):
    if user.is_authenticated:
        return False
    
    try:
        return userprofile.role == 'librarian'
    except userprofile.DoesNotExist:
        return False
    
@user_passes_test(is_librarian)
def admin_dashboard(request):
    return HttpResponse("Librarian Dashboard")