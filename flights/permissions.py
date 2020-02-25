from rest_framework.permissions import BasePermission
from django.utils import timezone
import datetime

class IsOwnerOrStaff(BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.user.is_staff or request.user == obj.user:
            return True
        return False

class ThreeDays(BasePermission):
    def has_object_permission(self,request,view,obj):
        if (obj.date - timezone.now().date()).days > 3:
            return True
        return False
