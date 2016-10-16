# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatar/default.png', upload_to='avatar/%Y/%m', max_length=200, blank=True, null=True, verbose_name='\u7528\u6237\u5934\u50cf'),
        ),
    ]
