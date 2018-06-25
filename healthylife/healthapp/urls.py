#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from healthapp import views as health_views

# Sport URLS's
urlpatterns = [

    url(r'^$', health_views.health, name='health'),

]
