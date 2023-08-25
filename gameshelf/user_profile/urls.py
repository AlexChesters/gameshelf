from django.urls import path

from .views import auth

app_name = "user_profile"
urlpatterns = [
    path("profile", auth.user_profile, name="profile"),
    path("sign-in", auth.sign_in, name="sign_in")
]
