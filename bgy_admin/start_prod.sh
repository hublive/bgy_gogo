#!/bin/bash

# 激活虚拟环境
source venv/bin/activate

# 收集静态文件
python manage.py collectstatic --noinput

# 执行数据库迁移
python manage.py migrate

# 使用 gunicorn 启动应用
gunicorn byg_admin.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --reload 