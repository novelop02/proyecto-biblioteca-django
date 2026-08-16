from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views import View
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BookModel
from django.http import Http404

class CreateBook(LoginRequiredMixin, CreateView):
  login_url = reverse_lazy('users:login')
  model = BookModel
  template_name = 'books/create_book.html'
  form_class = BookForm
  success_url = reverse_lazy('books:book_list')
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BookList(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('users:login')
  template_name = 'books/book_list.html'
  context_object_name = 'books'
  paginate_by = 6
  ordering = ['-id']
  
  def get_queryset(self):
    books = BookModel.objects.filter(user=self.request.user)
    
    return books
  
class UpdateBook(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('users:login')
  model = BookModel
  template_name = 'books/create_book.html'
  form_class = BookForm
  success_url = reverse_lazy('books:book_list')
  
  def get_queryset(self):
    books = BookModel.objects.filter(user=self.request.user)
    
    return books

  def get_success_url(self):
    return reverse('books:book_detail', args=(self.kwargs['pk'],))
  
  def get(self, request, *args, **kwargs):
    try:
      return super().get(request, *args, **kwargs)
    except Http404:
      return redirect('books:book_list')
  
class DetailBook(LoginRequiredMixin, DetailView):
  login_url = reverse_lazy('users:login')
  model = BookModel
  context_object_name = 'book'
  template_name = 'books/book_detail.html'
  
  def get_queryset(self):
    books = BookModel.objects.filter(user=self.request.user)
    
    return books
  
  def get(self, request, *args, **kwargs):
    try:
      return super().get(request, *args, **kwargs)
    except Http404:
      return redirect('books:book_list')
  
class DeleteBook(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('users:login')
  model = BookModel
  template_name = 'books/book_confirm_delete.html'
  context_object_name = 'book'
  success_url = reverse_lazy('books:book_list')
  
  def get_queryset(self):
    books = BookModel.objects.filter(user=self.request.user)
    
    return books
  
  def get(self, request, *args, **kwargs):
    try:
      return super().get(request, *args, **kwargs)
    except Http404:
      return redirect('books:book_list')
