from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from .models import User, Role, Department

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""

    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['last_login', 'date_joined']


class UserCreateSerializer(serializers.ModelSerializer):
    """用户创建序列化器
    
    用于创建新用户，包含密码验证
    """
    confirm_password = serializers.CharField(
        label='确认密码',
        write_only=True,
        required=True,
        help_text='确认密码'
    )
    
    class Meta:
        model = User
        fields = [
            'username', 'password', 'confirm_password', 'email',
            'phone', 'nickname', 'gender', 'roles', 'department',
            'is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate_password(self, value):
        """验证密码是否符合要求"""
        validate_password(value)
        return value
    
    def validate(self, attrs):
        """验证两次密码是否一致"""
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError('两次密码不一致')
        return attrs
    
    def create(self, validated_data):
        """创建用户并设置密码"""
        roles = validated_data.pop('roles', [])
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        if roles:
            user.roles.set(roles)
        return user


class RoleSerializer(serializers.ModelSerializer):
    """角色序列化器"""

    class Meta:
        model = Role
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """部门序列化器
    
    用于部门的增删改查操作
    
    Attributes:
        name: 部门名称
        parent: 父部门
        leader: 部门负责人
        order: 显示顺序
        is_active: 是否启用
        remark: 备注信息
    """
    
    # 添加父部门名称字段,用于展示
    parent_name = serializers.CharField(source='parent.name', read_only=True)
    # 添加负责人名称字段,用于展示  
    leader_name = serializers.CharField(source='leader.nickname', read_only=True)
    # 添加子部门数量字段
    children_count = serializers.SerializerMethodField()
    # 添加部门人数字段
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def get_children_count(self, obj):
        """获取子部门数量"""
        return obj.department_set.count()

    def get_member_count(self, obj):
        """获取部门人数"""
        return obj.user_set.count()

    def validate_parent(self, value):
        """验证父部门
        
        确保不会形成循环引用
        """
        if value:
            # 检查是否选择自己作为父部门
            if value.id == self.instance.id if self.instance else None:
                raise serializers.ValidationError("不能选择自己作为父部门")
            
            # 检查是否选择自己的子部门作为父部门
            if self.instance and value in self.instance.get_descendants():
                raise serializers.ValidationError("不能选择子部门作为父部门")
        return value


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """自定义Token获取序列化器
    
    继承自TokenObtainPairSerializer，添加了额外的用户信息和token过期时间
    
    Attributes:
        token_lifetime: token的有效期(秒)
        token_type: token类型，固定为"Bearer"
    """
    
    def validate(self, attrs):
        """验证用户凭证并返回token
        
        Args:
            attrs: 包含username和password的字典
            
        Returns:
            包含access_token和refresh_token的字典，格式如下：
            {
                "access_token": "xxx...",
                "refresh_token": "xxx...",
                "token_type": "Bearer",
                "expires_in": 3600
            }
            
        Raises:
            serializers.ValidationError: 用户名或密码错误
        """
        try:
            # 调用父类的validate方法获取token
            data = super().validate(attrs)
            
            # 获取token的有效期
            access_token = self.get_token(self.user)
            expires_in = int(access_token.access_token.lifetime.total_seconds())
            
            # 构造返回数据
            return {
                'access_token': str(data['access']),
                'refresh_token': str(data['refresh']),
                'token_type': 'Bearer',
                'expires_in': expires_in
            }
        except Exception as e:
            raise serializers.ValidationError({
                'message': '用户名或密码错误',
                'detail': str(e)
            })


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """自定义Token刷新序列化器
    
    继承自TokenRefreshSerializer，添加了token过期时间
    
    Attributes:
        token_lifetime: token的有效期(秒)
        token_type: token类型，固定为"Bearer"
    """
    
    def validate(self, attrs):
        """验证refresh_token并返回新的access_token
        
        Args:
            attrs: 包含refresh token的字典
            
        Returns:
            包含新access_token的字典，格式如下：
            {
                "access_token": "xxx...",
                "token_type": "Bearer",
                "expires_in": 3600
            }
            
        Raises:
            serializers.ValidationError: refresh token无效或已过期
        """
        # 调用父类的validate方法刷新token
        data = super().validate(attrs)
        
        # 获取token的有效期
        from rest_framework_simplejwt.settings import api_settings
        expires_in = int(api_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
        
        # 构造返回数据
        return {
            'access_token': str(data['access']),
            'token_type': 'Bearer',
            'expires_in': expires_in
        }


class LoginSerializer(serializers.Serializer):
    """登录序列化器"""
    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        allow_blank=False
    )
    password = serializers.CharField(
        label="密码",
        help_text="密码",
        required=True,
        allow_blank=False,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if not username or not password:
            raise serializers.ValidationError("请提供用户名和密码")
            
        return attrs


class LogoutSerializer(serializers.Serializer):
    """登出序列化器"""
    
    refresh_token = serializers.CharField(
        label="刷新令牌",
        help_text="用于注销的刷新令牌",
        required=True
    )


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器
    
    用于用户列表展示，只返回基本信息
    """
    roles = RoleSerializer(many=True, read_only=True)
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['last_login', 'date_joined']


class UserDetailSerializer(serializers.ModelSerializer):
    """用户详情序列化器"""
    roles = RoleSerializer(many=True, read_only=True)
    department = DepartmentSerializer(read_only=True)
    
    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['last_login', 'date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    """用户更新序列化器
    
    用于更新用户信息，不包含密码
    """
    class Meta:
        model = User
        fields = [
            'email', 'phone', 'nickname', 'gender',
            'roles', 'department', 'is_active'
        ]
    
    def validate_phone(self, value):
        """验证手机号是否已被使用"""
        if value and User.objects.exclude(pk=self.instance.pk).filter(phone=value).exists():
            raise serializers.ValidationError('该手机号已被使用')
        return value
    
    def validate_email(self, value):
        """验证邮箱是否已被使用"""
        if value and User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
            raise serializers.ValidationError('该邮箱已被使用')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    """修改密码序列化器"""
    old_password = serializers.CharField(
        label='原密码',
        write_only=True,
        required=True,
        help_text='当前登录密码'
    )
    new_password = serializers.CharField(
        label='新密码',
        write_only=True,
        required=True,
        help_text='新的登录密码'
    )
    confirm_password = serializers.CharField(
        label='确认密码',
        write_only=True,
        required=True,
        help_text='确认新密码'
    )
    
    def validate_old_password(self, value):
        """验证原密码是否正确"""
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('原密码错误')
        return value
    
    def validate_new_password(self, value):
        """验证新密码是否符合要求"""
        validate_password(value)
        return value
    
    def validate(self, attrs):
        """验证两次新密码是否一致"""
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError('两次密码不一致')
        return attrs
