#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from healthylifeapp import views as general_views
from shop import models as shop_models
from shop import forms as shop_forms
from healthylifeapp.views import *


# Shop Views
def product_list(request, shop_category_slug=None):
    """
    """
    category = None
    products = shop_models.Product.objects.filter(status=1, stock__gte=1)
    shop_filter_form = None

    if shop_category_slug:
        category = get_object_or_404(shop_models.Category, slug=shop_category_slug)
        products = products.filter(category=category)

    if request.method == 'POST':
        shop_filter_form = shop_forms.ProductFilter(request.POST)
        if shop_filter_form.is_valid():
            data = shop_filter_form.cleaned_data
            products = products.filter(name__icontains=data['name'])
            if data['category'] is not None:
                products = products.filter(category_id=data['category'].id)
            if data['minimum_price'] is not None:
                products = products.filter(price__gte=data['minimum_price'])
            if data['maximum_price'] is not None:
                products = products.filter(price__lte=data['maximum_price'])
            """
            if data['without_stock'] == True:
                products = products.filter(stock__gte=0)
            else:
                products = products.filter(stock__gte=1)
            """
            if data['with_discount'] == True:
                products = products.filter(discount_id__isnull=False)
            if data['order_by'] == '1':
                products = products.order_by('price')
            if data['order_by'] == '2':
                products = products.all().order_by('-price')
    else:
        shop_filter_form = shop_forms.ProductFilter()

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        #'categories': getShopCategories(),
        'shop_filter_form': shop_filter_form,
        'shoppingcart_form': getShoppingCart(),
        #"search_form": general_views.getSearchForm(),
        #'subscribe_form': general_views.getSubscribeForm(),
    })


def product_detail(request, product_slug):
    product = get_object_or_404(shop_models.Product, slug=product_slug)
    reviews = shop_models.Review.objects.filter(product=product.id, status=1, parent_id__isnull=True).order_by('creation_date')
    images = general_models.Image.objects.filter(album=product.album)
    shop_filter_form = shop_forms.ProductFilter()
    num_reviews = len(shop_models.Review.objects.filter(product=product.id, status=1))

    return render(request, 'product_detail.html', {
        'product': product,
        'images': images,
        'categories': getShopCategories(),
        'reviews': reviews,
        'num_reviews': num_reviews,
        'review_form': getReviewForm(request),
        'shop_filter_form': shop_filter_form,
        'shoppingcart_form': getShoppingCart(),
        "search_form": general_views.getSearchForm(),
    })


def last_products():
    return shop_models.Product.objects.filter(status=1, stock__gte=1).order_by("-created_date")[:6]


# Comments Views
def add_review(request, product_slug):
    """
    Method that add comment to product:
    - from existing user and new user
    - new comments and answers
    If user is new add it to subscribers list
    """
    product = get_object_or_404(shop_models.Product, slug=product_slug)
    reviw_form = getReviewForm(request)
    name = None
    review_parent = None

    try:
        review_parent_id = int(request.POST.get('review_parent_id'))
    except:
        review_parent_id = None

    if reviw_form.is_valid():
        data = reviw_form.cleaned_data
        if request.user.is_authenticated():
            name = request.user.username
        else:
            user = User.objects.filter(email=data['email'])
            if not user:
                general_models.Subscriber.objects.update_or_create(email=data['email'])
                name = data['name']
            else:
                name = user.username

        if review_parent_id:
            review_parent = shop_models.Review.objects.get(id=review_parent_id)
            if review_parent:
                review_parent_id = review_parent.id

        shop_models.Review.objects.create(
            title=data['title'],
            content=data['content'],
            author=name,
            product=product,
            parent=review_parent)

    return redirect('shop:product_detail', product_slug=product.slug)


# ShoppingCart Views
def cartAdd(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(shop_models.Product, id=product_id)
    cart.add(product)
    form = shop_forms.ShoppingCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data['quantity']
        cart.update(product, data)
    """
    form = shop_forms.ShoppingCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    """
    return redirect('shop:shoppingcart_detail')


def cartRemove(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(shop_models.Product, id=product_id)
    cart.remove(product)

    return redirect('shop:shoppingcart_detail')


def cartDetail(request):
    cart = ShoppingCart(request)
    for item in cart:
        item['shoppingcart_form'] = shop_forms.ShoppingCartForm(initial={'quantity': item['quantity']}) #, 'update':True})
    return render(request, 'shoppingcart.html', {
        'shoppingcart': cart,
    })


def cartUpdate(request, product_id):
    cart = ShoppingCart(request)
    product = get_object_or_404(shop_models.Product, id=product_id)
    form = shop_forms.ShoppingCartForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data['quantity']
        cart.update(product, data)

    return redirect('shop:shoppingcart_detail')


# Payment Views
"""
def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)
    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(request, 'payment.html', {
        'form': form,
        'payment': payment
    })
"""

def payment_checkout(request):
    print("payment_checkout view")
    cart = ShoppingCart(request)

    stripe_key = settings.STRIPE_TEST_API_KEY
    payment_checkout_form = shop_forms.PaymentCheckout()
    #cart.clear()

    return render(request, 'payment_checkout.html', {
        "payment_checkout_form": payment_checkout_form,
        "stripe_key": stripe_key,
    })


def payment_done(request):
    pass


def payment_canceled(request):
    pass

# Shipping Views
def shipping_checkout(request):


    return render(request, 'shipping_checkout.html', {
    })


# Profile Views
def ships(request, username):

    return render(request, 'ships.html', {

    })


# Common Methods
def getShopCategories():
    return shop_models.Category.objects.all()


def getShoppingCart():
    shoppingcart_form = shop_forms.ShoppingCartForm()

    return shoppingcart_form

def getShopFilter(request):
    shop_filter_form = shop_forms.ProductFilter(request.POST)

    return shop_filter_form


def getReviewForm(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            return shop_forms.ReviewFormAuthenticated(request.POST)
        else:
            return shop_forms.ReviewFormNotAuthenticated(request.POST)
    else:
        if request.user.is_authenticated():
            return shop_forms.ReviewFormAuthenticated()
        else:
            return shop_forms.ReviewFormNotAuthenticated()






#
