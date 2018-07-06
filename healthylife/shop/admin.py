#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from shop import models as shop_models
from guardian.admin import GuardedModelAdmin

# Admin Shop Models
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'name', 'created_date', 'category', 'stock', 'price', 'album', 'discount']
    list_filter = ['status', 'category']
    list_editable = ['status', 'name', 'category', 'stock', 'price', 'album', 'discount']
    search_fields = ['name', 'stock', 'price']
    readonly_fields = ('slug', 'author', 'album')
    # prepopulated_fields

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(ProductAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

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
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'content', 'creation_date', 'author', 'product', 'parent')
    list_editable = ('status', 'author')
    list_filter = ('status', 'parent')
    search_fields = ('title', 'content', 'author', 'post')

admin.site.register(shop_models.Review, ReviewAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount')

admin.site.register(shop_models.Discount, DiscountAdmin)

admin.site.register(shop_models.Shipping)
