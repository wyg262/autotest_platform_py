# -*- coding: utf-8 -*-
import os
from typing import Dict, Any
import yaml
from utils.logger import get_logger

logger = get_logger(__name__)

class Config:
    """配置管理类"""

    def __init__(self, config_file: str =None):
        # 初始化默认配置
        self.API_BASE_URL = "https://m-uat.z-trip.cn/"
        self.API_TIMEOUT = 30
        self.LOG_LEVEL = "INFO"

        # 可以从环境变量覆盖配置
        self.API_BASE_URL = os.getenv("API_BASE_URL", self.API_BASE_URL)
        self.API_TIMEOUT = int(os.getenv("API_TIMEOUT", str(self.API_TIMEOUT)))
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", self.LOG_LEVEL)

        if config_file:
            self.load_yaml_from_config(config_file)

    def load_yaml_from_config(self, file_path: str) -> None:
        """从 YAML 文件加载配置，并更新系统配置"""
        try:
            with open (file_path, 'r', encoding='utf-8' ) as file:
                 config_data = yaml.safe_load(file)
                 if config_data is None:
                     logger.warning(f"YAML配置文件为空: {file_path}")
                     return
                 
                 for k, v in config_data.items():
                    config_key = k.upper()
                    if hasattr(self, config_key):
                        old_value = getattr(self, config_key)
                        setattr(self, config_key, v)
                        logger.info(f"变更配置:{config_key}从{old_value}变更为{v}")
                    else:
                        logger.info(f"没有该配置项目:{config_key}")                           
        except Exception as e:
            logger.error(f"加载配置文件失败: {e}")
            return

# 创建全局配置实例
config =Config()
# 或者使用配置文件：config = Config("config/test.yaml")