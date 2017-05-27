from django.contrib import admin
from healthylifeapp.models import SportType, SportSession, Food, Measure, \
    Nutrient, Ingredient, Company, Award, Simpton, Illnes, GeneralStatistics, \
    SpecificStatistics

# Register your models here.
admin.site.register(SportType)
admin.site.register(SportSession)
admin.site.register(Food)
admin.site.register(Measure)
admin.site.register(Nutrient)
admin.site.register(Ingredient)
admin.site.register(Company)
admin.site.register(Award)
admin.site.register(Simpton)
admin.site.register(Illnes)
admin.site.register(GeneralStatistics)
admin.site.register(SpecificStatistics)
