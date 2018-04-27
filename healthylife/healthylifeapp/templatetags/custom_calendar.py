#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
# import calendar
from django import template
from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

register = template.Library()

def do_event_calendar(parser, token):
    try:
        tag_name, year, month, event_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
    return EventCalendarNode(year, month, event_list)


class EventCalendarNode(template.Node):

    def __init__(self, year, month, day, event_list):
        try:
            self.year = template.Variable(year)
            self.month = template.Variable(month)
            self.day = template.Variable(day)
            self.event_list = template.Variable(event_list)
        except ValueError:
            raise template.TemplateSyntaxError

    def render(self, context):
        try:
            my_event_list = self.event_list.resolve(context)
            my_year = self.year.resolve(context)
            my_month = self.month.resolve(context)
            cal = EventCalendar(my_event_list)
            return cal.formatmonth(init(my_year), init(my_month))
        except ValueError:
            return
        except template.VariableDoesNotExist:
            return


class EventCalendar(HTMLCalendar):
    """
    """

    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.group_by_day(events)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += 'today'
            if day in self.events:
                cssclass += 'filled'
                body = ['<ul>']
                for event in self.events[day]:
                    body.append('li')
                    body.append('<a href="%s">' % event.get_absolute-url())
                    body.append(esc(event.series.primary_key))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '<span class=dayNumber">%d</span> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<span class=dayNumberNoEvents">%d</span> %s' % (day))
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, slef).formatmonth(year, month)

    def group_by_day(self, events):
        field = lambda event: event.date_and_time.day
        return dict(
            [(day, list(items)) for day,items in groupby(events, field)]
        )

register.tag("event_calendar", do_event_calendar)
