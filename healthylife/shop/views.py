# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Shop Views
def product_list(request, shop_category_slug=None):
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
            print(data)
            products = products.filter(name__contains=data['name'])
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
                print("ascendente")
                products = products.order_by('price')
            if data['order_by'] == '2':
                print("descendente")
                products = products.all().order_by('-price')
    else:
        shop_filter_form = shop_forms.ProductFilter()

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        'categories': getShopCategories(),
        'shop_filter_form': shop_filter_form,
        'shoppingcart_form': getShoppingCart(),
    })


def product_detail(request, product_slug):
    product = get_object_or_404(shop_models.Product, slug=product_slug)
    # formularios
    return render(request, 'product_detail.html', {
        'product': product,
        'categories': getShopCategories(),
        'shop_filter_form': getShopFilter(request),
        'shoppingcart_form': getShoppingCart(),
    })

"""
def shop_search(request):
    products = None
    category = None

    if request.method == 'POST':
        form = shop_forms.SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['name'])
            products = shop_models.Product.objects.filter(stock__gt=1)

    return render(request, 'product_list.html', {
        'category': category,
        'products': products,
        'categories': getShopCategories(),
        'shop_filter_form': getShopFilter(request),
    })
"""
# ShoppingCart Views
#@required_POST
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


# Common Methods
def getShopCategories():
    return shop_models.Category.objects.all()


def getShoppingCart():
    shoppingcart_form = shop_forms.ShoppingCartForm()

    return shoppingcart_form

def getShopFilter(request):
    shop_filter_form = shop_forms.ProductFilter(request.POST)

    return shop_filter_form
