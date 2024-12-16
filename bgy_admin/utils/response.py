from rest_framework import status
from rest_framework.response import Response


class APIResponse(Response):
    """统一API响应格式"""

    def __init__(self, code=status.HTTP_200_OK, message="success", data=None, status=None, **kwargs):
        body = {
            'code': code,
            'message': message,
            'data': data
        }
        if kwargs:
            body.update(kwargs)
            
        super().__init__(data=body, status=status)
