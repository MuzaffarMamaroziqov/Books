from django.urls import path
from .views import BookListView, NotebookListView

urlpatterns=[
    path('', BookListView.as_view(), name='home'),
    path('notebook/', NotebookListView.as_view(), name='secondhome')
]