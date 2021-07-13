from django.http import HttpResponse


def home(request):
    return HttpResponse("Barcha musiqalar")

def single_music(request):
    return HttpResponse("Bitta qo'shiq")