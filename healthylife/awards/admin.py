# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from awards import models as award_models
from django.contrib.contenttypes.models import ContentType
from shop import models as shop_models
from django.forms.models import BaseInlineFormSet

# Register your models here.
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'title', 'award_type', 'amount', 'author')
    list_filter = ('status', 'award_type')
    search_fields = ('title', 'description')
    readonly_fields = ('slug', 'author', 'album', 'updated_date')
    # inlines = [ProductsInLine,]

    def get_queryset(self, request):
        queryset = super(AwardAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

    def save_model(self, request, obj, form, change):
        """
        Save the user that create the aeard as author
        """
        if not obj.author:
            obj.author = request.user
        obj.save()

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            kwargs['queryset'] = shop_models.Product.objects.all()
        else:
            kwargs['queryset'] = shop_models.Product.objects.filter(author_id=request.user.id)

        return super(AwardAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(award_models.Award, AwardAdmin)
