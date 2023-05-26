from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("create-user/", views.create_user, name="create_user"),
    path("create-internal-user/", views.create_internal_user,
         name="create-internal-user"),
]
