#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from events import models as event_models

# Register your models here.
class EventAdmin(GuardedModelAdmin):
    list_display = ('id', 'privacity', 'type', 'title', 'owner', 'creation_date', 'updated_date', 'start', 'end')
    list_filter = ('privacity', 'type', 'start', 'end')
    search_fields = ('title', 'owner', 'owner')

admin.site.register(event_models.Event, EventAdmin)


"""
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('year', 'month', 'day')

admin.site.register(event_models.Calendar, CalendarAdmin)
"""
# admin.site.register(custom_calendar.EventCalendar)
