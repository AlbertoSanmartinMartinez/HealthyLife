#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from events import views as calendar_views

urlpatterns = [

    # Calendar URLS's
    url(r'^(?P<username>\w+)/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/$', calendar_views.calendar, name='calendar'),
    #url(r'^mi_cuenta/(?P<username>\w+)/calendario/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/(?<slug>\w)/$', views.event, name='detail_event'),
    url(r'^(?P<username>\w+)/eventos/nuevo/$', calendar_views.event, name='add_event'),
]
