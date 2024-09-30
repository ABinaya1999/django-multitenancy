from django.contrib import admin
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from shared.models import Client, Domain, Feature
from client.models import Employee


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'employee', 'department')
    

class AllTenantEmployeesAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        tenants = Client.objects.all()  # Assuming Client holds all tenant instances
        all_employees = []  # List to hold employees from all tenants
        
        # Loop through all tenants and fetch employees from their schemas
        for tenant in tenants:
            with schema_context(tenant.schema_name):  # Switch to the tenant's schema
                employees = Employee.objects.all()
                all_employees.extend(employees)
                
        # Since Django admin expects a queryset, you can't return a mixed list directly
        # However, you can customize how you display the data manually, e.g., in a template.
        return Employee.objects.none()  # Placeholder queryset to satisfy Django admin requirements
    
    # Customize the list display (adjust according to your Employee model fields)
    list_display = ['name', 'department']
    
    
class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.site_title = "Master Admin"
        self.site_header = "Master Admin"
        self.index_title = "Tenant"
        
        self.register(User)
        self.register(Client) 
        self.register(Domain) 
        self.register(Feature, FeatureAdmin) 
        self.register(Employee, AllTenantEmployeesAdmin)
        
        
tenant_admin_site = TenantAdminSite(name="tenant_admin_site")

