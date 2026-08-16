from django.urls import path
from django.views.generic import RedirectView

app_name = 'core'

urlpatterns = [
  path('', RedirectView.as_view(pattern_name='books:book_list', permanent=False), name='home'),
]