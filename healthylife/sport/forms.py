from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    telephone = forms.IntegerField()
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
