# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_auto_20141205_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
