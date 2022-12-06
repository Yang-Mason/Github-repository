import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from poium import PageWait

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.channel_page import ChannelPage


class TestImageText:

    def test_new_single_imagetext(self, browser, base_url):
        """ 新增群发单图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.new_imagetext.click()
        PageWait(page.single)
        page.single.click()
        PageWait(page.single_title)
        page.single_title = "test-single"
        sleep(1)
        page.single_add_picture.click()
        PageWait(page.single_select_picture)
        page.single_select_picture.click()
        page.single_nextstep.click()
        sleep(1)
        page.single_submit1.click()
        sleep(1)
        page.single_vxpicture.click()
        PageWait(page.single_select_picture)
        page.single_select_picture.click()
        page.single_nextstep.click()
        PageWait(page.single_submit2)
        page.single_submit2.click()
        assert page.imagetext_test.text == "test-single"

    def test_search_single_imagetext(self, browser, base_url):
        """ 搜索群发单图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        PageWait(page.single_search)
        page.single_search = "test-single"
        sleep(1)
        page.immediate_screen_single.click()
        PageWait(page.imagetext_test)
        assert page.imagetext_test.text == "test-single"

    def test_edit_single_imagetext(self, browser, base_url):
        """ 编辑群发单图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        PageWait(page.single_edit)
        page.single_edit.click()
        sleep(1)
        page.single_title.click()
        page.single_title = "-edit"
        sleep(1)
        page.single_submit2.click()
        assert page.imagetext_test.text == "test-single-edit"

    def test_delete_single_imagetext(self, browser, base_url):
        """ 删除群发单图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        PageWait(page.single_delete)
        page.single_delete.click()
        PageWait(page.delete_submit)
        page.delete_submit.click()
        sleep(1)
        assert page.test_delete_multi.text == "图文删除成功"

    def test_new_multi_imagetext(self, browser, base_url):
        """ 新增群发多图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.new_imagetext.click()
        PageWait(page.multi)
        page.multi.click()
        # 填写一级图文
        PageWait(page.multi_title)
        page.multi_title = "test-multi1"
        sleep(1)
        page.multi_add_picture.click()
        sleep(1)
        page.multi_select_picture.click()
        page.multi_nextstep.click()
        sleep(1)
        page.multi_submit1.click()
        sleep(1)
        page.multi_vxpicture.click()
        PageWait(page.multi_select_picture)
        page.multi_select_picture.click()
        page.multi_nextstep.click()
        sleep(1)
        page.multi_submit2.click()
        # 填写二级图文
        sleep(1)
        page.multi_title = "test-multi2"
        sleep(1)
        page.multi_add_picture.click()
        PageWait(page.multi_select_picture)
        page.multi_select_picture.click()
        page.multi_nextstep.click()
        sleep(1)
        page.multi_submit1.click()
        sleep(1)
        page.multi_vxpicture.click()
        PageWait(page.multi_select_picture)
        page.multi_select_picture.click()
        page.multi_nextstep.click()
        sleep(1)
        page.multi_submit2.click()
        assert page.multi_test.text == "test-multi1"

    def test_edit_multi_imagetext(self, browser, base_url):
        """ 编辑群发多图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        PageWait(page.multi_edit)
        page.multi_edit.click()
        sleep(1)
        page.multi_title.click()
        page.multi_title = "-edit"
        sleep(1)
        page.multi_submit2.click()
        assert page.multi_test.text == "test-multi1-edit"

    def test_delete_multi_imagetext(self, browser, base_url):
        """ 删除群发多图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        PageWait(page.multi_delete)
        page.multi_delete.click()
        PageWait(page.delete_submit_multi)
        page.delete_submit_multi.click()
        sleep(1)
        assert page.test_delete_multi.text == "图文删除成功"

    def test_new_senior_imagetext(self, browser, base_url):
        """ 新增带参数的高级图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.senior_imagetext.click()
        sleep(1)
        page.new_senior.click()
        sleep(1)
        page.senior_title = "test-senior"
        page.dynamic_parameter.click()
        sleep(1)
        page.dropdown_box.click()
        PageWait(page.dropdown_box_sex)
        page.dropdown_box_sex.click()
        PageWait(page.dropdown_box_submit)
        page.dropdown_box_submit.click()
        sleep(1)
        page.senior_add_picture.click()
        PageWait(page.senior_select_picture)
        page.senior_select_picture.click()
        page.senior_nextstep.click()
        sleep(1)
        page.senior_submit1.click()
        sleep(1)
        page.senior_link = "http://www.baidu.com"
        sleep(1)
        page.senior_submit2.click()
        assert page.test_add_senior.text == "test-senior顾客"
        
    def test_search_senior_imagetext(self, browser, base_url):
        """ 搜素高级图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.senior_imagetext.click()
        PageWait(page.senior_input)
        page.senior_input = "test-senior"
        sleep(1)
        page.immediate_screen_senior.click()
        assert page.test_add_senior.text == "test-senior顾客"

    def test_edit_senior_imagetext(self, browser, base_url):
        """ 编辑高级图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.senior_imagetext.click()
        PageWait(page.senior_edit)
        page.senior_edit.click()
        sleep(1)
        page.senior_title.click()
        page.senior_title = "-edit"
        sleep(1)
        page.senior_submit2.click()
        assert page.test_add_senior.text == "test-senior顾客-edit"

    def test_delete_senior_imagetext(self, browser, base_url):
        """ 删除高级图文 """
        page = ChannelPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.imagetext_management)
        page.imagetext_management.click()
        sleep(2)
        page.senior_imagetext.click()
        PageWait(page.senior_delete)
        page.senior_delete.click()
        PageWait(page.senior_delete_submit)
        page.senior_delete_submit.click()
        sleep(1)
        assert page.test_delete_senior.text == "图文删除成功"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_03_imagetext.py"])
