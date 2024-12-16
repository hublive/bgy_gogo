from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.core.cache import cache


class User(AbstractUser):
    """用户模型
    
    继承自 Django 的 AbstractUser，添加了额外的字段
    
    Attributes:
        nickname: 用户昵称
        phone: 手机号
        gender: 性别(0:未知 1:男 2:女)
        avatar: 头像
        roles: 角色
        department: 部门
        login_count: 登录次数
        last_login_ip: 最后登录IP
    """
    
    # 性别选项
    GENDER_UNKNOWN = 0
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_UNKNOWN, '未知'),
        (GENDER_MALE, '男'),
        (GENDER_FEMALE, '女'),
    )
    
    # 手机号验证器
    phone_validator = RegexValidator(
        regex=r'^1[3-9]\d{9}$',
        message='请输入正确的手机号'
    )
    
    nickname = models.CharField(
        '昵称',
        max_length=50,
        blank=True,
        help_text='用户昵称'
    )
    phone = models.CharField(
        '手机号',
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        validators=[phone_validator],
        help_text='手机号'
    )
    gender = models.SmallIntegerField(
        '性别',
        choices=GENDER_CHOICES,
        default=GENDER_UNKNOWN,
        help_text='性别(0:未知 1:男 2:女)'
    )
    avatar = models.ImageField(
        '头像',
        upload_to='avatars/%Y/%m',
        null=True,
        blank=True,
        help_text='用户头像'
    )
    roles = models.ManyToManyField(
        'Role',
        verbose_name='角色',
        blank=True,
        help_text='用户角色'
    )
    department = models.ForeignKey(
        'Department',
        verbose_name='部门',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='所属部门'
    )
    login_count = models.IntegerField(
        '登录次数',
        default=0,
        help_text='累计登录次数'
    )
    last_login_ip = models.GenericIPAddressField(
        '最后登录IP',
        null=True,
        blank=True,
        help_text='最后登录的IP地址'
    )

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-date_joined']
        db_table = 'sys_user'

    def __str__(self):
        return f'{self.username}({self.nickname})'


class Department(models.Model):
    """部门模型"""
    name = models.CharField(max_length=50, verbose_name='部门名称')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='父部门'
    )
    leader = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leading_departments',
        verbose_name='部门负责人'
    )
    order = models.IntegerField(default=0, verbose_name='显示顺序')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name
        ordering = ['order']
        db_table = 'sys_department'

    def __str__(self):
        return self.name


class Role(models.Model):
    """角色模型"""
    name = models.CharField(max_length=32, unique=True, verbose_name='角色名称')
    key = models.CharField(max_length=32, unique=True, verbose_name='角色标识')
    desc = models.CharField(max_length=128, blank=True, verbose_name='角色描述')
    permissions = models.ManyToManyField(
        'system.Permission',
        blank=True,
        verbose_name='权限'
    )
    menus = models.ManyToManyField(
        'system.Menu',
        blank=True,
        verbose_name='菜单权限'
    )
    data_scope = models.CharField(
        max_length=32,
        choices=(
            ('ALL', '全部数据权限'),
            ('CUSTOM', '自定义数据权限'),
            ('DEPT', '本部门数据权限'),
            ('DEPT_AND_CHILD', '本部门及以下数据权限'),
            ('SELF', '仅本人数据权限'),
        ),
        default='SELF',
        verbose_name='数据范围'
    )
    departments = models.ManyToManyField(
        'Department',
        blank=True,
        verbose_name='数据权限-部门'
    )
    order = models.IntegerField(default=0, verbose_name='显示顺序')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name
        ordering = ['order']
        db_table = 'sys_role'

    def __str__(self):
        return self.name


class UserSession(models.Model):
    """用户会话记录
    
    记录用户的登录会话信息
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='用户'
    )
    session_key = models.CharField(
        max_length=500,  # 增加长度以存储 JWT token
        verbose_name='会话标识'
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name='IP地址'
    )
    user_agent = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='用户代理'
    )
    last_activity = models.DateTimeField(
        auto_now=True,
        verbose_name='最后活动时间'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = '用户会话'
        verbose_name_plural = verbose_name
        ordering = ['-last_activity']
        db_table = 'sys_user_session'

    def __str__(self):
        return f'{self.user.username} - {self.ip_address}'
