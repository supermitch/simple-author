# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20141130_2327'),
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
                'verbose_name_plural': 'Book Sections',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='booksections',
            unique_together=set([('book', 'section')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='sections',
            field=models.ManyToManyField(to='books.Section', through='books.BookSections'),
            preserve_default=True,
        ),
    ]
