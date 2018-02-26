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

    url(r'^blog/$', blog, name='blog'),
    url(r'^blog/(?P<slug>\w+)/$', detail_post, name='detail_post'),
    # url(r'^blog/admin/$', admin_blog, name='admin_blog'),

    url(r'^conocenos/$', know_us, name='know_us'),

    url(r'^shop/$', shop, name='shop'),

    url(r'^registro/', register, name='register'),
    url(r'^login/', login, name='login'),

    url(r'^trabaja_con_nosotros/', work_with_our, name='work_with_our'),
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

    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^media/'),

    url(r'^mi_cuenta/', include('registration.backends.default.urls')),
]

"""
^mi_cuenta/ ^activate/complete/$ [name='registration_activation_complete']
^mi_cuenta/ ^activate/resend/$ [name='registration_resend_activation']
^mi_cuenta/ ^activate/(?P<activation_key>\w+)/$ [name='registration_activate']
^mi_cuenta/ ^register/complete/$ [name='registration_complete']
^mi_cuenta/ ^register/closed/$ [name='registration_disallowed']
^mi_cuenta/ ^register/$ [name='registration_register']
^mi_cuenta/ ^login/$ [name='auth_login']
^mi_cuenta/ ^logout/$ [name='auth_logout']
^mi_cuenta/ ^password/change/$ [name='auth_password_change']
^mi_cuenta/ ^password/change/done/$ [name='auth_password_change_done']
^mi_cuenta/ ^password/reset/$ [name='auth_password_reset']
^mi_cuenta/ ^password/reset/complete/$ [name='auth_password_reset_complete']
^mi_cuenta/ ^password/reset/done/$ [name='auth_password_reset_done']
^mi_cuenta/ ^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$ [name='auth_password_reset_confirm']
"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URL's
urlpatterns += [

]
