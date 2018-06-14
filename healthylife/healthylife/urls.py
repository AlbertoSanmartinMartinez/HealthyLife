#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from django.conf import settings
from healthylife import settings
from django.contrib import admin
from django.views.generic import DetailView, ListView, UpdateView
from healthylifeapp import views as general_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from shop import views as shp_views

admin.site.site_header = 'Barbastro Se Mueve'
admin.autodiscover()

urlpatterns = [

    # Admin URLS's
    url(r'^administracion/', include(admin.site.urls)),

    # API URLS's
    url(r'^api/$', general_views.api, name='api'),

    # Blog URLS's
    url(r'^blog/', include('blog.urls', namespace='blog')),

    # Search URLS's
    url(r'^resultado_busqueda/$', general_views.search, name='search'),

    # Shop URLS's
    url(r'^tienda/', include('shop.urls', namespace='shop')),

    # Pages URLS's
    url(r'^$', general_views.home, name='home'),
    url(r'^conocenos/$', general_views.know_us, name='know_us'),
    url(r'^conocenos/colaboradores/(?P<username>\w+)/$', general_views.know_us_collaborator, name='collaborator'),
    url(r'^conocenos/empresas/(?P<companyname>\w+)/$', general_views.know_us_company, name='company'),

    url(r'^trabaja_con_nosotros/', general_views.work_with_our, name='work_with_our'),
    url(r'^informacion_legal/', general_views.legal_information, name='legal_information'),
    url(r'^contacto/', general_views.contact, name='contact'),

    # Sport URLS's
    url(r'^deporte/', include('sportapp.urls', namespace='sportapp')),

    # Health URLS's
    url(r'^salud/$', general_views.health, name='health'),

    # Nutrition URLS's
    url(r'^nutricion/', include('nutritionapp.urls', namespace='nutritionapp')),

    # Statistics URLS's
    url(r'^estadisticas/$', general_views.statistics, name='statistics'),

    # Awards URLS's
    url(r'^premios/$', general_views.awards, name='awards'),

    # Editor de Texto HTML URL's
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # Registro URLS's
    # url(r'^mi_cuenta/$', include('django.contrib.auth.urls')),
    url(r'^mi_cuenta/registro/$', general_views.custom_registration, name='custom_register'),
    url(r'^mi_cuenta/registro/completado/$', general_views.registration_complete, name='custom_register_complete'),
    url(r'^mi_cuenta/registro/cancelado/$', general_views.registration_disallowed, name='registration_disallowed'),

    # Profile URLS's
    url(r'^mi_cuenta/(?P<username>\w+)/$', general_views.profile, name='profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/pedidos/$', general_views.ships, name='ships'),

    # Calendar URLS's
    url(r'^mi_cuenta/(?P<username>\w+)/calendario/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/$', general_views.calendar, name='calendar'),
    #url(r'^mi_cuenta/(?P<username>\w+)/calendario/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/(?<slug>\w)/$', views.event, name='detail_event'),
    url(r'^mi_cuenta/(?P<username>\w+)/calendario/eventos/nuevo/$', general_views.event, name='add_event'),

    url(r'^mi_cuenta/(?P<username>\w+)/deporte/$', general_views.sport_profile, name='sport_profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/nutricion/$', general_views.nutrition_profile, name='nutrition_profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/salud/$', general_views.health_profile, name='health_profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/premios/$', general_views.awards_profile, name='awards_profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/colaborador/$', general_views.collaborator_profile, name='collaborator_profile'),

    # Company URLS's
    #url(r'^empresas/(?P<company>\w+)/empresa/$', views.company, name='company'),

    # Collaborators URLS's
    #url(r'^colaboradores/(?P<username>\w+)/$', views.company, name='collaborators'),

    # Login URLS's
    url(r'^acceso/$', general_views.custom_login, name='custom_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    url(r'^mi_cuenta/password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^mi_cuenta/password_change_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^mi_cuenta/password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^mi_cuenta/password_reset_done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^mi_cuenta/password_confirm/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^mi_cuenta/password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
