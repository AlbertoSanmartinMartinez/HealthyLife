# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0003_auto_20180427_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='healthylifeapp.Comment'),
        ),
    ]
