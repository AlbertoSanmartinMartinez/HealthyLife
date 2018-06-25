#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from shop import models as shop_models
from guardian.admin import GuardedModelAdmin

# Admin Shop Models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'created_date', 'category', 'description', 'stock', 'price', 'album', 'discount']
    list_filter = ['status', 'category']
    list_editable = ['status', 'name', 'category', 'description', 'stock', 'price', 'album', 'discount']
    search_fields = ['name', 'stock', 'price']
    # prepopulated_fields

admin.site.register(shop_models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parent']
    list_filter = ['name', 'description', 'parent']
    list_editable = ['name', 'description', 'parent']
    search_fields = ['name', 'description', 'parent']
    # prepopulated_fields

admin.site.register(shop_models.Category, CategoryAdmin)


class ShopingChartAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_date', 'products']

admin.site.register(shop_models.ShopingChart, ShopingChartAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

admin.site.register(shop_models.Provider, ProviderAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']

admin.site.register(shop_models.Tag, TagAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_date', 'status']

admin.site.register(shop_models.Order, OrderAdmin)
"""
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    inlines = [ImageInLine,]

admin.site.register(models.Album, AlbumAdmin)
"""
class CommentAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'content', 'creation_date')

admin.site.register(shop_models.Comment, CommentAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount')

admin.site.register(shop_models.Discount, DiscountAdmin)

admin.site.register(shop_models.Shipping)
