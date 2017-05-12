from django import forms
# from django.forms import ModelForm


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    telephone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    topic = forms.CharField(max_length=500)
