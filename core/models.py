from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=10,null=True,blank=True)
class Author(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
class Book(models.Model):
    title = models.CharField(max_length=20,null=True,blank=True)
    author = models.ManyToManyField(Author,null=True)
    tags = models.ManyToManyField(Tag,null=True)
