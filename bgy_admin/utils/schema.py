from drf_spectacular.drainage import warn
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes

def preprocessing_filter_spec(endpoints):
    """预处理钩子"""
    return endpoints

def postprocessing_filter_spec(result, generator, request, public):
    """后处理钩子，添加自定义响应格式"""
    # 添加通用响应格式
    result['components']['schemas']['CommonResponse'] = {
        'type': 'object',
        'properties': {
            'code': {'type': 'integer', 'example': 200},
            'message': {'type': 'string', 'example': 'success'},
            'data': {'type': 'object', 'nullable': True}
        }
    }

    # 添加Token响应格式
    result['components']['schemas']['TokenResponse'] = {
        'type': 'object',
        'properties': {
            'code': {'type': 'integer', 'example': 200},
            'message': {'type': 'string', 'example': 'success'},
            'data': {
                'type': 'object',
                'properties': {
                    'access_token': {'type': 'string'},
                    'refresh_token': {'type': 'string'},
                    'token_type': {'type': 'string', 'example': 'Bearer'},
                    'expires_in': {'type': 'integer', 'example': 3600}
                }
            }
        }
    }

    return result 