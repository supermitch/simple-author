from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    """ Extend the User model w/ Author information. """
    user = models.OneToOneField(User)
    website = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)

class Book(models.Model):
    """ A book contains everything. """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=200)

class Chapter(models.Model):
    """ A chapter is the fundamental container of content. """
    book = models.ForeignKey(Book)
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200)

