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
                ('website', models.CharField(max_length=100, blank=True)),
                ('bio', models.CharField(max_length=500, blank=True)),
                ('privacy', models.CharField(default=b'Public', max_length=10, choices=[(b'Private', b'Private'), (b'Public', b'Public')])),
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
                ('privacy', models.CharField(default=b'Public', max_length=8, choices=[(b'Private', b'Private'), (b'Public', b'Public')])),
                ('pub_date', models.DateField(verbose_name=b'Date Published', blank=True)),
                ('description', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookSections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('content', models.TextField(default=b'', blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
                'verbose_name_plural': 'Book Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=15, choices=[(b'Half Title', b'Half Title'), (b'Title Page', b'Title Page'), (b'Colophon', b'Colophon'), (b'Contents', b'Contents'), (b'Foreward', b'Foreward'), (b'Preface', b'Preface'), (b'Acknowledgment', b'Acknowlegment'), (b'Introduction', b'Introduction'), (b'Dedication', b'Dedication'), (b'Epigraph', b'Epigraph'), (b'Prologue', b'Prologue'), (b'Chapter', b'Chapter'), (b'Epilogue', b'Epilogue'), (b'Afterward', b'Afterward'), (b'Conclusion', b'Conclusion'), (b'Postscript', b'Postscript'), (b'Appendix', b'Appendix'), (b'Glossary', b'Glossary'), (b'Bibliography', b'Bibliography'), (b'Index', b'Index'), (b'Colophon', b'Colophon')])),
                ('multiple', models.BooleanField(default=False)),
                ('initial_order', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=5, choices=[(b'Front', b'Front'), (b'Body', b'Body'), (b'Back', b'Back')])),
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
        migrations.AddField(
            model_name='book',
            name='sections',
            field=models.ManyToManyField(to='books.Section', through='books.BookSections'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
