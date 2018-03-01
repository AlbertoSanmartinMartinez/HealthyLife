from django import forms
from django import forms
from healthylifeapp import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        email = forms.EmailField
        usernmae = forms.CharField
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
    TYPE_WORK = (('Owner Shop'), ('Blogger'))
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    telephone = forms.IntegerField()
    work_type = forms.ChoiceField(required=True, choices=TYPE_WORK)


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
"""
class PostForm(ModelForm):
    class Meta;
        model = Post
"""

# Profile forms
class UserInformationForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = []
