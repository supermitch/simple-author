# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_auto_20141118_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_type', models.CharField(max_length=15, choices=[(b'half_title', b'Half title'), (b'title_page', b'Title Page'), (b'colophon', b'Colophon'), (b'contents', b'Contents'), (b'foreward', b'Foreward'), (b'preface', b'Preface'), (b'acknowledgment', b'Acknowlegment'), (b'introduction', b'Introduction'), (b'dedication', b'Dedication'), (b'epigraph', b'Epigraph'), (b'prologue', b'Prologue'), (b'epilogue', b'Epilogue'), (b'afterward', b'Afterward'), (b'conclusion', b'Conclusion'), (b'postscript', b'Postscript'), (b'appendix', b'Appendix'), (b'glossary', b'Glossary'), (b'bibliography', b'Bibliography'), (b'index', b'Index'), (b'colophon', b'Colophon')])),
                ('content', models.TextField(default=b'', blank=True)),
                ('book', models.ForeignKey(to='books.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='title',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='content',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chapter',
            name='name',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
