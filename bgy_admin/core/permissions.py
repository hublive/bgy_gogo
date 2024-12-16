from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    """基于角色的权限控制"""
    
    def has_permission(self, request, view):
        # 超级管理员拥有所有权限
        if request.user.is_superuser:
            return True
            
        # 获取当前用户的角色
        if not hasattr(request.user, 'role'):
            return False
            
        # 检查角色是否有对应权限
        required_perm = f"{view.__class__.__name__}.{request.method.lower()}"
        return request.user.role.permissions.filter(codename=required_perm).exists() 