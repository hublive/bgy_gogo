from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, DepartmentViewSet, LoginViewSet
from apps.system.views import RoleViewSet

# 创建路由器
router = DefaultRouter()
router.register(r'auth', LoginViewSet, basename='auth')
router.register(r'users', UserViewSet, basename='users')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'roles', RoleViewSet, basename='roles')

urlpatterns = [
    path('admin/', admin.site.urls),
    # 应用路由
    path('api/users/', include('apps.users.urls')),
    path('api/system/', include('apps.system.urls')),
    path('api/monitor/', include('apps.monitor.urls')),
    # API文档
    path('api/schema/', SpectacularAPIView.as_view(
        permission_classes=[],
        authentication_classes=[]
    ), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # 视图集路由
    path('api/', include(router.urls)),
]

# 开发环境下添加媒体文件路由
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 