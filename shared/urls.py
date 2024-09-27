from django.urls import path
from shared.views import index


urlpatterns = [
    path("", index, name="index"),
]
