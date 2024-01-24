import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Poll, Choice
from django.views import generic
from django.contrib import messages


def index(request):
    context = {"umfragen": Poll.objects.all()}
    return render(request=request, template_name='polls/index.html', context=context)


class PollDetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/umfrage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_see_result = False
        if 'voted_polls' in self.request.session:
            if type(self.request.session['voted_polls']) == list:
                if context['object'].id in self.request.session['voted_polls']:
                    user_see_result = True
        context['voted'] = user_see_result
        return context


class ResultsDetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_see_result = False
        if 'voted_polls' in self.request.session:
            if type(self.request.session['voted_polls']) == list:
                if context['object'].id in self.request.session['voted_polls']:
                    user_see_result = True
        context['access'] = user_see_result
        return context


def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        choose_answer = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "Fehler: keine bzw. eine ungültige Antwort ausgewählt")
        return HttpResponseRedirect(reverse('polls:umfrage-detail', args=(umfrage.slug,)))
    else:
        choose_answer.votes += 1
        choose_answer.save()
        if 'voted_polls' in request.session:
            if type(request.session['voted_polls']) == list:
                voted_polls = request.session['voted_polls']
                voted_polls.append(umfrage.id)
                request.session['voted_polls'] = voted_polls
            else:
                request.session['voted_polls'] = [umfrage.id]
        else:
            request.session['voted_polls'] = [umfrage.id]

        return HttpResponseRedirect(reverse('polls:results', args=(umfrage.slug,)))

