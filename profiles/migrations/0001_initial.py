# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.SlugField(unique=True, blank=True)),
                ('website', models.URLField(max_length=100, blank=True)),
                ('bio', models.TextField(max_length=500, blank=True)),
                ('privacy', models.CharField(default=b'Public', max_length=10, choices=[(b'Private', b'Private'), (b'Public', b'Public')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
