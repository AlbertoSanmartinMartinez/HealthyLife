from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SportType(models.Model):
    sport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # default=''

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


class SportSesion(models.Model):
    session_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType)
    date = models.DateField()
    usuario = models.ForeignKey(User)
    # duration
    # calories
    # time

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name
