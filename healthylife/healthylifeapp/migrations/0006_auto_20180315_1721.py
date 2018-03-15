# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 16:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0005_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, default=b' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, default=b'000000000', max_length=9),
        ),
        migrations.AlterField(
            model_name='company',
            name='web',
            field=models.CharField(blank=True, max_length=50, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default=b'000000000', max_length=9),
        ),
    ]
