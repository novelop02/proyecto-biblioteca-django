from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
  path('signup/', views.UserSignUpView.as_view(), name='signup'),
  path('login/', views.UserLoginView.as_view(), name='login'),
  path('logout/', views.UserLogoutView.as_view(), name='logout'),
  path('password_change/', views.UserChangePasswordView.as_view(), name='password_change'),
]
