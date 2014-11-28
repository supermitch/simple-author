from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    """ Extend the User model w/ Author information. """
    user = models.OneToOneField(User)
    website = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    """ A book contains everything. """
    PRIVATE = 'private'
    PUBLIC = 'public'
    PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    )
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    url = models.SlugField(blank=True, null=True)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES,
                               default=PUBLIC)
    pub_date = models.DateField('date published', blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

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
    """ Back and Front matter are stored here. """
    name = models.CharField(max_length=15, choices=SECTION_CHOICES)
    LOCATION_CHOICES = (('front', 'Front'), ('back', 'Back'))
    order = models.IntegerField(default=0)
    location = models.CharField(max_length=5, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.name


class BookSections(models.Model):
    """ Links Sections to Books. """
    book = models.ForeignKey(Book)
    section = models.ForeignKey(Section)
    content = models.TextField(blank=True, default='')


class Chapter(models.Model):
    """ A chapter is the fundamental container of content. """
    book = models.ForeignKey(Book)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=200, blank=True, default='')
    content = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

