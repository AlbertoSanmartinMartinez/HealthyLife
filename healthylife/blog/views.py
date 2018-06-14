# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import permissions, generics
from blog import models as blog_models
from blog import serializer as blog_serializer

# Blog Views
def list_posts(request):
    posts = blog_models.Post.objects.filter(status=1).order_by("-creation_date")

    return render(request, "blog.html", {
        "posts": posts,
        "categories": obtenerCategorias(request),
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })


def detail_post(request, post_slug):
    post = blog_models.Post.objects.get(slug=post_slug)
    comments = blog_models.Comment.objects.filter(post=post.id, status=1, parent_id__isnull=True).order_by("-creation_date")
    images = blog_models.Image.objects.filter(album=post.album)

    return render(request, "post.html", {
        "post": post,
        "images": images,
        "categories": obtenerCategorias(request),
        "comments":comments,
        "comment_form": getCommentForm(),
        "answer_form": getCommentForm(),
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'comment_parent_id': 24,
    })


def category_posts(request, category):
    category = blog_models.Category.objects.get(slug=category)
    posts = blog_models.Post.objects.filter(status=1, category=category.id)

    return render(request, 'blog.html', {
        "posts":posts,
        "categories": obtenerCategorias(request),
        "search_form":getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })


def author_posts(request, username):
    author = User.objects.get(username=username)
    posts = blog_models.Post.objects.filter(status=1, author=author.id)
    categories = blog_models.Category.objects.order_by("name")

    return render(request, 'blog.html', {
        "categories":categories,
        "posts":posts,
        "categories": obtenerCategorias(request),
        "search_form":getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })


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
