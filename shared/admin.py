from django.contrib import admin
from django.contrib.auth.models import User
from django_tenants.utils import schema_context
from shared.models import Client, Domain, Feature
from client.models import Employee


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'employee', 'department')
    
    
    
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
        
        
tenant_admin_site = TenantAdminSite(name="tenant_admin_site")

