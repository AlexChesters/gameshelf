import re

from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.db import transaction

from user_profile.models import ShelfUser
from shelf.models import Game

@login_required
def edit_order(request: HttpRequest, status: str):
    if request.method == "POST":
        form_rankings = {k: v for k, v in request.POST.dict().items() if k.startswith("game_ranking_")}
        form_ranking_regex = r"game_ranking_(?P<game_id>[0-9]+)"

        for form_ranking in form_rankings:
            game_id = re.search(form_ranking_regex, form_ranking).groupdict()["game_id"]
            game_ranking = form_rankings[form_ranking]
            with transaction.atomic():
                game = Game.objects.get(id=game_id)
                game.ranking = game_ranking
                game.save()

        return HttpResponseRedirect(reverse(f"shelf:{status}"))
    else:
        user: ShelfUser = ShelfUser.objects.get(id=request.user.id)

        context = {
            "games": user.collection.games.all().filter(status=status)
        }
        return render(request, "shelf/edit_order.html", context)
