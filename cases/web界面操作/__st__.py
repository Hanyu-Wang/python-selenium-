from hyrobot.common import INFO
from lib.login import open_browser, get_global_webdriver


# 整个测试目录的初始化
def suite_setup():
    INFO('打开浏览器')
    open_browser()


# 整个测试目录的消除
def suite_teardown():
    INFO('关闭浏览器')
    driver = get_global_webdriver()
    driver.quit()
