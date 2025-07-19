from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, HttpResponse

# userprofile = UserProfile

def is_admin(user):
    if user.is_authenticated:
        return False
    
    if user.role == 'admin':
        return True

    # try:
    #     return user.role == 'admin'
    # except user.userprofile.DoesNotExist:
    #     return False
    
    
@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")