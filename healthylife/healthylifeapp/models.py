from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.forms import ModelForm

# General models
class OwnUser(models.Model):
    pass

# Sport models
class SportType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


class SportSession(models.Model):
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType)
    date = models.DateField(datetime.today)
    usuario = models.ForeignKey(User)
    duration = models.TimeField()
    calories = models.IntegerField()

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


# Nutrition models
class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(datetime.today)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def addIngredient(self):
        pass


class Measure(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    fats = models.ForeignKey(Nutrient, default='')
    # carbohydrates = models.ForeignKey(Nutrient)
    # proteins = models.ForeignKey(Nutrient)
    # fiber = models.ForeignKey(Nutrient)
    # sodium = models.ForeignKey(Nutrient)
    # calories = models.ForeignKey(Nutrient)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# Awards models
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Award(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# Health models
class Simpton(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Illnes(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    simpton = models.ManyToManyField(Simpton)


# Statistics models
class GeneralStatistics(models.Model):
    pass


class SpecificStatistics(models.Model):
    pass

# Blog models
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=3)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
    # header_image = models.ImageField(upload_to="photos")
    # autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    def publishPost(self):
        pass

class Comment(models.Model):
    Status = ((1, "Publicado"), (2, "Borrador"), (3, "Eliminado"))
    status = models.IntegerField(choices=Status, default=3)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# Shop models
class Product(models.Model):
    pass
