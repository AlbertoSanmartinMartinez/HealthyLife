#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import url
from awards import views as awards_views

urlpatterns = [

    # Awards URLS's
    url(r'^$', awards_views.awards, name='awards'),
    url(r'^$', awards_views.awards, name='search_awards'),

    url(r'^(?P<username>\w+)/conseguidos/$', awards_views.awards_profile, name='awards_profile'),
    
    url(r'^(?P<award_slug>.*)/$', awards_views.award_detail, name='award_detail'),

    # Coupon Urls
    url(r'^cupon/$', awards_views.coupon, name='coupon'),
]
