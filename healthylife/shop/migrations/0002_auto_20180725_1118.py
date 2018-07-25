# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 09:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='shop_tags', to='shop.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='author',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shop_tag_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 25, 11, 18, 39, 59055)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
