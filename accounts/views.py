from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .models import User
from .forms import *

class Login(LoginView):
    authentication_form=UserLoginForm
    redirect_authenticated_user = True

def logout_view(request):
    logout(request)
    #messages.success(request, 'logged out')
    return HttpResponseRedirect(reverse('accounts:login'))
