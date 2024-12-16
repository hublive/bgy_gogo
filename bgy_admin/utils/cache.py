from django.core.cache import cache
from django.conf import settings

class DepartmentPermissionCache:
    """部门权限缓存
    
    用于缓存部门的权限配置,提高访问性能
    
    使用 Redis 作为缓存后端,支持以下功能:
    1. 缓存部门的直接权限
    2. 缓存部门继承的权限
    3. 自动清理过期缓存
    """

    @staticmethod
    def get_cache_key(department_id):
        """获取缓存键名"""
        return f'dept_perms_{department_id}'

    @staticmethod
    def get_permissions(department_id):
        """获取部门权限
        
        先从缓存获取,如果没有则从数据库获取并缓存
        
        Args:
            department_id: 部门ID
            
        Returns:
            包含直接权限和继承权限的字典
        """
        cache_key = DepartmentPermissionCache.get_cache_key(department_id)
        
        # 尝试从缓存获取
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data
            
        # 从数据库获取
        from apps.users.models import DepartmentPermission, Department
        
        department = Department.objects.get(id=department_id)
        
        # 获取直接权限
        direct_permissions = DepartmentPermission.objects.filter(
            department=department
        ).select_related('role')
        
        # 获取继承的权限
        inherited_permissions = []
        if department.parent:
            inherited_permissions = DepartmentPermission.objects.filter(
                department=department.parent,
                inherit=True
            ).select_related('role')
        
        # 构造缓存数据
        permissions_data = {
            'direct_permissions': [
                {
                    'role_id': perm.role_id,
                    'permissions': perm.permissions,
                    'inherit': perm.inherit
                }
                for perm in direct_permissions
            ],
            'inherited_permissions': [
                {
                    'role_id': perm.role_id,
                    'permissions': perm.permissions,
                    'inherit': perm.inherit
                }
                for perm in inherited_permissions
            ]
        }
        
        # 设置缓存
        cache.set(
            cache_key,
            permissions_data,
            timeout=getattr(settings, 'DEPARTMENT_PERMISSIONS_CACHE_TIMEOUT', 3600)
        )
        
        return permissions_data

    @staticmethod
    def clear_permissions(department_id):
        """清除部门权限缓存"""
        cache_key = DepartmentPermissionCache.get_cache_key(department_id)
        cache.delete(cache_key)

    @staticmethod
    def clear_tree_permissions(department):
        """清除部门及其所有子部门的权限缓存"""
        # 清除当前部门的缓存
        DepartmentPermissionCache.clear_permissions(department.id)
        
        # 清除所有子部门的缓存
        for child in department.get_descendants():
            DepartmentPermissionCache.clear_permissions(child.id) 