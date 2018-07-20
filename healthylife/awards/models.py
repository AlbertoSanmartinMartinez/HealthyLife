#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User
import datetime
from healthylifeapp import models as general_models

# Awards models
@autoconnect
class Award(models.Model):
    """modelo para los premios de los usuarios"""
    Status = ((1, "Activo"), (2, "Inactivo"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    AwardType = ((1,'Porcentaje'), (2, 'Cantidad'))
    award_type = models.IntegerField(choices=AwardType, default=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    author = models.ForeignKey(User, default=1)
    # company = models.ForeignKey(Company, default=1)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        metodo de la clase post para calcular el slug de un post y crear un album asociado a ese post
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            album = general_models.Album.objects.create(name='album_premio_'+self.title)
            self.album = album
        super(Award, self).save(*args, **kwargs)
