#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User
import datetime
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields

# Calendar models
"""
class Calendar(object):
    year
    month
    week
"""

# Event Models
@autoconnect
class Event(models.Model):
    """
    Clase para los eventos.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=250, blank=True)
    PrivacityType = ((1, 'Público'), (2, 'Privado'))
    privacity = models.IntegerField(choices=PrivacityType, default=1, blank=True)
    owner = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True)
    updated_date= models.DateTimeField(auto_now_add=True)
    # tipo de evento (sport, nutrition, health)
    participant = models.ManyToManyField(User, related_name='participants', blank=True)
    """
    year = models.PositiveIntegerField(default=str(datetime.datetime.now().year), blank=True)
    MONTHS = ((1, 'Enero'), (3, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre'))
    month = models.IntegerField(choices=MONTHS, default=1)
    DAYS = [(i, str(i)) for i in range(1, 33)]
    day = models.IntegerField(choices=DAYS, default=1)
    start_hour = models.TimeField(auto_now=True)
    end_hour = models.TimeField(auto_now=True)
    """
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())
    address = models.CharField(max_length=250, default='', blank=True)
    notes = models.CharField(max_length=250, default='', blank=True)

    def __unicode__(self):
        return self.title

    def pre_save(self):
        """Metodo para aignar el slug de un evento automaticamente al crearlo"""
        self.slug = self.title.replace(" ", "_").lower()
        # self.year = str(datetime.datetime.now().year)
        # hora final mayor que hora inicial

    def inviteParticipants(self):
        """
        Metodo que envia un correo a un usuario para que se una al evento
        """
        pass

# Sport Event
# Nutrition Event
# Health Event
