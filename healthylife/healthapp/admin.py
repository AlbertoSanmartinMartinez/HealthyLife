# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from healthapp import models as health_models
from guardian.admin import GuardedModelAdmin
from django.contrib import admin

# Admin Health Models
class IllnesAdmin(GuardedModelAdmin):
    model = health_models.Illnes

admin.site.register(health_models.Illnes, IllnesAdmin)
