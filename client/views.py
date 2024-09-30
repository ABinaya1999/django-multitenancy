from django.http import HttpResponse
from .models import Employee, Department
from client.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.generics import ListAPIView
from shared.permissions import FeatureAccessPermissions

# Create your views here.

def index(request):
    return HttpResponse(f"<p>Hello, {request.tenant}</p>")


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    feature_flag = 'employee' 
    permission_classes = [FeatureAccessPermissions]


class DepartmentListAPIView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    feature_flag = 'department' 
    permission_classes = [FeatureAccessPermissions]
