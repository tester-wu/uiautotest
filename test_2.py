import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://adfsuat.segway-ninebot.com:8001/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2fuatninebot.segway-ninebot.com%3a8002%2f&wctx=rm%3d1%26id%3de50d9392-5512-4af3-805e-92180bf1bd83%26ru%3dhttps%253a%252f%252fuatninebot.segway-ninebot.com%253a8002%252fmain.aspx%26crmorgid%3d217ac2bb-3e91-eb11-9c24-fabc190f3900&wct=2025-04-23T07%3a02%3a06Z&wauth=urn%3aoasis%3anames%3atc%3aSAML%3a1.0%3aam%3apassword")
    page.get_by_text("Active Directory").click()
    page.get_by_role("textbox", name="用户帐户").click()
    page.get_by_role("textbox", name="用户帐户").fill("ye.wu@ninebot.com")
    page.get_by_role("textbox", name="密码").click()
    page.get_by_role("textbox", name="密码").press("CapsLock")
    page.get_by_role("textbox", name="密码").fill("C")
    page.get_by_role("textbox", name="密码").press("CapsLock")
    page.get_by_role("textbox", name="密码").fill("Cyber@123")
    page.get_by_role("button", name="登录").click()
    page.locator("iframe[name=\"InlineDialog_Iframe\"]").content_frame.get_by_role("link", name="关闭").click()
    expect(page.get_by_role("link", name="Microsoft Dynamics")).to_be_visible()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
