# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0007_auto_20180312_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, b'Publicado'), (2, b'Pendiente de Revision'), (3, b'Eliminado')], default=3),
        ),
    ]
