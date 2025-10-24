#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

def run_tests():
    """运行测试"""
    commands = [
        # 运行所有测试
        ["pytest", "testcases/", "-v", "--html=reports/report.html"],
        
        # 只运行 API 测试
        # ["pytest", "testcases/api/", "-m", "api", "-v"],
        
        # 并行运行测试
        # ["pytest", "testcases/", "-n", "4", "-v"],
        
        # 生成 Allure 报告
        # ["pytest", "testcases/", "--alluredir=reports/allure-results"]
    ]
    
    for cmd in commands:
        print(f"执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print("测试执行失败!")
            sys.exit(1)

if __name__ == "__main__":
    run_tests()