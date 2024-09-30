from django.urls import path
from shared.views import index
from shared.admin import tenant_admin_site


urlpatterns = [
    path('admin/', tenant_admin_site.urls),
    path("", index, name="index"),
]
