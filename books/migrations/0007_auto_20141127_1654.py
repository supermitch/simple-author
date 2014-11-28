# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20141124_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
                ('section', models.ForeignKey(to='books.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='section',
            name='book',
        ),
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
        migrations.AddField(
            model_name='section',
            name='location',
            field=models.CharField(default='', max_length=5, choices=[(b'front', b'Front'), (b'back', b'Back')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
