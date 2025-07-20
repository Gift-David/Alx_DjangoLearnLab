from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, HttpResponse

userprofile = UserProfile

def is_librarian(user):
    if user.is_authenticated:
        return False
    
    try:
        return userprofile.role == 'librarian'
    except userprofile.DoesNotExist:
        return False
    
    return hasattr

@login_required
@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Librarian Dashboard")