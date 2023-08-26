from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django import forms

from user_profile.models import ShelfUser
from shelf.models import Game, game_platforms, game_statuses

class GameForm(forms.Form):
    title = forms.CharField(max_length=200)
    platform = forms.ChoiceField(choices=game_platforms)
    status = forms.ChoiceField(choices=game_statuses)

    def __init__(self, *args, **kwargs):
        disable_title = kwargs.pop("disable_title", None)
        super(GameForm, self).__init__(*args, **kwargs)

        if disable_title:
            self.fields["title"].disabled = True

@login_required
def unplayed_games(request: HttpRequest):
    user: ShelfUser = request.user

    games = user.collection.games.all().filter(status="unplayed")

    context = {
        "games": games
    }
    return render(request, "shelf/games/unplayed.html", context)

@login_required
def currently_playing_games(request: HttpRequest):
    user: ShelfUser = request.user

    games = user.collection.games.all().filter(status="playing")

    context = {
        "games": games
    }
    return render(request, "shelf/games/playing.html", context)

@login_required
def completed_games(request: HttpRequest):
    user: ShelfUser = request.user

    games = user.collection.games.all().filter(status="completed")

    context = {
        "games": games
    }
    return render(request, "shelf/games/completed.html", context)

@login_required
def add_a_game(request: HttpRequest):
    if request.method == "POST":
        user: ShelfUser = ShelfUser.objects.get(id=request.user.id)

        game, _ = Game.objects.get_or_create(
            title=request.POST["title"],
            platform=request.POST["platform"],
            status=request.POST["status"]
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

        game = Game.objects.get(id=game_id)

        game.platform = request.POST["platform"]
        game.status = request.POST["status"]
        game.save()

        user.collection.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse("shelf:index"))
    else:
        game = get_object_or_404(Game, pk=game_id)
        context = {
            "form": GameForm(
                initial={
                    "title": game.title,
                    "platform": game.platform,
                    "status": game.status
                },
                disable_title=True
            )
        }
        return render(request, "shelf/add_a_game.html", context)
