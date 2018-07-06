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


# Admin Statistics Models
admin.site.register(models.GeneralStatistics)
admin.site.register(models.SpecificStatistics)

class ImageAdmin(GuardedModelAdmin):
    list_display = ('id', 'image', 'description', 'alt', 'album')

class ImageInLine(admin.TabularInline):
    model = models.Image
    list_display = ('id', 'image', 'description', 'alt')
    extra = 1

admin.site.register(models.Image, ImageAdmin)

class AlbumAdmin(GuardedModelAdmin):
    list_display = ('id', 'name', 'author')
    search_fields = ('name', 'author')
    inlines = [ImageInLine,]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(AlbumAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super(AlbumAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)


admin.site.register(models.Album, AlbumAdmin)

# Admin Profile Models
admin.site.register(models.UserProfile)

class CollaboratorProfileAdmin(GuardedModelAdmin):
    list_display = ('user', 'position', 'company', 'education', 'extract')

admin.site.register(models.CollaboratorProfile, CollaboratorProfileAdmin)

admin.site.register(models.Address)
admin.site.register(models.BankInformation)
admin.site.register(models.Company)


# Admin Permissions Models
admin.site.register(Permission)
admin.site.register(UserObjectPermission)

# Admin General Models
admin.site.register(models.Subscriber)
