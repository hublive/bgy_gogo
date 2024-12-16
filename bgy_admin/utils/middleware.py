from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied
from utils.cache import DepartmentPermissionCache
from loguru import logger

class DepartmentPermissionMiddleware(MiddlewareMixin):
    """部门权限中间件
    
    用于检查用户是否有权限访问指定部门的数据
    
    实现以下功能:
    1. 自动检查部门访问权限
    2. 支持权限继承
    3. 支持数据权限过滤
    """

    def process_request(self, request):
        """处理请求
        
        检查用户是否有权限访问当前部门数据
        """
        # 跳过不需要验证的路径
        if not self._need_check(request):
            return None
            
        try:
            # 获取当前用户
            user = request.user
            if not user.is_authenticated:
                return None
                
            # 获取请求的部门ID
            department_id = self._get_department_id(request)
            if not department_id:
                return None
                
            # 检查用户是否有权限访问该部门
            if not self._has_department_permission(user, department_id):
                raise PermissionDenied("没有权限访问该部门数据")
                
        except Exception as e:
            logger.error(f"部门权限检查失败: {str(e)}")
            raise PermissionDenied("部门权限检查失败")

    def _need_check(self, request):
        """判断是否需要检查权限"""
        # 排除不需要检查的路径
        exclude_paths = [
            '/api/auth/',
            '/api/docs/',
            '/admin/',
            '/static/',
            '/media/'
        ]
        
        path = request.path_info
        return not any(path.startswith(p) for p in exclude_paths)

    def _get_department_id(self, request):
        """获取请求的部门ID"""
        # 从URL参数获取
        department_id = request.GET.get('department')
        if department_id:
            return int(department_id)
            
        # 从请求体获取
        if request.method in ['POST', 'PUT', 'PATCH']:
            department_id = request.data.get('department')
            if department_id:
                return int(department_id)
                
        return None

    def _has_department_permission(self, user, department_id):
        """检查用户是否有权限访���部门"""
        # 超级管理员拥有所有权限
        if user.is_superuser:
            return True
            
        # 获取用户角色
        if not user.role:
            return False
            
        # 获取部门权限
        permissions = DepartmentPermissionCache.get_permissions(department_id)
        
        # 检查直接权限
        for perm in permissions['direct_permissions']:
            if perm['role_id'] == user.role.id:
                return True
                
        # 检查继承的权限
        for perm in permissions['inherited_permissions']:
            if perm['role_id'] == user.role.id and perm['inherit']:
                return True
                
        return False 