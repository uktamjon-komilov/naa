from django.urls import path
from .views import home, single_music


urlpatterns = [
    path("", home),
    path("1/", single_music),
]