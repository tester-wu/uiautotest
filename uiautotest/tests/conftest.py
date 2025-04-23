import pytest
# 导入初始化浏览器的函数
from core_utils.browser_manager import init_browser

@pytest.fixture(scope="function")
def page():
    """
    pytest测试夹具，用于在每个测试函数执行前后管理浏览器和页面
    :return: 浏览器页面对象
    """
    # 初始化浏览器
    browser = init_browser()
    assert browser is not None,"浏览器初始化失败"     #添加断言
    # 创建一个新的浏览器页面
    page = browser.new_page()
    # 将页面对象提供给测试函数使用
    yield page
    # 测试函数执行完毕后，关闭页面
    page.close()
    # 关闭浏览器
    browser.close()