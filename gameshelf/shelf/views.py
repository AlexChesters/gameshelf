from django.shortcuts import render, get_object_or_404
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
        "games": user.collection.games.all()
    }
    return render(request, "shelf/index.html", context)

@login_required
def add_a_game(request: HttpRequest):
    if request.method == "POST":
        user: ShelfUser = ShelfUser.objects.get(id=request.user.id)

        game, _ = Game.objects.get_or_create(
            title=request.POST["title"],
            platform=request.POST["platform"]
        )

        user.collection.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse("shelf:index"))
    else:
        context = {
            "form": GameForm()
        }
        return render(request, "shelf/add_a_game.html", context)

@login_required
def edit_a_game(request: HttpRequest, game_id):
    if request.method == "POST":
        user: ShelfUser = request.user

        game = Game(
            title=request.POST["title"],
            platform=request.POST["platform"]
        )

        game.save()
        user.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse("shelf:index"))
    else:
        game = get_object_or_404(Game, pk=game_id)
        context = {
            "form": GameForm(initial={"title": game.title, "platform": game.platform})
        }
        return render(request, "shelf/add_a_game.html", context)
