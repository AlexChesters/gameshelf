from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from user_profile.models import ShelfUser
from shelf.models import Game
from shelf.views.forms.game_form import GameForm

@login_required
def edit_a_game(request: HttpRequest, game_id):
    if request.method == "POST":
        if "save" in request.POST:
            user: ShelfUser = request.user

            game = Game.objects.get(id=game_id)

            game.platform = request.POST["platform"]
            game.release_date = request.POST["release_date"] or None
            game.status = request.POST["status"]
            game.rating = request.POST["rating"]
            game.save()

            user.collection.games.add(game)
            user.save()

            return HttpResponseRedirect(reverse(f"shelf:{game.status}"))
        elif "delete" in request.POST:
            game = Game.objects.get(id=game_id)
            status_to_redirect_to = game.status
            game.delete()

            return HttpResponseRedirect(reverse(f"shelf:{status_to_redirect_to}"))
    else:
        game = get_object_or_404(Game, pk=game_id)
        context = {
            "form": GameForm(
                initial={
                    "title": game.title,
                    "release_date": game.release_date,
                    "platform": game.platform,
                    "status": game.status,
                    "rating": game.rating
                },
                disable_title=True
            ),
            "game": game
        }
        return render(request, "shelf/edit_a_game.html", context)
