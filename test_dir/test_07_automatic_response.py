import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage


class TestAutomatic_response:

    def test_add_response(self, browser, base_url):
        """ 新增关键词回复"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.automatic_response)
        page.automatic_response.click()
        sleep(3)
        page.keyword_response_new.click()
        sleep(1)
        page.rule_name = "masontest-keyword-response"
        page.keyword = "makeyword"
        page.response_new.click()
        page.text_response.click()
        sleep(1)
        page.text_input = "masontest-text-keyword"
        sleep(1)
        page.response_submit.click()
        sleep(1)
        page.keyword_response_submit.click()
        assert page.test_new_keyword.text == "关键词规则创建成功"

    def test_edit_response(self, browser, base_url):
        """ 编辑关键词回复"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.automatic_response)
        page.automatic_response.click()
        PageWait(page.keyword_response_edit)
        page.keyword_response_edit.click()
        sleep(1)
        page.rule_name.click()
        page.rule_name = "-edit"
        sleep(1)
        page.keyword_response_submit.click()
        assert page.test_edit_keyword.text == "关键词规则更新成功"

    def test_delete_response(self, browser, base_url):
        """ 删除关键词回复"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.automatic_response)
        page.automatic_response.click()
        PageWait(page.keyword_response_delete)
        page.keyword_response_delete.click()
        PageWait(page.delete_keyword_submit)
        page.delete_keyword_submit.click()
        assert page.test_delete_keyword.text == "关键词规则删除成功"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_07_automatic_response.py"])