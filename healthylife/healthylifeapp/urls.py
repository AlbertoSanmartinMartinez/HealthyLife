from django.conf.urls import url  # include
from healthylifeapp.views import inicio

urlpatterns = [
    url(r'^$', inicio, name='inicio'),
    url(r'^register/', register, name='register'),
    url(r'^login/', ownlogin, name='login'),
    url(r'^contact/', contact, name='contact'),
    url(r'^sport/$', sport, name='sport'),
    url(r'^health/$', views.health, name='health'),
    url(r'^nutrition/$', views.nutrition, name='nutrition'),
    url(r'^statistics/$', view.statistics, name='statistics'),
    url(r'^awards/$', views.awards, name='awards'),
]

# API URL's
urlpatterns += [

]
