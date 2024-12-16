import os
import sys
from datetime import datetime
from loguru import logger

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志文件路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 日志文件名格式
current_date = datetime.now().strftime('%Y%m%d')

# 日志格式
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "{message}"
)

# 移除默认的控制台输出
logger.remove()

# 添加控制台输出
logger.add(
    sys.stdout,
    format=log_format,
    level="DEBUG",
    colorize=True,
    enqueue=True
)

# 添加文件输出
logger.add(
    os.path.join(LOG_DIR, f"info_{current_date}.log"),
    format=log_format,
    level="INFO",
    rotation="100 MB",
    retention="30 days",
    encoding="utf-8",
    enqueue=True
)

logger.add(
    os.path.join(LOG_DIR, f"error_{current_date}.log"),
    format=log_format,
    level="ERROR",
    rotation="100 MB",
    retention="30 days",
    encoding="utf-8",
    enqueue=True
)

logger.add(
    os.path.join(LOG_DIR, f"debug_{current_date}.log"),
    format=log_format,
    level="DEBUG",
    rotation="100 MB",
    retention="30 days",
    encoding="utf-8"
)

# 添加异常处理器
def error_handler(exc_type, exc_value, exc_traceback):
    """全局异常处理器"""
    if issubclass(exc_type, KeyboardInterrupt):
        return sys.__excepthook__(exc_type, exc_value, exc_traceback)
    logger.opt(exception=(exc_type, exc_value, exc_traceback)).error("Uncaught exception:")

sys.excepthook = error_handler
