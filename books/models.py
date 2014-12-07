from django.contrib.auth.models import User
from django.db import models


PRIVATE = 'Private'
PUBLIC = 'Public'
PRIVACY = (
    (PRIVATE, 'Private'),
    (PUBLIC, 'Public'),
)

FRONT_MATTER = [
   #('db_value', 'human readable'),
    ('Half Title', 'Half Title'),
    ('Title Page', 'Title Page'),
    ('Colophon', 'Colophon'),
    ('Contents', 'Contents'),
    ('Foreward', 'Foreward'),
    ('Preface', 'Preface'),
    ('Acknowledgment', 'Acknowlegment'),
    ('Introduction', 'Introduction'),
    ('Dedication', 'Dedication'),
    ('Epigraph', 'Epigraph'),
    ('Prologue', 'Prologue'),
]

BODY_MATTER = [('Chapter', 'Chapter')]

BACK_MATTER = [
    ('Epilogue', 'Epilogue'),
    ('Afterward', 'Afterward'),
    ('Conclusion', 'Conclusion'),
    ('Postscript', 'Postscript'),
    ('Appendix', 'Appendix'),
    ('Glossary', 'Glossary'),
    ('Bibliography', 'Bibliography'),
    ('Index', 'Index'),
    ('Colophon', 'Colophon'),
]

SECTIONS = FRONT_MATTER + BODY_MATTER + BACK_MATTER

LOCATIONS = (('Front', 'Front'), ('Body', 'Body'), ('Back', 'Back'))


class Section(models.Model):
    """ Back and Front matter are stored here. """
    kind = models.CharField(max_length=15, choices=SECTIONS)
    multiple = models.BooleanField(default=False)
    initial_order = models.IntegerField(default=0)
    location = models.CharField(max_length=5, choices=LOCATIONS)

    def __str__(self):
        return self.kind

class Book(models.Model):
    """ A book contains everything. """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    url = models.SlugField(blank=True, null=True)
    privacy = models.CharField(max_length=8, choices=PRIVACY, default=PUBLIC)
    pub_date = models.DateField('Date Published', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    sections = models.ManyToManyField(Section, through='BookSections')

    def __str__(self):
        return self.title

class BookSections(models.Model):
    """ Links many Sections to each book. """
    book = models.ForeignKey(Book)
    section = models.ForeignKey(Section)
    name = models.CharField(max_length=200, blank=True, default='')
    order = models.IntegerField(default=0)
    content = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = 'Book Sections'

    def __str__(self):
        return self.name

