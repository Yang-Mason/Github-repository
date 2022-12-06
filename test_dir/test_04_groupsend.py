import sys
from time import sleep
import pytest
import datetime
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage
from page.login_page import LoginPage


class TestGroupsend:

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

    def test_new_groupsend1(self, browser, base_url):
        """ 新增按群组选择的群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.group_sending)
        page.group_sending.click()
        sleep(1)
        page.groupsend_new_ordinary.click()
        sleep(3)
        page.groupsend_select_object.click()
        page.groupsend_group.click()
        sleep(1)
        page.groupsend_select_group.click()
        sleep(1)
        page.groupsend_select_group = "masontest_群发"
        sleep(1)
        page.groupsend_submit_group.click()
        page.groupsend_content.click()
        page.groupsend_content = "test-groupsend-immediately"
        sleep(1)
        page.groupsend_submit1.click()
        sleep(1)
        page.groupsend_submit2.click()
        assert page.test_new_groupsend.text == "群发消息创建成功,请稍后刷新已发送列表"

    def test_new_groupsend2(self, browser, base_url):
        """ 新增按微信标签的群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.group_sending)
        page.group_sending.click()
        sleep(1)
        page.groupsend_new_ordinary.click()
        sleep(3)
        page.groupsend_select_object.click()
        page.groupsend_vxlabel.click()
        sleep(1)
        page.groupsend_select_vxlabel.click()
        sleep(1)
        page.groupsend_submit_vxlabel.click()
        page.groupsend_content = "test-groupsend-immediately"
        sleep(1)
        page.groupsend_submit1.click()
        sleep(1)
        page.groupsend_submit2.click()
        assert page.test_new_groupsend.text == "群发消息创建成功,请稍后刷新已发送列表"

    def test_new_timing_groupsend(self, browser, base_url):
        """ 新增定时群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.group_sending)
        page.group_sending.click()
        sleep(1)
        page.groupsend_new_ordinary.click()
        sleep(3)
        page.groupsend_select_object.click()
        page.groupsend_vxlabel.click()
        sleep(1)
        page.groupsend_select_vxlabel.click()
        sleep(1)
        page.groupsend_submit_vxlabel.click()
        page.groupsend_content = "test-groupsend-timing"
        sleep(1)
        page.groupsend_new_timing.click()
        now_time1 = datetime.datetime.now().strftime('%Y%m%d')
        now_time2 = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime('%H%M')
        page.groupsend_time1 = now_time1
        sleep(1)
        page.groupsend_time2 = now_time2
        sleep(1)
        page.groupsend_submit1.click()
        sleep(1)
        page.groupsend_submit3.click()
        assert page.test_new_timing_groupsend.text == "群发消息创建成功"

    def test_edit_timing_groupsend(self, browser, base_url):
        """ 编辑定时群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.group_sending)
        page.group_sending.click()
        PageWait(page.groupsend_edit)
        page.groupsend_edit.click()
        sleep(3)
        page.groupsend_content.click()
        page.groupsend_content = "-edit"
        sleep(1)
        page.groupsend_submit1.click()
        sleep(1)
        page.groupsend_submit3.click()
        assert page.test_edit_timing_groupsend.text == "群发消息更新成功"

    def test_delete_timing_groupsend(self, browser, base_url):
        """ 删除定时群发"""
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.group_sending)
        page.group_sending.click()
        PageWait(page.groupsend_delete)
        page.groupsend_delete.click()
        PageWait(page.groupsend_submit4)
        page.groupsend_submit4.click()
        assert page.test_delete_timing_groupsend.text == "群发删除成功"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_04_groupsend.py"])