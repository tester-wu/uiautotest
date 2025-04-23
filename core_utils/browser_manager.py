from playwright.sync_api import sync_playwright
# 导入读取YAML文件的工具函数
from core_utils.yaml_reader import read_yaml

def init_browser():
    """
    根据配置文件初始化浏览器
    :return: 初始化后的浏览器对象
    """
    # 读取配置文件
    config = read_yaml('config/config.yaml')
    if not config:
        return None
    # 启动Playwright同步API
    playwright = sync_playwright().start()
    # 获取配置文件中指定的浏览器类型
    browser_type = config['browser']['type']
    # 获取配置文件中是否以无头模式运行的设置
    headless = config['browser']['headless']
    # 启动指定类型的浏览器
    browser = playwright[browser_type].launch(headless=headless)
    return browser