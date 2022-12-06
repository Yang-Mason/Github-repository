from poium import Page, PageElement, PageElements


class LoginPage(Page):
    login_username = PageElement(id_="account", describe="用户名")
    login_password = PageElement(id_="password", describe="密码")
    login_sign = PageElement(xpath="//button[@type='submit']", describe="登录")
    login_channel = PageElement(xpath="//div[@class='account-list']/div/div[1]", describe="选择渠道")