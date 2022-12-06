import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage


class TestCustommenu:

    def test_add_custommenu(self, browser, base_url):
        """ 新增菜单、添加子菜单并发布"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.custom_menu)
        page.custom_menu.click()
        sleep(3)
        page.personalized_menu.click()
        sleep(1)
        page.personalized_menu_new.click()
        sleep(3)
        page.personalized_menu_name = "test-custommenu"
        page.personalized_menu_select.click()
        page.personalized_menu_system.click()
        page.personalized_menu_select_system.click()
        page.personalized_menu_Android.click()
        page.personalized_menu_main.click()
        sleep(1)
        page.menu_main_name = "test-mainmenu"
        sleep(1)
        page.menu_main_preserve.click()
        page.menu_sub_new.click()
        sleep(1)
        page.menu_sub_name = "test-submenu"
        page.menu_sub_clickaction.click()
        page.menu_sub_message.click()
        sleep(1)
        page.menu_sub_input = "test-submenu-input"
        sleep(1)
        page.menu_sub_preserve.click()
        sleep(1)
        page.menu_release.click()
        assert page.test_new_custommenu.text == "发布菜单成功"

    def test_delete_submenu(self, browser, base_url):
        """ 删除子菜单并发布"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.custom_menu)
        page.custom_menu.click()
        sleep(3)
        page.personalized_menu.click()
        PageWait(page.menu_sub_edit)
        page.menu_sub_edit.click()
        sleep(2)
        page.menu_sub_select.click()
        sleep(1)
        page.menu_sub_delete.click()
        PageWait(page.menu_sub_delete_submit)
        page.menu_sub_delete_submit.click()
        sleep(1)
        page.menu_main_click.click()
        page.menu_main_edit.click()
        page.menu_main_set.click()
        sleep(1)
        page.menu_sub_message.click()
        sleep(1)
        page.menu_sub_input = "test-customer-input"
        sleep(1)
        page.menu_sub_preserve.click()
        sleep(1)
        page.menu_sub_release.click()
        assert page.test_new_custommenu.text == "发布菜单成功"

    def test_delete_custommenu(self, browser, base_url):
        """ 删除自定义菜单"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.custom_menu)
        page.custom_menu.click()
        sleep(3)
        page.personalized_menu.click()
        PageWait(page.custommenu_delete)
        page.custommenu_delete.click()
        PageWait(page.custommenu_delete_submit)
        page.custommenu_delete_submit.click()
        sleep(1)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_06_custommenu.py"])