# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 15:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SportSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.datetime.today)),
                ('duration', models.TimeField()),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='sportsession',
            name='sport_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportapp.SportType'),
        ),
    ]
