# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0007_auto_20180315_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Illnes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
