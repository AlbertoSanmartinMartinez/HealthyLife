#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from sportapp import views as sport_views

# Sport URLS's
urlpatterns = [

    url(r'^$', sport_views.sport, name='sport'),
    url(r'^ejercicios/$', sport_views.sport, name='search_sport'),
]
