#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from awards import views as awards_views

urlpatterns = [

    # Awards URLS's
    url(r'^premios/$', awards_views.awards, name='awards'),
    url(r'^premios/lista_de_pemios$', awards_views.awards, name='search_awards'),

    url(r'^mi_cuenta/(?P<username>\w+)/premios/$', awards_views.awards_profile, name='awards_profile'),
]
