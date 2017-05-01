from django.shortcuts import render
from .forms import RegisterForm, LogInForm, ContactForm, SportSessionForm
# from .models import SportSession


# Create your views here.
def inicio(request):
    return render(request, "inicio.html", {})


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "register_form": form,
    }
    return render(request, "register.html", context)


def login(request):
    form = LogInForm(request.POST or None)
    context = {
        "login_form": form,
    }
    return render(request, "login.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        print form_data.get("name")
    context = {
        "contact_form": form,
    }
    return render(request, "contact.html", context)


def sport(request):
    form = SportSessionForm()
    context = {
        "sport_session_form": form,
    }
    return render(request, "sport.html", context)


def health(request):
    return render(request, "health.html", {})


def nutrition(request):
    return render(request, "nutrition.html", {})


def statistics(request):
    return render(request, "statistics.html", {})


def awards(request):
    return render(request, "awards.html", {})
