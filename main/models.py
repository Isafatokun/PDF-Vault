from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    author_name = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='book/pdf')

    def __str__(self):
        return self.title

