from django.conf.urls import url

from . import views

app_name = 'gamelog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^gamelog/$', views.GameLogView.as_view(), name='gamelog'),
    url(r'^gamelog/(?P<pk>[0-9]+)/$', views.GameView.as_view(), name='game'),
    url(r'^gamelog/add/$', views.add_game, name='add_game'),
    url(r'^stats/$', views.StatsView.as_view(), name='stats'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
]
