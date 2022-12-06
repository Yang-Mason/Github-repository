import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage
from page.login_page import LoginPage


class TestFans:

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

    def test_search(self, browser, base_url):
        """ 按昵称搜索粉丝 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.search_input)
        page.search_input = "茶白"
        sleep(3)
        page.search.click()
        sleep(2)
        PageWait(page.test_search)
        assert page.test_search.text == "茶"

    def test_labul(self, browser, base_url):
        """ 给粉丝打标签"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.search_input)
        page.search_input = "茶白"
        page.search.click()
        sleep(1)
        page.labeling.click()
        sleep(1)
        page.label_input.click()
        page.label_input = "matest-1标签"
        sleep(1)
        page.label_select.click()
        page.label_submit.click()
        sleep(1)
        page.labeling.click()
        PageWait(page.label_test)
        assert page.label_test.text == "matest-1标签"
        PageWait(page.label_delete)
        page.label_delete.click()
        page.label_submit.click()
        sleep(1)

    def test_group_send(self, browser, base_url):
        """ 选择粉丝进行群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.advanced_screen)
        page.advanced_screen.click()
        PageWait(page.country_select)
        page.country_select.click()
        PageWait(page.chinese)
        page.chinese.click()
        PageWait(page.province_select)
        page.province_select.click()
        PageWait(page.shandong)
        page.shandong.click()
        PageWait(page.city_select)
        page.city_select.click()
        PageWait(page.city_heze)
        page.city_heze.click()
        page.immediate_screen_fans.click()
        sleep(1)
        page.select_fans1.click()
        page.select_fans2.click()
        page.mass_message.click()
        PageWait(page.mass_input)
        page.mass_input = "test"
        sleep(1)
        page.mass_send.click()
        assert page.mass_test.text == "消息群发成功，您可以点击群发菜单查看详情"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_02_fans.py"])
