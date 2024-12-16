from django.db import models
from django.conf import settings


class OperationLog(models.Model):
    """操作日志模型"""
    STATUS_CHOICES = (
        (1, '成功'),
        (0, '失败'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='操作用户'
    )
    module = models.CharField(max_length=50, verbose_name='操作模块')
    action = models.CharField(max_length=50, verbose_name='操作行为')
    method = models.CharField(max_length=20, verbose_name='请求方法')
    path = models.CharField(max_length=200, verbose_name='请求路径')
    ip_addr = models.GenericIPAddressField(verbose_name='IP地址')
    location = models.CharField(
        max_length=64,
        blank=True,
        default='',
        verbose_name='操作地点'
    )
    browser = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name='浏览器'
    )
    os = models.CharField(
        max_length=256,
        blank=True,
        default='',
        verbose_name='操作系统'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name='操作状态'
    )
    params = models.TextField(blank=True, default='', verbose_name='请求参数')
    result = models.TextField(blank=True, default='', verbose_name='返回结果')
    error_msg = models.TextField(blank=True, default='', verbose_name='错误信息')
    duration = models.FloatField(default=0, verbose_name='执行时长(秒)')
    elapsed_time = models.IntegerField(default=0, verbose_name='耗时(ms)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '操作日志'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
        db_table = 'sys_operation_log'

    def __str__(self):
        return f"{self.user}的{self.action}操作"


class SystemInfo(models.Model):
    """系统信息模型"""
    STATUS_CHOICES = (
        (1, '成功'),
        (0, '失败'),
    )
    
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='操作用户'
    )
    module = models.CharField(max_length=32, verbose_name='操作模块')
    action = models.CharField(max_length=32, verbose_name='操作行为')
    method = models.CharField(max_length=16, verbose_name='请求方法')
    path = models.CharField(max_length=256, verbose_name='请求路径')
    ip_addr = models.GenericIPAddressField(verbose_name='IP地址')
    location = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='操作地点'
    )
    params = models.TextField(
        blank=True,
        verbose_name='请求参数'
    )
    result = models.TextField(
        blank=True,
        verbose_name='返回结果'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name='操作状态'
    )
    error_msg = models.TextField(
        blank=True,
        verbose_name='错误信息'
    )
    browser = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='浏览器'
    )
    os = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='操作系统'
    )
    elapsed_time = models.IntegerField(
        default=0,
        verbose_name='耗时(ms)'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )

    class Meta:
        verbose_name = '系统信息'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
        db_table = 'sys_system_info'

    def __str__(self):
        return f"{self.user}的{self.action}操作"


class LoginLog(models.Model):
    """登录日志模型"""
    STATUS_CHOICES = (
        (1, '成功'),
        (0, '失败'),
    )
    
    username = models.CharField(max_length=150, verbose_name='用户名')
    ip_addr = models.GenericIPAddressField(verbose_name='IP地址')
    location = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='登录地点'
    )
    browser = models.CharField(max_length=256, verbose_name='浏览器')
    os = models.CharField(max_length=256, verbose_name='操作系统')
    device = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='设备信息'
    )
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=1,
        verbose_name='状态'
    )
    msg = models.CharField(max_length=128, verbose_name='消息')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '登录日志'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
        db_table = 'sys_login_log'

    def __str__(self):
        return f"{self.username}的登录记录"


class OnlineUser(models.Model):
    """在线用户模型"""
    token_id = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='会话标识'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='用户'
    )
    ip_addr = models.GenericIPAddressField(verbose_name='IP地址')
    location = models.CharField(
        max_length=64,
        blank=True,
        verbose_name='登录地点'
    )
    browser = models.CharField(max_length=256, verbose_name='浏览器')
    os = models.CharField(max_length=256, verbose_name='操作系统')
    device = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='设备信息'
    )
    login_time = models.DateTimeField(verbose_name='登录时间')
    last_active_time = models.DateTimeField(
        auto_now=True,
        verbose_name='最后活跃时间'
    )

    class Meta:
        verbose_name = '在线用户'
        verbose_name_plural = verbose_name
        ordering = ['-last_active_time']
        db_table = 'sys_online_user'

    def __str__(self):
        return f"{self.user}的在线记录"
