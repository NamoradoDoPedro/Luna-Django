from django.shortcuts import render
from .models import User


def home(request):
    context = {}
    return render(request, "home.html", context)


def create(request):
    context = {}
    return render(request, "create.html", context)


def view(request):
    users_list = {
        'users_list': User.objects.all(),
    }
    return render(request, "view.html", users_list)


def user_post(request):
    new_user = User()
    new_user.name = request.POST.get("name")
    new_user.email = request.POST.get("email")
    new_user.age = request.POST.get("age")
    new_user.sex = request.POST.get("sex")
    new_user.save()

    return render(request, "create.html")
