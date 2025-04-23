import os
import sys

# 将项目根目录添加到 sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def run_tests():
    """
    运行所有测试用例并生成Allure测试报告
    """
    # 执行pytest测试，将结果保存到指定目录
    os.system('pytest tests/')
    # 生成Allure报告，覆盖原有报告
    os.system('allure generate allure-results -o allure-report --clean')

if __name__ == "__main__":
    # 脚本作为主程序运行时，调用run_tests函数
    run_tests()