from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
  path('create_book/', views.CreateBook.as_view(), name='create_book'),
  path('book_list/', views.BookList.as_view(), name='book_list'),
  path('update_book/<int:pk>', views.UpdateBook.as_view(), name='update_book'),
  path('book_detail/<int:pk>', views.DetailBook.as_view(), name='book_detail'),
  path('book_delete/<int:pk>', views.DeleteBook.as_view(), name='book_delete'),
]