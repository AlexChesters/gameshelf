import datetime

from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from user_profile.models import ShelfUser
from shelf.models import Game, game_platforms, game_ratings, game_statuses

@login_required
def edit_a_game(request: HttpRequest, game_id):
    # TODO: add back support for deleting
    # game = Game.objects.get(id=game_id)
    # status_to_redirect_to = game.status
    # game.delete()

    # return HttpResponseRedirect(reverse(f"shelf:{status_to_redirect_to}"))
    if request.method == "POST":
        user: ShelfUser = request.user

        game = Game.objects.get(id=game_id)

        print(request.POST["release_date"])

        game.title = request.POST["title"]
        game.platform = request.POST["platform"] or None
        game.release_date = request.POST["release_date"] or None
        game.status = request.POST["status"]
        game.rating = request.POST["rating"] or None
        game.save()

        user.collection.games.add(game)
        user.save()

        return HttpResponseRedirect(reverse(f"shelf:{game.status}"))

    else:
        game = get_object_or_404(Game, pk=game_id)

        release_date_str = datetime.datetime.strftime(game.release_date, "%Y-%m-%d")

        context = {
            "game": game,
            "release_date_str": release_date_str,
            "platforms": game_platforms,
            "statuses": game_statuses,
            "ratings": game_ratings
        }
        return render(request, "shelf/edit_a_game.html", context)
