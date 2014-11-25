# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20141124_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='privacy',
            field=models.CharField(default=b'public', max_length=10, choices=[(b'private', b'Private'), (b'public', b'Public')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
