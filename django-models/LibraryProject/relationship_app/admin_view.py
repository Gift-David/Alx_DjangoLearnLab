from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, HttpResponse

# userprofile = UserProfile

def is_admin(user):    
    if user.role == 'admin':
        return True

    # try:
    #     return user.role == 'admin'
    # except user.userprofile.DoesNotExist:
    #     return False
    
@login_required   
@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Admin Dashboard")