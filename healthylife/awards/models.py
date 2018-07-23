#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from django.contrib.auth.models import User
from shop import models as shop_models
from healthylifeapp import models as general_models
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
import datetime

# Awards models
@autoconnect
class Award(models.Model):
    """
    modelo para los premios de los usuarios
    https://docs.djangoproject.com/en/2.0/ref/contrib/contenttypes/#reverse-generic-relations
    """
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
    author = models.ForeignKey(User, editable=False, null=True, blank=True)
    album = models.ForeignKey(general_models.Album, blank=True, null=True)
    object = models.ManyToManyField(shop_models.Product)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Award method that save the slug, updated date and create the award album
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            album = general_models.Album.objects.create(name='Album Premio '+self.title, author=self.author, )
            self.album = album
            general_models.Image.objects.create(album=self.album, header_image=True, image='photos/header_award_default_image.jpg')
        general_models.Album.objects.filter(id=self.album.id).update(name='Album Premio ' + self.title)
        super(Award, self).save(*args, **kwargs)

    def get_limit_choices_to(self):
        pass




    #
