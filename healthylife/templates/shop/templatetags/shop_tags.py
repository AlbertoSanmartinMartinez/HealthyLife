#!/usr/local/bin/python
# coding: utf-8

from django import template
from django.shortcuts import render
from shop import models as shop_models
from healthylifeapp import models as general_models

register = template.Library()

@register.simple_tag
def calculateStockItem(product_id):
    product = shop_models.Product.objects.filter(id=product_id)

    return product.stock

@register.simple_tag
def getHeaderImage(product_id):
    product = shop_models.Product.objects.get(id=str(product_id))
    picture = general_models.Image.objects.get(header_image=True, album=product.album)

    return picture

@register.simple_tag
def getImages(product_id):
    product = shop_models.Product.objects.get(id=product_id)
    pictures = general_models.Image.objects.filer(header_image=False, album=product.album)

    return picture
