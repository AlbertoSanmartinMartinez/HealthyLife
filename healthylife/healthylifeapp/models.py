from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class OwnUser(models.Model):
    # USER_TYPE = (('Owner Shop'), ('Blogger'))
    # model = User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_type = models.CharField(max_length=100)
    # user_type = models.ChoiceField(required=True, choices=USER_TYPE)


class TrainerUser(models.Model):
    user = models.OneToOneField(OwnUser, on_delete=models.CASCADE)


class ChefUser(models.Model):
    user = models.OneToOneField(OwnUser, on_delete=models.CASCADE)


class ShopUser(models.Model):
    user = models.OneToOneField(OwnUser, on_delete=models.CASCADE)


class BlogerUser(models.Model):
    user = models.OneToOneField(OwnUser, on_delete=models.CASCADE)


# sport models
class SportType(models.Model):
    sport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # default=''

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


class SportSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sport_type = models.ForeignKey(SportType)
    date = models.DateField()
    usuario = models.ForeignKey(User)
    # duration
    # calories = models.IntegerField()

    def __unicode__(self):  # python 2
        return self.name

    def __str__(self):  # python 3
        return self.name


# nutrition models
class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(date.today)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def addIngredient(self):
        pass


class Measure(models.Model):
    measure_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    nutrient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
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


# awards models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Award(models.Model):
    award_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# health models
class Illnes(models.Model):
    pass


class Simpton(models.Model):
    pass


# statistics models
class GeneralStatistics(models.Model):
    pass
