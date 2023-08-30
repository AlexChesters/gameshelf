from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Max
from django.urls import reverse

from user_profile.models import ShelfUser
from shelf.models import Game
from shelf.views.forms.game_form import GameForm

@login_required
def add_a_game(request: HttpRequest):
    if request.method == "POST":
        user: ShelfUser = ShelfUser.objects.get(id=request.user.id)

        game, _ = Game.objects.get_or_create(
            title=request.POST["title"],
            release_date=request.POST["release_date"] or None,
            platform=request.POST["platform"],
            status=request.POST["status"],
            rating=request.POST["rating"],
            ranking=Game.objects.aggregate(Max("ranking"))["ranking__max"] + 1
        )

        user.collection.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse("shelf:add_a_game"))
    else:
        context = {
            "form": GameForm()
        }
        return render(request, "shelf/add_a_game.html", context)
