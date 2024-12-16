from rest_framework import serializers

from ..models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """
    部门序列化器
    
    用于部门数据的序列化和反序列化
    """

    class Meta:
        model = Department
        fields = ['id', 'name', 'parent', 'leader', 'order', 'is_active']
        extra_kwargs = {
            'name': {
                'help_text': '部门名称',
                'required': True,
                'min_length': 2,
                'max_length': 50
            },
            'parent': {
                'help_text': '父部门ID',
                'required': False,
                'allow_null': True
            },
            'leader': {
                'help_text': '部门负责人ID',
                'required': False,
                'allow_null': True
            },
            'order': {
                'help_text': '显示顺序',
                'required': False,
                'min_value': 0,
                'default': 0
            },
            'is_active': {
                'help_text': '是否启用',
                'required': False,
                'default': True
            }
        }

    def validate_parent(self, value):
        """
        验证父部门
        
        - 不能将部门的父部门设置为自己
        - 不能将部门的父部门设置为其子部门
        """
        if not value:
            return value

        if self.instance and value.id == self.instance.id:
            raise serializers.ValidationError('不能将部门的父部门设置为自己')

        if self.instance and value in self.instance.get_descendants():
            raise serializers.ValidationError('不能将部门的父部门设置为其子部门')

        return value
