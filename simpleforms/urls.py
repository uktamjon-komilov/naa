from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="news-list"),
    path("create/", views.create, name="news-create"),
    path("update/<int:pk>/", views.update, name="news-update"),
    path("delete/<int:pk>/", views.delete, name="news-delete"),

    path("example/", views.category_example_form, name="example-form")
]