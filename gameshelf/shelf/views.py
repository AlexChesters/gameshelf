from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from user_profile.models import ShelfUser

@login_required
def index(request: HttpRequest):
    user: ShelfUser = get_user_model()

    print(user.games.get())

    return render(request, "shelf/index.html")
