from django.db.models import fields
from django.db.models.fields.files import FileField
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import transaction

from .models import Director, Filial, News
from .forms import NewsForm, DirectorForm, FilialForm
from .utils import parse_date_time


def index(request):
    filials = Filial.objects.all()
    context = {
        "filials": filials
    }
    return render(request, "simpleforms/list.html", context)


def create(request):
    director_form = DirectorForm()
    filial_form = FilialForm()

    if request.method == "POST":
        director_form = DirectorForm(request.POST)
        filial_form = FilialForm(request.POST)

        if director_form.is_valid() and filial_form.is_valid():
            filial = filial_form.save(commit=False)
            director = director_form.save(commit=False)

            director.filial = filial

            filial.save()
            director.save()

            return redirect(reverse("news-list"))

    context = {
        "filial_form": filial_form,
        "director_form": director_form
    }
    return render(request, "simpleforms/create.html", context)


def update(request, pk):
    try:
        filial = Filial.objects.get(id=pk)
    except:
        return redirect(reverse("news-list"))

    director_form = DirectorForm(instance=filial.director)
    filial_form = FilialForm(instance=filial)

    if request.method == "POST":
        director_form = DirectorForm(request.POST, instance=filial.director)
        filial_form = FilialForm(request.POST, instance=filial)

        if director_form.is_valid() and filial_form.is_valid():
            filial = filial_form.save(commit=False)
            director = director_form.save(commit=False)

            director.filial = filial

            filial.save()
            director.save()

            return redirect(reverse("news-list"))


    context = {
        "director_form": director_form,
        "filial_form": filial_form
    }
    return render(request, "simpleforms/update.html", context)


def delete(request, pk):
    try:
        Filial.objects.get(id=pk).delete()
    except:
        pass

    return redirect(reverse("news-list"))



def category_example_form(request):
    form = NewsForm()
    context = {
        "form": form
    }
    return render(request, "simpleforms/example.html", context)