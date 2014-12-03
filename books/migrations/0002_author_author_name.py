# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_book_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_name',
            field=models.SlugField(default='mitch', blank=True),
            preserve_default=False,
        ),
    ]
