# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_sections(apps, schema_editor):
    # Don't just use books.models.Section, that could be out of date
    Section = apps.get_model('books', 'Section')

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

    for order, (sect_name, _) in enumerate(FRONT_MATTER_CHOICES):
        sect = Section(name=sect_name, order=order, location='front')
        sect.save()
    for order, (sect_name, _) in enumerate(BACK_MATTER_CHOICES):
        sect = Section(name=sect_name, order=order, location='back')
        sect.save()

def remove_sections(apps, schema_editor):
    """ Just make the migration reversible, by calling this function. """
    Section = apps.get_model('books', 'Section')
    for section in Section.objects.all():
        section.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sections, remove_sections),
    ]

