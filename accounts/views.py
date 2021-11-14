from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class LoginUser(SuccessMessageMixin, auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_message = "You Logged in successfully"
    redirect_authenticated_user = True



class LogoutUser(SuccessMessageMixin, auth_views.LogoutView):
    redirect_authenticated_user = True



class RegisterUser(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
