# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161007_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba', blank=True, to='blog.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='rid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name=b'\xe5\x90\x8c\xe7\xba\xa7\xe5\x9b\x9e\xe5\xa4\x8d', blank=True, to='blog.Response', null=True),
        ),
    ]
