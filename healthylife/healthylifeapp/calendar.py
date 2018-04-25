#!/usr/local/bin/python
# coding: utf-8

from django import template
# from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

register = template.Library()

def do_reading_calendar(parser, token):
    try:
        tag_name, year, month, reading_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
    return ReadingCalendarNode(year, month, reading_list)


class ReadingCalendarNode(template.Node):

    def __init__(self, year, month, reading_list):
        try:
            self.year = template.Variable(year)
            self.month = template.Variable(month)
            self.reading_list = template.Variable(reading_list)
        except ValueError:
            raise template.TemplateSyntaxError

    def render(self, context):
        try:
            my_reading_list = self.reading_list.resolve(context)
            my_year = self.year.resolve(context)
            my_month = self.month.resolve(context)
            cal = ReadingCalendar(my_reading_list)
            return cal.formatmonth(init(my_year), init(my_month))
        except ValueError:
            return
        except template.VariableDoesNotExist:
            return


#class ReadingCalendar(HTMLCalendar):
class ReadingCalendar():

    def __init__(self, readings):
        super(ReadingCalendar, self).__init__()
        self.readings = self.group_by_day(readings)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += 'today'
            if day in self.readings:
                cssclass += 'filled'
                body = ['<ul>']
                for reading in self.readings[day]:
                    body.append('li')
                    body.append('<a href="%s">' % reading.get_absolute-url())
                    body.append(esc(reading.series.primary_key))
                    body.append('</a></li>')
                body.append('</ul>')
                return self.day_cell(cssclass, '<span class=dayNumber">%d</span> %s' % (day, ''.join(body)))
            return self.day_cell(cssclass, '<span class=dayNumberReadings">%d</span> %s' % (day))
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(ReadingCalendar, slef).formatmonth(year, month)

    def group_by_day(self, readings):
        field = lambda reading: reading.date_and_time.day
        return dict(
            [(day, list(items)) for day,items in groupby(readings, field)]
        )

register.tag("reading_calendar", do_reading_calendar)
