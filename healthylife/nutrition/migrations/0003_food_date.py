# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20170429_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 5, 1, 9, 6, 14, 851020, tzinfo=utc), verbose_name=datetime.date.today),
            preserve_default=False,
        ),
    ]
