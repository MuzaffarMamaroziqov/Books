from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=13)

    def __str__(self):
        return self.title


class Notebook(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name