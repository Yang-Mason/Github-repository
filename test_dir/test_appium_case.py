import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait
from selenium.webdriver.common.keys import Keys

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage
from page.appium_page import AppiumPage
from page.appium_setting import TestAppium
from page.channel_page import ChannelPage


class Testappiumcase:

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

    def test_appiumcase1(self):
        """ 测试移动端向公众号发送消息"""
        try:
            page = AppiumPage(TestAppium.driver)
            page.mail_list.click()
            page.public_address.click()
            page.qunshuoceshi2.click()
            page.dianjifaxiaoxi.click()
            page.biaoqing.click()
            sleep(1)
            page.weixiao.click()
            page.fasong.click()
            sleep(6)
            TestAppium.reset(self)

        except BaseException as msg:
            print(msg)
            TestAppium.reset(self)

    def test_send_text_message(self, browser, base_url):
        """ 给用户发送文本消息"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.interactive_news)
        page.interactive_news.click()
        sleep(1)
        page.interactive_input = "/::)"
        page.interactive_input = Keys.ENTER
        sleep(1)
        page.interactive_reply.click()
        page.interactive_replyinput = "互动消息回复"
        sleep(1)
        page.interactive_send.click()
        assert page.test_send_interactive.text == "成功发送消息"

    def test_appiumcase2(self):
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
    pytest.main(["-v", "-s", "test_appium_case.py"])