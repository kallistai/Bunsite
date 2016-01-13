from django import forms
from gamelog.models import Format, Location, Player


class GameForm(forms.Form):
    format = forms.ModelChoiceField(queryset=Format.objects.all(),
                                    empty_label='--Select Format--',
                                    required=True, label='Format:')
    location = forms.ModelChoiceField(queryset=Location.objects.all(),
                                      empty_label='--Select Location--',
                                      required=True, label='Location:')
    players = forms.ModelChoiceField(queryset=Player.objects.all(),
                                     empty_label='--Select Player--')
    player_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        player = kwargs.pop('player', 0)
        super(GameForm, self).__init__(*args, **kwargs)

        self.fields['player_count'].initial = player
        for i in range(int(player)):
            self.fields['player_{i}'.format(i=i)] = forms.CharField()
