from django.contrib import admin
from .models import Game, Player, Location, Format, Deck


class DeckInLine(admin.TabularInline):
    model = Deck
    extra = 3


class PlayerAdmin(admin.ModelAdmin):
    inlines = [DeckInLine]


admin.site.register(Location)
admin.site.register(Format)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game)
admin.site.register(Deck)
