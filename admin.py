from django.contrib import admin
from .models import Book
from .models import Notebook

admin.site.register(Book)
admin.site.register(Notebook)

# Register your models here.
