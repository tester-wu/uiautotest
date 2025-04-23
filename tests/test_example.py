import re
import time

from playwright.sync_api import Page, expect

# 导入读取测试数据的工具函数
from tests.test_utils.data_reader import read_test_data
# 导入获取元素选择器的工具函数
from tests.test_utils.element_locator import get_element_selector

def test_example(page: Page) -> None:
    """
    测试登录流程的函数
    :param page: 浏览器页面对象，用于操作浏览器页面
    """
    # 导航到测试环境的基础URL
    page.goto("https://uatninebot.segway-ninebot.com:8002/main.aspx")
    # 读取登录测试数据
    login_data = read_test_data("login_data.yaml")
    # 点击Active Directory文本元素
    page.get_by_text(get_element_selector("login_page", "active_directory_text")).click()
    # 点击用户名输入框
    page.get_by_role("textbox", name=get_element_selector("login_page", "username_textbox")).click()
    # 在用户名输入框中输入用户名
    page.get_by_role("textbox", name=get_element_selector("login_page", "username_textbox")).fill(login_data["username"])
    # 点击密码输入框
    page.get_by_role("textbox", name=get_element_selector("login_page", "password_textbox")).click()
    # 按下CapsLock键
    page.get_by_role("textbox", name=get_element_selector("login_page", "password_textbox")).press("CapsLock")
    # 在密码输入框中输入字母C
    page.get_by_role("textbox", name=get_element_selector("login_page", "password_textbox")).fill("C")
    # 再次按下CapsLock键
    page.get_by_role("textbox", name=get_element_selector("login_page", "password_textbox")).press("CapsLock")
    # 在密码输入框中输入完整密码
    page.get_by_role("textbox", name=get_element_selector("login_page", "password_textbox")).fill(login_data["password"])
    # 点击登录按钮
    page.get_by_role("button", name=get_element_selector("login_page", "login_button")).click()
    # 点击关闭链接（在iframe内）
    time.sleep(5)
    page.locator(get_element_selector("login_page", "close_link")).content_frame.get_by_role("link", name="关闭").click()
    # 断言Microsoft Dynamics链接元素是否可见
    expect(page.get_by_role("link", name=get_element_selector("login_page", "microsoft_dynamics_link"))).to_be_visible()
