from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from user_profile.models import ShelfUser

@login_required
def wishlist_games(request: HttpRequest):
    user: ShelfUser = request.user

    games = user.collection.games.all().filter(status="wishlist")

    context = {
        "games": games
    }
    return render(request, "shelf/games/wishlist.html", context)
