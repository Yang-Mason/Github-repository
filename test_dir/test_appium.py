import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage
from page.appium_page import AppiumPage
from page.appium_setting import TestAppium


class Testappium:

    def test_login(self, browser):
        """ 登录"""
        page = LoginPage(browser)
        page.get("https://staging.quncrm.com/site/login")
        page.login_username = "17864199421@163.com"
        page.login_password = "Szz1996yyyy"
        PageWait(page.login_sign)
        page.login_sign.click()
        PageWait(page.login_channel)
        page.login_channel.click()
        sleep(2)

    def test_appium1(self):
        """ 测试移动端进入会员中心"""
        try:
            page = AppiumPage(TestAppium.driver)
            page.mail_list.click()
            page.public_address.click()
            page.qunshuoceshi2.click()
            page.qunshuo_menu.click()
            page.member_center.click()
            sleep(6)
            TestAppium.reset(self)

        except BaseException as msg:
            print(msg)
            TestAppium.reset(self)

    def test_appium2(self):
        """ 测试移动端搜索公众号“群硕测试2"""
        try:
            page = AppiumPage(TestAppium.driver)
            page.mail_list.click()
            page.public_address.click()
            page.search.click()
            page.search_input = "群硕测试2"
            sleep(1)
            TestAppium.driver.quit()

        except BaseException as msg:
            print(msg)
            TestAppium.driver.quit()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_appium.py"])