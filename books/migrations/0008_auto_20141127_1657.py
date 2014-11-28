# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20141127_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section_type',
            new_name='name',
        ),
    ]
