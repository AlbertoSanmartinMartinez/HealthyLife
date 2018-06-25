# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import permissions, generics
from blog import models as blog_models
from blog import serializer as blog_serializer
from blog import forms as blog_forms
from healthylifeapp import models as general_models
from healthylifeapp import views as general_views
from django.contrib.auth.models import User

# Blog Views
def list_posts(request):
    posts = blog_models.Post.objects.filter(status=1).order_by("-creation_date")

    return render(request, "blog.html", {
        "posts": posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
    })


def detail_post(request, post_slug):
    post = blog_models.Post.objects.get(slug=post_slug)
    comments = blog_models.Comment.objects.filter(post=post.id, status=1, parent_id__isnull=True).order_by("-creation_date")
    images = general_models.Image.objects.filter(album=post.album)

    return render(request, "post.html", {
        "post": post,
        "images": images,
        "categories": getBlogCategories(),
        "comments":comments,
        "comment_form": getCommentForm(request),
        "answer_form": getCommentForm(request),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'comment_parent_id': 24,
    })


def category_posts(request, category):
    category = blog_models.Category.objects.get(slug=category)
    posts = blog_models.Post.objects.filter(status=1, category=category.id)

    return render(request, 'blog.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
    })


def author_posts(request, username):
    author = User.objects.get(username=username)
    posts = blog_models.Post.objects.filter(status=1, author=author.id)
    categories = blog_models.Category.objects.order_by("name")

    return render(request, 'blog.html', {
        "categories":categories,
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
    })


def add_comment(request):#, post_slug, comment_parent_id=None):
    #post = blog_models.Post.get_object_or_404(slug=post_slug)
    comment_form = getCommentForm(request)
    print(request.GET['post'])

    if request.user.is_authenticated():
        user = request.user.id
    else:
        user = None

    if comment_parent_id:
        response = comment_parent_id
    else:
        response = None

    if comment_form.is_valid():
        data = comment_form.cleaned_data
        blog_models.Comment.objects.create(
            status=2,
            title=data['title'],
            content=data['content'],
            author=user,
            post=1,
            parent=response)

    return redirect('blog:shoppingcart_detail post_slug=post.slug')

# Common Functions
def getBlogCategories():
    return blog_models.Category.objects.filter(parent__isnull=True).order_by("name")


def getCommentForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            return blog_forms.CommentFormAuthenticated(request.POST)
        else:
            return blog_forms.CommentFormNotAuthenticated(request.POST)
    else:
        if request.user.is_authenticated():
            return blog_forms.CommentFormAuthenticated()
        else:
            return blog_forms.CommentFormNotAuthenticated()


# Blog Api Views
class APIPostList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'slug']
    model = blog_models.Post
    serializer_class = blog_serializer.PostSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.query_params
        return blog_models.Post.objects.filter(status=data['status'])


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = blog_serializer.PostSerializer
    model = blog_models.Post
    """
    def get_queryset(self, *args, **kwargs):
        status = self.request.query_params.get('status', None)
        if status:
            queryset = models.Post.objects.filter(status=status)
            return queryset
    """

class APICategoryList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Category.objects.all()
    serializer_class = blog_serializer.CategorySerializer


class APICategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Category.objects.all()
    serializer_class = blog_serializer.CategorySerializer

    def get_queryset(self):
        queryset = blog_models.Category.objects.all()
        queryset = queryset.filter(name=self.request.query_params.get('category_id'))


class APICommentList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = blog_models.Category
    serializer_class = blog_serializer.CommentSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.query_params
        return blog_models.Comment.objects.filter(post_id=data['post_id'])


class APICommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Comment.objects.all()
    serializer_class = blog_serializer.CommentSerializer
