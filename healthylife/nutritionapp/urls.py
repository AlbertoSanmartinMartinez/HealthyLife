#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from nutritionapp import views as nutrition_views

# Nutrition URLS's
urlpatterns = [

    url(r'^$', nutrition_views.nutrition, name='nutrition'),
    url(r'^resultado_busqueda/$', nutrition_views.search_food, name='search_food'),
]
