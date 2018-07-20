#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from healthylife.decorators import autoconnect
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from healthylifeapp import models as general_models
import datetime

# Blog models
class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    slug = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()

    def __unicode__(self):
        return self.name


@autoconnect
class Category(models.Model):
    """Modelo para las categorias del blog"""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    author = models.ForeignKey(User, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def pre_save(self, *args, **kwargs):
        """
        """
        self.slug = self.name.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()


class PostType(models.Model):
    pass
    # nombre
    # plantilla


@autoconnect
class Post(models.Model):
    """Modelo para los articulos del blog"""
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=100, blank=False)
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=200, blank=False)
    content = RichTextField(default=" ", blank=False)
    category = models.ForeignKey(Category, default=1)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    author = models.ForeignKey(User, editable=False, null=True, blank=True)
    album = models.ForeignKey(general_models.Album, default=1, blank=True, null=True)
    # tags


    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        metodo de la clase post para calcular el slug de un post y crear un album asociado a ese post
        """
        self.slug = self.title.replace(" ", "_").lower()
        self.updated_date = datetime.datetime.now()
        if not self.pk:
            album = general_models.Album.objects.create(name='album ' + self.title, author=self.author)
            self.album = album
            general_models.Image.objects.create(album=self.album, header_image=True, image='photos/header_post_default_image.jpg')
        general_models.Album.objects.filter(id=self.album.id).update(name='Album Post ' + self.title)
        super(Post, self).save(*args, **kwargs)

    def publishPost(self):
        """metodo de la clase post para publicar en redes sociles un post"""
        pass


@autoconnect
class Comment(models.Model):
    """Modelo para los comentarios del blog"""
    Status = ((1, "Publicado"), (2, "Pendiente de Revision"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField()
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    parent = models.ForeignKey('self', related_name='answers', null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated_date = datetime.datetime.now()

    def post_save(self):
        self.notifyNewComment()

    def notifyNewComment(self):
        """Metodo que avisa de un nuevo comentario en el blog"""
        self.status = 1
        print("notificacion enviada")
