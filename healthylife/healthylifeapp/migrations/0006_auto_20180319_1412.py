# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0005_address_is_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, default=b'         ', max_length=9),
        ),
    ]