from poium import Page, PageElement, PageElements


class ChannelPage(Page):
    login_username = PageElement(id_="account", describe="用户名")
    login_password = PageElement(id_="password", describe="密码")
    login_sign = PageElement(xpath="//button[@type='submit']", describe="登录")
    fans_management = PageElement(link_text="粉丝管理", describe="粉丝管理")
    imagetext_management = PageElement(link_text="图文管理", describe="图文管理")
    group_sending = PageElement(link_text="群发", describe="群发")
    interactive_news = PageElement(link_text="互动消息", describe="互动消息")
    custom_menu = PageElement(link_text="自定义菜单", describe="自定义菜单")
    automatic_response = PageElement(link_text="自动回复", describe="自动回复")
    extend_QR_code = PageElement(link_text="推广二维码", describe="推广二维码")
    message_management = PageElement(link_text="留言管理", describe="留言管理")
    channel_payment_record = PageElement(link_text="渠道支付记录", describe="渠道支付记录")

    '''粉丝管理'''
    '''按昵称搜索粉丝'''
    search_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div/input",
                               describe="搜索输入")
    search = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div[1]/div/button",
                         describe="搜索")
    test_search = PageElement(xpath="//span[@wm-tooltip='茶白']", describe="测试搜索结果")
    '''给粉丝打标签'''
    labeling = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr/td[6]/i",
                           describe="打标签")
    label_input = PageElement(xpath="/html/body/div[11]/div/div/div/div[2]/div/div[1]/ul/input", describe="输入标签")
    label_select = PageElement(xpath="/html/body/div[12]/ul[3]/li", describe="选择标签")
    label_test = PageElement(xpath="/html/body/div[11]/div/div/div/div[2]/div/div[1]/ul/li[2]/div/span[1]",
                             describe="测试")
    label_delete = PageElement(xpath="/html/body/div[11]/div/div/div/div[2]/div/div[1]/ul/li[2]/div/span[2]",
                               describe="删除标签")
    label_submit = PageElement(xpath="/html/body/div[11]/div/div/div/div[3]/button", describe="确定")
    '''选择粉丝进行群发'''
    advanced_screen = PageElement(xpath="//*[@class='search-tabs-wrapper']/div[2]/span[2]", describe="高级筛选")
    immediate_screen_fans = PageElement(xpath="//*[@class='filter-wrapper btn-wrapper']/button[1]", describe="立即筛选")
    country_select = PageElement(xpath="//*[@class='flex']/div[1]/div/div[1]/div", describe="国家下拉框")
    chinese = PageElement(xpath="//ul[@class='menu ng-scope']/li[3]/div/span", describe="中国")
    province_select = PageElement(xpath="//*[@class='flex']/div[2]/div/div[1]/div", describe="省份下拉框")
    shandong = PageElement(xpath="//ul[@class='menu ng-scope']/li[17]/div/span", describe="山东")
    city_select = PageElement(xpath="//*[@class='flex']/div[3]/div/div[1]/div", describe="市区下拉框")
    city_heze = PageElement(css="[wm-tooltip=菏泽]", describe="菏泽")
    select_fans1 = PageElement(
        xpath="/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr[1]/td[1]/div/label",
        describe="选择粉丝1")
    select_fans2 = PageElement(
        xpath="/html/body/div[2]/div/div/div/div[1]/div/div[3]/table/tbody/tr[3]/td[1]/div/label",
        describe="选择粉丝2")
    mass_message = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div[1]/div[3]/span",
                               describe="群发消息")
    mass_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[5]/div[2]/form/div[2]/div/div/div["
                                   "1]/div[2]/div[1]", describe="群发消息输入框")
    mass_send = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[5]/div[2]/form/div[4]/input",
                            describe="发送")
    mass_test = PageElement(xpath="/html/body/div[1]/div/span", describe="弹出的消息")

    '''图文管理'''
    '''新增群发单图文'''
    new_imagetext = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button",
                                describe="新增群发图文")
    single = PageElement(xpath="/html/body/div[9]/div/div/div[2]/div/div[1]/div[1]", describe="单图文")
    single_title = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div/input",
                               describe="标题")
    single_add_picture = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div["
                                           "2]/div/div/div/span", describe="添加图片")
    single_select_picture = PageElement(
        xpath="/html/body/div[8]/div/div/section/div[1]/div[2]/section[1]/div[2]/div[1]",
        describe="选择图片")
    single_nextstep = PageElement(xpath="/html/body/div[8]/div/div/section/div[2]/button", describe="下一步")
    single_submit1 = PageElement(xpath="/html/body/div[11]/div/div/div/div[3]/button[2]", describe="确定")
    single_frame = PageElement(xpath="//div[@class='graphic-form-wrapper']/div[4]/div[1]/div[1]/div[2]/iframe",
                               describe="frame")
    single_detail = PageElement(xpath="/html/body/p", describe="图文详情")
    single_vxpicture = PageElement(xpath="//div[@title='微信图片']/div[1]", describe="微信图片")
    single_submit2 = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[2]/input", describe="确定")
    imagetext_test = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                       "1]/div/div/div/div[3]/div[2]/span", describe="测试图文")
    '''搜索群发单图文'''
    single_search = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[2]/form/ng-switch["
                                      "1]/div/div[2]/input", describe="搜素输入框")
    immediate_screen_single = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[2]/form/div["
                                                "2]/button[1]", describe="立即筛选")
    '''编辑群发单图文'''
    single_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                    "1]/div/div/div/div[4]/div[1]", describe="编辑")
    '''删除群发单图文'''
    single_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                      "1]/div/div/div/div[4]/div[4]", describe="删除")
    delete_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定删除")
    test_delete_multi = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除掉了单图文")
    '''新增群发多图文'''
    multi = PageElement(xpath="//div[@ng-click='graphic.editGraphic(1)']", describe="多图文")
    multi_title = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div/input",
                              describe="标题")
    multi_add_picture = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div["
                                          "2]/div/div/div/span", describe="添加图片")
    multi_select_picture = PageElement(xpath="//section[@class='pictures-wrap']/div[2]/div[1]", describe="选择图片")
    multi_nextstep = PageElement(xpath="//section[@class='os modal ng-scope']/div[2]/button", describe="下一步")
    multi_submit1 = PageElement(xpath="//div[@class='modal fade ng-isolate-scope crop-picture-modal "
                                      "in']/div/div/div/div[3]/button[2]", describe="确定")
    multi_vxpicture = PageElement(xpath="//div[@title='微信图片']/div[1]", describe="微信图片")
    multi_submit2 = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[2]/input", describe="确定")
    multi_test = PageElement(xpath="//div[@wm-waterfall='graphics.waterfallOptions']/div[1]/div/div/div/div[3]/div["
                                   "2]/div[2]/span", describe="测试图文")
    '''编辑群发多图文'''
    multi_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                   "1]/div/div/div/div[5]/div[1]", describe="编辑")
    '''删除群发多图文'''
    multi_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                     "1]/div/div/div/div[5]/div[4]", describe="删除")
    delete_submit_multi = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定删除")
    test_delete_multi = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除掉了多图文")
    '''新增带参数的高级图文'''
    senior_imagetext = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/ul/li[2]/span",
                                   describe="高级图文")
    new_senior = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[1]/button", describe="新增高级图文")
    senior_title = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div/input",
                               describe="标题")
    dynamic_parameter = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[1]/div/i",
                                    describe="添加动态参数")
    dropdown_box = PageElement(xpath="//div[@class='default text ng-binding ng-scope']", describe="下拉框")
    dropdown_box_sex = PageElement(xpath="//span[@wm-tooltip='姓名']", describe="姓名")
    dropdown_box_submit = PageElement(xpath="/html/body/div[7]/div/div/div/form/div[2]/button", describe="确定")
    senior_add_picture = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div["
                                           "2]/div/div/div/span", describe="添加图片")
    senior_select_picture = PageElement(xpath="/html/body/div[7]/div/div/section/div[1]/div[2]/section[1]/div[2]/div[1]",
                                        describe="选择图片")
    senior_nextstep = PageElement(xpath="/html/body/div[7]/div/div/section/div[2]/button", describe="下一步")
    senior_submit1 = PageElement(xpath="/html/body/div[10]/div/div/div/div[3]/button[2]", describe="确定按钮1")
    senior_link = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div[2]/div/div[4]/input",
                              describe="跳转链接")
    senior_submit2 = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[2]/input", describe="确定按钮2")
    test_add_senior = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div["
                                        "1]/div/div/div/div[3]/div[2]/span", describe="测试新增高级图文")
    '''搜素高级图文'''
    senior_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[2]/form/ng-switch["
                                     "1]/div/div[2]/input", describe="输入")
    immediate_screen_senior = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[2]/form/div["
                                                "2]/button[1]", describe="立即筛选")
    '''编辑高级图文'''
    senior_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                    "1]/div/div/div/div[4]/div[1]", describe="编辑")
    '''删除高级图文'''
    senior_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div/div["
                                      "1]/div/div/div/div[4]/div[4]", describe="删除")
    senior_delete_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定删除")
    test_delete_senior = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除掉了高级图文")

    '''群发'''
    '''新增按微信标签的群发'''
    groupsend_new_ordinary = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/button", describe="新增普通群发")

    groupsend_select_object = PageElement(xpath="//*[@id='broadcast-form']/div[1]/div[2]/div[1]/div[1]/div/div[1]/div",
                                          describe="设置群发对象")
    groupsend_vxlabel = PageElement(xpath="//span[@wm-tooltip='按微信标签选择']", describe="按微信标签选择")
    groupsend_group = PageElement(xpath="//span[@wm-tooltip='按群组选择']", describe="按群组选择")
    groupsend_select_vxlabel = PageElement(xpath="//*[@id='broadcast-form']/div[1]/div[2]/div[1]/div[3]/div/div[1]/div",
                                            describe="选择微信标签")
    groupsend_select_group = PageElement(xpath="//*[@id='broadcast-form']/div[1]/div[2]/div[1]/div[5]/div[2]/div/div["
                                               "1]/ul/input", describe="选择群组标签")
    groupsend_submit_group = PageElement(xpath="//span[@class='hilight']", describe="选择静态群组masontest_群发")
    groupsend_submit_vxlabel = PageElement(xpath="//span[@wm-tooltip='0901']", describe="微信标签0901")
    groupsend_content = PageElement(xpath="//*[@id='broadcast-form']/div[2]/div[2]/div/div[1]/div[2]/div[1]",
                                    describe="群发内容")
    groupsend_submit1 = PageElement(xpath="//*[@id='broadcast-form']/div[4]/button", describe="确定")
    groupsend_submit2 = PageElement(xpath="//div[@class='os success button ng-scope']", describe="确定")
    test_new_groupsend = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增群发成功")
    '''新增定时群发'''
    groupsend_new_timing = PageElement(xpath="//*[@id='broadcast-form']/div[3]/div/div[2]/div/label/span",
                                       describe="定时群发")
    groupsend_time1 = PageElement(xpath="//*[@id='broadcast-form']/div[3]/div[2]/div[1]/div/input", describe="年月日")
    groupsend_time2 = PageElement(xpath="//*[@id='broadcast-form']/div[3]/div[2]/div[2]/div/div/input", describe="时分")
    groupsend_submit3 = PageElement(xpath="//div[@class='os success button ng-scope']", describe="确定")
    test_new_timing_groupsend = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增定时群发成功")
    '''编辑定时群发'''
    groupsend_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[6]/i[1]",
                                 describe="编辑")
    test_edit_timing_groupsend = PageElement(xpath="/html/body/div[1]/div/span", describe="测试编辑定时群发成功")
    '''删除定时群发'''
    groupsend_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/table/tbody/tr[1]/td["
                                         "6]/i[2]", describe="删除")
    groupsend_submit4 = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定")
    test_delete_timing_groupsend = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除定时群发成功")

    '''互动消息'''
    '''按内容搜索消息'''
    interactive_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[1]/input",
                                    describe="输入框")
    test_interactive_search = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/ul/li/section["
                                                "1]/section/div[2]", describe="测试搜索出来的消息")
    '''给用户发送文本消息'''
    interactive_reply = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/ul/li/section[1]/i", describe="回复")
    interactive_replyinput = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/ul/li/section["
                                               "2]/div/div/div[1]/div[2]/div[1]", describe="输入")
    interactive_send = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/ul/li/section[2]/button",
                                   describe="发送")
    test_send_interactive = PageElement(xpath="/html/body/div[1]/div/span", describe="测试成功回复消息")
    '''给用户发送图文消息'''
    interactive_imagetext = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/ul/li/section[2]/div/div/div["
                                              "1]/div[1]/span[2]", describe="图文消息")
    interactive_search_imagetext = PageElement(xpath="/html/body/div[7]/div/div/div[2]/div[2]/div[1]/div/input",
                                               describe="搜索图文")
    interactive_select_imagetext = PageElement(xpath="//div[@class='news-view ng-scope']", describe="选择图文")
    interactive_submit = PageElement(xpath="/html/body/div[7]/div/div/div[3]/button", describe="确定")

    '''自定义菜单'''
    '''新增菜单、添加子菜单并发布'''
    personalized_menu = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[1]/li[2]/span", describe="个性化菜单")
    personalized_menu_new = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[1]/div/div/a",
                                        describe="新增个性化菜单")
    personalized_menu_name = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[1]/form/div[1]/div/input",
                                         describe="个性化菜单名称")
    personalized_menu_select = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[1]/form/div["
                                                 "2]/div/div[1]/div/div/div[1]/div", describe="选择微信用户属性")
    personalized_menu_system = PageElement(xpath="//*[@class='simple-select-menu  os-dropdown-menu-wrapper "
                                                 "os-dropdown-menu-wrapper']/ul/li[3]/div/span", describe="手机操作系统")
    personalized_menu_select_system = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[1]/form/div["
                                                        "2]/div/div[1]/div[2]/div/div[1]/div[1]", describe="选择手机操作系统")
    personalized_menu_Android = PageElement(xpath="//*[@class='cascade-select-menu gray-hover "
                                                  "os-dropdown-menu-wrapper ng-scope ng-isolate-scope']/ul[1]/li["
                                                  "2]/span", describe="Android")
    personalized_menu_main = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div["
                                               "1]/div[1]/div[2]/div/span", describe="添加主菜单")
    menu_main_name = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div["
                                       "2]/form/div[1]/div/input", describe="主菜单名称")
    menu_main_preserve = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                           "2]/div[2]/form/div[3]/button", describe="保存")
    menu_sub_new = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div["
                                     "2]/div[1]/div[2]/span", describe="添加子菜单")
    menu_sub_name = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div["
                                      "2]/form/div[1]/div/input", describe="子菜单名称")
    menu_sub_clickaction = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                             "2]/div[2]/form/div[2]/div/div/div/span", describe="设置点击动作")
    menu_sub_message = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                         "2]/div[2]/form/div[2]/div/div/div[2]/div[1]/div/div[1]/div/i", describe="发送消息")
    menu_sub_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div["
                                       "2]/form/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]",
                                 describe="输入")
    menu_sub_preserve = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                          "2]/div[2]/form/div[3]/button", describe="保存")
    menu_release = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[3]/button",
                               describe="发布")
    test_new_custommenu = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增菜单")
    '''删除子菜单并发布'''
    menu_sub_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[2]/table/tbody/tr[1]/td["
                                      "3]/a[1]", describe="编辑")
    menu_sub_select = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                        "1]/div[2]/div[1]/div[2]/div", describe="选择子菜单")
    menu_sub_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                        "1]/div[2]/div[1]/div[2]/i[2]", describe="删除子菜单")
    menu_sub_delete_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定删除")
    menu_main_click = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                        "1]/div[2]/div[1]/div[1]/div", describe="点击主菜单")
    menu_main_edit = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                       "2]/div[2]/form/div[3]/span", describe="编辑")
    menu_main_set = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                      "2]/div[2]/form/div[2]/div/div/div/span", describe="设置点击动作")
    menu_main_web = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                      "2]/div[2]/form/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div", describe="跳转到网页")
    menu_main_weblinkinput = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div["
                                               "1]/div[2]/div[2]/form/div[2]/div/div/div[2]/div/div/div[2]/input",
                                         describe="输入")
    menu_main_release = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div["
                                          "2]/div[2]/form/div[3]/button", describe="保存")
    menu_sub_release = PageElement(xpath="/html/body/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[3]/button",
                                   describe="发布")
    '''删除自定义菜单'''
    custommenu_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[2]/table/tbody/tr["
                                          "1]/td[3]/i", describe="删除")
    custommenu_delete_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定")

    '''自动回复'''
    '''新增关键词回复'''
    keyword_response_new = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[1]/div/div/a",
                                       describe="新增关键词")
    rule_name = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div/div[2]/div/div/input",
                            describe="规则名称")
    keyword = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div/div[3]/div/div/input", describe="关键词")
    response_new = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div/div[4]/div/div/span",
                               describe="新增回复")
    text_response = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/form/div/div[4]/div/div/div/span[1]",
                                describe="文本回复")
    text_input = PageElement(xpath="/html/body/div[6]/div/div/div/div[1]/div/div[2]", describe="输入")
    response_submit = PageElement(xpath="//span[@ng-click='text.submit()']", describe="确定")
    keyword_response_submit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div/div[6]/button",
                                          describe="确定")
    test_new_keyword = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增关键词回复")
    '''编辑关键词回复'''
    keyword_response_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[2]/div[1]/div["
                                              "1]/div[2]/div[2]/a", describe="编辑")
    test_edit_keyword = PageElement(xpath="/html/body/div[1]/div/span", describe="测试编辑关键词回复")
    '''删除关键词回复'''
    keyword_response_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/ul[2]/li/div/div[2]/div[1]/div["
                                                "1]/div[2]/div[2]/i[2]", describe="删除")
    delete_keyword_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定")
    test_delete_keyword = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除关键词回复")

    '''推广二维码'''
    '''新增推广二维码'''
    QRcode_new = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/ol/div/a", describe="新增二维码")
    QRcode_name = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[1]/div/input", describe="名称")
    QRcode_response = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[2]/div/div/div[1]/div["
                                        "2]/div[1]", describe="回复内容")
    QRcode_describe = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/div[3]/div/textarea",
                                  describe="描述")
    QRcode_new_submit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div/form/button", describe="确定")
    test_new_QRcode = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增二维码")
    '''搜素推广二维码'''
    QRcode_search_input = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/input",
                                      describe="输入框")
    QRcode_search = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/button/i",
                                describe="搜索")
    test_QRcode_search = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div[3]/table/tbody/tr/td["
                                           "1]/div/a", describe="测试搜索出来的二维码")
    '''编辑推广二维码'''
    QRcode_edit = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[6]/a",
                              describe="编辑")
    test_edit_QRcode = PageElement(xpath="/html/body/div[1]/div/span", describe="测试编辑二维码")
    '''删除推广二维码'''
    QRcode_delete = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[6]/i",
                                describe="删除")
    QRcode_delete_submit = PageElement(xpath="/html/body/div[2]/div[2]/div[2]/span[1]", describe="确定")
    test_delete_QRcode = PageElement(xpath="/html/body/div[1]/div/span", describe="测试删除二维码")

    a = PageElement(xpath="", describe="")
