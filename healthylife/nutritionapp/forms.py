#!/usr/local/bin/python
# coding: utf-8

from django import forms
from nutritionapp import models as nutrition_models

# Nutrition forms
class SearchFoodForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Descubre alimentación saludable'}))

    class Meta:
        model = nutrition_models.Food
        exclude = ['description', 'date']
