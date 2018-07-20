# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 09:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healthylifeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.Category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(1, 'Cantidad'), (2, 'Porcentaje')], default=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=300)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(1, 'Pendiente de pago'), (2, 'Cancelado'), (3, 'Pagado'), (4, 'En preparaci\xf3n'), (5, 'Enviado'), (6, 'Entregado')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Activo'), (2, 'Inactivo')], default=2)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('stock', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('size', models.IntegerField(blank=True, choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')], default=1, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5)),
                ('album', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='healthylifeapp.Album')),
                ('author', models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Discount')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='proveedor', max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Publicado'), (2, 'Pendiente de Revision'), (3, 'Eliminado')], default=2)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=100)),
                ('mark', models.IntegerField(default=10)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='shop.Review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShopingChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(default='', max_length=300, unique=True)),
                ('products', models.CharField(default='', max_length=300)),
                ('status', models.IntegerField(choices=[(1, 'Activo'), (2, 'Abandonado')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
