from django.urls import path
from apps.users.api.api import UserAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="users_api"),
]
