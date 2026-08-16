from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at',)
  search_fields = ('title',)

class StateAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at',)
  search_fields = ('title',)
  
class BookAdmin(admin.ModelAdmin):
  readonly_fields = ('created_at', 'updated_at',)
  ordering = ('-updated_at',)
  search_fields = ('title',)
  date_hierarchy = 'created_at'
  list_filter = ('category', 'state',)
  
admin.site.register(models.CategoryModel, CategoryAdmin)
admin.site.register(models.StateModel, StateAdmin)
admin.site.register(models.BookModel, BookAdmin)