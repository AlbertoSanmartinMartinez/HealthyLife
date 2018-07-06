# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from awards import models as award_models

# Register your models here.
class AwardAdmin(GuardedModelAdmin):
    list_display = ('id', 'title', 'description', 'award_type', 'amount', 'author')
    list_filter = ('title', 'description', 'award_type', 'amount', 'author')
    search_fields = ('title', 'description', 'award_type', 'amount', 'author')

    def get_queryset(self, request):
        queryset = super(AwardAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author_id=request.user.id)

admin.site.register(award_models.Award, AwardAdmin)
