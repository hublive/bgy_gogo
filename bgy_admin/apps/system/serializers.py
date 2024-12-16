from rest_framework import serializers
from django.contrib.auth.models import Permission
from apps.users.models import Role


class PermissionSerializer(serializers.ModelSerializer):
    """权限序列化器"""
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']


class RoleListSerializer(serializers.ModelSerializer):
    """角色列表序列化器"""
    user_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Role
        fields = [
            'id', 'name', 'is_active',
            'created_at', 'updated_at', 'user_count'
        ]
        
    def get_user_count(self, obj):
        """获取角色下的用户数量"""
        return obj.user_set.count()


class RoleDetailSerializer(serializers.ModelSerializer):
    """角色详情序列化器"""
    permissions = PermissionSerializer(many=True, read_only=True)
    user_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Role
        fields = [
            'id', 'name', 'is_active', 'remark',
            'permissions', 'user_count',
            'created_at', 'updated_at'
        ]
        
    def get_user_count(self, obj):
        """获取角色下的用户数量"""
        return obj.user_set.count()


class RoleCreateSerializer(serializers.ModelSerializer):
    """角色创建序列化器"""
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        required=False
    )
    
    class Meta:
        model = Role
        fields = [
            'name', 'is_active', 'remark',
            'permissions'
        ]
        
    def validate_code(self, value):
        """验证角色编码唯一性"""
        if Role.objects.filter(code=value).exists():
            raise serializers.ValidationError("角色编码已存在")
        return value


class RoleUpdateSerializer(serializers.ModelSerializer):
    """角色更新序列化器"""
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        required=False
    )
    
    class Meta:
        model = Role
        fields = [
            'name', 'is_active', 'remark',
            'permissions'
        ]
        
    def validate_code(self, value):
        """验证角色编码唯一性"""
        instance = self.instance
        if Role.objects.exclude(pk=instance.pk).filter(code=value).exists():
            raise serializers.ValidationError("角色编码已存在")
        return value


class RoleSerializer(serializers.ModelSerializer):
    """角色基础序列化器"""
    class Meta:
        model = Role
        fields = [
            'id', 'name', 'is_active', 'remark',
            'created_at', 'updated_at'
        ]