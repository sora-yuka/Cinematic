from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
<<<<<<< HEAD
        return request.user.is_staff and request.user.is_authenticated        
=======
        return request.user.is_staff
>>>>>>> 28f76ffc287dd02cff39f4d31921bc9d56fa10d8
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff and request.user.is_authenticated