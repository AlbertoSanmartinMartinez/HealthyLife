#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render, render_to_response, redirect
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
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login
#from calendar import HTMLCalendar

# API imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# General views
def home(request):
    last_posts = models.Post.objects.filter(status=1).order_by("-creation_date")[:6]
    return render(request, "base.html", {
        "search_form":getSearchForm(),
        "last_posts": last_posts,
    })


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
    Vista que regitra a un colaborador y le da permisos
    """
    if request.method == 'POST':
        # perfil colaborador
        user_form = forms.CustomRegisterColaboratorForm(data=request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()
            collaborator = models.CollaboratorProfile.objects.create(user_id = user.id)
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
                health_colaborator_group = Group.objects.get(name='colaboradores_salud')
                health_colaborator_group.user_set.add(user)
            return redirect('home')
    else:
        user_form = forms.CustomRegisterColaboratorForm()

    return render(request, 'work_with_our.html', {
        "user_form": user_form
    })


def legal_information(request):
    context = {
        "search_form":getSearchForm(),
    }
    return render(request, 'aviso_legal.html', context)


def know_us(request):
    collaborators = models.CollaboratorProfile.objects.all()
    companies = models.Company.objects.all()

    return render(request, 'know_us.html', {
        "search_form":getSearchForm(),
        "companies": companies,
        "collaborators": collaborators,
    })


def know_us_collaborator(request, username):
    user = User.objects.get(username=username)
    print(user)
    collaborator = models.CollaboratorProfile.objects.get(user_id=user.id)
    print(collaborator.education)

    return render(request, 'collaborator.html', {
        "collaborator": collaborator,
        "search_form":getSearchForm(),
    })


def know_us_company(request, companyname):
    company = models.Company.objects.get(slug=companyname)

    return render(request, 'company.html', {
        "company": company,
        "search_form":getSearchForm(),
    })


# Login views
def custom_login(request):
    if request.method == 'POST':
        form = forms.CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
    else:
        form = forms.CustomAuthenticationForm()

    return render(request, 'custom_login.html', {
        "search_form": getSearchForm,
        "form": form,
    })


# Registration views
def cutom_registration(request):
    if request.method == 'POST':
        form = forms.CustomRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.CustomRegisterForm()

    return render(request, 'custom_register.html', {
        "search_form": getSearchForm,
        "form": form,
    })


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
    return render(request, 'nutrition.html', {
        "search_form": getSearchForm(),
    })


# Health views
def health(request):
    return render(request, 'health.html', {
        "search_form": getSearchForm(),
    })


# Award views
def awards(request):
    return render(request, 'awards.html', {})


# Sport views
def sport(request):
    return render(request, 'sport.html', {
        "search_form": getSearchForm(),
    })


# Blog views
def blog(request):
    posts = models.Post.objects.filter(status=1).order_by("-creation_date")

    return render(request, "blog.html", {
        "posts": posts,
        "categories": obtenerCategorias(request),
        "search_form": getSearchForm(),
    })


def detail_post(request, post):
    post = models.Post.objects.get(slug=post)
    comments = models.Comment.objects.filter(post=post.id)
    images = models.Image.objects.filter(album=post.album)

    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
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
        "images": images,
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
    form = forms.SearchForm(request.POST)
    if form.is_valid():
        word = form.cleaned_data['word']
        posts = models.Post.objects.filter(status=1, title__contains=word).order_by("-creation_date")
        categories =  obtenerCategorias(request)
    else:
        form = forms.SearchForm()
        posts = None
    return render(request, 'blog.html', {
        "posts": posts,
        "categories": obtenerCategorias(request),
        "search_form": getSearchForm(),
    })

# Shop views
def shop(request):
    return render(request, 'shop.html', {
        "search_form": getSearchForm(),
    })


# Profile views
@login_required(redirect_field_name='custom_login')
def profile(request, username):
    """
    Vista que muestra la informacion del perfil de usuario
    """
    user = User.objects.get(username=username)
    user_profile = models.UserProfile.objects.get(user_id=user.id)
    bank_information = models.BankInformation.objects.get(user_id=user.id, is_company=False)
    address = models.Address.objects.get(user_id=user.id, is_company=False)

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST, instance=request.user)
        user_profile_form = forms.UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        address_form = forms.AddressForm(data=request.POST, instance=address)
        bank_information_form = forms.BankInformationForm(data=request.POST, instance=bank_information)

        if user_form.is_valid():
            user_form.save()
        if user_profile_form.is_valid():
            user_profile_form.save()
        if bank_information_form.is_valid():
            bank_information_form.save()
        if address_form.is_valid():
            address_form.save()

    else:
        user_form = forms.UserForm(instance=request.user)
        bank_information_form = forms.BankInformationForm(instance=bank_information)
        address_form = forms.AddressForm(instance=address)
        user_profile_form = forms.UserProfileForm(instance=request.user.userprofile)

    return render(request, 'profile.html', {
        "user_form": user_form,
        "bank_information_form": bank_information_form,
        "address_form": address_form,
        "user_profile_form": user_profile_form,
        "search_form": getSearchForm(),
        "user_profile": user_profile,
    })


@login_required(redirect_field_name='custom_login')
def collaborator_profile(request, username):
    """
    Vista que muestra la informacion del perfil de colaborador
    """
    user = User.objects.get(username=username)
    collaborator_profile = models.CollaboratorProfile.objects.get(user_id=user.id)
    try:
        company = models.Company.objects.get(user_id=user.id)
    except:
        company = None
    try:
        bank_information = models.BankInformation.objects.get(user_id=user.id, is_company=True)
    except:
        bank_information = None
    try:
        address = models.Address.objects.get(user_id=user.id, is_company=True)
    except:
        address = None
    if request.method == 'POST':
        collaborator_profile_form = forms.CollaboratorProfileForm(data=request.POST, instance=collaborator_profile)
        if user.is_staff:
            if company is None:
                company_form = forms.CompanyForm(request.POST, request.FILES)
                if company_form.is_valid():
                    data = company_form.cleaned_data
                    company = models.Company.objects.create(
                        user_id=user.id,
                        company_name=data['company_name'],
                        description=data['description'],
                        phone=data['phone'],
                        web=data['web'])
                    company.save()
            else:
                company_form = forms.CompanyForm(request.POST, request.FILES, instance=company)
                if company_form.is_valid():
                    company_form.save()

            if bank_information is None:
                bank_information_form = forms.BankInformationForm(data=request.POST)
                if bank_information_form.is_valid():
                    data_bank_information = bank_information_form.cleaned_data
                    # bank_information_form.save()
                    data_bank_information = models.BankInformation.objects.create(
                        bank_name = data_bank_information['bank_name'],
                        account = data_bank_information['account'],
                        month = data_bank_information['month'],
                        year = data_bank_information['year'],
                        security_code = data_bank_information['security_code'],
                        user_id = user.id,
                        is_company = True)
            else:
                bank_information_form = forms.BankInformationForm(data=request.POST, instance=bank_information)
                if bank_information_form.is_valid():
                    bank_information_form.save()

            if address is None:
                address_form = forms.AddressForm(data=request.POST)
                if address_form.is_valid():
                    data = address_form.cleaned_data
                    address = models.Address.objects.create(
                        user_id=user.id,
                        address_name=data['address_name'],
                        city=data['city'],
                        postal_code=data['postal_code'],
                        street = data['street'],
                        number = data['number'],
                        floor = data['floor'],
                        door = data['door'],
                        is_company = True)
                    address.save()
            else:
                address_form = forms.AddressForm(data=request.POST, instance=address)
                if address_form.is_valid():
                    address_form.save()
        if collaborator_profile_form.is_valid():
            collaborator_profile_form.save()

    else:
        if company is None:
            company_form = forms.CompanyForm()
        else:
            company_form = forms.CompanyForm(instance=company)
        if bank_information is None:
            bank_information_form = forms.BankInformationForm()
        else:
            bank_information_form = forms.BankInformationForm(instance=bank_information)
        if address is None:
            address_form = forms.AddressForm()
        else:
            address_form = forms.AddressForm(instance=address)
        collaborator_profile_form = forms.CollaboratorProfileForm(instance=collaborator_profile)

    return render(request, 'collaborator_profile.html', {
        "bank_information_form": bank_information_form,
        "address_form": address_form,
        "company_form": company_form,
        "company": company,
        "search_form": getSearchForm(),
        "collaborator_profile_form": collaborator_profile_form,
        "collaborator_profile": collaborator_profile,
        })


def sport_profile(request, username):
    return render(request, 'sport_profile.html', {
        "search_form": getSearchForm(),
    })


def nutrition_profile(request, username):
    return render(request, 'nutrition_profile.html', {
        "search_form": getSearchForm(),
    })


def health_profile(request, username):
    return render(request, 'health_profile.html', {
        "search_form": getSearchForm(),
    })


def awards_profile(request, username):
    return render(request, 'awards_profile.html', {
        "search_form": getSearchForm(),
    })


# Calendar views
def calendarMonth(request, username, month):
    """
    https://williambert.online/2011/06/django-event-calendar-for-a-django-beginner/
    continuar por las views del calendario
    """
    calendar = HTMLCalendar()
    calendar = calendar.formatmonth(2018, 04)
    user = User.objects.get(username=username)
    #events = models.Event.objects.filter(owner_id=user.id)

    """
    if request.method == 'POST':
        event_form = forms.EventForm(data=request.POST)
        if event_form.is_valid():
            data = event_form.cleaned_data
            event = models.Event.objects.create()
            event.save()
    else:
        event_form = forms.EventForm()
    """

    return render(request, 'prueba_calendar.html', {
        "search_form": getSearchForm(),
        #"events": events,
        #"event_form": event_form,
        "calendar": calendar,
    })


def calendarDay(reques, username, month, day):
    pass


def event(reques):
    pass


def ships(request, username):
    return render(request, 'ships.html', {
        "search_form": getSearchForm(),
    })


# Admin views


############################## API VIEWS ##############################
def api(request):
    return render(request, 'api.html', {
        "search_form": getSearchForm(),
    })


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """clase para los permisos de la API∫"""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


# General Api Views
def userLoginAPI(request):
    pass


@api_view(['POST'])
def userRegistrationAPI(request):
    """metodo de la api para registrar a un usuario"""
    if request.method == 'POST':
        print('metodo post django')
        serializer = User(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.create(
                username = serializer['username'],
                mail = serializer['email'],
                password = serializer['password']
            )
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        print('metodo get')
    else:
        print('otro metodo')


#@user_passes_test(lambda u: u.is_superuser)
class APIUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


#@user_passes_test(lambda u: u.is_superuser)
class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# Blog Api Views
class APIPostList(generics.ListAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'slug']
    model = models.Post
    serializer_class = serializers.PostSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.query_params
        return models.Post.objects.filter(status=data['status'])


class APIPostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = serializers.PostSerializer
    model = models.Post
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
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class APICategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    # model = models.Category
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = models.Category.objects.all()
        queryset = queryset.filter(name=self.request.query_params.get('category_id'))


class APICommentList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = models.Category
    serializer_class = serializers.CommentSerializer

    def get_queryset(self, *args, **kwargs):
        data = self.request.query_params
        return models.Comment.objects.filter(post_id=data['post_id'])


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


# Error Views
def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
