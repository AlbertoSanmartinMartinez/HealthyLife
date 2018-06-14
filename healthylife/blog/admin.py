#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from blog import models as blog_models
from guardian.admin import GuardedModelAdmin

# Admin Blog Models
class CategoryAdmin(GuardedModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('name', 'parent')
    search_fields = ('name', 'parent')

admin.site.register(blog_models.Category, CategoryAdmin)

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

admin.site.register(blog_models.Post, PostAdmin)


class TagsAdmin(GuardedModelAdmin):
    list_display = ('name', 'created_date')

admin.site.register(blog_models.Tag, TagsAdmin)


class CommentAdmin(GuardedModelAdmin):
    list_display = ('status', 'title', 'author', 'post', 'parent')
    list_filter = ('status', 'title', 'author', 'post', 'parent')
    search_fields = ('status', 'title', 'author', 'post', 'parent')

admin.site.register(blog_models.Comment, CommentAdmin)
