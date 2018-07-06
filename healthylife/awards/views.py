# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from healthylifeapp import views as general_views

# Award views
def awards(request):
    return render(request, 'awards.html', {
        'subscribe_form': general_views.getSubscribeForm(),
    })


def awards_profile(request, username):
    return render(request, 'awards_profile.html', {
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
    })
