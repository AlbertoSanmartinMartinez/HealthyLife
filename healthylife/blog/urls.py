#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from django.conf import settings
from healthylife import settings
from blog import views as blog_views

urlpatterns = [

    # Blog URLS's
    url(r'^posts/$', blog_views.list_posts, name='list_post'),
    url(r'^posts/$', blog_views.list_posts, name='blog_search'),

    # hacer generica
    #url(r'^blog/subscripcion/$', blog_views.subscribe, name='subscribe'),

    url(r'^posts/(?P<post_slug>.*)/$', blog_views.detail_post, name='detail_post'),
    url(r'^posts/(?P<post_slug>.*)/comentario', blog_views.add_comment, name='add_comment'),

    url(r'^comentarios/(?P<comment_id>\d+)/borrar/$', blog_views.delete_comment, name='delete_comment'),

    # url(r'^blog/(?P<post_slug>\w+)/(?P<comment_parent_id>\w+)/comentado/$', views.comment, name='comment'),
    url(r'^categorias/(?P<category>\w+)/$', blog_views.category_posts, name='category_posts'),
    url(r'^autores/(?P<username>\w+)/$', blog_views.author_posts, name='author_posts'),
    url(r'^etiquetas/(?P<tag_slug>\w+)/$', blog_views.tag_posts, name='tag_posts'),

]
