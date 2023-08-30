from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user_profile.models import ShelfUser

@login_required
def unplayed_games(request: HttpRequest):
    user: ShelfUser = request.user

    games = user.collection.games.all().filter(status="unplayed")

    context = {
        "games": games
    }
    return render(request, "shelf/games/unplayed.html", context)
