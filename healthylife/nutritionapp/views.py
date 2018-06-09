#!/usr/local/bin/python
# coding: utf-8

from __future__ import unicode_literals
from nutritionapp import forms as nutrition_forms
from django.shortcuts import render
from healthylife import settings
from healthylifeapp import views as general_views

import requests
# import urllib2
import json

# Nutrition views
def nutrition(request):
    """
    Vista principal para la seccion de nutricion
    """
    food_information = None

    return render(request, 'nutrition.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'search_food_form': getSearchFoodForm(),
        'food_information': food_information,
    })


def search_food(request):
    food_information = None
    if request.method == 'POST':
        food_form = nutrition_forms.SearchFoodForm(data=request.POST)
        if food_form.is_valid():
            food = food_form.cleaned_data['name']
            # tratar el idioma de la consulta
            food_information = getNutritionixApiInformation(food)
    else:
        food_form = nutrition_forms.SearchFoodForm()

    return render(request, 'nutrition.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'search_food_form': getSearchFoodForm(),
        'food_information': food_information,
    })


# Common Functions
def getSearchFoodForm():
    """
    Funcion que devuelve el formulario de la consulta a la api de alimentacion
    """
    return nutrition_forms.SearchFoodForm()


def getNutritionixApiInformation(food):
    """
    Funcion que realiza la consulta http get a la api
    Ejemplo consultas manuales https://www.nutritionix.com/natural-demo
    Ejemplo respuesta https://gist.github.com/mattsilv/6d19997bbdd02cf5337e9d4806b4f464
    """
    url = "https://trackapi.nutritionix.com/v2/search/instant?"
    body = {
      'query': food,
    }
    headers = {
        'x-app-id': settings.X_APP_ID,
        'x-app-key': settings.X_APP_KEY,
        #'x-remote-user-id': "7a43c5ba-50e7-44fb-b2b4-bbd1b7d22632",
    }
    response = requests.request("GET", url, params=body, headers=headers)

    print(response.json()['common'])
