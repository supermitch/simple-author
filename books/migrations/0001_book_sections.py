# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', 'sections_data_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sections',
            field=models.ManyToManyField(to='books.Section', through='books.BookSections'),
            preserve_default=True,
        ),
    ]
