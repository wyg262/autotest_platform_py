# -*- coding: utf-8 -*-
import os
from typing import Dict, Any
import yaml
from pydantic import BaseSettings

class Settings(BaseSettings):
    """配置管理类"""
    
    # API 配置
    API_BASE_URL: str = "http://api.example.com"
    API_TIMEOUT: int = 30
    
    # 数据库配置
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "test"
    DB_PASSWORD: str = "test"
    
    # 日志配置
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # 测试配置
    TEST_ENV: str = "test"
    HEADLESS: bool = False
    
    class Config:
        env_file = ".env"
    
    @classmethod
    def load_yaml_config(cls, file_path: str) -> Dict[str, Any]:
        """从 YAML 文件加载配置"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)

config = Settings()