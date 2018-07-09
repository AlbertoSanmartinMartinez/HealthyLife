#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from nutritionapp import views as nutrition_views

# Nutrition URLS's
urlpatterns = [

    url(r'^$', nutrition_views.nutrition, name='nutrition'),
    url(r'^informacion_nutricional/$', nutrition_views.nutrition, name='search_food'),
]
