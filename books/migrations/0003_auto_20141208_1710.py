# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20141206_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='show_toc',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='view_mode',
            field=models.CharField(default=b'Section', max_length=20, choices=[(b'Single', b'Single Page'), (b'Section', b'Section View'), (b'Page', b'Page View')]),
            preserve_default=True,
        ),
    ]
