# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20141130_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='sections',
        ),
    ]
