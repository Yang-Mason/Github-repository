import sys
from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage


class TestInteractive:

    def test_search_interactive(self, browser, base_url):
        """ 按内容搜索消息"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.interactive_news)
        page.interactive_news.click()
        sleep(1)
        page.interactive_input = "test-interactive"
        page.interactive_input = Keys.ENTER
        sleep(1)
        assert page.test_interactive_search.text == "test-interactive"

    def test_send_text_message(self, browser, base_url):
        """ 给用户发送文本消息"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.interactive_news)
        page.interactive_news.click()
        sleep(1)
        page.interactive_input = "test-interactive"
        page.interactive_input = Keys.ENTER
        sleep(1)
        page.interactive_reply.click()
        page.interactive_replyinput = "test-interactive-reply-news"
        sleep(1)
        page.interactive_send.click()
        assert page.test_send_interactive.text == "成功发送消息"

    def test_send_imagetext_message(self, browser, base_url):
        """ 给用户发送图文消息"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.interactive_news)
        page.interactive_news.click()
        sleep(1)
        page.interactive_input = "test-interactive"
        page.interactive_input = Keys.ENTER
        sleep(1)
        page.interactive_reply.click()
        page.interactive_imagetext.click()
        sleep(1)
        page.interactive_search_imagetext = "mason-test-interactive"
        page.interactive_search_imagetext = Keys.ENTER
        page.interactive_select_imagetext.click()
        page.interactive_submit.click()
        sleep(1)
        page.interactive_send.click()
        assert page.test_send_interactive.text == "成功发送消息"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_05_interactive.py"])