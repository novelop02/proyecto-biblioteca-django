from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
  title = models.CharField(max_length=32, null=False, verbose_name="Título")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  
  def __str__(self):
    return self.title
  
  class Meta:
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"
    
class StateModel(models.Model):
  title = models.CharField(max_length=32, null=False, verbose_name="Título")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Estado"
    verbose_name_plural = "Estados"
    
class BookModel(models.Model):
  title = models.CharField(max_length=32, null=False, verbose_name="Título")
  description = models.TextField(max_length=256, verbose_name="descripción", null=True, blank=True)
  category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
  state = models.ForeignKey(StateModel, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha actualización")
  
  class Meta:
    verbose_name = "Libro"
    verbose_name_plural = "Libros"