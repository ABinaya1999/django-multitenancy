from django.contrib import admin
from .models import Client, Domain
from django_tenants.admin import TenantAdminMixin

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("name",)
    
    
@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ("domain","tenant")