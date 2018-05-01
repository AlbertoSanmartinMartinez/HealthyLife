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

# Admin Sport Models
admin.site.register(models.SportType)

class SportSessionAdmin(GuardedModelAdmin):
    model = models.SportSession

admin.site.register(models.SportSession, SportSessionAdmin)

# Admin Nutrition Models
admin.site.register(models.Food)
admin.site.register(models.Measure)
admin.site.register(models.Nutrient)
admin.site.register(models.Ingredient)

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
"""
class TagAdmin(GuardedModelAdmin):
    list_display = ('name', 'slug')

admin.site.register(models.Tag, TagAdmin)
"""

class CategoryAdmin(GuardedModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('name', 'parent')
    search_fields = ('name', 'parent')

admin.site.register(models.Category, CategoryAdmin)

class PostAdmin(GuardedModelAdmin):
    """
    Modelo de administracion para los posts
    """
    list_display = ('status', 'title', 'slug', 'category', 'author')
    list_filter = ('status', 'title', 'slug', 'category', 'author')
    search_fields = ('status', 'title', 'slug', 'category', 'author')
    readonly_fields = ('author', 'slug', 'album')

    def save_model(self, request, obj, form, change):
        """
        Metodo que modifica el author del post
        """
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)

admin.site.register(models.Post, PostAdmin)

"""
class PostTagsAdmin(GuardedModelAdmin):
    list_display = ('name', 'description')

admin.site.register(models.PosTags, PostTagsAdmin)
"""

class CommentAdmin(GuardedModelAdmin):
    list_display = ('status', 'title', 'author', 'post', 'parent')
    list_filter = ('status', 'title', 'author', 'post', 'parent')
    search_fields = ('status', 'title', 'author', 'post', 'parent')

admin.site.register(models.Comment, CommentAdmin)

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

# Admin Health Models
class IllnesAdmin(GuardedModelAdmin):
    model = models.Illnes

admin.site.register(models.Illnes, IllnesAdmin)

# Admin General Models
admin.site.register(models.Subscriber)
