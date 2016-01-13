from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Game, Location, Format, Player
import forms


class IndexView(generic.TemplateView):
    template_name = 'gamelog/home.html'


class GameLogView(generic.ListView):
    template_name = 'gamelog/gamelog.html'
    context_object_name = 'gamelog_list'
    queryset = Game.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GameLogView, self).get_context_data(**kwargs)
        context['Locations'] = Location.objects.all()
        context['Formats'] = Format.objects.all()
        context['Players'] = Player.objects.all()
        context['form'] = forms.GameForm()
        return context


class GameView(generic.DetailView):
    model = Game
    template_name = 'gamelog/game.html'


class StatsView(generic.TemplateView):
    template_name = 'gamelog/stats.html'


class ProfileView(generic.TemplateView):
    template_name = 'gamelog/profile.html'


def add_game(request):
    # Get players

    # Get decks

    # Get location
    location_id = request.POST['location']
    l = Location.objects.get(pk=location_id)

    # Get format
    format_id = request.POST['format']
    f = Format.objects.get(pk=format_id)

    # Create game object
    g = Game(location=l, format=f)

    # Save it
    g.save()

    # Show results
    return HttpResponseRedirect(reverse('gamelog:game', args=(g.id,)))


