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
                ('website', models.CharField(max_length=100, blank=True)),
                ('bio', models.CharField(max_length=500, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.SlugField(null=True, blank=True)),
                ('privacy', models.CharField(default=b'public', max_length=10, choices=[(b'private', b'Private'), (b'public', b'Public')])),
                ('pub_date', models.DateField(verbose_name=b'date published', blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookSections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
                'verbose_name_plural': 'Book Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('name', models.CharField(default=b'', max_length=200, blank=True)),
                ('content', models.TextField(default=b'', blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15, choices=[(b'half_title', b'Half title'), (b'title_page', b'Title Page'), (b'colophon', b'Colophon'), (b'contents', b'Contents'), (b'foreward', b'Foreward'), (b'preface', b'Preface'), (b'acknowledgment', b'Acknowlegment'), (b'introduction', b'Introduction'), (b'dedication', b'Dedication'), (b'epigraph', b'Epigraph'), (b'prologue', b'Prologue'), (b'epilogue', b'Epilogue'), (b'afterward', b'Afterward'), (b'conclusion', b'Conclusion'), (b'postscript', b'Postscript'), (b'appendix', b'Appendix'), (b'glossary', b'Glossary'), (b'bibliography', b'Bibliography'), (b'index', b'Index'), (b'colophon', b'Colophon')])),
                ('order', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=5, choices=[(b'front', b'Front'), (b'back', b'Back')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='booksections',
            name='section',
            field=models.ForeignKey(to='books.Section'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='booksections',
            unique_together=set([('book', 'section')]),
        ),
    ]
