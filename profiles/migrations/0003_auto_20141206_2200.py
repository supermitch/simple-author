# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141206_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email_privacy',
        ),
        migrations.AddField(
            model_name='author',
            name='public_email',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
