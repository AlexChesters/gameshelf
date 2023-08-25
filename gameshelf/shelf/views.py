from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

from user_profile.models import ShelfUser

@login_required
def index(request: HttpRequest):
    user: ShelfUser = request.user

    print(user.games.all())

    return render(request, "shelf/index.html")
