from django.urls import path

from .views import index

app_name = "shelf"
urlpatterns = [
    path("", index, name="index")
]
