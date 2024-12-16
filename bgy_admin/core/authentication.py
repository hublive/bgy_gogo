from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

class CustomJWTAuthentication(JWTAuthentication):
    """自定义JWT认证"""
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except Exception as e:
            return None 