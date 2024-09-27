from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def index(request):
    return HttpResponse(f"<p>Hello, {request.tenant}</p>")

def employee(request):
    employees = Employee.objects.all()
    return render(request, "employee.html", {"employees":employees})