# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeneralStatistics',
        ),
        migrations.DeleteModel(
            name='SpecificStatistics',
        ),
    ]
