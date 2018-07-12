#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from events import views as calendar_views
from events import models as calendar_models

urlpatterns = [

    # Calendar URLS's
    url(r'^(?P<username>\w+)/(?P<year>\w+)/(?P<month>\w+)/$', calendar_views.month, name='month_calendar'),
    url(r'^(?P<username>\w+)/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/$', calendar_views.day, name='day_calendar'),

    # Event Urls
    url(r'^(?P<username>\w+)/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/eventos/(?P<event_slug>\w+)/$', calendar_views.event, name='detail_event'),
    url(r'^eventos/nuevo/$', calendar_views.add_event, name='add_event'),
]
