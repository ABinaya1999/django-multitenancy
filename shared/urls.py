from django.urls import path
from shared.views import index, FeatureListAPIView, FeatureRetrieveAPIView
from shared.admin import tenant_admin_site


urlpatterns = [
    path('admin/', tenant_admin_site.urls),
    path("", index, name="index"),
    path("feature/", FeatureListAPIView.as_view(), name="features"),
    path("feature/<int:pk>", FeatureRetrieveAPIView.as_view(), name="feature")
    
]
