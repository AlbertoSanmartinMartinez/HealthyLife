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
    list_display = ('id', 'status', 'title', 'slug', 'category', 'author')
    list_filter = ('status', 'category', 'author')
    search_fields = ('title', 'slug', 'author')
    list_editable = ('status', 'title', 'category')
    readonly_fields = ('slug', 'author', 'album')
    #exclude = ('author', 'album')

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

admin.site.register(blog_models.Post, PostAdmin)


class TagsAdmin(GuardedModelAdmin):
    list_display = ('name', 'created_date')

admin.site.register(blog_models.Tag, TagsAdmin)


class CommentAdmin(GuardedModelAdmin):
    list_display = ('id', 'status', 'title', 'creation_date', 'author', 'post', 'parent')
    list_editable = ('status', 'author')
    list_filter = ('status', 'parent')
    search_fields = ('title', 'content', 'author', 'post')

admin.site.register(blog_models.Comment, CommentAdmin)
