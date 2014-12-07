# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email_privacy',
            field=models.CharField(default=b'Private', max_length=9, choices=[(b'Private', b'Private'), (b'Public', b'Public')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='privacy',
            field=models.CharField(default=b'Public', max_length=9, choices=[(b'Private', b'Private'), (b'Public', b'Public')]),
            preserve_default=True,
        ),
    ]
