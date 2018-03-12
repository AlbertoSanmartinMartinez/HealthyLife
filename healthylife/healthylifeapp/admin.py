from django.contrib import admin
from healthylifeapp import models

# Register your models here.
admin.site.register(models.SportType)
admin.site.register(models.SportSession)
admin.site.register(models.Food)
admin.site.register(models.Measure)
admin.site.register(models.Nutrient)
admin.site.register(models.Ingredient)
admin.site.register(models.Company)

class AwardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'award_type', 'amount', 'company', 'author')
    list_filter = ('name', 'description', 'award_type', 'amount', 'company', 'author')
    search_fields = ('name', 'description', 'award_type', 'amount', 'company', 'author')

admin.site.register(models.Award, AwardAdmin)

admin.site.register(models.GeneralStatistics)
admin.site.register(models.SpecificStatistics)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('name', 'parent')
    search_fields = ('name', 'parent')

admin.site.register(models.Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'slug', 'category', 'author')
    list_filter = ('status', 'title', 'slug', 'category', 'author')
    search_fields = ('status', 'title', 'slug', 'category', 'author')

admin.site.register(models.Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'author', 'post')
    list_filter = ('status', 'title', 'author', 'post')
    search_fields = ('status', 'title', 'author', 'post')

admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.Address)
admin.site.register(models.BankInformation)
admin.site.register(models.Product)
