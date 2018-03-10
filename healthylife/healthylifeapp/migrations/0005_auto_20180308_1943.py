# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0004_auto_20180302_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('discount', models.IntegerField(default=1, choices=[(1, b'Cantidad'), (2, b'Porcentaje')])),
                ('amount', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='award',
            name='price',
        ),
        migrations.RemoveField(
            model_name='company',
            name='telefone',
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(default=b'000000000', max_length=9),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=b'000000000', max_length=9),
        ),
        migrations.AlterField(
            model_name='company',
            name='web',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
