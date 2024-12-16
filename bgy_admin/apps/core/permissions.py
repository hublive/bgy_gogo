from rest_framework import permissions

class CustomPermission(permissions.BasePermission):
    """自定义权限基类"""
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return True 