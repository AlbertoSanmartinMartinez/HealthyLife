from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import SportSessionForm
from .models import SportSession
from datetime import date


# Create your views here.
def sport(request):
    if request.method == "POST":
        form = SportSessionForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data  # obtenemos la info del formulario
            obj = SportSession()
            obj.name = form_data.get("name")
            obj.sport_type = form_data.get("sport_type")
            obj.date = date.today()
            # si el usuario esta registrado:
            # else:
            obj.user = request.user.id
            obj.save()
    else:
        form = SportSessionForm()
    context = {
        "sport_session_form": form,
    }
    return render(request, "sport.html", context)
