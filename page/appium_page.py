from poium import PageElement, Page


class AppiumPage(Page):
    mail_list = PageElement(xpath="//android.widget.TextView[contains(@text, '通讯录')]")
    public_address = PageElement(xpath="//android.widget.TextView[contains(@text, '公众号')]")
    qunshuoceshi2 = PageElement(xpath="//android.widget.TextView[contains(@text, '群硕测试2')]")
    qunshuo_menu = PageElement(xpath="//android.widget.TextView[contains(@text, '菜单')]")
    member_center = PageElement(xpath="//android.widget.TextView[contains(@text, '会员中心')]")

    search = PageElement(xpath="//android.widget.ImageButton[@content-desc='搜索']")
    search_input = PageElement(xpath="//android.widget.EditText[contains(@text, '搜索')]")
    mason = PageElement(xpath="//android.view.View[contains(@text, 'Mason')]")
    message = PageElement(xpath="//android.widget.TextView[contains(@text, '发消息')]")

    dianjifaxiaoxi = PageElement(xpath="//android.widget.ImageView[@content-desc='消息']")
    biaoqing = PageElement(xpath="//android.widget.ImageButton[@content-desc='表情']")
    weixiao = PageElement(xpath="//com.tencent.mm.ui.MMImageView[@content-desc='[微笑]']")
    fasong = PageElement(xpath="//android.widget.Button[contains(@text, '发送')]")
    jinruqunshuo2 = PageElement(xpath="//android.view.View[contains(@text, '群硕测试2')]")
    a = PageElement(xpath="")
