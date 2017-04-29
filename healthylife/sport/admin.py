from django.contrib import admin
from .models import SportType, SportSession


# Register your models here.
class AdminSportSession(admin.ModelAdmin):
    list_display = ["session_id", "name", "sport_type", "date", "usuario"]
    list_filter = ["usuario", "sport_type"]
    # list_editable = ["sport_type"]
    search_fields = ["date", "name"]

    class Meta:
        model = SportSession


admin.site.register(SportType)
admin.site.register(SportSession, AdminSportSession)
