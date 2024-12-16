from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from utils.decorators import log_operation
from drf_spectacular.openapi.parameter import OpenApiParameter

from .serializers import DepartmentSerializer
from ..models import Department


@extend_schema_view(
    list=extend_schema(
        summary="获取部门列表",
        description="获取系统中的部门列表，支持分页、搜索和过滤",
        parameters=[
            OpenApiParameter(name='page', description='页码', required=False, type=int),
            OpenApiParameter(name='page_size', description='每页数量', required=False, type=int),
            OpenApiParameter(name='search', description='搜索关键词', required=False, type=str),
            OpenApiParameter(name='name', description='部门名称(模糊匹配)', required=False, type=str),
            OpenApiParameter(name='leader', description='负责人ID', required=False, type=int),
            OpenApiParameter(name='is_active', description='是否激活', required=False, type=bool),
            OpenApiParameter(name='created_at_after', description='创建时间起始', required=False, type=str, format='date'),
            OpenApiParameter(name='created_at_before', description='创建时间截止', required=False, type=str, format='date'),
            OpenApiParameter(name='ordering', description='排序字段', required=False, type=str),
        ],
        responses={200: DepartmentSerializer(many=True)}
    ),
    create=extend_schema(
        summary="创建部门",
        description="创建新部门",
        request=DepartmentSerializer,
        responses={201: DepartmentSerializer}
    ),
    retrieve=extend_schema(
        summary="获取部门详情",
        description="获取指定部门的详细信息",
        parameters=[
            OpenApiParameter(name='id', description='部门ID', required=True, type=int, location=OpenApiParameter.PATH)
        ],
        responses={200: DepartmentSerializer}
    ),
    update=extend_schema(
        summary="更新部门",
        description="更新指定部门的信息",
        parameters=[
            OpenApiParameter(name='id', description='部门ID', required=True, type=int, location=OpenApiParameter.PATH)
        ],
        request=DepartmentSerializer,
        responses={200: DepartmentSerializer}
    ),
    destroy=extend_schema(
        summary="删除部门",
        description="删除指定部门(需确保部门下没有子部门和用户)",
        parameters=[
            OpenApiParameter(name='id', description='部门ID', required=True, type=int, location=OpenApiParameter.PATH)
        ],
        responses={204: None}
    )
)
@extend_schema(tags=['部门管理'])
class DepartmentViewSet(viewsets.ModelViewSet):
    """部门管理视图集"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """获取查询集"""
        queryset = super().get_queryset()
        user = self.request.user
        
        if user.is_superuser:
            return queryset
            
        return queryset.filter(
            id__in=user.get_accessible_departments()
        )
    
    @log_operation('部门管理', '查询部门列表')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @log_operation('部门管理', '创建部门')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @log_operation('部门管理', '更新部门')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @log_operation('部门管理', '删除部门')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        summary="获取部门树",
        description="获取部门的树形结构数据",
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'description': '部门ID'},
                    'name': {'type': 'string', 'description': '部门名称'},
                    'children': {'type': 'array', 'description': '子部门列表'},
                }
            }
        }
    )
    @log_operation('部门管理', '获取部门树')
    @action(detail=False, methods=['get'])
    def tree(self, request):
        """获取部门树形结构"""
        return super().tree(request)

    @extend_schema(
        summary="获取部门用户",
        description="获取指定部门及其子部门的所有用户",
        parameters=[
            OpenApiParameter(name='id', description='部门ID', required=True, type=int, location=OpenApiParameter.PATH),
            OpenApiParameter(name='page', description='页码', required=False, type=int),
            OpenApiParameter(name='page_size', description='每页数量', required=False, type=int),
            OpenApiParameter(name='search', description='搜索关键词', required=False, type=str),
            OpenApiParameter(name='ordering', description='排序字段(username/date_joined)', required=False, type=str),
        ],
        responses={200: UserListSerializer(many=True)}
    )
    @log_operation('部门管理', '获取部门用户')
    @action(detail=True, methods=['get'])
    def users(self, request, pk=None):
        """获取部门用户列表"""
        return super().users(request, pk)

    @extend_schema(
        summary="导出部门",
        description="导出部门数据为Excel文件，包含：部门名称、父部门、负责人、排序号、状态、备注等信息",
        responses={
            200: {
                'type': 'string',
                'format': 'binary',
                'content': {
                    'application/vnd.ms-excel': {}
                }
            }
        }
    )
    @log_operation('部门管理', '导出部门')
    @action(detail=False, methods=['get'])
    def export(self, request):
        """导出部门数据"""
        return super().export(request)

    @extend_schema(
        summary="导入部门",
        description="""从Excel文件导入部门数据，支持以下功能：
        1. 批量创建部门
        2. 更新已存在的部门
        3. 自动处理部门层级关系
        
        Excel文件格式要求：
        - 必须包含列：部门名称、父部门、负责人、排序号、状态
        - 可选列：备注
        """,
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'file': {
                        'type': 'string',
                        'format': 'binary',
                        'description': 'Excel文件(.xlsx)'
                    }
                },
                'required': ['file']
            }
        },
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'success_count': {'type': 'integer', 'description': '成功导入数量'},
                    'error_count': {'type': 'integer', 'description': '失败数量'},
                    'error_msgs': {'type': 'array', 'items': {'type': 'string'}, 'description': '错误信息列表'}
                }
            }
        }
    )
    @log_operation('部门管理', '导入部门')
    @action(detail=False, methods=['post'], parser_classes=[MultiPartParser])
    def import_departments(self, request):
        """导入部门数据"""
        return super().import_departments(request)

    @extend_schema(
        summary="部门统计",
        description="""获取部门相关的统计数据，包括：
        1. 部门总数和活跃部门数
        2. 各层级部门数量分布
        3. 人员最多的前5个部门
        4. 最近30天新增部门趋势
        """,
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'overview': {
                        'type': 'object',
                        'properties': {
                            'total_departments': {'type': 'integer', 'description': '部门总数'},
                            'active_departments': {'type': 'integer', 'description': '活跃部门数'}
                        }
                    },
                    'level_distribution': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'level': {'type': 'integer', 'description': '层级'},
                                'count': {'type': 'integer', 'description': '数量'}
                            }
                        }
                    },
                    'top_departments': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'name': {'type': 'string', 'description': '部门名称'},
                                'member_count': {'type': 'integer', 'description': '人员数量'}
                            }
                        }
                    },
                    'daily_new_departments': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'date': {'type': 'string', 'format': 'date', 'description': '日期'},
                                'count': {'type': 'integer', 'description': '新增数量'}
                            }
                        }
                    }
                }
            }
        }
    )
    @log_operation('部门管理', '部门统计')
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """获取部门统计数据"""
        return super().statistics(request)