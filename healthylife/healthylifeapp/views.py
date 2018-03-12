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


# General views
def inicio(request):
    context = {
        "search_form":getSearchForm(),
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
    https://www.programcreek.com/python/example/50077/django.contrib.auth.models.Permission
    """
    blog_colaborator_group = Group.objects.get(name='colaboradores_blog')
    shop_colaborator_group = Group.objects.get(name='colaboradores_premios')
    award_colaborator_group = Group.objects.get(name='colaboradores_tienda')

    if request.method == 'POST':
        user_form = forms.CustomRegisterColaboratorForm(data=request.POST)
        if user_form.is_valid():
            blog_colaborator = user_form.cleaned_data.get('blog_colaborator')
            shop_colaborator = user_form.cleaned_data.get('shop_colaborator')
            award_colaborator = user_form.cleaned_data.get('award_colaborator')
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()
            if blog_colaborator == True:
                blog_colaborator_group.user_set.add(user)
            if shop_colaborator == True:
                shop_colaborator_group.user_set.add(user)
            if award_colaborator == True:
                award_colaborator_group.user_set.add(user)
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


class SportSessionDetail(DetailView):
    model = models.SportSession
    template_name = 'sport_session_detail.html'

    def get_context(self, **kwargs):
        context = super(SportSessionDetail. self).get_context(*+kwargs)
        return context


class SportSessionList(ListView):
    model = models.SportSession
    template_name = 'sport_session_list.html'

    def get_context_data(self, **kwargs):
        context = super(SportSessionList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SportSessionUpdate(UpdateView):
    template_name = 'form.html'


class SportSessionCreate(CreateView):
    model = models.SportSession
    form_class = forms.SportSessionForm
    template = 'form.html'
    succes_url = '/'

    def form_valid(self, form):
        return super(SportSessionCreate, self).form_valid(form)


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
    context = {
        "post":post,
        "categories": obtenerCategorias(request),
        "comments":comments,
        "search_form":getSearchForm(),
    }
    return render(request, "post.html", context)


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
    print(username)
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

def search(request):
    form = forms.SearchForm(request.GET or None)
    if form.is_valid():
        word = form.cleaned_data['word']
        posts = models.Post.objects.filter(status=1, title__contains=word).order_by("-creation_date")
        categories =  obtenerCategorias()
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


def shop_admin(request, username):
    posts = models.Post.objects.filter(username=username)
    context = {
        "posts":posts
    }
    return render(request, 'shop_admin.html', context)


# Profile views
@login_required(redirect_field_name='custom_login')
def profile(request, username):
    """
    Vista que muestra la informacion de un usuario
    """
    user = User.objects.get(username = username)
    bank_information = models.BankInformation.objects.get(user_id = user.id)
    address = models.Address.objects.get(user_id = user.id)
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST, instance = user)
        bank_information_form = forms.BankInformationForm(data=request.POST, instance = bank_information)
        address_form = forms.AddressForm(data=request.POST, instance = address)
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

    return render(request, 'profile.html', {
        "user_form": user_form,
        "bank_information_form": bank_information_form,
        "address_form": address_form
        })


def calendar(request):
    return render(request, 'calendar.html', {})


def ships(request):
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
