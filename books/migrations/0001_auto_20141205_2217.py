# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', 'sections_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, verbose_name=b'Date Published', blank=True),
            preserve_default=True,
        ),
    ]
