#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from healthylifeapp import views as general_views
from calendar import HTMLCalendar
from events import models as events_models

# Calendar views
def named_month(month_number):
    return date(1900, month_number, 1).strftime("%B")


def this_month(request):
    today = datetime.now()
    return calendar(request, today.year, today.month)


def event(request, username):
    """
    Vista para los eventos
    """
    if request.method == 'POST':
        event_form = forms.EventForm(data=request.POST)
        if event_form.is_valid():
            data = event_form.cleaned_data
            event = models.Event.objects.create()
            event.save()
    else:
        event_form = forms.EventForm()

    return render(request, 'event.html', {
        "search_form": getSearchForm(),
        "event": event,
    })

# login requerido
def calendar(request, username, year, month, day):
    """
    Vista para el calendario.
    """
    # Controlar si no hay usuario loggeado para mostrar solo los eventos publicos

    year = int(year)
    month = int(month)

    #calendar = models.EventCalendar()
    # htmlcalendar = HTMLCalendar(calendar.MONDAY)
    htmlcalendar = HTMLCalendar()
    htmlcalendar = htmlcalendar.formatmonth(year, month)

    #calendar_from_month = datetime(my_year, my_month, 1)
    #my_calendar_to_month = datetime(my_year, my_month, 1)
    #my_calendar_to_month = datetime(my_year, my_month, monthrange(my_year,my_month)[1])

    events = events_models.Event.objects.all() # filtrar por mes y usuario

    previous_year = year
    previous_month = month -1

    if previous_month == 0:
        previous_year = year -1
        previous_month = 12

    next_year = year
    next_month = month +1

    if next_month == 13:
        next_year = year +1
        next_month = 1

    year_after_this = year +1
    year_before_this = year -1

    return render(request, 'calendar.html', {
        "calendar": htmlcalendar,
        'search_form': general_views.getSearchForm(),
        'events': events,
        'month': month,
		'year': year,
		'previous_month': previous_month,
	    'previous_year': previous_year,
		'next_month': next_month,
		'next_year': next_year,
		'year_before_this': year_before_this,
		'year_after_this': year_after_this,
        'subscribe_form': general_views.getSubscribeForm(),
        #'month_name': named_month(my_month),
        #'previous_month_name': named_month(my_previous_month),
        #'next_month_name': named_month(my_next_month),
    })


def event(reques):
    pass
