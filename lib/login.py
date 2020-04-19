from selenium import webdriver
from hyrobot.common import GSTORE, INFO


def open_browser():
    print('打开浏览器')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    GSTORE['global_webdriver'] = driver
    return driver


def get_global_webdriver():
    return GSTORE['global_webdriver']


def mgr_login(driver):
    INFO('管理员登录')
    driver.get('http://127.0.0.1/mgr/sign.html')
    # 登录系统
    driver.find_element_by_id('username').send_keys('byhy')
    driver.find_element_by_id('password').send_keys('88888888')
    driver.find_element_by_tag_name('button').click()
