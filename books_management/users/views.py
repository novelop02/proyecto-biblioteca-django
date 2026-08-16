from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreateForm, UserLoginForm, UserChangePasswordForm

class UserSignUpView(CreateView):
  template_name = 'users/signup.html'
  form_class = UserCreateForm
  success_url = reverse_lazy('users:login')

class UserLoginView(LoginView):
  template_name = 'users/login.html'
  authentication_form = UserLoginForm
  next_page = reverse_lazy('core:home')
  
class UserLogoutView(LogoutView):
  next_page = reverse_lazy("users:login")
  
class UserChangePasswordView(PasswordChangeView):
  template_name = 'users/change_password.html'
  form_class = UserChangePasswordForm
  success_url = reverse_lazy('core:home')