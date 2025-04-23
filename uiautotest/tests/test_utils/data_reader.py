# 导入读取YAML文件的工具函数
from core_utils.yaml_reader import read_yaml
import os

def read_test_data(file_name):
    """
    读取指定文件名的测试数据文件
    :param file_name: 测试数据文件的名称
    :return: 解析后的测试数据字典
    """
    # 构建测试数据文件的完整路径
    data_path = os.path.join("data", "test_data", file_name)
    # 调用read_yaml函数读取并解析YAML文件
    return read_yaml(data_path)