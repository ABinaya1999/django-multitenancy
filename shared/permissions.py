from rest_framework.permissions import BasePermission
from shared.models import Feature

class FeatureAccessPermissions(BasePermission):
    message = 'Access to this API is restricted for your tenant.'
    
    def has_permission(self, request, view):
        tenant = request.tenant
        feature_name = getattr(view, "feature_flag", None)
        if feature_name:
            try:
                feature = Feature.objects.get(tenant=tenant)
                return getattr(feature, feature_name, False)
            except Feature.DoesNotExist:
                return False
        return True  