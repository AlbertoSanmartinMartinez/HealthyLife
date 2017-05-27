from django.shortcuts import render, render_to_response
from .forms import RegisterForm, LogInForm, ContactForm
# from django.contrib.auth import User
from .models import OwnUser
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login


# Create your views here.
def inicio(request):
    return render(request, "inicio.html", {})


# https://docs.djangoproject.com/en/dev/topics/auth/
"""
def register(request):
    form = RegisterForm
    context = {
        'register_form': form
    }
    return render(request, 'register.html', context)
"""


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # obj = form.save(commit=False)
            form_data = form.cleaned_data
            obj = OwnUser()
            obj.user_name = form_data.get("name")
            obj.age = form_data.get("age")
            obj.email = form_data.get("email")
            obj.telephone = form_data.get("telephone")
            obj.password = form_data.get("password")
            obj.save()
            return HttpResponseRedirect('.')
    else:
        form = RegisterForm()
    context1 = {
        'register_form': form
    }
    context2 = RequestContext(request)
    return render('/register.html', context1, context2)


def ownlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
    else:
        return render(request, 'home.html', {})


"""
def login(request):
    form = LogInForm(request.POST or None)
    context = {
        "login_form": form,
    }
    return render(request, "login.html", context)
"""


def logout(request):
    return render(request, "login.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        print form_data.get("name")
    context = {
        "contact_form": form,
    }
    return render(request, "contact.html", context)
