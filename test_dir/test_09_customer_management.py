import datetime
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.login_page import LoginPage
from page.customer_page import CustomerPage


class TestLogin:

    def test_login(self, browser):
        page = LoginPage(browser)
        page.get("https://staging.quncrm.com/site/login")
        page.login_username = "17864199421@163.com"
        page.login_password = "Szz1996yyyy"
        page.login_sign.click()
        sleep(2)
        page.login_channel.click()
        sleep(2)

    def test_new_customer(self, browser, base_url):
        """ 新增客户 """
        page = CustomerPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        sleep(2)
        page.customer.click()
        sleep(2)
        page.new_customer.click()
        sleep(2)
        now_time1 = datetime.datetime.now().strftime('%m%d')
        now_time2 = datetime.datetime.now().strftime('%H%M%S')
        page.name_input = now_time1 + "matest"
        page.phone_input = "1" + now_time1 + now_time2
        sleep(1)
        page.new_customer_submit.click()
        assert page.test_new_customer.text == "客户创建成功"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_09_customer_management.py"])
