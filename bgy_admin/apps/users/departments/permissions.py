from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    """
    部门管理员权限
    
    检查用户是否有权限管理指定的部门
    """
    
    def has_permission(self, request, view):
        """
        检查用户是否有部门管理权限
        """
        return request.user and request.user.has_perm('departments.manage_department')
    
    def has_object_permission(self, request, view, obj):
        """
        检查用户是否有管理特定部门的权限
        """
        if request.user.is_superuser:
            return True
            
        if request.method in permissions.SAFE_METHODS:
            return obj.id in request.user.get_accessible_departments()
            
        return obj.id in request.user.get_manageable_departments() 