# import os
# import sys
from config.config import config
from utils.logger import get_logger

# 添加当前包路径到 Python 路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, current_dir)


def main():
    print("=== 自动化测试框架 ===")
    print(f"默认 API_BASE_URL: {config.API_BASE_URL}")
    print(f"默认 API_TIMEOUT: {config.API_TIMEOUT}")
    print(f"默认 LOG_LEVEL: {config.LOG_LEVEL}")
    print("框架启动成功！")

    config.load_yaml_from_config('config/prod_config.yaml')
    print("=================修改后的参数配置==========")
    print(f"修改后的 API_BASE_URL: {config.API_BASE_URL}")
    print(f"修改后的 API_TIMEOUT: {config.API_TIMEOUT}")
    print(f"修改后的 LOG_LEVEL: {config.LOG_LEVEL}")

if __name__ == '__main__':
    main()
    