# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 10:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20180929_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 12, 54, 50, 653952)),
        ),
    ]