#!/usr/local/bin/python
# coding: utf-8

from __future__ import unicode_literals
from sportapp import forms as sport_forms
from django.shortcuts import render
from healthylifeapp import views as general_views

# Sport views
def sport(request):
    print("llega a la funcion")
    return render(request, 'sport.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
    })
