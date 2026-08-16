from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms

class UserCreateForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields["username"].widget = forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Usuario",
    })
    
    self.fields["password1"].widget = forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Contraseña",
    })
    
    self.fields["password2"].widget = forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Confirmar contraseña",
    })

class UserLoginForm(AuthenticationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields["username"].widget = forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Usuario",
    })
    
    self.fields["password"].widget = forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Contraseña",
    })
    
class UserChangePasswordForm(PasswordChangeForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self.fields["old_password"].widget.attrs.update({
      "class": "form-control",
      "placeholder": "Contraseña actual",
    })

    self.fields["new_password1"].widget.attrs.update({
      "class": "form-control",
      "placeholder": "Nueva contraseña",
    })

    self.fields["new_password2"].widget.attrs.update({
      "class": "form-control",
      "placeholder": "Repetir nueva contraseña",
    })