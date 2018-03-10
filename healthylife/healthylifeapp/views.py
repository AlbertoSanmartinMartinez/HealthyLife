#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp import forms
from healthylifeapp import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from healthylifeapp import serializers
from rest_framework import viewsets

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

"""
class WorkWithOurView(CreateView):
    model = User
    template_name = 'work_with_our.html'
    form_class = forms.WorkWithOurForm
    success_url = reverse_lazy('registration_complete')

    def validate_form(self):
        if form.is_valid:
            instance = form_class.save()
            print(instance.blog)
"""

def work_with_our(request):
    context = {}
    if request.method == 'POST':
        user_form = forms.RegisterForm()
        collaborator_form.WorkWithOurForm()
        # word = form.cleaned_data['word']
        if user_form.is_valid() and collaborator_form.is_valid():
            # user_form.forms
            # user =
            context += {
            # "user_form": user_form,
                "collaborator_form": collaborator_form,
                "search_form": getSearchForm(),
            }

    return render(request, 'work_with_our.html', context)


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
def access(request):
    context = {
        "search_form":getSearchForm(),
    }
    return render(request, 'access.html', context)

# Registration views
class RegistrationView(CreateView):
    model = User
    template_name = 'registration/registration_register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('registration_complete')


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
def profile(request, username):
    user = User.objects.get(username=username)
    custom_user = models.CustomUser.objects.get(user_id=user.id)
    bank_information = models.BankInformation.objects.filter(user_id=user.id)
    address_information = models.Address.objects.filter(user_id=user.id)
    context = {
        "user": user,
        "custom_user":custom_user,
        "bank_information": bank_information,
        "address_information": address_information,
        "search_form":getSearchForm(),
    }
    return render(request, 'profile.html', context)


def calendar(request):
    return render(request, 'calendar.html', {})


def ships(request):
    return render(request, 'ships.html', {})


# Admin views
def admin(request, username):
    user = models.User.objects.get(username=username)
    custom_user = models.CustomUser.objects.get(user_id=user.id)
    context = {
        "custom_user": custom_user,
        "search_form": getSearchForm(),
    }
    return render(request, 'admin.html', context)

def admin_blog(request):
    posts = models.Post.objects.filter(author=request.user.id).order_by("-creation_date")
    categories = models.Category.objects.order_by("name")
    context = {
	"posts": posts,
	"categories": categories,
    }
    return render(request, 'admin_blog.html', context)


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


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer


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

"""
class APIUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
"""

# Funciones Comunes
def obtenerCategorias(request):
    return models.Category.objects.order_by("name")

def getSearchForm():
    return forms.SearchForm()
