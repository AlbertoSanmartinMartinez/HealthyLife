#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from django.conf import settings
from healthylife import settings
from blog import views as blog_views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # Blog URLS's
    url(r'^posts/$', blog_views.list_posts, name='list_post'),
    # hacer generica
    #url(r'^blog/subscripcion/$', blog_views.subscribe, name='subscribe'),

    url(r'^posts/(?P<post_slug>\w+)/$', blog_views.detail_post, name='detail_post'),
    # url(r'^blog/(?P<post_slug>\w+)/(?P<comment_parent_id>\w+)/comentado/$', views.comment, name='comment'),
    url(r'^categorias/(?P<category>\w+)/$', blog_views.category_posts, name='category_posts'),
    url(r'^autores/(?P<username>\w+)/$', blog_views.author_posts, name='author_posts'),
    #url(r'^blog/etiquetas/(?P<tag>\w+)/$', views.blog_tag_posts, name='blog_tag_posts'),

    url(r'^commentario/$', blog_views.add_comment, name='add_comment'),

    # API URL's
    #url(r'^posts/$', blog_views.APIPostList.as_view(), name='post-list'),
    #url(r'^posts/(?P<pk>\d+)/$', blog_views.APIPostDetail.as_view(), name='post-detail'),

    #url(r'^categories/$', blog_views.APICategoryList.as_view(), name='category-list'),
    #url(r'^categories/(?P<pk>\d+)/$', blog_views.APICategoryDetail.as_view(), name='category-detail'),

    #url(r'^comments/$', blog_views.APICommentList.as_view(), name='comment-list'),
    #url(r'^comments/(?P<pk>\d+)/$', blog_views.APICommentDetail.as_view(), name='comment-detail'),

    #url(r'^users/$', blog_views.APIUserList.as_view(), name='user-list'),
    #url(r'^users/(?P<pk>\d+)/$', blog_views.APIUserDetail.as_view(), name='user-detail'),

    #url(r'^users/login$', blog_views.userLoginAPI, name='user-login-api'),
    #url(r'^users/register/$', blog_views.userRegistrationAPI, name='user-register-api'),
]

# Format suffixes
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
