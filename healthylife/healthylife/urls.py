"""healthylife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from sport import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^sport/', views.sport, name='sport'),
    url(r'^health/', views.health, name='health'),
    url(r'^nutrition/', views.nutrition, name='nutrition'),
    url(r'^statistics/', views.statistics, name='statistics'),
    url(r'^awards/', views.awards, name='awards'),
    # url(r'^blog/', views.blog, name='blog')
]
