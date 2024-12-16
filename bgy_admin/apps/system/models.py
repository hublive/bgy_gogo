from django.db import models


class Permission(models.Model):
    """权限模型"""
    TYPE_CHOICES = (
        ('menu', '菜单'),
        ('button', '按钮'),
        ('api', '接口'),
    )
    
    name = models.CharField(max_length=32, unique=True, verbose_name='权限名称')
    type = models.CharField(
        max_length=32, 
        choices=TYPE_CHOICES, 
        default='api', 
        verbose_name='权限类型'
    )
    method = models.CharField(
        max_length=32,
        choices=(
            ('GET', 'GET'),
            ('POST', 'POST'),
            ('PUT', 'PUT'),
            ('DELETE', 'DELETE'),
        ),
        default='GET',
        verbose_name='请求方法'
    )
    codename = models.CharField(max_length=32, unique=True, verbose_name='权限代码')
    desc = models.CharField(max_length=128, blank=True, verbose_name='权限描述')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='父权限'
    )
    order = models.IntegerField(default=0, verbose_name='显示顺序')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name
        ordering = ['id']
        db_table = 'sys_permission'

    def __str__(self):
        return self.name


class Menu(models.Model):
    """菜单模型"""
    TYPE_CHOICES = (
        ('CATALOG', '目录'),
        ('MENU', '菜单'),
        ('BUTTON', '按钮'),
    )
    
    name = models.CharField(max_length=32, verbose_name='菜单名称')
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name='父菜单'
    )
    type = models.CharField(
        max_length=32,
        choices=TYPE_CHOICES,
        default='MENU',
        verbose_name='菜单类型'
    )
    icon = models.CharField(max_length=32, blank=True, verbose_name='图标')
    path = models.CharField(max_length=128, blank=True, verbose_name='路由路径')
    component = models.CharField(max_length=128, blank=True, verbose_name='组件路径')
    permission = models.CharField(max_length=32, blank=True, verbose_name='权限标识')
    order = models.IntegerField(default=0, verbose_name='排序')
    is_cache = models.BooleanField(default=False, verbose_name='是否缓存')
    is_visible = models.BooleanField(default=True, verbose_name='是否可见')
    is_frame = models.BooleanField(default=False, verbose_name='是否外链')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['order']
        db_table = 'sys_menu'

    def __str__(self):
        return self.name


class Config(models.Model):
    """系统配置模型"""
    name = models.CharField(max_length=32, unique=True, verbose_name='配置名称')
    key = models.CharField(max_length=32, unique=True, verbose_name='配置键名')
    value = models.TextField(verbose_name='配置键值')
    type = models.CharField(
        max_length=32,
        choices=(
            ('string', '字符串'),
            ('number', '数字'),
            ('boolean', '布尔值'),
            ('json', 'JSON'),
        ),
        default='string',
        verbose_name='配置类型'
    )
    is_active = models.BooleanField(default=True, verbose_name='是否启用')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    remark = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        verbose_name = '系统配置'
        verbose_name_plural = verbose_name
        db_table = 'sys_config'

    def __str__(self):
        return self.name
