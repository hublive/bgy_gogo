#!/bin/bash

# 激活虚拟环境
source venv/bin/activate

# 收集静态文件
python manage.py collectstatic --noinput

# 执行数据库迁移
python manage.py migrate

# 启动开发服务器
python manage.py runserver 0.0.0.0:8000 