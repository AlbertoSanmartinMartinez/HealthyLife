#!/usr/local/bin/python
# coding: utf-8

from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.timezone import datetime
from django.forms import ModelForm
from django.db.models import signals
from django.dispatch import receiver
from django.utils.text import slugify
from healthylife.decorators import autoconnect
from django.core.validators import URLValidator
from guardian.shortcuts import assign_perm
from taggit.managers import TaggableManager
#from taggit.models import TagBase

# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFit

# General models
@autoconnect
class Address(models.Model):
    """Modelo para las direcciones postales"""
    address_name = models.CharField(max_length=50, default='mi direccion')
    city = models.CharField(max_length=50, default=' ', blank=True)
    postal_code = models.CharField(max_length=5, default='     ', blank=True)
    street = models.CharField(max_length=50, default=' ', blank=True)
    number = models.CharField(max_length=4, default=' ', blank=True)
    floor = models.CharField(max_length=3, default=' ', blank=True)
    door = models.CharField(max_length=3, default=' ', blank=True)
    user = models.ForeignKey(User, default=1)
    is_company = models.BooleanField(default=False)

    def __unicode__(self):
        return self.address_name

    @receiver(signals.post_save, sender=User)
    def create_user_address(sender, instance, created, **kwargs):
        """este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            Address.objects.create(user_id=instance.id)

    def pre_save(self):
        """metodo de la clase Address para estandarizar los atributos"""
        self.address_name = self.address_name.capitalize()
        self.city = self.city.title()
        self.street = self.street.title()
        self.door = self.door.upper()


class BankInformation(models.Model):
    """modelo para la informacion bancaria"""
    bank_name = models.CharField(max_length=50, default='mi informacion bancaria')
    account = models.CharField(max_length=20, default=' ', blank=True)
    month = models.CharField(max_length=2, default=' ', blank=True)
    year = models.CharField(max_length=4, default=' ', blank=True)
    security_code = models.CharField(max_length=3, default=' ', blank=True)
    user = models.ForeignKey(User, default=1)
    is_company = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.bank_name)

    def pre_save(self):
        """metodo de la clase BankInformation para estandarizar los atributos"""
        self.bank_name = self.bank_name.capitalize()

    @receiver(signals.post_save, sender=User)
    def create_user_bank_information(sender, instance, created, **kwargs):
        if created:
            BankInformation.objects.create(user_id=instance.id)


class UserProfile(models.Model):
    """Modelo para el perfil de un usuario"""
    user = models.OneToOneField(User)
    bio = models.TextField(max_length=100, blank=True)
    phone = models.CharField(max_length=9, default='         ', blank=True)
    profile_image = models.ImageField(upload_to="photos", default='photos/perfil_miniatura.jpg', blank=True)

    def __unicode__(self):
        return str(self.user.username)

    @receiver(signals.post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """Este metodo crea la direccion postal y la informacion bancaria de un usuario"""
        if created:
            UserProfile.objects.create(user_id=instance.id)


class CollaboratorProfile(models.Model):
    """Modelo para el perfil de un colaborador"""
    user = models.ForeignKey(User)
    position = models.CharField(max_length=50, default=' ', blank=True)
    company = models.CharField(max_length=50, default=' ', blank=True)
    education = models.CharField(max_length=50, default=' ', blank=True)
    extract = models.TextField(default=' ', blank=True)
    collaborator_image = models.ImageField(upload_to="photos", default='photos/perfil.jpg', blank=True)

    def __unicode__(self):
        return self.user.username


class Subscriber(models.Model):
    email = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.email


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
    # image_header = models.IntegerField(Image)

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


@autoconnect
class Company(models.Model):
    """modelo para las empresa de la tienda"""
    company_name = models.CharField(max_length=50, default='mi empresa')
    slug = models.CharField(max_length=100, default=' ', blank=True)
    description = models.CharField(max_length=100, default=' ', blank=True)
    phone = models.CharField(max_length=9, default='000000000', blank=True)
    web =  models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, default=1)
    company_image = models.ImageField(upload_to="photos", default='photos/perfil.jpg', blank=True)

    def __unicode__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """metodo de la clase company para calcular el slug"""
        self.slug = self.company_name.replace(" ", "_").lower()
        super(Company, self).save(*args, **kwargs)


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

    def __unicode__(self):
        return self.name

    def pre_save(self):
        """Metodo para asignar el usuario y la empresa automaticamente al crear un premio"""
        pass


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


# SEO models
class MetaData(models.Model):
    pass
