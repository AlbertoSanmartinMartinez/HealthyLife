from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from healthylifeapp.views import inicio, contact, sport, health, awards, \
    statistics, nutrition, work_with_our, legal_information, \
    SportSessionCreate, SportSessionDetail, blog, detail_post, know_us, \
    login, register, shop
from healthylifeapp.models import SportSession
from django.views.generic import DetailView, ListView, UpdateView

# General URLS's
urlpatterns = [
    # url(r'^', include('healthylifeapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio, name='inicio'),

    url(r'^blog/', blog, name='blog'),
    # url(r'^blog/(?P<idpost>[0-9]+)/$', 'detail_post', name="detail_post"),

    url(r'^conocenos/$', know_us, name='know_us'),

    url(r'^shop/$', shop, name='shop'),

    url(r'^registro/', register, name='register'),
    url(r'^login/', login, name='login'),

    url(r'^trabaja_con_nostros/', work_with_our, name='work_with_our'),
    url(r'^informacion_legal/', legal_information, name='legal_information'),
    url(r'^contacto/', contact, name='contact'),

    # url general para deporte
    url(r'^deporte/$', sport, name='sport'),
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

    url(r'^salud/$', health, name='health'),
    url(r'^nutricion/$', nutrition, name='nutrition'),

    url(r'^estadisticas/$', statistics, name='statistics'),
    url(r'^premios/$', awards, name='awards'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URL's
urlpatterns += [

]
