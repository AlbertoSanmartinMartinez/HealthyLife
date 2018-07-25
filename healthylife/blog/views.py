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
from django.core.paginator import Paginator, PageNotAnInteger
from shop import views as shop_views

# Blog Views
def list_posts(request, blog_category_slug=None):

    category = None
    posts = blog_models.Post.objects.filter(status=1)
    blog_filter_form = None

    if blog_category_slug:
        category = get_object_or_404(blog_models.Category, slug=blog_category_slug)
        post = posts.filter(category=category)

    if request.method == 'POST':
        blog_filter_form = blog_forms.PostFilter(request.POST)
        if blog_filter_form.is_valid():
            data = blog_filter_form.cleaned_data
            posts = posts.filter(title__icontains=data['title'],
                description__icontains=data['title'],
                content__icontains=data['title'])
            if data['category'] is not None:
                posts = posts.filter(category_id=data['category'].id)
            if data['minimum_date'] is not None:
                posts = posts.filter(created_date__gte=data['minimum_date'])
            if data['maximum_date'] is not None:
                posts = posts.filter(created_date__lte=data['maximum_date'])
            if data['order_by'] == 1:
                posts = posts.all().order_by('created_date')
            if data['order_by'] == 2:
                posts = posts.all().order_by('-created_date')
    else:
        blog_filter_form = blog_forms.PostFilter()

    paginator = Paginator(posts, 12)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog.html", {
        'category': category,
        "posts": posts,
        #"categories": getBlogCategories(),
        'blog_filter_form': blog_filter_form,
        #'shoppingcart_form': getShoppingCart(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def detail_post(request, post_slug):
    post = get_object_or_404(blog_models.Post, slug=post_slug)
    comments = blog_models.Comment.objects.filter(post=post.id, status=1, parent_id__isnull=True).order_by("created_date")
    images = general_models.Image.objects.filter(album=post.album)
    blog_filter_form = blog_forms.PostFilter()
    num_comments = len(blog_models.Comment.objects.filter(post=post.id, status=1))

    return render(request, "post.html", {
        "post": post,
        "images": images,
        #"categories": getBlogCategories(),
        "comments":comments,
        "num_comments": num_comments,
        "comment_form": getCommentForm(request),
        #"answer_form": getCommentForm(request),
        'blog_filter_form': blog_filter_form,
        #'shoppingcart_form': getShoppingCart(),
        "search_form": general_views.getSearchForm(),
        #'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def category_posts(request, category):
    category = blog_models.Category.objects.get(slug=category)
    posts = blog_models.Post.objects.filter(status=1, category=category.id)

    return render(request, 'blog.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def author_posts(request, username):
    author = User.objects.get(username=username)
    posts = blog_models.Post.objects.filter(status=1, author=author.id)
    categories = blog_models.Category.objects.order_by("name")

    return render(request, 'blog.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def tag_posts(request, tag_slug):
    print(tag_slug)
    tag = blog_models.Tag.objects.filter(slug=tag_slug)
    print(tag)
    posts = blog_models.Post.objects.filter(status=1, tags=tag)

    return render(request, 'blog.html', {
        "posts":posts,
        "categories": getBlogCategories(),
        "search_form": general_views.getSearchForm(),
        'subscribe_form': general_views.getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def last_posts():

    return blog_models.Post.objects.filter(status=1).order_by('-created_date')[:3]


# Comments Views
def add_comment(request, post_slug):
    """
    Method that add comment to post:
    - from existing user and new user
    - new comments and answers
    If user is new add it to subscribers list
    """
    post = get_object_or_404(blog_models.Post, slug=post_slug)
    comment_form = getCommentForm(request)
    name = None
    comment_parent = None

    try:
        print("probamos a coger el identificador del padre")
        comment_parent_id = int(request.POST.get('comment_parent_id'))
    except:
        print("el identificador del padre no existe")
        comment_parent_id = None

    if comment_form.is_valid():
        data = comment_form.cleaned_data
        if request.user.is_authenticated():
            name = request.user.username
        else:
            user = User.objects.filter(email=data['email'])
            if not user:
                general_models.Subscriber.objects.update_or_create(email=data['email'])
                name = data['name']
            else:
                name = user.username

        if comment_parent_id:
            print("el identificador del padre existe")
            comment_parent = blog_models.Comment.objects.get(id=comment_parent_id)
            if comment_parent:
                comment_parent_id = comment_parent.id

        blog_models.Comment.objects.create(
            status=2,
            title=data['title'],
            content=data['content'],
            author=name,
            post=post,
            parent=comment_parent)

    return redirect('blog:detail_post', post_slug=post.slug)


def delete_comment(request, comment_id):
    print("funcion que borrar un comentario")
    print(comment_id)
    comment = get_object_or_404(blog_models.Comment, id=comment_id)
    post = get_object_or_404(blog_models.Post, id=comment.post.id)
    print(comment)
    print(post)
    comment.delete()

    return redirect('blog:detail_post', post_slug=post.slug)

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

"""
class APICommentList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = blog_models.Category
    serializer_class = blog_serializer.CommentSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.query_params
        return blog_models.Comment.objects.filter(post_id=data['post_id'])
"""
"""
class APICommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = blog_models.Comment.objects.all()
    serializer_class = blog_serializer.CommentSerializer
"""



#
