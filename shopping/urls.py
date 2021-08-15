from django.urls import path

from .views import *


urlpatterns = [
    path("add-cartitem/<int:cartitem_id>/", add_cartitem, name="add-cartitem"),
    path("subtract-cartitem/<int:cartitem_id>/", subtract_cartitem, name="subtract-cartitem"),
    path("remove-cartitem/<int:cartitem_id>/", remove_cartitem, name="remove-cartitem"),
    path("cart/", cart, name="cart"),
]