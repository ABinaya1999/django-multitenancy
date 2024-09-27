from django.urls import path
from django.contrib import admin
from client.views import index, employee


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="client_index"),
    path("employee/", employee, name="client_employee")
]
