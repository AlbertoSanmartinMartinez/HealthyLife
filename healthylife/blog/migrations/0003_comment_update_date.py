# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180704_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
