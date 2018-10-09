# coding: utf-8

from django.conf.urls import include, url

from api import views as api_views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [

    url(r'^$', api_views.api, name='api_home'),

    # API Blog URLS
    # url(r'^blog/posts/$', api_views.APIPostList.as_view(), name='post-list'),
    url(r'^blog/posts/$', api_views.api_list_posts, name='post-list'),
    # url(r'^api/posts/(?P<pk>\d+)/$', blog_views.APIPostDetail.as_view(), name='post-detail'),

    url(r'^blog/categories/$', api_views.APICategoryList.as_view(), name='category-list'),
    # url(r'^api/categories/(?P<pk>\d+)/$', blog_views.APICategoryDetail.as_view(), name='category-detail'),

    url(r'^blog/comments/$', api_views.APICommentList.as_view(), name='comment-list'),
    # url(r'^api/comments/(?P<pk>\d+)/$', blog_views.APICommentDetail.as_view(), name='comment-detail'),

    url(r'^blog/tags/$', api_views.APITagList.as_view(), name='tag-list'),
    # url(r'^api/tags/(?P<pk>\d+)/$', blog_views.APITagDetail.as_view(), name='tag-detail'),

    # url(r'^users/$', blog_views.APIUserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>\d+)/$', blog_views.APIUserDetail.as_view(), name='user-detail'),

    # url(r'^users/login$', blog_views.userLoginAPI, name='user-login-api'),
    # url(r'^users/register/$', blog_views.userRegistrationAPI, name='user-register-api'),


    # API Shop URLS
    url(r'^shop/products/$', api_views.api_list_products, name='product-list'),
    #url(r'^api/products/$', blog_views.APIProductList.as_view(), name='product-list'),

    url(r'^shop/categories/$', api_views.APICategoryList.as_view(), name='category-list'),
    #url(r'^api/products/$', blog_views.APIProductList.as_view(), name='category-detail'),

    url(r'^shop/reviews/$', api_views.APIReviewList.as_view(), name='review-list'),
    #url(r'^api/products/$', blog_views.APIProductList.as_view(), name='review-detail'),

    url(r'^shop/tags/$', api_views.APIReviewList.as_view(), name='tag-list'),
    #url(r'^api/products/$', blog_views.APIProductList.as_view(), name='tag-detail'),

    # API Blog URLS
    url(r'^awards/$', api_views.api_list_awards, name='awards-list'),

    # API General URLS
    url(r'^users/$', api_views.APIUserList.as_view(), name='user-list'),
    url(r'^users/register/$', api_views.custom_registration_api, name='user-register'),
    url(r'^api-token-auth/', obtain_jwt_token),

]











#
