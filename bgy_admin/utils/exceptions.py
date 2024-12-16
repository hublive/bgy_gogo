from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from loguru import logger

def custom_exception_handler(exc, context):
    """自定义异常处理器
    
    处理 DRF 的异常，返回统一的响应格式
    """
    # 先调用 REST framework 的默认异常处理
    response = exception_handler(exc, context)
    
    # 记录异常信息
    logger.error(f"发生异常: {exc}, 上下文信息: {context}")
    
    if response is None:
        if isinstance(exc, DjangoValidationError):
            response = Response({
                'code': status.HTTP_400_BAD_REQUEST,
                'message': str(exc),
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response({
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': '服务器内部错误',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # 处理 JWT Token 相关异常
        if isinstance(exc, (TokenError, InvalidToken)):
            response.data = {
                'code': status.HTTP_401_UNAUTHORIZED,
                'message': 'Token无效或已过期',
                'data': None
            }
            response.status_code = status.HTTP_401_UNAUTHORIZED
        # 处理验证错误
        elif isinstance(exc, DRFValidationError):
            response.data = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': exc.detail.get('message', '请求参数错误'),
                'data': None
            }
            response.status_code = status.HTTP_400_BAD_REQUEST
        # 处理其他异常
        else:
            response.data = {
                'code': response.status_code,
                'message': response.data.get('detail', '未知错误'),
                'data': None
            }
    
    return response 