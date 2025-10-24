# -*- coding: utf-8 -*-
import pytest
from core.base_test import BaseTest

class TestUserAPI(BaseTest):
    """用户 API 测试用例"""
    
    @pytest.mark.parametrize("user_data", [
        {"name": "user1", "email": "user1@test.com"},
        {"name": "user2", "email": "user2@test.com"}
    ])
    def test_create_user(self, user_data):
        """测试创建用户"""
        # 发送创建用户请求
        response = self.api_client.post("/users", data=user_data)
        
        # 断言
        self.assertion.assert_status_code(response, 201)
        self.assertion.assert_json_path(response, "$.name", user_data["name"])
        self.assertion.assert_json_path(response, "$.email", user_data["email"])
        
        # JSON Schema 断言
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "email": {"type": "string"},
                "created_at": {"type": "string"}
            },
            "required": ["id", "name", "email", "created_at"]
        }
        self.assertion.assert_json_schema(response, schema)
    
    def test_get_user(self):
        """测试获取用户"""
        # 先创建用户
        user_data = {"name": "test_user", "email": "test@example.com"}
        create_response = self.api_client.post("/users", data=user_data)
        user_id = create_response.json()["id"]
        
        # 获取用户
        response = self.api_client.get(f"/users/{user_id}")
        
        # 断言
        self.assertion.assert_status_code(response, 200)
        self.assertion.assert_response_time(response, 2.0)
    
    @pytest.mark.slow
    def test_delete_user(self):
        """测试删除用户"""
        # 先创建用户
        user_data = {"name": "delete_user", "email": "delete@example.com"}
        create_response = self.api_client.post("/users", data=user_data)
        user_id = create_response.json()["id"]
        
        # 删除用户
        response = self.api_client.delete(f"/users/{user_id}")
        
        # 断言
        self.assertion.assert_status_code(response, 204)