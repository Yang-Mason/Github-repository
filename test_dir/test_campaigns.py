import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.marketing_page import MarketingPage
from page.login_page import LoginPage
from poium import PageWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCampaigns:
    """
    def test_login(self, browser):
        ''' 登录'''
        page = LoginPage(browser)
        page.get("https://staging.quncrm.com/site/login")
        page.login_username = "17864199421@163.com"
        page.login_password = "Szz1996yyyy"
        PageWait(page.login_sign)
        page.login_sign.click()
        PageWait(page.login_channel)
        page.login_channel.click()
        sleep(2)
    """

    def test_New_Campaign_tpye01(self, browser, base_url):
        """
        创建营销活动
           类型：由客户主动触发的活动
           名称：'AutoCampaign_客户主动触发'
           目标客户群：选择所有客户
           客户进入规则：允许同一个客户重复进入
           活动触发条件：向微信公众号发消息，限定属性，限定次数和时间
           动作：发送微信消息- 图文

        """
        CAMPAIGN_NAME = 'AutoCampaign_type1'
        LIMIT_TIMES = '2'
        LIMIT_DAYS = '31'
        GRAPGIC_NAME = 'AutoTest_GraphicMsg'
        page = MarketingPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(4)
        """ 新增活动"""
        page.new_campaign_btn.click()
        sleep(5)
        page.campaign_name_input = CAMPAIGN_NAME
        sleep(2)
        page.customer_entry_rule_checkbox.click()
        page.select_customer_behaviors_dropdown.click()
        PageWait(page.behavior_WechatEvents)
        page.behavior_WechatEvents.click()
        page.behavior_WechatEvents_sendWechatMsgToAccunt.click()
        sleep(1)
        """ 限定属性"""
        page.limit_property_checkbox.click()
        page.limit_checkbox_times.click()
        page.select_or_input_WeChatAccountName.click()
        sleep(1)
        page.select_or_input_WeChatAccountName = "群硕测试2"
        sleep(1)
        page.select_wechat_account1.click()  # 选择“群硕测试2”
        page.next_btn.click()
        """ 限定次数+限定时间"""
        page.limit_times_input = LIMIT_TIMES
        page.limit_time_dropdown.click()
        page.limit_time_limt_time.click()
        page.days_input = LIMIT_DAYS
        """ 点击下一步"""
        page.next_btn.click()
        sleep(10)  # 等待页面加载
        """ 添加动作：发微信消息- 图文"""
        PageWait(page.add_btn)
        page.add_btn.click()
        sleep(3)
        PageWait(page.action_btn)
        page.action_btn.click()
        PageWait(page.action_send_wechat)
        page.action_send_wechat.click()
        page.please_select_account.click()
        sleep(1)
        page.select_wechat_account2.click()  # 选择渠道
        page.graphic_message_menu.click()  # 点击“设置微信消息- 图文”
        sleep(3)  # 等待图文选择框弹出
        """ 选择图文"""
        PageWait(page.graphic_message_popup_searchbox)
        page.graphic_message_popup_searchbox = GRAPGIC_NAME  # 输入图文名称
        sleep(3)
        page.graphic_message_popup_searchbox = Keys.ENTER  # 点击Enter键搜索
        sleep(2)  # 等待搜索
        page.graphic_message_search_result_1.click()  # 点击第一个搜索结果
        sleep(1)
        page.graphic_message_popup_ok_btn.click()
        sleep(1)
        """ 保存动作"""
        page.wechat_ok_btn.click()
        sleep(2)
        """ 添加结束"""
        page.add_btn.click()
        PageWait(page.end_btn)
        page.end_btn.click()
        """ 保存活动"""
        page.save_btn.click()
        sleep(3)
        """ 返回营销活动管理页面"""
        page.Campaigns.click()  # 点击左侧菜单
        assert page.tr1_campaign_name.text == CAMPAIGN_NAME

    def test_Delete_Campaign_type1(self, browser, base_url):
        """
        删除营销活动
        """
        page = MarketingPage(browser)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        page.tr1_operation_delete.click()
        page.confirm_ok_btn.click()
        PageWait(page.toast_sucess)
        assert page.toast_sucess.text == '删除营销活动成功'

    def test_New_Campaign_tpye02(self, browser, base_url):
        """
        创建营销活动
           类型：由特殊规则触发的活动
           名称：'AutoCampaign_特殊规则触发'
           目标客户群：按标签选择客户
           特殊规则：默认生日营销-生日当天00:00
           动作：发送短信

        """
        CAMPAIGN_NAME = 'AutoCampaign_type2'
        CONTENT = '微信文本：生日快乐！'
        page = MarketingPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        """新增活动"""
        page.new_campaign_btn.click()
        sleep(5)
        page.campaign_type2.click()
        sleep(2)
        page.campaign_name_input = CAMPAIGN_NAME
        sleep(2)
        """
        目标客户-按标签
        方式1：点击指定的一级标签以及对应的二级标签
        """
        page.customers_by_label.click()
        sleep(2)
        page.label_input.click()
        PageWait(page.label_select1)
        page.label_select1.click()
        page.label_select2.click()
        """
        目标客户-按标签
        方式2：输入标签进入搜索，选择标签结果
        page.customers_by_label.click()
        sleep(2)
        page.label_input.click()
        sleep(2)
        page.label_input = LABEL
        sleep(2)
        page.search_result_0.click()
        sleep(2)
        """
        """点击下一步"""
        page.next_btn.click()
        sleep(10)
        """添加动作：发短信"""
        PageWait(page.add_btn)
        page.add_btn.click()
        sleep(3)
        PageWait(page.action_btn)
        page.action_btn.click()
        sleep(1)
        PageWait(page.action_send_msg)
        page.action_send_msg.click()  # 动作-发短信
        page.msg_content_textarea = CONTENT
        sleep(1)
        page.msg_ok_btn.click()
        """添加结束"""
        page.add_btn.click()
        PageWait(page.end_btn)
        page.end_btn.click()
        """保存活动"""
        page.save_btn.click()
        sleep(3)
        """返回营销活动管理页面"""
        page.Campaigns.click()  # 点击左侧菜单
        assert page.tr1_campaign_name.text == CAMPAIGN_NAME

    def test_Delete_Campaign_type2(self, browser, base_url):
        """
        删除营销活动：
        """
        page = MarketingPage(browser)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        page.tr1_operation_delete.click()
        page.confirm_ok_btn.click()
        PageWait(page.toast_sucess)
        assert page.toast_sucess.text == '删除营销活动成功'

    def test_New_Campaign_tpye03(self, browser, base_url):
        """
        创建营销活动
           类型：即时触发的活动
           名称：'AutoCampaign_即时触发'
           目标客户群：按群组选择客户
           动作：发放优惠券

        """
        CAMPAIGN_NAME = 'AutoCampaign_type3'
        page = MarketingPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        """新增活动"""
        page.new_campaign_btn.click()
        sleep(5)
        page.campaign_type3.click()
        sleep(2)
        page.campaign_name_input = CAMPAIGN_NAME
        sleep(2)
        """目标客户-按群组-动态群组"""
        page.customers_by_group.click()
        page.label_input.click()
        sleep(2)
        PageWait(page.dynamic_group1)
        page.dynamic_group1.click()
        page.dynamic_group2.click()
        page.i_help_tip.click()
        """点击下一步"""
        page.next_btn.click()
        sleep(10)
        """添加动作：发放优惠券"""
        PageWait(page.add_btn)
        page.add_btn.click()
        sleep(3)
        PageWait(page.action_btn)
        page.action_btn.click()
        sleep(1)
        PageWait(page.action_send_coupon)
        page.action_send_coupon.click()
        sleep(2)
        page.please_select_coupon_dropdown.click()
        sleep(3)
        page.specific_coupon.click()  # 点击指定优惠券
        sleep(3)
        # 点击“全部优惠券类型”下拉列表，防止“确定”按钮元素被遮盖。遇到多选都有这个问题，因为下拉列表不会自动收起
        page.Issue_coupon_all_type.click()
        sleep(1)
        page.Issue_coupon_ok_btn.click()
        sleep(2)
        """添加结束"""
        page.add_btn.click()
        PageWait(page.end_btn)
        page.end_btn.click()
        """保存活动"""
        page.save_btn.click()
        sleep(3)
        """返回营销活动管理页面"""
        page.Campaigns.click()  # 点击左侧菜单
        assert page.tr1_campaign_name.text == CAMPAIGN_NAME

    def test_Edit_Campaign_type03(self, browser, base_url):
        """
        编辑营销活动：
        编辑营销活动名称
        添加动作变更客户属性 - 职位
        """
        COMPAIGN_Edited_NAME = "Edited_AutoCampaign"
        page = MarketingPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        """编辑活动"""
        page.tr1_operation_edit.click()
        sleep(10)
        """ 编辑活动名称"""
        PageWait(page.edit_info_btn)
        page.edit_info_btn.click()
        sleep(6)
        page.edit_form_campaign_name_input.clear()  # 清除已有营销活动的名称
        page.edit_form_campaign_name_input = COMPAIGN_Edited_NAME
        sleep(1)
        page.edit_form_ok_btn.click()
        sleep(3)
        """鼠标hover"""
        action = ActionChains(browser)
        above = page.hover_line
        browser.execute_script("arguments[0].scrollIntoView();", above)  # 拖动到可见的元素去
        sleep(2)
        action.move_to_element(above).perform()
        sleep(2)
        """等待+出现并且点击"""
        PageWait(page.add_visible_btn)
        page.add_visible_btn.click()
        sleep(3)
        PageWait(page.action_btn)
        page.action_btn.click()
        """变更客户属性"""
        page.action_act_attr.click()  # 点击动作-变更客户属性
        sleep(1)
        page.please_select_customer_properties.click()  # 点击请选择客户属性的下拉框
        page.property_position.click()  # 选择客户属性 - 职位
        PageWait(page.please_select_positions)
        page.please_select_positions.click()  # 选择职位
        PageWait(page.property_position_value)
        page.property_position_value.click()
        page.property_ok_btn.click()
        sleep(1)
        """保存活动"""
        page.save_btn.click()
        sleep(3)
        """返回营销活动管理页面"""
        page.Campaigns.click()
        sleep(2)  # 点击左侧菜单
        assert page.tr1_campaign_name.text == COMPAIGN_Edited_NAME

    def test_Delete_Campaign_type03(self, browser, base_url):
        """
        删除营销活动：
        """
        page = MarketingPage(browser)
        browser.implicitly_wait(10)
        page.get(base_url)
        PageWait(page.More_Nav)
        page.More_Nav.click()
        sleep(1)
        page.Intelligent_Marketing.click()
        sleep(2)
        page.tr1_operation_delete.click()
        page.confirm_ok_btn.click()
        PageWait(page.toast_sucess)
        assert page.toast_sucess.text == '删除营销活动成功'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_campaigns.py"])
