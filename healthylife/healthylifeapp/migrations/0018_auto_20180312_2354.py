# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 22:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthylifeapp', '0017_auto_20180312_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default=b' '),
        ),
    ]
