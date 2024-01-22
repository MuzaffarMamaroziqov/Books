from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Notebook


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

class NotebookListView(ListView):
    model = Notebook
    template_name = 'notebook_list.html'
    context_object_name='notebook'