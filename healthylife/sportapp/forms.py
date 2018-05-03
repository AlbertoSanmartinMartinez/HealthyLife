#!/usr/local/bin/python
# coding: utf-8

from django import forms
from sportapp import models as sport_models

# Sport forms
class SportSessionForm(forms.ModelForm):
    class Meta:
        model = sport_models.SportSession
        fields = ['name', 'sport_type', 'date', 'duration', 'calories']


class SportTypeForm(forms.ModelForm):
    class Meta:
        model = sport_models.SportType
        fields = []
