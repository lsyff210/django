# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-24 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thing', models.CharField(max_length=200, verbose_name='待做的事情')),
            ],
        ),
    ]
