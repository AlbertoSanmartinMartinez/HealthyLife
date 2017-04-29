from django.contrib import admin
from .models import Food, Ingredient, Measure, Nutrient

# Register your models here.
admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(Nutrient)
admin.site.register(Measure)
