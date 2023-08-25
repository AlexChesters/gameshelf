from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django import forms

from user_profile.models import ShelfUser

class AuthenticateForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

@login_required
def user_profile(request: HttpRequest):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_profile:sign_in'))
    else:
        context = {
            "username": request.user.username
        }
        return render(request, "user_profile/profile.html", context)

def sign_in(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user_profile:profile"))
        else:
            return HttpResponseRedirect(f"{reverse('user_profile:sign_up')}?reason=user_not_found")
    else:
        context = {
            "form": AuthenticateForm()
        }
        return render(request, "user_profile/sign_in.html", context)

def sign_up(request):
    if request.method == "POST":
        username = request.POST["user_name"]
        password = request.POST["password"]

        user = ShelfUser.objects.create_user(username=username, email=None, password=password)
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("user_profile:profile"))
    else:
        context = {
            "form": AuthenticateForm(),
            "user_not_found": request.GET.get("reason") == "user_not_found"
        }
        return render(request, "user_profile/sign_up.html", context)
