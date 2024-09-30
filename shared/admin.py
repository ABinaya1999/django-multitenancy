from django.contrib import admin
from django.contrib.auth.models import User
from shared.models import Client, Domain, Feature


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
