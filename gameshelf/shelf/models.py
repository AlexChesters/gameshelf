from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
