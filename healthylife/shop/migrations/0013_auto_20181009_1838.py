# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20181008_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 18, 38, 58, 882318)),
        ),
    ]
