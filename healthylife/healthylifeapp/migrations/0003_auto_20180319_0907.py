# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0002_auto_20180318_2348'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default=b'/perfil.jpg', upload_to=b'photos'),
        ),
    ]
