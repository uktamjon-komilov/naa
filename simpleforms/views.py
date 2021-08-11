from django.db.models import fields
from django.db.models.fields.files import FileField
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import transaction

from .models import Category, Director, Filial, News
from .forms import NewsForm
from .utils import parse_date_time


def index(request):
    filials = Filial.objects.all()
    context = {
        "filials": filials
    }
    return render(request, "simpleforms/list.html", context)


def create(request):
    if request.method == "POST":
        title = request.POST.get("title", None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        director = request.POST.get("director", None)
        experience = request.POST.get("experience", None)

        with transaction.atomic():
            f = Filial(
                title=title,
                established_at=parse_date_time(date, time)
            )
            f.save()

            d = Director(
                fullname=director,
                experience=experience,
                filial=f
            )
            d.save()

        return redirect(reverse("news-list"))

    context = {}
    return render(request, "simpleforms/create.html", context)


def update(request, pk):
    try:
        filial = Filial.objects.get(id=pk)
        date = filial.established_at.strftime("%Y-%m-%d")
        time = filial.established_at.strftime("%H:%M")
    except:
        return redirect(reverse("news-list"))

    if request.method == "POST":
        title = request.POST.get("title", None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        director = request.POST.get("director", None)
        experience = request.POST.get("experience", None)

        with transaction.atomic():
            filial.title = title
            filial.established_at=parse_date_time(date, time)
            filial.director.fullname = director
            filial.director.experience = experience
            filial.save()
            filial.director.save()

        return redirect(reverse("news-list"))

    context = {
        "filial": filial,
        "date": date,
        "time": time
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