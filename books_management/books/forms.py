from django import forms
from .models import BookModel

class BookForm(forms.ModelForm):
  class Meta:
    model = BookModel
    fields = ("title", "description", "category", "state",)
    
    widgets = {
      "title": forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Título"
      }),
      
      "description": forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Descripción",
      }),
      
      "category": forms.Select(attrs={
        "class": "form-select",
      }),
      
      "state": forms.Select(attrs={
        "class": "form-select",
      }),
    }