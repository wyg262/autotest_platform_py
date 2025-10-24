# -*- coding: utf-8 -*-
import pytest
import yaml
from typing import Dict, Any

def pytest_addoption(parser):
    """添加自定义命令行选项"""
    parser.addoption("--env", action="store", default="test", help="测试环境: test, staging, production")
    parser.addoption("--browser", action="store", default="chrome", help="浏览器: chrome, firefox")

@pytest.fixture(scope="session")
def test_config(request) -> Dict[str, Any]:
    """加载测试配置"""
    env = request.config.getoption("--env")
    with open("config/test_env.yaml", 'r', encoding='utf-8') as file:
        all_config = yaml.safe_load(file)
    return all_config.get(env, {})

def pytest_configure(config):
    """pytest 配置钩子"""
    # 添加自定义标记
    config.addinivalue_line("markers", "slow: 标记为慢速测试")
    config.addinivalue_line("markers", "api: API 测试")
    config.addinivalue_line("markers", "ui: UI 测试")

def pytest_html_report_title(report):
    """自定义 HTML 报告标题"""
    report.title = "自动化测试报告"

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取测试结果"""
    outcome = yield
    report = outcome.get_result()
    
    # 只在测试失败时执行
    if report.when == "call" and report.failed:
        # 这里可以添加失败截图、日志等
        pass