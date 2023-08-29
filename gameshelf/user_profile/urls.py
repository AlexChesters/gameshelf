from django.urls import path

from .views import user_profile, edit_profile, sign_in, sign_up

app_name = "user_profile"
urlpatterns = [
    path("profile", user_profile, name="profile"),
    path("edit-profile", edit_profile, name="edit_profile"),
    path("sign-in", sign_in, name="sign_in"),
    path("sign-up", sign_up, name="sign_up")
]
