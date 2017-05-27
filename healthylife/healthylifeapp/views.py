from django.shortcuts import render  # , render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from healthylifeapp.forms import ContactForm, SportTypeForm, \
    SportSessionForm, WorkWithOurForm
from healthylifeapp.models import SportSession, SportType
from django.utils import timezone


# Create your views here.
def inicio(request):
    return render(request, "base.html", {})


def contact(request):
    form = ContactForm(request.POST or None)
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


def sport(request):
    return render(request, 'sport.html', {})


def statistics(request):
    return render(request, 'statistics.html', {})


def nutrition(request):
    return render(request, 'nutrition.html', {})


def health(request):
    return render(request, 'health.html', {})


def awards(request):
    return render(request, 'awards.html', {})


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
