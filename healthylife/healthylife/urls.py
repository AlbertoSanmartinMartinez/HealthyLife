#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from healthylifeapp.models import SportSession
from django.views.generic import DetailView, ListView, UpdateView
from healthylifeapp import views
from healthylifeapp.views import SportSessionCreate, SportSessionDetail
from django.contrib.auth import views as auth_views

admin.site.site_header = 'Barbastro Se Mueve'

urlpatterns = [

    # Admin URLS's
    url(r'^admin/', include(admin.site.urls)),

    # API URLS's
    url(r'^api/', include('healthylifeapp.urls', namespace='api')),
    url(r'^api/$', views.api, name='api'),

    # Blog URLS's
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<post>\w+)/$', views.detail_post, name='detail_post'),
    url(r'^blog/categorias/(?P<category>\w+)/$', views.blog_category_posts, name='blog_category_posts'),
    url(r'^blog/autores/(?P<username>\w+)/$', views.blog_author_posts, name='blog_author_posts'),
    url(r'^resultado_busqueda/$', views.search, name='search'),

    # Shop URLS's
    url(r'^shop/$', views.shop, name='shop'),

    # Pages URLS's
    url(r'^$', views.inicio, name='home'),
    url(r'^conocenos/$', views.know_us, name='know_us'),
    url(r'^trabaja_con_nosotros/', views.work_with_our, name='work_with_our'),
    url(r'^informacion_legal/', views.legal_information, name='legal_information'),
    url(r'^contacto/', views.contact, name='contact'),

    # Sport URLS's
    url(r'^deporte/$', views.sport, name='sport'),
    url(r'^sport/sport_session/create/$', SportSessionCreate.as_view(), name='sport_session_create'),
    url(r'^sport_session/(?P<pk>\d+)/$', SportSessionDetail.as_view(), name='sport_session_detail'),
    url(r'^sport/sport_session/$',
        ListView.as_view(
            queryset=SportSession.objects.all,
            context_object_name='sport_session_list',
            template_name='sport_session_list.html'),
        name='sport_session_list'),

    # Health URLS's
    url(r'^salud/$', views.health, name='health'),

    # Nutrition URLS's
    url(r'^nutricion/$', views.nutrition, name='nutrition'),

    # Statistics URLS's
    url(r'^estadisticas/$', views.statistics, name='statistics'),

    # Awards URLS's
    url(r'^premios/$', views.awards, name='awards'),

    # Editor de Texto URLS's
    url(r'^tinymce/', include('tinymce.urls')),

    # Media URLS's
    # url(r'^media/'),

    # Registro URLS's
    url(r'^mi_cuenta/', include('django.contrib.auth.urls')),
    url(r'^mi_cuenta/registro/$', views.registration_register, name='registration_register'),
    url(r'^mi_cuenta/registro/completado/$', views.registration_complete, name='registration_complete'),
    url(r'^mi_cuenta/registro/cancelado/$', views.registration_disallowed, name='registration_disallowed'),

    # Profile URLS's
    url(r'^mi_cuenta/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/pedidos/$', views.ships, name='ships'),
    url(r'^mi_cuenta/(?P<username>\w+)/calendario/$', views.calendar, name='calendar'),

    # Login URLS's
    url(r'^mi_cuenta/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^mi_cuenta/logout/$', auth_views.LogoutView.as_view(), name='logout'),

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
