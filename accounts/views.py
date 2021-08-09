from django.shortcuts import render


def register(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)
        if email and password1 == password2:
            print("Ok")
        else:
            print(":((")

    return render(request, "learning.html")