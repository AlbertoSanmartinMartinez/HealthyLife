from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp.forms import ContactForm, SportTypeForm, \
    SportSessionForm, WorkWithOurForm, LogInForm, RegisterForm
from healthylifeapp.models import SportSession, SportType, Category, Post, Comment
from django.utils import timezone


# General views
def inicio(request):
    return render(request, "base.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "contact_form": form,
    }
    return render(request, "contact.html", context)


def login(request):
    form = LogInForm(request.POST or None)
    context = {
        "login_form": form,
    }
    return render(request, 'login.html', context)


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        "register_form": form,
    }
    return render(request, 'registration_form.html', context)


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
    model = SportSession
    template_name = 'sport_session_detail.html'

    def get_context(self, **kwargs):
        context = super(SportSessionDetail. self).get_context(*+kwargs)
        return context


class SportSessionList(ListView):
    model = SportSession
    template_name = 'sport_session_list.html'

    def get_context_data(self, **kwargs):
        context = super(SportSessionList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SportSessionUpdate(UpdateView):
    template_name = 'form.html'


class SportSessionCreate(CreateView):
    model = SportSession
    form_class = SportSessionForm
    template = 'form.html'
    succes_url = '/'

    def form_valid(self, form):
        return super(SportSessionCreate, self).form_valid(form)


# Blog views
def blog(request):
    posts = Post.objects.order_by("-creation_date")
    categories = Category.objects.order_by("name")
    context = {
        "posts":posts,
        "categories":categories
    }
    return render(request, "blog.html", context)


def detail_post(request, slug):
    post = Post.objects.get(slug=slug)
    # comments = Comment.objects.get(post=post.id)
    comments = Comment.objects.filter(post=post.id).values()
    context = {
        "post":post,
        "comments":comments,
    }
    return render(request, "post.html", context)

# Shop views
def shop(request):
    return render(request, 'shop.html', {})
