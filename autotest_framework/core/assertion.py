# -*- coding: utf-8 -*-
import jsonschema
from jsonpath_ng import parse
from typing import Any, Dict, List
from utils.logger import get_logger

logger = get_logger(__name__)

class Assertion:
    """断言工具类"""
    
    @staticmethod
    def assert_status_code(response, expected_code: int):
        """断言状态码"""
        actual_code = response.status_code
        assert actual_code == expected_code, \
            f"状态码断言失败: 期望 {expected_code}, 实际 {actual_code}"
        logger.info(f"状态码断言成功: {expected_code}")
    
    @staticmethod
    def assert_json_schema(response, schema: Dict):
        """断言 JSON Schema"""
        try:
            jsonschema.validate(instance=response.json(), schema=schema)
            logger.info("JSON Schema 断言成功")
        except jsonschema.ValidationError as e:
            logger.error(f"JSON Schema 断言失败: {e}")
            raise
    
    @staticmethod
    def assert_json_path(response, json_path: str, expected_value: Any):
        """断言 JSONPath"""
        json_data = response.json()
        expr = parse(json_path)
        matches = [match.value for match in expr.find(json_data)]
        
        assert matches, f"JSONPath '{json_path}' 未找到匹配项"
        assert expected_value in matches, \
            f"JSONPath 断言失败: 路径 '{json_path}' 期望值 '{expected_value}', 实际值 '{matches}'"
        logger.info(f"JSONPath 断言成功: {json_path} = {expected_value}")
    
    @staticmethod
    def assert_response_time(response, max_time: float):
        """断言响应时间"""
        response_time = response.elapsed.total_seconds()
        assert response_time <= max_time, \
            f"响应时间断言失败: 期望 <= {max_time}s, 实际 {response_time}s"
        logger.info(f"响应时间断言成功: {response_time}s <= {max_time}s")
    
    @staticmethod
    def assert_contains(response, expected_text: str):
        """断言响应包含文本"""
        response_text = response.text
        assert expected_text in response_text, \
            f"响应文本断言失败: 期望包含 '{expected_text}'"
        logger.info(f"响应文本断言成功: 包含 '{expected_text}'")