
from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission to allow access only to the owner of the object or staff members.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS (e.g., GET, HEAD, OPTIONS) are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Admin users have full access
        if request.user.is_staff:
            return True
            
        # Check for ownership based on model type
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'created_by'):
            return obj.created_by == request.user

        # Default to denying permission if no ownership attribute is found
        return False