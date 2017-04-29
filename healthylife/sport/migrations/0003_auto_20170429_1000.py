# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0002_auto_20170429_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportSesion',
            fields=[
                ('session_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('sport_type', models.ForeignKey(to='sport.SportType')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sportsession',
            name='sport_type',
        ),
        migrations.RemoveField(
            model_name='sportsession',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='SportSession',
        ),
    ]
