#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from events import models as event_models

# Register your models here.
class EventAdmin(GuardedModelAdmin):
    list_display = ('title', 'privacity', 'owner')
    list_filter = ('title', 'privacity', 'owner')
    search_fields = ('title', 'privacity', 'owner')

admin.site.register(event_models.Event, EventAdmin)

# admin.site.register(custom_calendar.EventCalendar)
