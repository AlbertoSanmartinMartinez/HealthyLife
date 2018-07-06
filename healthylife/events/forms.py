#!/usr/local/bin/python
# coding: utf-8

from django import forms
from events import models as event_models

# Calendar forms
class EventForm(forms.ModelForm):
    #date = forms.DateTimeField(input_formats=('%y/%m/%d'), label='Fecha:')
    #time = forms.DateTimeField(input_formats=('%H:%M'), label='Fecha:')

    class Meta:
        model = event_models.Event
        fields = ['title', 'description', 'privacity'] #, 'date', 'time']
