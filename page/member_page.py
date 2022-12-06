from poium import Page, PageElement, PageElements
'''
author: wendy.shi
module：会员管理
'''
class MemberPage(Page):
    MemberNav = PageElement(xpath="/html/body/nav/ul[1]/li[3]/a", describe="顶部导航栏-会员")
    Member_management = PageElement(link_text="会员管理")
    MemberCard_management = PageElement(link_text="会员卡管理")
    Member_Incentives = PageElement(link_text="会员激励")
    WeChat_Member_Cards = PageElement(link_text="微信会员卡")
    Ponits_Expiration_Settings = PageElement(link_text="积分过期设置")

    '''
    会员管理
    按会员姓名、手机号、会员卡号搜索
    '''
    search_input = PageElement(xpath="//input[@type='search']",describe ='会员搜索框')
    search_btn = PageElement(xpath="//button[@class='os button info ng-binding']",describe ='搜索确定按钮')
    searchResult_NoData = PageElement(xpath="//div[@class='member member-wrapper advanced-list ng-scope']/div[3]/div[2]",describe ='暂无数据')
    searchResult_ExpectNickname = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr[1]/td[1]/span/span",describe ='搜索结果中第一行第一列的值')
    searchResult_ExpectPhone = PageElement(xpath='/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr/td[2]/span/span',describe='预期手机号')
    searchResult_ExpectCardNo =PageElement(xpath='/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr[1]/td[4]/span')

    '''
    会员批量打标签
    '''
    Checkbox_ALL = PageElement(xpath="//span[@translate='all']",describe='全选checkbox')
    Member_Classification = PageElement(xpath="//div[@class='left-operation-wrapper']/div[2]/div/span",describe='会员分类')
    Member_TagLabel = PageElement(xpath="//div[@class='left-operation-wrapper']/div[2]/div/ul", describe='打标签')
    lbl_input = PageElement(xpath="//ul[@class='labels group']",describe='-请输入或选择-')
    lbl_group = PageElement(xpath="//div[contains(@class,'cascade-select-menu')]/ul[1]/li[3]/span[1]",describe='选择基本属性这个标签分组')
    lbl_select = PageElement(xpath ="//span[@wm-tooltip='青年']",describe= '选择基本属性-青年这个标签')
    Ok_btn = PageElement(xpath="//button[@translate='ok']",describe='确定按钮')
    Toast_sucess_tip = PageElement(xpath="//span[@class='text']",describe='标签设置成功的toast')
    
    '''
    业务操作
    '''

    Business_Operation = PageElement(xpath="//div[@class='left-operation-wrapper']/div[3]",describe='业务操作')
    Business_Operation_ActivateCard = PageElement(xpath="//div[@class='left-operation-wrapper']/div[3]/div/ul/li[1]",describe='激活会员卡')
    Business_Operation_IssueCard =PageElement(xpath="//div[@class='left-operation-wrapper']/div[3]/div/ul/li[2]",describe='发放会员卡')
    Business_Operation_Manual_Issuance = PageElement(xpath="//div[@class='left-operation-wrapper']/div[3]/div/ul/li[3]",describe='奖扣积分')
    IssueCard_drop = PageElement(xpath="/html/body/div[8]/div/div/div/form/div[1]/div[3]/div[1]/div",describe='请选择')
    IssueCard_firstcard = PageElement(xpath="//body/div[9]/ul/li[1]",describe='会员卡列表中第一张会员卡')
    IssueCard_Checkbox_ActiveCard = PageElement(xpath="//div[@class='issue-card-form-content']/div[2]/div/label[@class='ng-scope']",describe='发放后自动激活会员卡的复选框')
    Manual_Issuance_Input_Point = PageElement(xpath="//input[@os-form-tip='customert_point_input_string']",describe='积分输入框')
    Manual_Issuance_Input_description = PageElement(xpath="//textarea[@name='rule']",describe='描述')