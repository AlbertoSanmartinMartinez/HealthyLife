from django.shortcuts import render
from .forms import RegisterForm, LogInForm


# Create your views here.
def inicio(request):
    return render(request, "inicio.html", {})


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data
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
