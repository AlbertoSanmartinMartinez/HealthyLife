# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 15:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Activo'), (2, 'Inactivo')], default=2)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(blank=True, default=' ', max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('award_type', models.IntegerField(choices=[(1, 'Porcentaje'), (2, 'Cantidad')], default=2)),
                ('amount', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
