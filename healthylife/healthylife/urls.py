from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from healthylifeapp.models import SportSession
from django.views.generic import DetailView, ListView, UpdateView
from healthylifeapp import views
from healthylifeapp.views import SportSessionCreate, SportSessionDetail
from django.contrib.auth import views as auth_views

urlpatterns = [

    # General URLS's
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.inicio, name='inicio'),

    # Blog URLS's
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<slug>\w+)/$', views.detail_post, name='detail_post'),
    url(r'^blog/categorias/(?P<slug>\w+)/$', views.blog_category_posts, name='blog_category_posts'),
    url(r'^blog/autores/(?P<username>\w+)/$', views.blog_author_posts, name='blog_author_posts'),
    url(r'^resultado_busqueda/$', views.search, name='search'),

    # Shop URLS's
    url(r'^shop/$', views.shop, name='shop'),

    # Pages URLS's
    url(r'^conocenos/$', views.know_us, name='know_us'),
    url(r'^trabaja_con_nosotros/', views.work_with_our, name='work_with_our'),
    url(r'^informacion_legal/', views.legal_information, name='legal_information'),
    url(r'^contacto/', views.contact, name='contact'),

    # Sport URLS's
    url(r'^deporte/$', views.sport, name='sport'),
    url(r'^sport/sport_session/create/$', SportSessionCreate.as_view(), \
        name='sport_session_create'),
    url(r'^sport_session/(?P<pk>\d+)/$', SportSessionDetail.as_view(), \
        name='sport_session_detail'),
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

    url(r'^tinymce/', include('tinymce.urls')),

    # Media URLS's
    # url(r'^media/'),

    # Registro URLS's
    url(r'^mi_cuenta/', include('django.contrib.auth.urls')),
    url(r'^mi_cuenta/', include('registration.backends.hmac.urls')),

    url(r'^mi_cuenta/registro/$', views.RegistrationView.as_view(), name='registration_register'),
    url(r'^mi_cuenta/registro/completado/$', views.registration_complete, name='registration_complete'),
    url(r'^mi_cuenta/registro/cancelado/$', views.registration_disallowed, name='registration_disallowed'),

    url(r'^mi_cuenta/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^mi_cuenta/(?P<username>\w+)/pedidos/$', views.ships, name='ships'),
    url(r'^mi_cuenta/(?P<username>\w+)/calendario/$', views.calendar, name='calendar'),

    url(r'^administracion/(?P<username>\w+)/', views.admin, name='admin'),

    url(r'^mi_cuenta/login/$', auth_views.login, name='login'),
    url(r'^mi_cuenta/logout/$', auth_views.logout, name='logout'),
    # url(r'^acceso/$', views.access, name='access'),
]

"""
url(r'^mi_cuenta/activate/(?P<activation_key>\w+)/$', views.registration_activate, name='registration_activate'),
url(r'^mi_cuenta/complete/$', views.registration_activation_complete, name='registration_activation_complete'),
url(r'^resend/$', views.registration_resend_activation, name='registration_resend_activation'),

<li><a href="{% url 'password_change' %}">password_change</a></li>
<li><a href="{% url 'password_change_done' %}">password_change_done</a></li>
<li><a href="{% url 'password_reset' %}">password_reset</a></li>
<li><a href="{% url 'password_reset_done' %}">password_reset_done</a></li>
<li><a href="{% url 'password_reset_confirm' %}">password_reset_confirm</a></li>
<li><a href="{% url 'password_reset_complete' %}">password_reset_complete</a></li>
"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URL's
urlpatterns += [

]
