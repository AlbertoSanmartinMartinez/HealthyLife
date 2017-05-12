# from django import forms
from django.forms import ModelForm
from models import SportSession
# from datetime import date


class SportSessionForm(ModelForm):
    class Meta:
        model = SportSession
        exclude = ("usuario", "date", "session_id")
