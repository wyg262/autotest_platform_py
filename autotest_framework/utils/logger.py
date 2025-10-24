from datetime import datetime
import logging
import os


def setup_logger():
    '''配置日志系统'''
    # 创建日志目录
    if not os.path.exists('logs'):
        os.makedirs("logs")

    # 日志文件名
    log_file = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    # 创建logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 避免重复添加 handler
    if logger.handlers:
        logger.handlers.clear()

    # 创建 formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 文件handler
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # 控制台 handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # 添加 handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_logger(name: str)-> logging.Logger:
    '''获取 logger 实例'''
    return logging.getLogger(name)

# 初始化日志配置
setup_logger()
