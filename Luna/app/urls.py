from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("user/", views.user_post, name="user_post")
]
