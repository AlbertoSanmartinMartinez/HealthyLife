#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404, reverse
from healthylifeapp import views as general_views
from events import models as events_models
from events import forms as events_forms
import datetime
from calendar import monthrange
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Calendar views
def next_events(request):
    pass


@login_required(redirect_field_name='custom_login')
def month(request, username, year, month):
    """
    Calendar month view
    Calulate days of month
    """
    month = int(month)
    year = int(year)

    if month == 0:
        year = year-1
        month = 12

        month = unicode(month)
        year = unicode(year)

        return redirect('calendar:month_calendar', username=username, year=year, month=month)

    if month == 13:
        year = year+1
        month = 1

        month = unicode(month)
        year = unicode(year)

        return redirect('calendar:month_calendar', username=username, year=year, month=month)

    first_day_of_week_number = monthrange(year, month)[0]
    last_day_number = monthrange(year, month)[1]

    previous_month = month-1
    next_month = month+1

    days = []
    max_number = None
    num = 1

    # calculate minimum and maximum calendar days
    if last_day_number == 28:
        if first_day_of_week_number == 0:
            max_number = 28
        else:
            max_number = 35
    elif last_day_number == 29:
        max_number = 35
    elif last_day_number == 30:
        if first_day_of_week_number <= 5:
            max_number = 35
        else:
            max_number = 42
    elif last_day_number == 31:
        if first_day_of_week_number <= 4:
            max_number = 35
        else:
            max_number = 42
    else:
        max_number = None

    #create calendar days
    for item in range(0, max_number):
        if item >= first_day_of_week_number and num <= last_day_number:
            days.append(num)
            num += 1
        else:
            days.append(0)

    month_name = getMonthName(month)
    month = unicode(month)
    year = unicode(year)
    previous_month = unicode(previous_month)
    next_month = unicode(next_month)

    return render(request, 'month_calendar.html', {
        'days': days,
        'month': month,
        'month_name': month_name,
        'year': year,
        'previous_month': previous_month,
        'next_month': next_month,
        'event_form': getEventform(request),
        #'current_day': current_day,
        #'current_month': current_month,
        #'current_year': current_year
    })


@login_required(redirect_field_name='custom_login')
def day(request, username, year, month, day):
    events = events_models.Event.objects.all()

    month = int(month)
    year = int(year)
    day = int(day)

    last_day_number = monthrange(year, month)[1]

    if day > last_day_number:
        month = month+1
        day = 1

        if month == 13:
            year = year+1
            month = 1

        month = unicode(month)
        year = unicode(year)
        day = unicode(day)

        return redirect('calendar:day_calendar', username=username, year=year, month=month, day=day)

    if day == 0:
        month = month-1

        if month == 0:
            year = year-1
            month = 12

        day = monthrange(year, month)[1]

        month = unicode(month)
        year = unicode(year)
        day = unicode(day)

        return redirect('calendar:day_calendar', username=username, year=year, month=month, day=day)

    day_name = getDayName(datetime.datetime(year, month, day).weekday())

    previous_day = day-1
    next_day = day+1
    previous_day = unicode(previous_day)
    next_day = unicode(next_day)

    return render(request, 'day_calendar.html', {
        'events': events,
        'day': day,
        'month': month,
        'month_name': getMonthName(month),
        'day_name': day_name,
        'year': year,
        'previous_day': previous_day,
        'next_day': next_day,
        'event_form': getEventform(request),
    })


# def event(request, event_slug):
def event(request, username, year, month, day, event_slug):
    user = get_object_or_404(User, username=username)
    event = get_object_or_404(events_models.Event, slug=event_slug, owner=user.id)

    return render(request, 'event.html', {
        "search_form": general_views.getSearchForm(),
        # "event_form": event_form,
    })


def add_event(request):
    if request.method == 'POST':
        event_form = getEventform(request)
        if event_form.is_valid():
            data = event_form.cleaned_data
            print(data['title'])
            print(data['description'])
            print(data['address'])
            print(data['privacity'])
            user = request.user
            print(user.id)
            year = datetime.datetime.now().year
            print(year)
            month = data['month']
            print(month)
            day = data['day']
            print(day)
            print(data['start_hour'])
            print(data['start_minutes'])
            print(data['end_hour'])
            print(data['end_minutes'])

            #int(data['start_hour']),int(data['start_minutes'])

            events_models.Event.objects.create(
                title=data['title'],
                description=data['description'],
                address=data['address'],
                privacity=data['privacity'],
                owner=user,
                start=datetime.datetime(int(year),int(month),int(day),int(data['start_hour']),int(data['start_minutes'])),
                end=datetime.datetime(int(year),int(month),int(day),int(data['end_hour']),int(data['end_minutes'])),
                notes=data['notes']
            )
            #event_form.save()
    else:
        event_form = events_forms.EventForm()

    return redirect('calendar:day_calendar', username=user.username, year=year, month=month, day=day)


# Common Functions
def getEventform(request):
    if request.method == 'POST':
        return events_forms.EventForm(request.POST)
    else:
        return events_forms.EventForm()


def getMonthName(month):
    if (month == 1):
        return 'Enero'
    if (month == 2):
        return 'Febrero'
    if (month == 3):
        return 'Marzo'
    if (month == 4):
        return 'Abril'
    if (month == 5):
        return 'Mayo'
    if (month == 6):
        return 'Junio'
    if (month == 7):
        return 'Julio'
    if (month == 8):
        return 'Agosto'
    if (month == 9):
        return 'Septiembre'
    if (month == 10):
        return 'Octubre'
    if (month == 11):
        return 'Noviembre'
    if (month == 12):
        return 'Diciembre'

def getDayName(number):
    if (number == 0):
        return 'Lunes'
    if (number == 1):
        return 'Martes'
    if (number == 2):
        return 'Miércoles'
    if (number == 3):
        return 'Jueves'
    if (number == 4):
        return 'Viernes'
    if (number == 5):
        return 'Sábado'
    if (number == 6):
        return 'Domingo'





#
