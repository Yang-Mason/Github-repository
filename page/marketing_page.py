from poium import Page, PageElement, PageElements

'''
author: wendy.shi
module：智能营销
'''


class MarketingPage(Page):
    """========菜单========="""
    More_Nav = PageElement(link_text="更多")
    Intelligent_Marketing = PageElement(link_text="智能营销")
    Campaigns = PageElement(link_text="营销活动")

    '''========新增营销========='''
    new_campaign_btn = PageElement(link_text="新增营销活动")

    '''新增营销 -> 选择营销活动类型'''
    campaign_type2 = PageElement(xpath="//div[@class='condition-item ng-scope']", describe='营销活动类型2')
    campaign_type3 = PageElement(xpath="//div[@class='condition-item ng-scope last-border']", describe='营销活动类型3')

    '''新增营销 -> 营销活动名称'''
    campaign_name_input = PageElement(xpath="//input[@id='name']", describe='营销活动名称输入框')

    '''新增营销 -> 目标客户群'''
    customers_all = PageElement(xpath="//div[@class='form-group']/div[2]/div", describe='选择所有客户')
    # customers_by_label = PageElement(xpath="//div[@class='form-group']/div[3]/div", describe='按标签选择客户')  #也可以这么写
    # customers_by_group = PageElement(xpath="//div[@class='form-group']/div[5]/div", describe='按群组选择客户')
    customers_by_label = PageElement(xpath="//span[text()='按标签选择客户']")  # 可以这么写
    customers_by_group = PageElement(xpath="//span[text()='按群组选择客户']")  # 可以这么写
    label_input = PageElement(xpath="//input[@class='search ng-pristine ng-valid']", describe='标签/群组的通用输入框')
    search_result_0 = PageElement(xpath="//body/div[6]/ul[3]/li[1]", describe='输入标签后匹配打牌的第一个结果')
    label_select1 = PageElement(xpath="//span[text()='Test']", describe='一级标签：Test')
    label_select2 = PageElement(xpath="//span[text()='wendy测试营销专业标签']", describe='一级标签：Test')
    dynamic_group1 = PageElement(xpath="//span[text()='动态群组']", describe='动态群组')
    dynamic_group2 = PageElement(xpath="//span[text()='WS漏斗分析-动态群组']", describe='动态群组-WS漏斗分析-动态群组')
    static_group1 = PageElement(xpath="//span[text()='静态群组']", describe='静态群组')
    static_group2 = PageElement(xpath="//span[text()='漏斗分析-静态wendy']", describe='静态群组-漏斗分析-静态wendy')
    i_help_tip = PageElement(xpath="//i[@class='scrmfont i-common-point i-help-tip ng-scope']",
                             describe='提示语：系统会过滤重复的客户')

    '''新增营销 -> 客户进入规则'''
    customer_entry_rule_checkbox = PageElement(
        xpath="//div[@class='os checkbox ng-isolate-scope ng-pristine ng-valid']/label/span", describe='允许同一个客户重复进入')

    '''下一步'''
    next_btn = PageElement(xpath="//button[@class='os success button ng-scope']", describe='下一步')

    '''新增营销 -> 触发条件for由客户主动触发的活动'''

    select_customer_behaviors_dropdown = PageElement(xpath="//div[@class='os dropdown selection']", describe='请选择客户行为')
    behavior_WechatEvents = PageElement(xpath="//span[text()=' 微信事件 ']", describe='微信事件')
    behavior_WechatEvents_FollowAccount = PageElement(xpath="//span[text()=' 关注微信公众号 ']", describe='微信事件->关注微信公众号')
    behavior_WechatEvents_sendWechatMsgToAccunt = PageElement(xpath="//span[text()=' 向微信公众号发消息 ']",
                                                              describe='微信事件->向微信公众号发消息')
    limit_property_checkbox = PageElement(xpath="//label/span[@translate='marketing_automation_limit_property']",
                                          describe='限定属性')
    select_or_input_WeChatAccountName = PageElement(xpath="//input[@class='search ng-pristine ng-valid']",
                                                    describe='请输入或选择公众号名称')
    select_wechat_account1 = PageElement(xpath="//span[text()='群硕测试2']", describe='群硕测试2')
    left_part_area = PageElement(xpath="//div[@class='left-part']", describe='页面左侧区域')
    limit_checkbox_times = PageElement(xpath="//label/span[@translate='marketing_automation_limit_times']",
                                       describe='限定次数')
    limit_times_input = PageElement(xpath="//input[@name='times']", describe='限定次数输入框')
    limit_time_dropdown = PageElement(xpath="//div[@class='select-limit-times ng-scope']/div[2]/div/i",
                                      describe='不限时间的下拉小三角')
    limit_time_limt_time = PageElement(xpath="//span[text()=' 限定时间 ']", describe='限定时间')
    days_input = PageElement(xpath="//input[@name='reserveDays']", describe='请输入天数的输入框')

    '''===========流程============='''
    edit_info_btn = PageElement(xpath="//span[@class='scrmfont i-common-edit i-primary-circle ng-scope']",
                                describe='info的编辑按钮')
    edit_form_campaign_name_input = PageElement(xpath="//form[@name='editStartConditionForm']//input[@id='name']",
                                                describe='营销活动名称的编辑输入框')  # 省略路径使用//
    edit_form_ok_btn = PageElement(xpath="//button[@class='os success button ng-scope']", describe='info弹窗的确定按钮')
    add_btn = PageElement(xpath="//div[@class='add scrmfont i-common-add']", describe='+按钮')
    action_btn = PageElement(xpath="//i[@class='scrmfont i-marketing-action']", describe='动作')
    flow_btn = PageElement(xpath="//i[@class='scrmfont i-marketing-flow']", describe='流程控制')
    end_btn = PageElement(xpath="//i[@class='scrmfont i-marketing-end']", describe='结束')
    save_btn = PageElement(xpath="//button[@class='os button success ng-scope']", describe='保存营销活动的按钮')
    cancel_btn = PageElement(xpath="//button[@class='os button default ng-scope']", describe='取消营销活动的按钮')
    hover_line = PageElement(xpath="//*[name()='svg']/*[name()='path'][1]", describe='end按钮上方的流程线')
    add_visible_btn = PageElement(xpath="//i[@class='scrmfont i-common-add circle-add visible']",
                                  describe='hover后显示+按钮')

    '''流程 -> 动作'''
    action_send_msg = PageElement(xpath="//i[@class='scrmfont i-marketing-msg']", describe='发短信')
    action_send_wechat = PageElement(xpath="//i[@class='scrmfont i-marketing-wechat']", describe='发微信消息')
    action_temp_mes = PageElement(xpath="//i[@class='scrmfont i-marketing-temp_mes']", describe='发模板消息')
    action_email = PageElement(xpath="//i[@class='scrmfont i-marketing-email']", describe='发邮件')
    action_act_tag = PageElement(xpath="//i[@class='scrmfont i-marketing-act-tag']", describe='打标签')
    action_act_attr = PageElement(xpath="//i[@class='scrmfont i-marketing-act-attr']", describe='变更客户属性')
    action_send_coupon = PageElement(xpath="//i[@class='scrmfont i-marketing-coupon']", describe='发放优惠券')
    action_act_member_attr = PageElement(xpath="//i[@class='scrmfont i-marketing-vip1']", describe='变更会员属性')
    action_webh = PageElement(xpath="//i[@class='scrmfont i-marketing-webh']", describe='开发者模式')

    '''流程 -> 动作->发短信'''
    msg_content_textarea = PageElement(xpath="//textarea[@name='content']", describe='短信内容输入框')
    msg_ok_btn = PageElement(xpath="//form[@name='smsSettingForm']/div/button", describe='短信弹窗的确定按钮')
    msg_cancel_btn = PageElement(xpath="//form[@name='smsSettingForm']/div/span", describe='短信弹窗的取消按钮')

    '''流程 -> 动作->发微信消息'''
    please_select_account = PageElement(
        xpath="//div[@class='mb15 dropdown wrapper ng-isolate-scope ng-pristine ng-valid']/div/i",
        describe='设置微信消息，选择微信公众号的下拉小三角')
    select_wechat_account2 = PageElement(xpath="//span[text()=' 群硕测试2 ']", describe='群硕测试2')
    wechat_text_input = PageElement(xpath="//div[@class='message message-text form-control-message']", describe='文本输入框')
    text_menu = PageElement(xpath="//div[@class='type-select']/span[1]", describe='文本')
    graphic_message_menu = PageElement(xpath="//div[@class='type-select']/span[2]", describe='图文')
    graphic_message_popup_searchbox = PageElement(xpath="//input[@type='search']", describe='搜索图文的输入框')
    graphic_message_search_result_1 = PageElement(xpath="//div[@class='waterfall ng-isolate-scope']/div[1]",
                                                  describe='图文搜索结果的第一个图文')
    graphic_message_popup_ok_btn = PageElement(xpath="//button[@class='btn btn-success btn-sm ng-binding']",
                                               describe='图文选择框的确定按钮')
    picture_menu = PageElement(xpath="//div[@class='type-select']/span[3]", describe='图片')
    mini_program_card_menu = PageElement(xpath="//div[@class='type-select']/span[4]", describe='小程序卡片')
    wechat_ok_btn = PageElement(xpath="//form[@ng-submit='tab.submit(wechat)']/div[2]/button", describe='设置微信消息的确定按钮')
    wechat_cancel_btn = PageElement(xpath="//form[@ng-submit='tab.submit(wechat)/div[2]/sapn']", describe='设置微信消息的取消按钮')

    '''流程 -> 动作->发放优惠券'''
    Issue_coupon_all_type = PageElement(
        xpath="//form[@class='issue-coupon-wrapper ng-isolate-scope ng-pristine ng-valid']//div[@class='current-text "
              "text-el text-with-label ng-scope']",
        describe='全部优惠券类型')
    # Issue_coupon_banner_title = PageElement(xpath="//div[@translate='marketing_issue_coupons']",
    # describe='发放优惠券弹出标题--废弃，因为title会被优惠券列表遮挡')
    please_select_coupon_dropdown = PageElement(
        xpath="//form[@class='issue-coupon-wrapper ng-isolate-scope ng-pristine ng-valid']/div//ul/input",
        describe='请输入或选择优惠券')
    select_first_coupon = PageElement(
        xpath="//div[@class='auto-complete-select-menu gray-hover os-dropdown-menu-wrapper ng-scope "
              "ng-isolate-scope']/ul/li[2]/div/input",
        describe='列表中第一张优惠券')
    specific_coupon = PageElement(xpath="//span[text()='漏斗代金券-C1']", describe='指定优惠券：漏斗代金券-C1')
    Issue_coupon_ok_btn = PageElement(xpath="//form[@os-submit='tab.submit(coupon)']/div[2]/button",
                                      describe='发放优惠券的确定按钮')
    Issue_coupon_cancel_btn = PageElement(xpath="//form[@os-submit='tab.submit(coupon)']/div[2]/span",
                                          describe='发放优惠券的取消按钮')

    '''流程 -> 动作->变更客户属性'''
    please_select_customer_properties = PageElement(xpath="//div[@items='customer.properties']/div/i",
                                                    describe='请选择客户属性的下拉小三角')
    property_position = PageElement(xpath="//span[text()=' 职位 ']", describe='下拉属性-职位')
    please_select_positions = PageElement(xpath="//div[@items='customer.propertyOptions']/div/i",
                                          describe='请选择职位的下拉小三角')
    property_position_value = PageElement(xpath="//span[text()=' 总监 ']", describe='选择职位- 总监')
    property_ok_btn = PageElement(xpath="//form[@name='updateCustomerForm']/div[2]/input", describe='变更客户属性的确定按钮')
    property_cancel_btn = PageElement(xpath="//form[@name='updateCustomerForm']/div[2]/span", describe='变更客户属性的取消按钮')

    '''===========营销活动管理页面============='''
    tr1_campaign_name = PageElement(xpath="//tbody/tr[@class='ng-scope']/td[1]/a", describe='列表第一行第一列的活动名称')
    tr1_operation_edit = PageElement(xpath="//td[@data-title-text='operations']/a[1]", describe='列表第一行的编辑')
    tr1_operation_report = PageElement(xpath="//td[@data-title-text='operations']/a[2]", describe='列表第一行的查看报表')
    tr1_operation_copy = PageElement(xpath="//td[@data-title-text='operations']/i[1]", describe='列表第一行的复制')
    tr1_operation_delete = PageElement(xpath="//td[@data-title-text='operations']/i[2]", describe='列表第一行的删除')
    # campaign_names = PageElements(xpath="//tbody/tr[@class='ng-scope']/td[1]//text()", describe='第一列的20个活动名称')
    # delete_btn  = PageElement(xpath="//tbody/tr[@class='ng-scope'][{}]/td/i[2]".format(i))
    confirm_ok_btn = PageElement(xpath="//div[@class='confirm']//span[@class='btn btn-success btn-xs']",
                                 describe='删除弹出的确定按钮')
    toast_sucess = PageElement(xpath="//span[@class='text']", describe='Toast：删除营销活动成功')
