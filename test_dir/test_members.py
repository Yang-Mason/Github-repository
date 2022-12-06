import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.member_page import MemberPage
from page.login_page import LoginPage
from poium import PageWait


class TestMemberManagement:
    def test_login(self, browser):
        page = LoginPage(browser)
        page.get("https://staging.quncrm.com/site/login")
        page.login_username = "2436905449@qq.com"
        page.login_password = "STJstj123"
        page.login_sign.click()
        PageWait(page.login_account)
        page.login_account.click()
        sleep(1)

    def test_SearchByName(self, browser, base_url):
        '''搜索会员- 按姓名'''
        page = MemberPage(browser)
        page.get(base_url)
        PageWait(page.MemberNav)
        page.MemberNav.click()
        sleep(2)
        page.search_input = 'Tingjie'
        sleep(5)
        page.search_btn.click()
        sleep(5)
        assert page.searchResult_ExpectNickname.text == '*ingjie'

    def test_SearchByPhone(self, browser, base_url):
        '''搜索会员- 按手机号码'''
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.search_input = '18516779528'
        sleep(5)
        page.search_btn.click()
        sleep(5)
        assert page.searchResult_ExpectPhone.text == '185****9528'

    def test_SearchByMemberCard(self, browser, base_url):
        '''搜索会员- 按会员卡号 '''
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.search_input = '20605167'
        sleep(5)
        page.search_btn.click()
        sleep(5)
        assert page.searchResult_ExpectCardNo.text == '20605167'

    def test_TagLabel(self, browser, base_url):
        '''全选会员-打标签'''
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.Checkbox_ALL.click()
        page.Member_Classification.click()
        PageWait(page.Member_TagLabel)
        page.Member_TagLabel.click()
        page.lbl_input.click()
        sleep(5)
        PageWait(page.lbl_group)
        page.lbl_group.click()
        PageWait(page.lbl_select)
        page.lbl_select.click()
        page.Ok_btn.click()
        assert page.Toast_sucess_tip.text == '标签设置成功'

    def test_Activecard(self, browser, base_url):
        '''全选会员-激活会员卡'''
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.Checkbox_ALL.click()
        page.Business_Operation.click()
        PageWait(page.Business_Operation_ActivateCard)
        page.Business_Operation_ActivateCard.click()
        sleep(1)
        page.Ok_btn.click()
        sleep(1)  # 关键sleep
        assert page.Toast_sucess_tip.text == '激活会员卡成功'

    def test_Issue_Active_card(self, browser, base_url):
        '''全选会员-发放-激活会员卡'''
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.Checkbox_ALL.click()
        page.Business_Operation.click()
        PageWait(page.Business_Operation_IssueCard)
        page.Business_Operation_IssueCard.click()
        sleep(1)  # 关键sleep
        page.IssueCard_drop.click()
        PageWait(page.IssueCard_firstcard)
        page.IssueCard_firstcard.click()
        sleep(1)
        page.IssueCard_Checkbox_ActiveCard.click()
        sleep(1)
        page.Ok_btn.click()
        sleep(1)  # 关键sleep
        assert page.Toast_sucess_tip.text == '发放会员卡成功'

    def test_Issuance_addPoint(self, browser, base_url):
        '''全选会员-发放积分'''
        ADDPOINT_VAlUE = "500"
        DESCRIPTION = "积分奖励：自动化测试添加积分"
        page = MemberPage(browser)
        page.get(base_url)
        page.MemberNav.click()
        sleep(2)
        page.Checkbox_ALL.click()
        page.Business_Operation.click()
        PageWait(page.Business_Operation_Manual_Issuance)
        page.Business_Operation_Manual_Issuance.click()
        sleep(2)  # 关键sleep
        page.Manual_Issuance_Input_Point = ADDPOINT_VAlUE
        page.Manual_Issuance_Input_description = DESCRIPTION
        page.Ok_btn.click()
        sleep(1)  # 关键sleep
        assert page.Toast_sucess_tip.text == '积分发放成功'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_members.py"])
