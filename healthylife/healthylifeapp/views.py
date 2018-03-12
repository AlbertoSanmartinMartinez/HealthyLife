#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp import forms
from healthylifeapp import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from healthylifeapp import serializers
from rest_framework import viewsets
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from guardian.shortcuts import assign_perm


# General views
def inicio(request):
    context = {
        "search_form": getSearchForm(),
    }
    return render(request, "base.html", context)


def contact(request):
    form = forms.ContactForm(request.POST or None)
    if form.is_valid():
        email_form = form.cleaned_data.get("email")
        message_form = form.cleaned_data.get("mensaje")
        name_form = form.cleaned_data.get("nombre")
        asunto = 'Mensaje de contacto'
        email_to = email
        email_from = settings.EMAIL_HOST_USER
        email_message = "%s: %a enviado por %s" %(name_form, message_form, email_form)
        send_mail(asunto, email_from, email_to, email_message, fail_silently=True)
    context = {
        "contact_form": form,
        "search_form":getSearchForm(),
    }
    return render(request, "contact.html", context)


def work_with_our(request):
    """
    Vista que regitra a un cobaorador y le da permisos
    """
    if request.method == 'POST':
        user_form = forms.CustomRegisterColaboratorForm(data=request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()
            if data['blog_colaborator'] == True:
                blog_colaborator_group = Group.objects.get(name='colaboradores_blog')
                blog_colaborator_group.user_set.add(user)
            if data['shop_colaborator'] == True:
                shop_colaborator_group = Group.objects.get(name='colaboradores_tienda')
                shop_colaborator_group.user_set.add(user)
            if data['award_colaborator'] == True:
                award_colaborator_group = Group.objects.get(name='colaboradores_premios')
                award_colaborator_group.user_set.add(user)
            if data['sport_colaborator'] == True:
                sport_colaborator_group = Group.objects.get(name='colaboradores_deporte')
                sport_colaborator_group.user_set.add(user)
            if data['nutrition_colaborator'] == True:
                nutrition_colaborator_group = Group.objects.get(name='colaboradores_nutricion')
                nutrition_colaborator_group.user_set.add(user)
            if data['health_colaborator'] == True:
                health_colaborator_group = Group.objects.get(name='colaboradores_premios')
                health_colaborator_group.user_set.add(user)
            if data['company'] == True:
                company = models.Company.objects.create(user_id=user.id)
    else:
        user_form = forms.CustomRegisterColaboratorForm()

    return render(request, 'work_with_our.html', { "user_form": user_form })


def legal_information(request):
    context = {
        "search_form":getSearchForm(),
    }
    return render(request, 'aviso_legal.html', context)


def know_us(request):
    context = {
        "search_form":getSearchForm(),
    }
    return render(request, 'conocenos.html', context)


# Login views
class CustomLoginView(auth_views.LoginView):
    authentication_form = forms.CustomAuthenticationForm
    template_name = 'custom_login.html'

    # "search_form": getSearchForm(),


# Registration views
class CustomRegistrationView(CreateView):
    model = User
    form_class = forms.CustomRegisterForm
    template_name = 'custom_register.html'
    success_url = 'completado'


def registration_complete(request):
    return render(request, 'registration_complete.html', {})


def registration_disallowed(request):
    return render(request, 'registration_closed.html', {})


def registration_activate(request):
    return render(request, '')


def registration_activation_complete(request):
    return render(request, 'activation_complete.html', {})


# Statistics views
def statistics(request):
    return render(request, 'statistics.html', {})


# Nutrition views
def nutrition(request):
    return render(request, 'nutrition.html', {})


# Health views
def health(request):
    return render(request, 'health.html', {})


# Award views
def awards(request):
    return render(request, 'awards.html', {})


# Sport views
def sport(request):
    return render(request, 'sport.html', {})


# Blog views
def blog(request):
    posts = models.Post.objects.filter(status=1).order_by("-creation_date")
    context = {
        "posts":posts,
        "categories": obtenerCategorias(request),
        "search_form": getSearchForm(),
    }
    return render(request, "blog.html", context)


def detail_post(request, post):
    post = models.Post.objects.get(slug=post)
    comments = models.Comment.objects.filter(post=post.id)

    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            print(data)
            comment = models.Comment.objects.create(
                author_id=request.user.id,
                post_id=post.id,
                title = data['title'],
                content = data['content'])
            comment_form.save()
    else:
        comment_form = forms.CommentForm()

    return render(request, "post.html", {
        "post": post,
        "categories": obtenerCategorias(request),
        "comments":comments,
        "comment_form": comment_form,
        "search_form": getSearchForm(),
    })


def blog_category_posts(request, category):
    category = models.Category.objects.get(slug=category)
    posts = models.Post.objects.filter(status=1, category=category.id)
    context = {
        "posts":posts,
        "categories": obtenerCategorias(request),
        "search_form":getSearchForm(),
    }
    return render(request, 'blog.html', context)


def blog_author_posts(request, username):
    author = User.objects.get(username=username)
    posts = models.Post.objects.filter(status=1, author=author.id)
    categories = models.Category.objects.order_by("name")
    context = {
        "categories":categories,
        "posts":posts,
        "categories": obtenerCategorias(request),
        "search_form":getSearchForm(),
    }
    return render(request, 'blog.html', context)

# Search views
def search(request):
    form = forms.SearchForm(request.GET or None)
    if form.is_valid():
        word = form.cleaned_data['word']
        posts = models.Post.objects.filter(status=1, title__contains=word).order_by("-creation_date")
        categories =  obtenerCategorias(request)
        context = {
            "posts": posts,
            "categories": obtenerCategorias(request),
            "search_form":getSearchForm(),
        }
        return render(request, 'blog.html', context)
    else:
        return render(request, 'blog.html', {})

# Shop views
def shop(request):
    return render(request, 'shop.html', {})


# Profile views
@login_required(redirect_field_name='custom_login')
def profile(request, username):
    """
    Vista que muestra la informacion de un perfil particular
    """
    user = User.objects.get(username = username)
    bank_information = models.BankInformation.objects.get(user_id = user.id)
    address = models.Address.objects.get(user_id = user.id)
    try:
        company = models.Company.objects.get(user_id=user.id)
    except:
        company = None
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST, instance = user)
        bank_information_form = forms.BankInformationForm(data=request.POST, instance = bank_information)
        address_form = forms.AddressForm(data=request.POST, instance = address)
        company_form = forms.CompanyForm(data=request.POST, instance = company)
        if company_form.is_valid():
            company_form.save()
        if user_form.is_valid():
            user_form.save()
        if bank_information_form.is_valid():
            bank_information_form.save()
        if address_form.is_valid():
            address_form.save()
    else:
        user_form = forms.UserForm(instance=user)
        bank_information_form = forms.BankInformationForm(instance=bank_information)
        address_form = forms.AddressForm(instance=address)
        company_form = forms.CompanyForm(instance = company)

    return render(request, 'profile.html', {
        "user_form": user_form,
        "bank_information_form": bank_information_form,
        "address_form": address_form,
        "company_form": company_form,
        "company": company
        })


def sport_profile(request, username):
    return render(request, 'sport_profile.html', {})


def nutrition_profile(request, username):
    return render(request, 'nutrition_profile.html', {})


def health_profile(request, username):
    return render(request, 'health_profile.html', {})


def awards_profile(request, username):
    return render(request, 'awards_profile.html', {})


def calendar(request, username):
    return render(request, 'calendar.html', {})


def ships(request, username):
    return render(request, 'ships.html', {})


# Admin views

############################## API VIEWS ##############################
def api(request):
    return render(request, 'api.html', {})


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """clase para los permisos de la API∫"""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


# Blog Api Views
class APIPostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'slug']
    # model = models.Post
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Post
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class APICategoryList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # model = models.Category
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class APICategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class APICommentList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # model = models.Category
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class APICommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


# Funciones Comunes
def obtenerCategorias(request):
    return models.Category.objects.filter(parent__isnull=True).order_by("name")

def getSearchForm():
    return forms.SearchForm()
