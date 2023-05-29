from django.urls import path, include
from . import api_methods

urlpatterns = [
    path("get-user/", api_methods.get_user),
    path("post-user/", api_methods.post_user),
    path("delete-user/<int:id>/", api_methods.delete_user),
    path("get-by-id-user/<int:id>/", api_methods.get_user_by_id),
    path("put-user/<int:id>/", api_methods.put_user),
]
