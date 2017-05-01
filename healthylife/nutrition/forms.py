# from django import forms
from django.forms import ModelForm
# from datetime import date
from models import Food, Ingredient


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ()


class FoodForm(ModelForm):
    class Meta:
        model = Food
        exclude = ()
