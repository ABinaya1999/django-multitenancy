from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    
class Domain(DomainMixin):
    pass

class Feature(models.Model):
    tenant = models.OneToOneField(Client, on_delete=models.CASCADE)
    employee = models.BooleanField(default=False)
    department = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Features for {self.tenant.name}"