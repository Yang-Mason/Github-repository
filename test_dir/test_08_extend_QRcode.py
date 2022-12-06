import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage


class TestExtend_QRcode:

    def test_add_QRcode(self, browser, base_url):
        """ 新增推广二维码"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.extend_QR_code)
        page.extend_QR_code.click()
        sleep(2)
        page.QRcode_new.click()
        sleep(1)
        page.QRcode_name = "masontest-QRcode"
        page.QRcode_response = "欢迎啊！！！"
        page.QRcode_describe = "自动化测试推广二维码"
        sleep(1)
        page.QRcode_new_submit.click()
        assert page.test_new_QRcode.text == "二维码创建成功"

    def test_search_QRcode(self, browser, base_url):
        """ 搜素推广二维码"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.extend_QR_code)
        page.extend_QR_code.click()
        PageWait(page.QRcode_search_input)
        page.QRcode_search_input = "masontest-QRcode"
        sleep(1)
        page.QRcode_search.click()
        sleep(1)
        assert page.test_QRcode_search.text == "masontest-QRcode"

    def test_edit_QRcode(self, browser, base_url):
        """ 编辑推广二维码"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.extend_QR_code)
        page.extend_QR_code.click()
        PageWait(page.QRcode_edit)
        page.QRcode_edit.click()
        sleep(2)
        page.QRcode_name.click()
        page.QRcode_name = "-edit"
        sleep(1)
        page.QRcode_new_submit.click()
        assert page.test_edit_QRcode.text == "二维码更新成功"

    def test_delete_QRcode(self, browser, base_url):
        """ 删除推广二维码"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.extend_QR_code)
        page.extend_QR_code.click()
        PageWait(page.QRcode_delete)
        page.QRcode_delete.click()
        PageWait(page.QRcode_delete_submit)
        page.QRcode_delete_submit.click()
        assert page.test_delete_QRcode.text == "二维码删除成功"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_08_extend_QRcode.py"])