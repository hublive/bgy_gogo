import traceback
from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from loguru import logger

from apps.monitor.models import OperationLog
from utils.cache import DepartmentPermissionCache


def department_permission_required(permission_code):
    """部门权限装饰器
    
    用于检查用户是否有指定的部门权限
    
    Args:
        permission_code: 权限代码,如 'departments.view_department'
        
    Usage:
        @department_permission_required('departments.view_department')
        def my_view(request):
            ...
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                # 获取当前用户
                user = request.user
                if not user.is_authenticated:
                    raise PermissionDenied("请先登录")

                # 超级管理员拥有所有权限
                if user.is_superuser:
                    return view_func(request, *args, **kwargs)

                # 获取用户角色
                if not user.role:
                    raise PermissionDenied("用户未分配角色")

                # 获取部门ID
                department_id = kwargs.get('pk') or request.GET.get('department')
                if not department_id:
                    raise PermissionDenied("未指定部门")

                # 获取部门权限
                permissions = DepartmentPermissionCache.get_permissions(department_id)

                # 检查是否有权限
                has_permission = False

                # 检查直接权限
                for perm in permissions['direct_permissions']:
                    if (perm['role_id'] == user.role.id and
                            permission_code in perm['permissions']):
                        has_permission = True
                        break

                # 检查继承的权限
                if not has_permission:
                    for perm in permissions['inherited_permissions']:
                        if (perm['role_id'] == user.role.id and
                                permission_code in perm['permissions'] and
                                perm['inherit']):
                            has_permission = True
                            break

                if not has_permission:
                    raise PermissionDenied("没有操作权限")

                return view_func(request, *args, **kwargs)

            except Exception as e:
                logger.error(f"权限检查失败: {str(e)}")
                raise PermissionDenied("权限检查失败")

        return _wrapped_view

    return decorator


def department_filter_required():
    """部门数据过滤装饰器
    
    用于过滤用户有权限访问的部门数据
    
    Usage:
        @department_filter_required()
        def my_view(request):
            ...
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            try:
                # 获取当前用户
                user = request.user
                if not user.is_authenticated:
                    raise PermissionDenied("请先登录")

                # 超级管理员可以访问所有数据
                if user.is_superuser:
                    return view_func(request, *args, **kwargs)

                # 获取用户角色
                if not user.role:
                    raise PermissionDenied("用户未分配角色")

                # 获取用户可访问的部门ID列表
                accessible_departments = []

                # 获取用户所在部门及其子部门
                if user.department:
                    accessible_departments.append(user.department.id)
                    accessible_departments.extend(
                        [d.id for d in user.department.get_descendants()]
                    )

                # 获取用户有权限的其他部门
                from apps.users.models import Department
                for dept in Department.objects.all():
                    if dept.id not in accessible_departments:
                        permissions = DepartmentPermissionCache.get_permissions(dept.id)
                        for perm in permissions['direct_permissions']:
                            if perm['role_id'] == user.role.id:
                                accessible_departments.append(dept.id)
                                break

                # 将可访问的部门ID列表添加到请求中
                request.accessible_departments = accessible_departments

                return view_func(request, *args, **kwargs)

            except Exception as e:
                logger.error(f"数据过滤失败: {str(e)}")
                raise PermissionDenied("数据过滤失败")

        return _wrapped_view

    return decorator


def log_operation(module_name, action):
    """操作日志装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            start_time = timezone.now()
            response = None
            status = 1
            error_msg = ''
            
            # 构建基础日志信息
            log_info = {
                'user': request.user.username if request.user.is_authenticated else 'anonymous',
                'module': module_name,
                'action': action,
                'method': request.method,
                'path': request.path,
                'ip': request.META.get('REMOTE_ADDR'),
                'params': str(request.data if hasattr(request, 'data') else request.GET)
            }
            
            try:
                response = func(self, request, *args, **kwargs)
                duration = (timezone.now() - start_time).total_seconds()
                
                # 记录响应结果
                log_info.update({
                    'status': 'SUCCESS',
                    'result': str(response.data if hasattr(response, 'data') else response),
                    'duration': duration
                })
                
                # 打印成功日志
                success_msg = (
                    f"[操作日志] "
                    f"用户:{log_info['user']} "
                    f"模块:{log_info['module']} "
                    f"操作:{log_info['action']} "
                    f"方法:{log_info['method']} "
                    f"路径:{log_info['path']} "
                    f"IP:{log_info['ip']} "
                    f"参数:{log_info['params']} "
                    f"状态:成功 "
                    f"耗时:{duration:.3f}秒"
                )
                
                # 使用 loguru 记录日志
                logger.info(success_msg)
                
                # 记录到数据库
                OperationLog.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    module=module_name,
                    action=action,
                    method=request.method,
                    path=request.path,
                    ip_addr=log_info['ip'],
                    location='',
                    browser='',
                    os='',
                    status=status,
                    params=log_info['params'],
                    result=log_info['result'],
                    duration=duration,
                    elapsed_time=int(duration * 1000),
                    error_msg=''
                )
                
                return response
                
            except Exception as e:
                status = 0
                error_msg = str(e)
                duration = (timezone.now() - start_time).total_seconds()
                
                # 记录错误信息
                log_info.update({
                    'status': 'FAILED',
                    'result': error_msg,
                    'duration': duration,
                    'traceback': traceback.format_exc()
                })
                
                # 打印错误日志
                error_msg = (
                    f"[错误日志] "
                    f"用户:{log_info['user']} "
                    f"模块:{log_info['module']} "
                    f"操作:{log_info['action']} "
                    f"方法:{log_info['method']} "
                    f"路径:{log_info['path']} "
                    f"IP:{log_info['ip']} "
                    f"参数:{log_info['params']} "
                    f"状态:失败 "
                    f"耗时:{duration:.3f}秒 "
                    f"错误:{error_msg}"
                )
                
                # 使用 loguru 记录错误日志
                logger.error(error_msg)
                logger.error(f"详细错误信息:\n{log_info['traceback']}")
                
                # 记录到数据库
                try:
                    OperationLog.objects.create(
                        user=request.user if request.user.is_authenticated else None,
                        module=module_name,
                        action=action,
                        method=request.method,
                        path=request.path,
                        ip_addr=log_info['ip'],
                        location='',
                        browser='',
                        os='',
                        status=status,
                        params=log_info['params'],
                        result=error_msg,
                        duration=duration,
                        elapsed_time=int(duration * 1000),
                        error_msg=error_msg
                    )
                except Exception as db_e:
                    logger.error(f"记录操作日志到数据库失败: {str(db_e)}")
                
                raise
                
        return wrapper
    return decorator
