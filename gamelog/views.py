from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Game, Location, Format, Player, Deck
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
        # context['Decks'] = Deck.objects.all()
        # context['form'] = forms.GameForm()
        return context


class GameView(generic.DetailView):
    model = Game
    template_name = 'gamelog/game.html'

    def get_context_data(self, **kwargs):
        context = super(GameView, self).get_context_data(**kwargs)
        p = Game.objects.get(pk=self.kwargs['pk']).players
        player_ids = p.values_list('id', flat=True)
        context['decks'] = Deck.objects.filter(player_id__in=player_ids)
        return context


class StatsView(generic.TemplateView):
    template_name = 'gamelog/stats.html'


class ProfileView(generic.TemplateView):
    template_name = 'gamelog/profile.html'


def get_player_decks(request, player_id):
    if request.is_ajax():
        decks = Deck.objects.filter(player_id=player_id)
        response_data = []
        for deck in decks:
            data = {}
            data['id'] = deck.id
            data['name'] = deck.name
            data['format'] = deck.format.name
            response_data.append(data)

        return JsonResponse(response_data, safe=False)


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


