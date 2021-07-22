from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="home-page"),

    path("store/", store, name="store-page"),
    path("store/<slug:category_slug>/", category_products, name="category-products-page"),
    path("store/<slug:category_slug>/<slug:sub_category_slug>", sub_category_products, name="subcategory-products-page"),

    path("product/<slug:slug>/", product_detail, name="product-detail")
]