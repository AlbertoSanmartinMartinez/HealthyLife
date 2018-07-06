#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User

# Calendar models

#class EventCalendar(HTMLCalendar):
class Calendar(models.Model):
    """
    Clase para el calendario.
    Formado por un día, un mes y año. Infinitos calendarios
    """
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getEvents(self):
        """
        Devuelve todos los eventos de un calendario
        """
        events = models.Event.objects.filter()
        return events

    def addEvent(self):
        #controlar los parámetros que se pasan del calendario
        models.Event.create()

    def formatday(self, day, weekday):
        pass

    def formatmonth(self, year, month):
        pass

    def group_by_day(self, events):
        pass

    def render(self, context):
        try:
            events = self.events.resolve(context)
            year = self.year.resolve(context)
            month = self.month.resolve(context)
            day = self.day.resolve(context)
            cal = EventCalendar(events)
            return cal.formatmonth(int(year), int(month), int(day))
        except ValueError:
            return
        except template.VariableDoesNotExist:
            return


@autoconnect
class Event(models.Model):
    """
    Clase para los eventos.
    """
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default=' ', blank=True)
    description = models.TextField()
    PrivacityType = ((1, 'Público'), (2, 'Privado'))
    privacity = models.IntegerField(choices=PrivacityType, default=1, blank=True)
    owner = models.ForeignKey(User)
    # tipo de evento
    # participant = models.ManyToManyField(User, related_name='event_participants')
    #date = models.DateField(default=datetime.now)
    # end_date = models.DateField(default=datetime.now)
    #time = models.TimeField(default=datetime.now)
    #end_hour = models.TimeField(default=datetime.now)
    # address = models.ForeignKey(Address, default=1, blank=True)
    #calendar = models.ForeignKey(Calendar, default=datetime.today) #revisar la estandarizacion de la fecha

    def __unicode__(self):
        return self.title

    def pre_save(self):
        """Metodo para aignar el slug y el autor de un post automaticamente al crearlo"""
        self.slug = self.title.replace(" ", "_").lower()

    def inviteParticipants(self):
        """
        Metodo que envia un correo a un usuario para que se una al evento
        """
        pass

    # funcion para estandarizar el calendario del evento
