from django.db import models
from django.contrib.auth.models import AbstractUser

from shelf.models import Game

class Collection(models.Model):
    games = models.ManyToManyField(Game)

class ShelfUser(AbstractUser):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
