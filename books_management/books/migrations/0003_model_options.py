from django.db import migrations

def create_categories(apps, schema_editor):
  Category = apps.get_model('books', 'CategoryModel')
  Category.objects.get_or_create(title="Historia")
  Category.objects.get_or_create(title="Ciencia")
  Category.objects.get_or_create(title="Infantil")
  Category.objects.get_or_create(title="General")
  
def create_states(apps, schema_editor):
  State = apps.get_model('books', 'StateModel')
  State.objects.get_or_create(title="En existencia")
  State.objects.get_or_create(title="Prestado")
  State.objects.get_or_create(title="Perdido")
  State.objects.get_or_create(title="En proceso de compra")

class Migration(migrations.Migration):
  dependencies = [
    ('books', '0002_alter_bookmodel_options'),
  ]
  
  operations = [
    migrations.RunPython(create_categories),
    migrations.RunPython(create_states),
  ]