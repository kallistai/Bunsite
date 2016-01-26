from django.conf.urls import url

from . import views

app_name = 'gamelog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^gamelog/$', views.GameLogView.as_view(), name='gamelog'),
    url(r'^gamelog/(?P<pk>[0-9]+)/$', views.GameView.as_view(), name='game'),
    url(r'^gamelog/add/$', views.add_game, name='add_game'),
    url(r'^gamelog/get_player_decks/(?P<player_id>[0-9]+)/$', views.get_player_decks, name='get_player_decks'),
    url(r'^stats/$', views.StatsView.as_view(), name='stats'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
