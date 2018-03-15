#!/usr/local/bin/python
# coding: utf-8

from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.timezone import datetime
from django.forms import ModelForm
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify
from healthylifeapp.decorators import autoconnect
from django.core.validators import URLValidator
from guardian.shortcuts import assign_perm
from ckeditor.fields import RichTextField
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFit

# General models
class Address(models.Model):
    """Modelo para las direcciones postales"""
    name = models.CharField(max_length=50, default='mi direccion')
    city = models.CharField(max_length=50, default=' ', blank=True)
    postal_code = models.CharField(max_length=5, default='00000', blank=True)
    street = models.CharField(max_length=50, default=' ', blank=True)
    number = models.CharField(max_length=4, default=' ', blank=True)
    floor = models.CharField(max_length=3, default=' ', blank=True)
    door = models.CharField(max_length=3, default=' ', blank=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.name)

    @receiver(signals.post_save, sender=User)
    def create_user_address(sender, instance, created, **kwargs):
        """este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            Address.objects.create(user_id=instance.id)


class BankInformation(models.Model):
    """modelo para la informacion bancaria"""
    name = models.CharField(max_length=50, default='mi informacion bancaria')
    account = models.CharField(max_length=20, default=' ', blank=True)
    month = models.CharField(max_length=2, default=' ', blank=True)
    year = models.CharField(max_length=4, default=' ', blank=True)
    security_code = models.CharField(max_length=3, default=' ', blank=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return str(self.name)

    @receiver(signals.post_save, sender=User)
    def create_user_bank_information(sender, instance, created, **kwargs):
        if created:
            BankInformation.objects.create(user_id=instance.id)


class UserProfile(models.Model):
    """Modelo para el perfil de un usuario"""
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=9, default='000000000', blank=True)
    image = models.ImageField(upload_to="photos", default='/image.jpg', blank=False)


    def __unicode__(self):
        return str(self.user.username)

    @receiver(signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """Este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            UserProfile.objects.create(user_id=instance.id)


# Sport models
class SportType(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):  # python 2
        return self.name


class SportSession(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType)
    date = models.DateField(datetime.today)
    # usuario = models.ForeignKey(User)
    duration = models.TimeField()
    calories = models.IntegerField()

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


# Nutrition models
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(datetime.today)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def addIngredient(self):
        pass


class Measure(models.Model):
    """puede ser conveniente un campo de eleccion multiple antes que una clase"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    fats = models.ForeignKey(Nutrient, default='')
    # carbohydrates = models.ForeignKey(Nutrient)
    # proteins = models.ForeignKey(Nutrient)
    # fiber = models.ForeignKey(Nutrient)
    # sodium = models.ForeignKey(Nutrient)
    # calories = models.ForeignKey(Nutrient)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# Health models
class Illnes(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


# Statistics models
class GeneralStatistics(models.Model):
    pass

    def __unicode__(self):
        pass


class SpecificStatistics(models.Model):
    pass


# Gallery models
@autoconnect
class Album(models.Model):
    name = models.CharField(max_length=50, default='album')
    slug = models.CharField(max_length=100, blank=True)
    # image_header = models.IntegerField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """metodo de la clase Album para calcular el slug"""
        self.slug = self.name.replace(" ", "_").lower()
        super(Album, self).save(*args, **kwargs)


class Image(models.Model):
    """
    Modelo para las fotos
    https://stackoverflow.com/questions/765396/exif-manipulation-library-for-python
    """
    album = models.ForeignKey(Album, default=1)
    header_image = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos", default='/image.jpg', blank=False)
    # image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
    description = models.CharField(max_length=20, blank=True)
    alt = models.CharField(max_length=20, blank=True) # texto alternativo alt=""
    # tamaño (jpeg)
    # datos exif
    # sitemap de imagenes

    def __unicode__(self):
        return unicode(self.image)


# Blog models
@autoconnect
class Category(models.Model):
    """Modelo para las categorias del blog"""
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def pre_save(self):
        """metodo de la clase Category para calcular el slug de una categoria"""
        self.slug = self.name.replace(" ", "_").lower()


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
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=31, blank=True)
    album = models.ForeignKey(Album, default=1, blank=True, null=True)


    def __unicode__(self):
        return self.title

    def pre_save(self):
        pass

    def save(self, *args, **kwargs):
        """metodo de la clase post para calcular el slug de un post y crear un album asociado a ese post"""
        self.slug = self.title.replace(" ", "_").lower()
        album = Album.objects.create(name='album '+self.title)
        self.album = album
        super(Post, self).save(*args, **kwargs)

    def publishPost(self):
        """metodo de la clase post para publicar en redes sociles un post"""
        pass

    """
    @receiver(signals.post_save)
    def asignPermissions(sender, **kwargs):
        assign_perm('view_post', post.author, post)
    """

@autoconnect
class Comment(models.Model):
    """Modelo para los comentarios del blog"""
    Status = ((1, "Publicado"), (2, "Pendiente de Revision"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=2, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1)
    post = models.ForeignKey(Post, default=1)
    # guardar automaticamente el usuario que ha hecho el comentario

    def __unicode__(self):
        return self.title

    def notifyNewComment(self):
        """Metodo que avisa de un nuevo comentario en el blog"""
        pass

# Shop models
class Product(models.Model):
    """modelo para los productos de la tienda"""
    pass

    def __unicode__(self):
        pass


class Discount(models.Model):
    name = models.CharField(max_length=50)
    DiscountType = ((1, "Cantidad"), (2, "Porcentaje"))
    discount = models.IntegerField(choices=DiscountType, default=1)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        pass


class Company(models.Model):
    """modelo para las empresa de la tienda"""
    name = models.CharField(max_length=50, default='mi empresa')
    description = models.CharField(max_length=100, default=' ', blank=True)
    phone = models.CharField(max_length=9, default='000000000', blank=True)
    web =  models.CharField(max_length=50, validators=[URLValidator()], blank=True)
    user = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Awards models
@autoconnect
class Award(models.Model):
    """modelo para los premios de los usuarios"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    AwardType = ((1,'Porcentaje'), (2, 'Cantidad'))
    award_type = models.IntegerField(choices=AwardType, default=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    author = models.ForeignKey(User, default=1)
    company = models.ForeignKey(Company, default=1)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def pre_save(self):
        """Metodo para asignar el usuario y la empresa automaticamente al crear un premio"""
        pass


@autoconnect
class Event(models.Model):
    """
    Modelo para los eventos
    https://williambert.online/2011/06/django-event-calendar-for-a-django-beginner/
    https://djangosnippets.org/snippets/2464/
    """
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, default=' ', blank=True)
    description = models.TextField()
    PrivacityType = ((1, 'Público'), (2, 'Privado'))
    privacity = models.IntegerField(choices=PrivacityType, default=1)
    owner = models.ForeignKey(User)
    participant = models.ManyToManyField(User, related_name='event_participants')
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    address = models.ForeignKey(Address, default=1)

    def __unicode__(self):
        return self.name

    def pre_save(self):
        """Metodo para aignar el slug y el autor de un post automaticamente al crearlo"""
        self.slug = self.title.replace(" ", "_").lower()
        # self.owner = instance.username

    def inviteParticipants(self):
        """
        Metodo que envia un correo a un usuario para que se una al evento
        """
        pass


# SEO models
class MetaData(models.Model):
    pass
