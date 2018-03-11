#!/usr/local/bin/python
# coding: utf-8

from django import forms
from django import forms
from healthylifeapp import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Register Forms
class CustomRegisterForm(UserCreationForm):
    """
    Formulario para de registro para usuarios
    https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    """
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password2 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']


# Login Forms
class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulario de acceso para usuarios
    https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
    """
    username = forms.CharField(label='Nombre o email de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())


# General Forms
class CompanyForm(forms.Form):
    # name = forms.CharField
    # address =
    # phone =
    # web =
    # address =

    class Meta:
        model = models.Company
        fields = ['name']


class BankInformationForm(forms.ModelForm):

    class Meta:
        model = models.BankInformation
        fields = []


class AddressForm(forms.Form):

    class Meta:
        model = models.Address
        field = ["name"]


class ContactForm(forms.Form):
    """Formulario de contacto"""
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=500)


class WorkWithOurForm(forms.Form):
    """Formulario de registro para colaboradores"""
    # blog = forms.BooleanField(required=False)
    shop = forms.BooleanField(required=False)
    blog = forms.BooleanField(label='Colaborar en el blog', required=False)


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
    """
    Formulario de busqueda en el blog
    """
    word = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder':'Escribe aquí'}))


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = []


# Profile forms
class UserInformationForm(forms.ModelForm):
    
    class Meta:
        model = models.User
        fields = []
