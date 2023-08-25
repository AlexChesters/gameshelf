from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.urls import reverse
from django import forms

class AuthenticateForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

@login_required
def user_profile(request):
    context = {
        "username": request.user.username
    }
    return render(request, "user_profile/index.html", context)

def sign_in(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user_profile:profile"))
        else:
            return HttpResponseRedirect(reverse("user_profile:sign_up"))
    else:
        context = {
            "form": AuthenticateForm()
        }
        return render(request, "user_profile/sign_in.html", context)

def sign_up(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, email=None, password=password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("user_profile:profile"))
    else:
        context = {
            "form": AuthenticateForm()
        }
        return render(request, "user_profile/sign_up.html", context)
