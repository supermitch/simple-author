from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Chapter(models.Model):
    book = models.ForeignKey(Book)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200)

