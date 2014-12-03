# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_author_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='privacy',
            field=models.CharField(default=b'public', max_length=10, choices=[(b'private', b'Private'), (b'public', b'Public')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.SlugField(unique=True, blank=True),
            preserve_default=True,
        ),
    ]
