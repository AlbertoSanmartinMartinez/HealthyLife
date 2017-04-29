# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportSession',
            fields=[
                ('session_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('sport_type', models.ForeignKey(to='sport.SportType')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sportsesion',
            name='sport_type',
        ),
        migrations.RemoveField(
            model_name='sportsesion',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='SportSesion',
        ),
    ]
