# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161004_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('username', models.CharField(max_length=30, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('url', models.URLField(max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('date_publish', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('article', models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', blank=True, to='blog.Article', null=True)),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name': '\u56de\u590d',
                'verbose_name_plural': '\u56de\u590d',
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='pid',
        ),
        migrations.AddField(
            model_name='response',
            name='pid',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba', blank=True, to='blog.Comment', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='rid',
            field=models.ForeignKey(verbose_name=b'\xe5\x90\x8c\xe7\xba\xa7\xe5\x9b\x9e\xe5\xa4\x8d', blank=True, to='blog.Response', null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
