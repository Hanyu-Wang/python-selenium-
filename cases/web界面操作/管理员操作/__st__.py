from hyrobot.common import INFO
from lib.login import mgr_login, get_global_webdriver


# 整个测试目录的初始化
def suite_setup():
    mgr_login(get_global_webdriver())


# 整个测试目录的消除
def suite_teardown():
    INFO('suite_teardown')
    driver = get_global_webdriver()
    driver.quit()
