# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_sections(apps, schema_editor):
    # Don't just use books.models.Section, that could be out of date
    Section = apps.get_model('books', 'Section')

    front = ['Half title', 'Title Page', 'Colophon', 'Contents', 'Foreward',
        'Preface', 'Acknowlegment', 'Introduction', 'Dedication', 'Epigraph',
        'Prologue']
    body = ['Chapter']
    back = ['Epilogue', 'Afterward', 'Conclusion',
        'Postscript', 'Appendix', 'Glossary', 'Bibliography', 'Index',
        'Colophon']

    order = 0
    for sections, location in [(front, 'Front'), (body, 'Body'), (back, 'Back')]:
        for kind in sections:
            order += 1
            sect = Section(kind=kind, initial_order=order, location=location)
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

