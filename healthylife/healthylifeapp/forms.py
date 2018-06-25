#!/usr/local/bin/python
# coding: utf-8

from django import forms
from healthylifeapp import models as general_models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from datetimewidget.widgets import DateTimeWidget
# from django.contrib.admin import widgets

# Register Forms
class CustomRegisterForm(UserCreationForm):
    """
    Formulario para de registro para usuarios
    https://docs.djangoproject.com/en/2.0/ref/forms/fields/
    """
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre usuario', "size": 30 }))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder':'Correo electronico',"size": 30}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Contrasena', "size": 30 }))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirmar contrasena', "size": 30 }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Login Forms
class CustomAuthenticationForm(AuthenticationForm):
    """
    Formulario de acceso para usuarios
    https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.forms.AuthenticationForm
    """
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre usuario o correo electronico', "size": 30}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Contrasena', "size": 30 }))


class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Introduce tu correo electrónico', "size": 80}))

    class Meta:
        model = general_models.Subscriber
        exclude = []

# General Forms
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(label='Nombre')
    description = forms.CharField(label='Descripcion', required=False)
    phone = forms.CharField(label='Telefono', required=False)
    web = forms.CharField(label='Página web', required=False)
    company_image = forms.ImageField(required=False)

    class Meta:
        model = general_models.Company
        fields = ['company_name', 'description', 'phone', 'web', 'company_image']


class BankInformationForm(forms.ModelForm):
    bank_name = forms.CharField(label='Nombre', required=False)
    account = forms.CharField(label='Número de cuenta', required=False)
    month = forms.CharField(label='Mes de caducidad', required=False)
    year = forms.CharField(label='Año de caducidad', required=False)
    security_code = forms.CharField(label='Código de seguridad', required=False)

    class Meta:
        model = general_models.BankInformation
        fields = ['bank_name', 'account', 'month', 'year', 'security_code']


class AddressForm(forms.ModelForm):
    address_name = forms.CharField(label='Nombre')
    city = forms.CharField(label='Ciudad', required=False)
    postal_code = forms.CharField(label='Código postal', required=False)
    street = forms.CharField(label='Calle', required=False)
    number = forms.CharField(label='Número', required=False)
    floor = forms.CharField(label='Piso', required=False)
    door = forms.CharField(label='Puerta', required=False)

    class Meta:
        model = general_models.Address
        fields = ['address_name', 'city', 'postal_code', 'street', 'number', 'floor', 'door']


class ContactForm(forms.Form):
    """Formulario de contacto"""
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=500)


class CustomRegisterColaboratorForm(UserCreationForm):
    """
    Formulario para de registro de colaboradores
    """
    username = forms.CharField(label='Nombre de usuario', required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password2 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    blog_colaborator = forms.BooleanField(label='Quieres colaborar en el blog', required=False,)
    shop_colaborator = forms.BooleanField(label='Quieres colaborar en la tienda', required=False,)
    award_colaborator = forms.BooleanField(label='Quieres colaborar en el programa de premios y recompensas', required=False,)
    sport_colaborator = forms.BooleanField(label='Quieres colaborar en la seccion de deporte', required=False,)
    nutrition_colaborator = forms.BooleanField(label='Quieres colaborar en la sección de nutricion', required=False,)
    health_colaborator = forms.BooleanField(label='Quieres colaborar en la seccion de salud', required=False,)

    class Meta:
        model = User
        fields = ['username', 'email']


# Health forms

# Awards forms

# Profile forms
class CollaboratorProfileForm(forms.ModelForm):
    position = forms.CharField(label='Cargo', required=False, widget=forms.TextInput(attrs={'placeholder':'Puesto actual'}))
    company = forms.CharField(label='Empresa', required=False, widget=forms.TextInput(attrs={'placeholder':'Empresa actual'}))
    education = forms.CharField(label='Formacion', required=False, widget=forms.TextInput(attrs={'placeholder':'Formacion'}))
    extract = forms.CharField(label='Resumen', required=False, widget=forms.TextInput(attrs={'placeholder':'Resumen sobre ti para que los demás te conozcan'}))
    collaborator_image = forms.ImageField(required=False)

    class Meta:
        model = general_models.CollaboratorProfile
        fields = ['position', 'company', 'education', 'extract', 'collaborator_image']


class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(label='Bio', required=False, widget=forms.TextInput(attrs={'placeholder':'Bio de tu perfil'}))
    phone = forms.CharField(label='Teléfono', required=False, widget=forms.TextInput(attrs={'placeholder':'Teléfono'}))
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = general_models.UserProfile
        fields = ['bio', 'phone', 'profile_image']


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    #first_name = forms.CharField(label='Nombre')
    #last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class SearchForm(forms.Form):
    """
    Formulario de busqueda en el blog
    """
    word = forms.CharField(label='search', widget=forms.TextInput(attrs={'placeholder':'Escribe aquí'}))


# Calendar forms
class EventForm(forms.ModelForm):
    #date = forms.DateTimeField(input_formats=('%y/%m/%d'), label='Fecha:')
    #time = forms.DateTimeField(input_formats=('%H:%M'), label='Fecha:')

    class Meta:
        model = general_models.Event
        fields = ['title', 'description', 'privacity'] #, 'date', 'time']
