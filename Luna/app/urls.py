from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("edit/", views.edit, name="edit"),
    path("/*", views.edit, name="edit"),
]
