from django.shortcuts import render
from django.contrib.auth import views as atuh_views
from .forms import AuthenticationForm


class LoginView(atuh_views.LoginView):
    """ View user login through Django's security layers """
    form_class = AuthenticationForm
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(atuh_views.LogoutView):
    """ User exit using the Django structure """
    pass