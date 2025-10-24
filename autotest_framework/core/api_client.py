# -*- coding: utf-8 -*-
import requests
import json
from typing import Dict, Any, Optional
from utils.logger import get_logger

logger = get_logger(__name__)

class APIClient:
    """RESTful API 客户端"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "AutoTestFramework/1.0"
        })
    
    def set_headers(self, headers: Dict[str, str]):
        """设置请求头"""
        self.session.headers.update(headers)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """发送请求"""
        url = f"{self.base_url}{endpoint}"
        
        logger.info(f"发送 {method} 请求到 {url}")
        logger.debug(f"请求参数: {kwargs}")
        
        response = self.session.request(method, url, timeout=self.timeout, **kwargs)
        
        logger.info(f"响应状态码: {response.status_code}")
        logger.debug(f"响应内容: {response.text}")
        
        return response
    
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, params=params, **kwargs)
    
    def post(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, json=data, **kwargs)
    
    def put(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, json=data, **kwargs)
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)
    
    def patch(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        return self._request("PATCH", endpoint, json=data, **kwargs)