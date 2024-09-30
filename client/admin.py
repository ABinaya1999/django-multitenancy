from django.contrib import admin
from client.models import Employee, Department
# Register your models here.

admin.site.site_title = "Tenant Admin"
admin.site.site_header = "Tenant Admin"
admin.site.index_title = "Tenant"

admin.site.register(Employee)
admin.site.register(Department)