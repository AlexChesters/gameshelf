from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django import forms

from user_profile.models import ShelfUser
from shelf.models import Game, game_platforms

class GameForm(forms.Form):
    title = forms.CharField(max_length=200)
    platform = forms.ChoiceField(choices=game_platforms)

@login_required
def index(request: HttpRequest):
    user: ShelfUser = request.user

    context = {
        "games": user.games.all()
    }
    return render(request, "shelf/index.html", context)

@login_required
def add_a_game(request: HttpRequest):
    if request.method == "POST":
        print(request.POST["title"])
        user: ShelfUser = request.user

        game = Game(title=request.POST["title"])
        game.save()
        user.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse("shelf:index"))
    else:
        context = {
            "form": GameForm()
        }
        return render(request, "shelf/add_a_game.html", context)
