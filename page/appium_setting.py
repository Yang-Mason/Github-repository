import sys
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)
from appium import webdriver


class TestAppium:

    caps = {}
    caps["deviceName"] = "Android Emulator"
    caps["automationName"] = "appium"
    caps["platformName"] = "Android"
    caps["platformVersion"] = "5.1.1"
    caps["appPackage"] = "com.tencent.mm"
    caps["appActivity"] = ".ui.LauncherUI"
    caps["noReset"] = True

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(10)

    def reset(self):
        TestAppium.driver.close_app()
        TestAppium.driver.launch_app()
