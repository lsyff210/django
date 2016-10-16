# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161003_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='url',
            field=models.URLField(max_length=100, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(max_length=150, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xbd\x91\xe9\xa1\xb5\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='callback_url',
            field=models.URLField(null=True, verbose_name=b'\xe5\x9b\x9e\xe8\xb0\x83url', blank=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(upload_to=b'ad/%Y/%m', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True, to='blog.Category', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_recommend',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa8\xe8\x8d\x90'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe6\x98\xbe\xe7\xa4\xba\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(verbose_name=b'\xe6\x96\x87\xe7\xab\xa0', blank=True, to='blog.Article', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba', blank=True, to='blog.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='links',
            name='callback_url',
            field=models.URLField(verbose_name=b'url\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='links',
            name='date_publish',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='links',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x8f\x8b\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='links',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)'),
        ),
        migrations.AlterField(
            model_name='links',
            name='title',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'avatar/default.png', upload_to=b'avatar/%Y/%m', max_length=200, blank=True, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=11, unique=True, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=20, null=True, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
    ]
