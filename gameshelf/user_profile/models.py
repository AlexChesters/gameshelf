from django.db import models
from django.contrib.auth.models import User

from shelf.models import Game

class ShelfUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)
