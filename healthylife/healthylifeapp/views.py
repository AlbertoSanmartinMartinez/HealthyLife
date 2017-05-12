from django.shortcuts import render
from .forms import RegisterForm, LogInForm, ContactForm


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
