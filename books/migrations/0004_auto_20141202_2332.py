# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20141202_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_name',
            new_name='display_name',
        ),
    ]
