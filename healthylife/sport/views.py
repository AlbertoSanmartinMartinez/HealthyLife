from django.shortcuts import render
from .forms import RegisterForm, LogInForm


# Create your views here.
def inicio(request):
    return render(request, "inicio.html", {})


def register(request):
    form = RegisterForm()
    context = {
        "register_form": form,
    }
    return render(request, "register.html", context)


def login(request):
    form = LogInForm()
    context = {
        "login_form": form,
    }
    return render(request, "login.html", context)
