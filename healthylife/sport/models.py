from __future__ import unicode_literals
from django.db import models


# Create your models here.
class sport_sesion(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    # sport_type =
    # duration
    # calories
    # time

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


class sport_type(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name
