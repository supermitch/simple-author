# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('bio', models.CharField(max_length=500, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
