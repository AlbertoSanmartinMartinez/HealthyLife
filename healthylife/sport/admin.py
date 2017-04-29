from django.contrib import admin
from .models import SportType, SportSession


# Register your models here.
class AdminSportSession(admin.ModelAdmin):
    list_display = ["session_id", "name", "sport_type", "date", "usuario"]

    class Meta:
        model = SportSession


admin.site.register(SportType)
admin.site.register(SportSession, AdminSportSession)
