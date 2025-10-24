# -*- coding: utf-8 -*-
import pytest
from core.api_client import APIClient
from core.assertion import Assertion
from config.config import config
from utils.logger import get_logger

logger = get_logger(__name__)

class BaseTest:
    """测试基类"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """每个测试用例前的准备工作"""
        self.api_client = APIClient(base_url=config.API_BASE_URL)
        self.assertion = Assertion()
        logger.info("测试用例初始化完成")
        yield
        logger.info("测试用例清理完成")
    
    def set_auth_token(self, token: str):
        """设置认证 token"""
        self.api_client.set_headers({"Authorization": f"Bearer {token}"})
        logger.info(f"设置认证 token: {token}")