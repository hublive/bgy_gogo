# Generated by Django 4.2.17 on 2024-12-16 22:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("system", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True,
                        help_text="用户昵称",
                        max_length=50,
                        verbose_name="昵称",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="手机号",
                        max_length=11,
                        null=True,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="请输入正确的手机号", regex="^1[3-9]\\d{9}$"
                            )
                        ],
                        verbose_name="手机号",
                    ),
                ),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(0, "未知"), (1, "男"), (2, "女")],
                        default=0,
                        help_text="性别(0:未知 1:男 2:女)",
                        verbose_name="性别",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        help_text="用户头像",
                        null=True,
                        upload_to="avatars/%Y/%m",
                        verbose_name="头像",
                    ),
                ),
                (
                    "login_count",
                    models.IntegerField(
                        default=0, help_text="累计登录次数", verbose_name="登录次数"
                    ),
                ),
                (
                    "last_login_ip",
                    models.GenericIPAddressField(
                        blank=True,
                        help_text="最后登录的IP地址",
                        null=True,
                        verbose_name="最后登录IP",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
                "db_table": "sys_user",
                "ordering": ["-date_joined"],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="部门名称")),
                ("order", models.IntegerField(default=0, verbose_name="显示顺序")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="是否启用"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                ("remark", models.TextField(blank=True, verbose_name="备注")),
                (
                    "leader",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="leading_departments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="部门负责人",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.department",
                        verbose_name="父部门",
                    ),
                ),
            ],
            options={
                "verbose_name": "部门",
                "verbose_name_plural": "部门",
                "db_table": "sys_department",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="UserSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "session_key",
                    models.CharField(max_length=500, verbose_name="会话标识"),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="IP地址"
                    ),
                ),
                (
                    "user_agent",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="用户代理"
                    ),
                ),
                (
                    "last_activity",
                    models.DateTimeField(auto_now=True, verbose_name="最后活动时间"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户会话",
                "verbose_name_plural": "用户会话",
                "db_table": "sys_user_session",
                "ordering": ["-last_activity"],
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=32, unique=True, verbose_name="角色名称"
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        max_length=32, unique=True, verbose_name="角色标识"
                    ),
                ),
                (
                    "desc",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="角色描述"
                    ),
                ),
                (
                    "data_scope",
                    models.CharField(
                        choices=[
                            ("ALL", "全部数据权限"),
                            ("CUSTOM", "自定义数据权限"),
                            ("DEPT", "本部门数据权限"),
                            ("DEPT_AND_CHILD", "本部门及以下数据权限"),
                            ("SELF", "仅本人数据权限"),
                        ],
                        default="SELF",
                        max_length=32,
                        verbose_name="数据范围",
                    ),
                ),
                ("order", models.IntegerField(default=0, verbose_name="显示顺序")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="是否启用"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                ("remark", models.TextField(blank=True, verbose_name="备注")),
                (
                    "departments",
                    models.ManyToManyField(
                        blank=True, to="users.department", verbose_name="数据权限-部门"
                    ),
                ),
                (
                    "menus",
                    models.ManyToManyField(
                        blank=True, to="system.menu", verbose_name="菜单权限"
                    ),
                ),
                (
                    "permissions",
                    models.ManyToManyField(
                        blank=True, to="system.permission", verbose_name="权限"
                    ),
                ),
            ],
            options={
                "verbose_name": "角色",
                "verbose_name_plural": "角色",
                "db_table": "sys_role",
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="user",
            name="department",
            field=models.ForeignKey(
                blank=True,
                help_text="所属部门",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.department",
                verbose_name="部门",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="roles",
            field=models.ManyToManyField(
                blank=True, help_text="用户角色", to="users.role", verbose_name="角色"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
