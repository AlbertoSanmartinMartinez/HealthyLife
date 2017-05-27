from django import forms
# from models import OwnUser
# from django.forms import ModelForm


class RegisterForm(forms.Form):
    # USER_TYPE = (('Owner Shop'), ('Blogger'))
    # USER_BLOGGER = (('Yes'), ('No'))
    user_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    telephone = forms.IntegerField()
    email = forms.EmailField()
    # user_type = forms.ChoiceField(required=True, choices=USER_TYPE)
    # user_blogger = forms.ChoiceField(required=True, choices=USER_BLOGGER)
    password = forms.CharField(widget=forms.PasswordInput())
    # exclude = ('first_name', 'last_name')


class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    topic = forms.CharField(max_length=500)
