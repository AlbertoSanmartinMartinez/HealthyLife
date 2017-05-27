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
from healthylifeapp.views import inicio, contact, sport, health, awards, \
    statistics, nutrition, work_with_our, legal_information, \
    SportSessionCreate, SportSessionDetail
from healthylifeapp.models import SportSession
from django.views.generic import DetailView, ListView, UpdateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio, name='inicio'),
    # url(r'^blog/$', views.blog, name='blog'),
    # url(r'^shop/$', views.shop, name='shop')
    # url(r'^register/', register, name='register'),
    # url(r'^login/', , name='login'),
    url(r'^work_with_our/', work_with_our, name='work_with_our'),
    url(r'^legal_information/', legal_information, name='legal_information'),
    url(r'^contact/', contact, name='contact'),

    # url general para sport
    url(r'^sport/$', sport, name='sport'),
    # url para crear sesiones de deporte
    url(r'^sport/sport_session/create/$', SportSessionCreate.as_view(), \
        name='sport_session_create'),
    # url para ver detalle sesion de deporte
    url(r'^sport_session/(?P<pk>\d+)/$', SportSessionDetail.as_view(), \
        name='sport_session_detail'),
    # url para ver sesiones de deporte
    url(r'^sport/sport_session/$',
        ListView.as_view(
            queryset=SportSession.objects.all,
            context_object_name='sport_session_list',
            template_name='sport_session_list.html'),
        name='sport_session_list'),

    url(r'^health/$', health, name='health'),
    url(r'^nutrition/$', nutrition, name='nutrition'),
    url(r'^statistics/$', statistics, name='statistics'),
    url(r'^awards/$', awards, name='awards'),
]

# API URL's
urlpatterns += [

]
