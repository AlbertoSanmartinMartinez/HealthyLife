from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp import forms
from healthylifeapp import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
# from django.contrib.auth.views import login, logout


# General views
def inicio(request):
    return render(request, "base.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
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
    }
    return render(request, "contact.html", context)


def work_with_our(request):
    form = WorkWithOurForm
    context = {
        'work_with_our_form': form
    }
    return render(request, 'work_with_our.html', context)


def legal_information(request):
    return render(request, 'aviso_legal.html', {})


def know_us(request):
    return render(request, 'conocenos.html', {})


# Login views
"""
def login(request):
    # form = LogInForm(request.POST or None)
    # context = {
    #     "login_form": form,
    # }
    return render(request, 'login.html', {})


def auth_logout(request):
    return render(request, 'logout.html', {})
"""

# Registration views
def registration_resgister(request):
    form = RegisterForm
    context = {
        "registration_form":form
    }
    return render(request, 'registration_form.html', context)


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
    posts = Post.objects.filter(status=1).values().order_by("-creation_date")
    categories = Category.objects.order_by("name")
    context = {
        "posts":posts,
        "categories":categories
    }
    return render(request, "blog.html", context)


def detail_post(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post.id).values()
    categories = Category.objects.order_by("name")
    context = {
        "post":post,
        "categories":categories,
        "comments":comments,
    }
    return render(request, "post.html", context)


def blog_category_posts(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(status=1, category=category.id).values()
    categories = Category.objects.order_by("name")
    context = {
        "categories":categories,
        "posts":posts,
        "categories":categories,
    }
    return render(request, 'blog.html', context)


def blog_autor_posts(request, username):
    author = User.objects.get(username=username)
    posts = Post.objects.filter(status=1, author=author.id).values()
    categories = Category.objects.order_by("name")
    context = {
        "categories":categories,
        "posts":posts,
        "categories":categories,
    }
    return render(request, 'blog.html', context)


# Shop views
def shop(request):
    return render(request, 'shop.html', {})


# Profile views
def profile(request, username):
    user = CustomUser.objects.get(username=username)
    context = {

    }
    return render(request, 'profile.html', context)
