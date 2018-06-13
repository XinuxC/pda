# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statisticsrecord',
            name='datatime',
            field=models.DateTimeField(verbose_name='更新时间', default='2018-06-13'),
        ),
    ]
