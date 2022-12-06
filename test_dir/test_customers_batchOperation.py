import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.customer_page import CustomerPage
from page.login_page import LoginPage
from poium import PageWait

class TestCustomer: 

    def test_login(self, browser):
        page = LoginPage(browser)
        page.get("https://staging.quncrm.com/site/login")
        page.login_username = "2436905449@qq.com"
        page.login_password = "STJstj123"
        page.login_sign.click()
        PageWait(page.login_account)
        page.login_account.click()
        sleep(1)


    def test_batch_staticGroup_addPoint(self,browser,base_url):
        '''
        批量对象：动态群组->WS漏斗分析-动态群组
        操作备注：
        设置批量操作：添加积分->500 ; 减扣积分->500

        '''
        remarks ="批量操作备注：自动化测试"
        points ="500"
        page = CustomerPage(browser)
        page.get(base_url)
        page.customer.click()
        page.batch_operation.click()
        sleep(2)
        PageWait(page.new_batch_btn)
        page.new_batch_btn.click()
        sleep(5)  # 页面跳转较慢，需要等待的时间更长
        PageWait(page.select_operatiton_objects_drop)
        page.select_operatiton_objects_drop.click()
        sleep(1)
        page.objects_byGroup.click()
        sleep(1)
        page.select_group_drop.click()
        page.object_Static_group.click()
        sleep(3)
        page.object_Static_group_01.click()        # 指定静态群组： 漏斗分析-静态wendy 
        page.operation_remarks = remarks
        page.operation_select_an_operation.click()
        PageWait(page.operation_addPoints)   
        page.operation_addPoints.click()            # 点击“添加积分”
        page.operation_InputPonit = points
        page.superimpose_an_operation.click()       # 点击“叠加操作”
        PageWait(page.operation_select_an_operation2)
        page.operation_select_an_operation2.click() # 点击第二个“请选择操作”
        sleep(5)
        PageWait(page.operation_reductPoints)
        page.operation_reductPoints.click()         # 点击“减扣积分”
        sleep(2)
        page.operation_InputPonit = points
        page.action_btn.click()
        sleep(5)
        assert page.row_operation_remark.text == remarks











if __name__ == '__main__':
   pytest.main(["-v", "-s", "test_customers_batchOperation.py"])