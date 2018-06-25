# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from payments import PurchasedItem
from payments.models import BasePayment
from healthylife.decorators import autoconnect
from healthylifeapp import models as general_models

# Shop Models
@autoconnect
class Category(models.Model):
    """
    Model for categories from a shop
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def pre_save(self):
        self.slug = self.name.replace(' ', '_').lower()


class Discount(models.Model):
    name = models.CharField(max_length=50)
    DiscountType = ((1, "Cantidad"), (2, "Porcentaje"))
    type = models.IntegerField(choices=DiscountType, default=1)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __unicode__(self):
        return self.name


@autoconnect
class Product(models.Model):
    Status = ((1, "Activo"), (2, 'Inactivo'))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100, db_index=True, unique=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # professional_prize
    album = models.ForeignKey(general_models.Album, default=1, blank=True, null=True)
    # color
    Size = ((1, "XS"), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'))
    size = models.IntegerField(choices=Size, default=1, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    discount = models.ForeignKey(Discount, blank=True, null=True)
    #tag

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """metodo de la clase post para calcular el slug de un producto y crear un album asociado a ese producto"""
        self.slug = self.name.replace(" ", "_").lower()
        if not self.pk:
            album = general_models.Album.objects.create(name='album '+self.name)
            self.album = album
        super(Product, self).save(*args, **kwargs)

    """
    def pre_save(self):
        self.slug = self.name.replace(' ', '_').lower()
    """

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])


class ShopingChart(models.Model):
    # name = models.CharField(max_length=100, db_index=True)
    created_date = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=300, default="")
    products = models.CharField(max_length=300, default="")
    # controlar el estado del carrito
    # convertir en pedido cuando se finaliza el pedido
    # saber de quien es el carrito

    def __unicode__(self):
        return self.code


# https://www.wordstream.com/blog/ws/2016/03/17/shopping-cart-abandonment
class Order(models.Model):
    code = models.CharField(max_length=300, default="")
    created_date = models.DateTimeField(auto_now=True)
    OrderStatus = ((1, 'Pendiente de pago'), (2, 'Cancelado'), (3, 'Pagado'), (4, 'En preparación'), (5, 'Enviado'), (6, 'Entregado'))
    status = models.IntegerField(choices=OrderStatus, default=1)

    def __unicode__(self):
        return self.code


class Provider(models.Model):
    name = models.CharField(max_length=100, db_index=True, default='proveedor')
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    # slug

    def __unicode__(self):
        return self.name


# SEO Models
class MetaData(models.Model):
    pass


# Payment Models



@autoconnect
class Comment(models.Model):
    """Modelo para los comentarios de la tienda"""
    Status = ((1, "Publicado"), (2, "Pendiente de Revision"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, default=1)
    product = models.ForeignKey(Product, default=1)
    # guardar automaticamente el usuario que ha hecho el comentario
    parent = models.ForeignKey('self', related_name='answer', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def post_save(self):
        self.notifyNewComment()

    def notifyNewComment(self):
        """Metodo que avisa de un nuevo comentario en el blog"""
        self.status = 1
        print("notificacion enviada")


class Shipping(models.Model):
    company = models.CharField(max_length=100)
    # weight
    # country
    # region
    # province
    # city
    # time

    def __unicode__(self):
        return self.company
"""
https://www.youtube.com/watch?v=Z5dBopZWOzo
https://django-payments.readthedocs.io/en/latest/index.html

"""
