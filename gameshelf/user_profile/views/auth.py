from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms

class SignInForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

@login_required
def user_profile(request):
    return render(request, "user_profile/index.html")

def sign_in(request):
    context = {
        "form": SignInForm()
    }
    return render(request, "user_profile/sign_in.html", context)
