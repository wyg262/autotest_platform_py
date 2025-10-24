# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime
from config.config import config

def setup_logger():
    """配置日志"""
    # 创建 logs 目录
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # 日志文件名
    log_file = f"logs/test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    # 配置日志
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

def get_logger(name: str) -> logging.Logger:
    """获取 logger 实例"""
    return logging.getLogger(name)

# 初始化日志配置
setup_logger()