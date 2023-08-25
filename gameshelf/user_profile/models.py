from django.db import models
from django.contrib.auth.models import AbstractUser

from shelf.models import Game

class ShelfUser(AbstractUser):
    games = models.ManyToManyField(Game)
