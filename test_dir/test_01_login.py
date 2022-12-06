import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage


class TestLogin:

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


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_01_login.py"])