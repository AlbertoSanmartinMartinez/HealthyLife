# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180725_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]