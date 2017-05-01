from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    telephone = forms.IntegerField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LogInForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class SportSessionForm(forms.Form):
    # session_id = models.AutoField(primary_key=True)
    name = forms.CharField(max_length=100)
    # sport_type = models.ForeignKey(SportType)
    # date = models.DateField(date.today)
    # usuario = models.ForeignKey(User)
    # duration
    # calories
    # time
