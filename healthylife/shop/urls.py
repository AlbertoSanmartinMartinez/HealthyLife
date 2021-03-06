# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf.urls.static import static
from shop import views as shop_views
from django.conf import settings

urlpatterns = [

    # Products Shop Urls
    url(r'^productos/$', shop_views.product_list, name='product_list'),
    url(r'^productos/(?P<product_slug>.*)/$', shop_views.product_detail, name='product_detail'),
    url(r'^productos/(?P<product_slug>.*)/comentario', shop_views.add_review, name='add_review'),

    # Category Urls
    url(r'^categorias/(?P<shop_category_slug>\w+)/$', shop_views.product_list, name='product_list_category'),

    #Search Urls
    url(r'^productos/$', shop_views.product_list, name='shop_search'),

    # Payments Urls
    url(r'^pago/realizado$', shop_views.payment_done, name='payment_done'),
    url(r'^pago/cancelado$', shop_views.payment_canceled, name='payment_canceled'),

    # Shipping Urls
    url(r'^direccion_envio/$', shop_views.address_checkout, name='address_checkout'),
    url(r'^metodo_envio/$', shop_views.shipping_checkout, name='shipping_checkout'),
    url(r'^metodo_pago/$', shop_views.payment_checkout, name='payment_checkout'),

    url(r'^pedido/$', shop_views.order_checkout, name='order_checkout'),

    # ShopingChart Urls
    url(r'^carrito/$', shop_views.shoppingcart, name='shoppingcart_detail'),
    url(r'^carrito/nuevo/(?P<product_id>\d+)/$', shop_views.cartAdd, name='shoppingcart_add'),

    #Profile Urls
    url(r'^mi_cuenta/(?P<username>\w+)/pedidos/$', shop_views.ships, name='ships'),
    
]
