from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    telephone = forms.IntegerField()
