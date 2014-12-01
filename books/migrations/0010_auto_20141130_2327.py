# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20141127_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksections',
            name='book',
        ),
        migrations.RemoveField(
            model_name='booksections',
            name='section',
        ),
        migrations.DeleteModel(
            name='BookSections',
        ),
        migrations.AddField(
            model_name='book',
            name='sections',
            field=models.ManyToManyField(to='books.Section'),
            preserve_default=True,
        ),
    ]
