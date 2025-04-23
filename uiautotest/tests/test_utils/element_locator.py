# 导入读取YAML文件的工具函数
from core_utils.yaml_reader import read_yaml
import os

def get_element_selector(page_name, element_name):
    """
    根据页面名称和元素名称获取元素的定位选择器
    :param page_name: 页面名称，对应YAML文件的文件名
    :param element_name: 元素名称，对应YAML文件中的键
    :return: 元素的定位选择器
    """
    # 构建页面元素定位信息文件的完整路径
    elements_path = os.path.join("data", "page_elements", f"{page_name}.yaml")
    # 调用read_yaml函数读取并解析YAML文件
    elements = read_yaml(elements_path)
    # 从解析后的字典中获取指定元素的定位选择器
    return elements.get(element_name)