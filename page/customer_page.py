from poium import Page, PageElement, PageElements


class CustomerPage(Page):
    customer = PageElement(xpath="/html/body/nav/ul[1]/li[2]/a", describe="客户")
    customer_management = PageElement(link_text="客户管理", describe="客户管理")
    group_management = PageElement(link_text="群组管理", describe="群组管理")
    batch_operation = PageElement(link_text="批量操作", describe="批量操作")
    customer_label = PageElement(link_text="客户标签", describe="客户标签")
    customer_stage = PageElement(link_text="客户阶段", describe="客户阶段")
    customer_property = PageElement(link_text="客户属性", describe="客户属性")
    customer_events = PageElement(link_text="客户事件", describe="客户事件")
    customer_data_scoring = PageElement(link_text="客户资料评分", describe="客户资料评分")
    blacklist = PageElement(link_text="黑名单", describe="黑名单")

    '''客户管理'''
    '''新增客户'''
    new_customer = PageElement(xpath="/html/body/div[2]/div/div/div/div[1]/div[1]/ol/div/div/a", describe="新增客户")
    name_input = PageElement(xpath="//form[@id='editMemberForm']/div[1]/div/div/input", describe="姓名输入")
    phone_input = PageElement(xpath="//form[@id='editMemberForm']/div[2]/div/div/input", describe="手机输入")
    new_customer_submit = PageElement(xpath="//input[@value='确定']", describe="确定")
    test_new_customer = PageElement(xpath="/html/body/div[1]/div/span", describe="测试新增客户")

    '''批量操作---wendy2019.09.18'''
    new_batch_btn = PageElement(xpath="//a[@translate='member_new_batch_operation']", describe="新增批量操作按钮")
    select_operatiton_objects_drop = PageElement(xpath="//div[@class='operate-target-select']", describe="请选择操作对象")
    objects_byGroup = PageElement(xpath="//body/div[5]/ul/li[1]", describe="按群组选择")
    select_group_drop = PageElement(xpath="//div[@class='group-select']", describe="请选择群组")
    object_Dynamic_group = PageElement(xpath="//div[contains(@class,'cascade-select-menu')]/ul/li[1]", describe="动态群组")
    object_Static_group = PageElement(xpath="//div[contains(@class,'cascade-select-menu')]/ul/li[2]", describe="静态群组")
    object_Dynamic_group_01 = PageElement(xpath="//span[text()=' WS漏斗分析-动态群组 ']")
    object_Static_group_01 = PageElement(xpath="//span[text()=' 漏斗分析-静态wendy ']")
    operation_remarks = PageElement(xpath="//textarea[@name='remarks']", describe="操作备注")
    objects_byImportObjects = PageElement(xpath="//section[@class='form-group target-form-group']/div[2]/div", describe='导入操作对象')
    operation_select_an_operation = PageElement(xpath="//form/section[3]/div/div/div", describe='第一个选择操作')
    operation_select_an_operation2 = PageElement(xpath="//form/section[3]/div[2]/div[2]/div", describe='第二个选择操作')
    operation_addPoints = PageElement(xpath="//body/div[7]/ul/li[1]", describe='第一个操作：加积分')
    operation_InputPonit = PageElement(xpath="//input[contains(@class,'form-control ng-pristine ng-invalid')]", describe='积分输入框')
    operation_reductPoints = PageElement(xpath="//body/div[8]/ul/li[2]", describe="第二个操作：减积分")
    superimpose_an_operation = PageElement(xpath="//span[@translate='member_overlay_operation']", describe='叠加操作')
    action_btn = PageElement(xpath="//button[@class='os button success ng-scope']", describe='立即执行')
    row_operation_remark = PageElement(xpath="//tbody/tr[1]/td[2]/span", describe='批量操作列表第一行第一列操作对象的名称')

    '''群组管理'''
    page_total_count= PageElement(xpath="//span[@class='page-total-number ng-binding']", describe='群组列表总页数')
    tb_tr_groupName = PageElements(xpath="//tbody/tr[@class='ng-scope']/td[1]", describe='群组列表第一列的20个群组名称')
    nextStep_btn = PageElement(xpath = "//span[@class='next ng-binding']", describe='翻页功能-下一步按钮')

    a = PageElement(xpath="", describe="")
    a = PageElement(xpath="", describe="")
    a = PageElement(xpath="", describe="")

