from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="bosh-sahifa"),
    path("one/", single, name="single-sahifa"),
]