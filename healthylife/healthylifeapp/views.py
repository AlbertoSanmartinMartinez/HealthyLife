#!/usr/local/bin/python
# coding: utf-8

from django.shortcuts import render, render_to_response, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp import forms as general_forms
from healthylifeapp import models as general_models
# from blog import models as blog_models
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
import calendar
from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect

# from shop import models as shop_models
# from awards import models as award_models
# from events import models as events_models
# from shop import forms as shop_forms
# from shop import views as shop_views

# API imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# General views
def home(request):
    from blog import models as blog_models
    from shop import models as shop_models
    from shop import forms as shop_forms
    from shop import views as shop_views
    from awards import models as award_models
    from awards import views as award_views

    last_posts = blog_models.Post.objects.filter(status=1).order_by("-created_date")[:3]
    # last_products = shop_models.Product.objects.filter(status=1, stock__gte=1).order_by("-created_date")[:6]
    # next events
    # best_awards = award_models.Award.objects.filter(status=1).order_by("-created_date")[:3]

    return render(request, "home.html", {
        "search_form":getSearchForm(),
        "last_posts": last_posts,
        "last_products": shop_views.last_products(),
        "best_awards": award_views.best_awards(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart_form': shop_forms.ShoppingCartForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def contact(request):
    from shop import views as shop_views

    form = general_forms.ContactForm(request.POST or None)
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
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    }
    return render(request, "contact.html", context)


def work_with_our(request):
    """
    Vista que regitra a un colaborador y le da permisos
    """
    from shop import views as shop_views

    if request.method == 'POST':
        # perfil colaborador
        user_form = general_forms.CustomRegisterColaboratorForm(data=request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = user_form.save(commit=False)
            user.is_staff = True
            user.save()
            collaborator = general_models.CollaboratorProfile.objects.create(user_id = user.id)
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
        user_form = general_forms.CustomRegisterColaboratorForm()

    return render(request, 'work_with_our.html', {
        "user_form": user_form,
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def legal_information(request):
    from shop import views as shop_views

    return render(request, 'aviso_legal.html', {
        "search_form":getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def know_us(request):
    from shop import views as shop_views

    collaborators = general_models.CollaboratorProfile.objects.all()
    companies = general_models.Company.objects.all()

    return render(request, 'know_us.html', {
        "search_form":getSearchForm(),
        "companies": companies,
        "collaborators": collaborators,
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def know_us_collaborator(request, username):
    from shop import views as shop_views

    user = User.objects.get(username=username)
    collaborator = models.CollaboratorProfile.objects.get(user_id=user.id)

    return render(request, 'collaborator.html', {
        "collaborator": collaborator,
        "search_form":getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def know_us_company(request, companyname):
    from shop import views as shop_views

    company = models.Company.objects.get(slug=companyname)

    return render(request, 'company.html', {
        "company": company,
        "search_form":getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


# Login views
def custom_login(request):
    from shop import views as shop_views

    if request.method == 'POST':
        print("metodo post")
        form = general_forms.CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            print("formulario valido")
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                print("user correcto")
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                    #return HttpResponseRedirect(request.POST.get('next', reverse('index')))
                    """
                    if request.POST["next"] is not "":
                        print("next no esta vacio")
                        return HttpResponseRedirect(request.POST["next"])
                    else:
                        print("next esta vacio")
                        #HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
                        return redirect(settings.LOGIN_REDIRECT_URL)
                    """

    else:
        print("metodo no post")
        form = general_forms.CustomAuthenticationForm()

    shoppingcart = shop_views.getShoppingCart(request)

    return render(request, 'custom_login.html', {
        "search_form": getSearchForm,
        "form": form,
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shoppingcart,
    })


# Registration views
def custom_registration(request):
    from shop import views as shop_views

    if request.method == 'POST':
        form = general_forms.CustomRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = general_forms.CustomRegisterForm()

    shoppingcart = shop_views.getShoppingCart(request)

    return render(request, 'custom_register.html', {
        "search_form": getSearchForm,
        "form": form,
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shoppingcart,
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
    return render(request, 'statistics.html', {
        'subscribe_form': getSubscribeForm(),
    })


"""
def health(request):
    return render(request, 'health.html', {
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })
"""

# Blog views
def subscribe(request):
    print("funcion de subscripcion")
    if request.method == 'POST':
        subscribe_form = forms.SubscriberForm(data=request.POST)
        if subscribe_form.is_valid():
            data = subscribe_form.cleaned_data['email']
            subscribe_form.save()
    else:
        subscribe_form = forms.SubscriberForm()

    return redirect('home')


"""
#@login_required(redirect_field_name='custom_login')
def comment(request, post_slug, comment_parent_id):
    post = models.Post.objects.get(slug=post_slug)
    if request.method == 'POST':
        print("metodo post")
        if request.user.is_authenticated:
            print("usuario suscrito")
            comment_form = forms.CommentFormAuthenticated(data=request.POST)
            if comment_form.is_valid():
                print("formulario valido")
                data = comment_form.cleaned_data
                comment = models.Comment.objects.create(
                    author_id=request.user.id,
                    post_id=post.id,
                    title = data['title'],
                    content = data['content'],
                    parent_id = comment_parent_id)
        else:
            print("usuario no suscrito")
            comment_form = forms.CommentFormNotAuthenticated(data=request.POST)
            if comment_form.is_valid():
                #data = comment_form.cleaned_data
                print("formulario valido")
                #subscribe(request)
    else:
        print("metodo no post")
        comment_form = forms.CommentForm()

    return detail_post(request, post_slug)
"""


# Search views
def search(request):
    form = forms.SearchForm(request.POST)
    if form.is_valid():
        word = form.cleaned_data['word']
        posts = models.Post.objects.filter(status=1, title__contains=word).order_by("-created_date")
    else:
        form = forms.SearchForm()
        posts = None

    return render(request, 'blog.html', {
        "posts": posts,
        "categories": obtenerCategorias(request),
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })


# Profile views
@login_required(redirect_field_name='custom_login')
def profile(request, username):
    """
    View for user information section
    https://www.codementor.io/lakshminp/handling-multiple-forms-on-the-same-page-in-django-fv89t2s3j
    """
    from shop import views as shop_views

    user = User.objects.get(username=username)
    user_profile = general_models.UserProfile.objects.get(user_id=user.id)
    bank_information = general_models.BankInformation.objects.get(user_id=user.id, is_company=False)
    address = general_models.Address.objects.get(user_id=user.id, is_company=False)

    if request.method == 'POST' and 'user_profile' in request.POST:
        user_profile_form = general_forms.UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_profile_form.is_valid():
            user_profile_form.save()
    else:
        user_profile_form = general_forms.UserProfileForm(instance=request.user.userprofile)

    if request.method == 'POST' and 'bank_information' in request.POST:
        bank_information_form = general_forms.BankInformationForm(data=request.POST, instance=bank_information)
        if bank_information_form.is_valid():
            bank_information_form.save()
    else:
        bank_information_form = general_forms.BankInformationForm(instance=bank_information)

    if request.method == 'POST' and 'address' in request.POST:
        address_form = general_forms.AddressForm(data=request.POST, instance=address)
        if address_form.is_valid():
            address_form.save()
    else:
        address_form = general_forms.AddressForm(instance=address)

    return render(request, 'profile.html', {
        # "user_form": user_form,
        "bank_information_form": bank_information_form,
        "address_form": address_form,
        "user_profile_form": user_profile_form,
        "user_profile": user_profile,
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


@login_required(redirect_field_name='custom_login')
def collaborator_profile(request, username):
    """
    Vista que muestra la informacion del perfil de colaborador
    """
    from shop import views as shop_views

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
            company_form = general_forms.CompanyForm()
        else:
            company_form = general_forms.CompanyForm(instance=company)
        if bank_information is None:
            bank_information_form = general_forms.BankInformationForm()
        else:
            bank_information_form = general_forms.BankInformationForm(instance=bank_information)
        if address is None:
            address_form = general_forms.AddressForm()
        else:
            address_form = general_forms.AddressForm(instance=address)
        collaborator_profile_form = general_forms.CollaboratorProfileForm(instance=collaborator_profile)

    return render(request, 'collaborator_profile.html', {
        "bank_information_form": bank_information_form,
        "address_form": address_form,
        "company_form": company_form,
        "company": company,
        "search_form": getSearchForm(),
        "collaborator_profile_form": collaborator_profile_form,
        "collaborator_profile": collaborator_profile,
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
        })


def sport_profile(request, username):
    from shop import views as shop_views

    return render(request, 'sport_profile.html', {
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


def nutrition_profile(request, username):
    from shop import views as shop_views

    return render(request, 'nutrition_profile.html', {
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
    })


def health_profile(request, username):
    from shop import views as shop_views

    return render(request, 'health_profile.html', {
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
        'shoppingcart': shop_views.getShoppingCart(request),
    })


############################## API VIEWS ##############################
def api(request):
    return render(request, 'api.html', {
        "search_form": getSearchForm(),
        'subscribe_form': getSubscribeForm(),
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


# Common Functions
def getSearchForm():
    return general_forms.SearchForm()


def getSubscribeForm():
    return general_forms.SubscriberForm()


# Error Views
def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
