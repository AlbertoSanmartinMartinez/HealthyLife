#!/usr/local/bin/python
# coding: utf-8
"""
https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.save_model
"""

from django.contrib import admin
from healthylifeapp import models
from healthylifeapp import custom_calendar
from django.contrib.auth.models import Permission
from guardian.admin import GuardedModelAdmin
from guardian.models import UserObjectPermission
from taggit.managers import TaggableManager
# from rollyourown.seo.admin import register_seo_admin
# from myapp.seo import MyMetadata
# from collections import OrderedDict as SortedDict

# Admin Awards Models
class AwardAdmin(GuardedModelAdmin):
    list_display = ('name', 'description', 'award_type', 'amount', 'company', 'author')
    list_filter = ('name', 'description', 'award_type', 'amount', 'company', 'author')
    search_fields = ('name', 'description', 'award_type', 'amount', 'company', 'author')

admin.site.register(models.Award, AwardAdmin)

# Admin Statistics Models
admin.site.register(models.GeneralStatistics)
admin.site.register(models.SpecificStatistics)

# Admin Blog Models


class ImageAdmin(GuardedModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(GuardedModelAdmin):
    list_display = ('name', 'slug')
    inlines = [ImageInLine,]

admin.site.register(models.Album, AlbumAdmin)

# Admin Profile Models
admin.site.register(models.UserProfile)

class CollaboratorProfileAdmin(GuardedModelAdmin):
    list_display = ('user', 'position', 'company', 'education', 'extract')

admin.site.register(models.CollaboratorProfile, CollaboratorProfileAdmin)

admin.site.register(models.Address)
admin.site.register(models.BankInformation)
admin.site.register(models.Company)

# Admin Shop Models
class ProductAdmin(GuardedModelAdmin):
    model = models.Product

admin.site.register(models.Product)

# Admin Events Models
class EventAdmin(GuardedModelAdmin):
    list_display = ('title', 'privacity', 'owner')
    list_filter = ('title', 'privacity', 'owner')
    search_fields = ('title', 'privacity', 'owner')

admin.site.register(models.Event, EventAdmin)

# admin.site.register(custom_calendar.EventCalendar)

# Admin Permissions Models
admin.site.register(Permission)
admin.site.register(UserObjectPermission)

# Admin General Models
admin.site.register(models.Subscriber)
