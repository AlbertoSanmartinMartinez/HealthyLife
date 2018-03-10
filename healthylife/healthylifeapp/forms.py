#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django import forms
from healthylifeapp import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

"""
class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
"""

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=500)


class WorkWithOurForm(forms.Form):
    # blog = forms.BooleanField(required=False)
    shop = forms.BooleanField(required=False)
    blog = forms.BooleanField(label='Colaborar en el blog', required=False)
    # word = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder':'Escribe aquí'}))


# Sport forms
class SportSessionForm(forms.ModelForm):
    class Meta:
        model = models.SportSession
        fields = ['name', 'sport_type', 'date', 'duration', 'calories']


class SportTypeForm(forms.ModelForm):
    class Meta:
        model = models.SportType
        fields = []

# Nutrition forms

# Health forms

# Awards forms

# Blog forms
class SearchForm(forms.Form):
    word = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder':'Escribe aquí'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = []


class AuthorForm(forms.ModelForm):
    pass


# Profile forms
class UserInformationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = []


class BankInformationForm(forms.ModelForm):
    class Meta:
        model = models.BankInformation
        fields = []


class AddressInformationForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = []
