#!/usr/local/bin/python
# coding: utf-8

from django import forms
from awards import models as award_models

# Award forms
class AwardFilter(forms.ModelForm):
    
    class Meta:
        model = award_models.Award
        exclude = ['slug', 'status']
