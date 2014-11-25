from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    """ Extend the User model w/ Author information. """
    user = models.OneToOneField(User)
    website = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=500, blank=True)

class Book(models.Model):
    """ A book contains everything. """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published', blank=True)
    description = models.CharField(max_length=200, blank=True)

FRONT_MATTER_CHOICES = [
   #('db_value', 'human readable'),
    ('half_title', 'Half title'),
    ('title_page', 'Title Page'),
    ('colophon', 'Colophon'),
    ('contents', 'Contents'),
    ('foreward', 'Foreward'),
    ('preface', 'Preface'),
    ('acknowledgment', 'Acknowlegment'),
    ('introduction', 'Introduction'),
    ('dedication', 'Dedication'),
    ('epigraph', 'Epigraph'),
    ('prologue', 'Prologue'),
]

BACK_MATTER_CHOICES = [
    ('epilogue', 'Epilogue'),
    ('afterward', 'Afterward'),
    ('conclusion', 'Conclusion'),
    ('postscript', 'Postscript'),
    ('appendix', 'Appendix'),
    ('glossary', 'Glossary'),
    ('bibliography', 'Bibliography'),
    ('index', 'Index'),
    ('colophon', 'Colophon'),
]

SECTION_CHOICES = FRONT_MATTER_CHOICES + BACK_MATTER_CHOICES

class Section(models.Model):
    book = models.ForeignKey(Book)
    section_type = models.CharField(max_length=15, choices=SECTION_CHOICES)
    content = models.TextField(blank=True, default='')

class Chapter(models.Model):
    """ A chapter is the fundamental container of content. """
    book = models.ForeignKey(Book)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=200, blank=True, default='')
    content = models.TextField(blank=True, default='')

