#!/bin/bash

PROJECT_NAME="autotest_framework"

echo "开始创建自动化测试框架项目..."
mkdir -p $PROJECT_NAME/{config,core,testcases/{api,ui},test_data,utils,reports,logs,.vscode}

echo "创建 __init__.py 文件..."
find $PROJECT_NAME -type d -exec touch {}/__init__.py \;

echo "创建主要代码文件..."
touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/config/config.py
touch $PROJECT_NAME/config/test_env.yaml
touch $PROJECT_NAME/core/base_test.py
touch $PROJECT_NAME/core/api_client.py
touch $PROJECT_NAME/core/assertion.py
touch $PROJECT_NAME/core/report_generator.py
touch $PROJECT_NAME/testcases/api/test_user_api.py
touch $PROJECT_NAME/testcases/api/test_product_api.py
touch $PROJECT_NAME/testcases/ui/test_login_ui.py
touch $PROJECT_NAME/test_data/api_data.yaml
touch $PROJECT_NAME/test_data/ui_data.yaml
touch $PROJECT_NAME/utils/logger.py
touch $PROJECT_NAME/utils/file_reader.py
touch $PROJECT_NAME/utils/db_client.py
touch $PROJECT_NAME/conftest.py
touch $PROJECT_NAME/run_tests.py
touch $PROJECT_NAME/.vscode/settings.json
touch $PROJECT_NAME/.vscode/launch.json

echo "项目结构创建完成！"
echo "现在可以在 VS Code 中打开项目："
echo "code $PROJECT_NAME"