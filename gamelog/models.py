from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Format(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    created_date = models.DateTimeField(editable=False, default=timezone.now())
    updated_date = models.DateTimeField(editable=False)

    def save(self):
        self.updated_date = timezone.now()
        return super(Player, self).save()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Deck(models.Model):
    name = models.CharField(max_length=50)
    format = models.ForeignKey(Format)
    web_link = models.CharField(max_length=100)
    player = models.ForeignKey(Player, null=True)
    
    def __str__(self):
        return self.format.name + ": " + self.name
    
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
   

class Game(models.Model):
    players = models.ManyToManyField(Player, related_name='players')
    location = models.ForeignKey(Location)
    format = models.ForeignKey(Format)
    created_date = models.DateTimeField(editable=False, default=timezone.now())
    updated_date = models.DateTimeField(editable=False)
    winner = models.ForeignKey(Player, related_name='winner', null=True)
    
    def save(self):
        self.updated_date = timezone.now()
        return super(Game, self).save()

