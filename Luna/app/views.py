from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def home(request):
    context = {
        'current_page': 'home'
    }
    return render(request, "home.html", context)


def create(request):
    context = {
        'current_page': 'create'
    }
    return render(request, "create.html", context)


def edit(request):
    context = {
        'current_page': 'edit'
    }
    return render(request, "edit.html", context)


def view(request):
    context = {
        'users_list': User.objects.all(),
        'current_page': 'view'
    }
    return render(request, "view.html", context)
