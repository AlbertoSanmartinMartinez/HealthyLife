#!/usr/local/bin/python
# coding: utf-8

from django.conf.urls import include, url
from healthylifeapp import views
from rest_framework.urlpatterns import format_suffix_patterns


# API URL's
urlpatterns = [

    # Blog URL's
    url(r'^posts/$', views.APIPostList.as_view(), name='post-list'),
    url(r'^post(?P<pk>\d+)/$', views.APIPostDetail.as_view(), name='post-detail'),

    url(r'^categories/$', views.APICategoryList.as_view(), name='category-list'),
    url(r'^category(?P<pk>\d+)/$', views.APICategoryDetail.as_view(), name='category-detail'),

    url(r'^comments/$', views.APICommentList.as_view(), name='comment-list'),
    url(r'^comment(?P<pk>\d+)/$', views.APICommentDetail.as_view(), name='comment-detail'),

    # url(r'^users/$', views.APIUserList.as_view(), name='user-list'),
    # url(r'^user(?P<pk>\w+)/$', views.APIUserDetail.as_view(), name='user-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
