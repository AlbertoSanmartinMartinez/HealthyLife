from django import forms
# from models import OwnUser
from django.forms import ModelForm
from .models import SportSession, SportType, User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    #email = forms.EmailField()
    #password = forms.CharField(widget=forms.PasswordInput())
    #password2 = forms.CharField(widget=forms.PasswordInput())


class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    topic = forms.CharField(max_length=500)


class WorkWithOurForm(forms.Form):
    TYPE_WORK = (('Owner Shop'), ('Blogger'))
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    telephone = forms.IntegerField()
    work_type = forms.ChoiceField(required=True, choices=TYPE_WORK)


# Sport forms
class SportSessionForm(ModelForm):
    class Meta:
        model = SportSession
        fields = ['name', 'sport_type', 'date', 'duration', 'calories']


class SportTypeForm(ModelForm):
    class Meta:
        model = SportType
        fields = []

# Nutrition forms

# Health forms

# Awards forms

# Blog forms
"""
class PostForm(ModelForm):
    class Meta;
        model = Post
"""

# Profile forms
class UserInformationForm(ModelForm):
    class Meta:
        model = User
        fields = []
