from django.urls import path
from django.contrib import admin
from client.views import index, EmployeeListAPIView, DepartmentListAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="client_index"),
    path("employee/", EmployeeListAPIView.as_view(), name="client_employee"),
    path("department/", DepartmentListAPIView.as_view(), name="client_department")
]
