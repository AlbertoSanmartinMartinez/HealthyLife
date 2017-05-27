from django import forms
# from models import OwnUser
from django.forms import ModelForm
from healthylifeapp.models import SportSession, SportType


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
