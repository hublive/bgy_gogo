import os
from django.core.wsgi import get_wsgi_application
from utils.logger import logger  # 导入并初始化日志配置

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'byg_admin.settings.production')

application = get_wsgi_application()

logger.info("Application started") 