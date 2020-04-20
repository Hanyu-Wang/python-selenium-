from hyrobot.common import STEP, CHECK_POINT, INFO
import time
from lib.login import get_global_webdriver

# # 整个测试文件的初始化
# def suite_setup():
#     INFO('suite_setup')
#     driver = open_browser()
#     mgr_login(driver)
#
#
# # 整个测试文件的消除
# def suite_teardown():
#     INFO('suite_teardown')
#     driver = get_global_webdriver()
#     driver.quit()
# 给用例添加标签(全局)
force_tags = ['登录功能', '冒烟测试', 'UI测试']



class TestOne:
    # 测试用例的名字
    name = '第一个测试用例'
    # 给用例添加标签(单个)
    tags = ['登录功能', '冒烟测试', 'UI测试']
    # 单个测试用例初始化操作
    # def setup(self):
    #     INFO('单个用例初始化')
    #
    # # 单个测试用例清楚操作
    # def teardown(self):
    #     INFO('单个用例消除')

    # 测试用例的执行步骤
    def teststeps(self):
        driver = get_global_webdriver()
        STEP(1, '列表上方的信息')
        items = driver.find_element_by_css_selector("#navbar > ul")
        fields = items.find_elements_by_tag_name('li')[:6]
        texts = [field.text for field in fields]
        INFO(texts)

        CHECK_POINT('展示的内容是否一致', texts == ['客户', '销售', '药品', '订单', '统计', '退出'])


class TestTwo:
    # 测试用例的名字
    name = '测试添加用户'

    # def setup(self):
    #     INFO('单个用例初始化')
    #
    # def teardown(self):
    #     INFO('单个用例消除')

    # 测试用例的执行步骤
    def teststeps(self):
        driver = get_global_webdriver()

        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/button').click()

        STEP(1, '填入用户信息')
        # 填入信息
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[1]/div[1]/input').send_keys('小颖')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[1]/div[2]/input').send_keys(
            '18811111111')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[1]/div[3]/input').send_keys('xy_11')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[1]/div[4]/input').send_keys(
            '88888888')
        driver.find_element_by_css_selector('#root textarea').send_keys(
            '123456')
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[1]/div[2]/button[1]').click()
        time.sleep(1)
        # 找到新增内容的最上方一个
        items = driver.find_elements_by_xpath('//*[@id="root"]/div/div[3]')[0]
        fields = items.find_elements_by_tag_name('span')[:8]
        texts = [field.text for field in fields]
        INFO(texts)

        # 期望结果
        expected = [
            '客户名：', '小颖', '登录名：', 'xy_11', '联系电话：', '18811111111', '描述：',
            '123456'
        ]
        STEP(2, '验证展示的数据是否和期望值相同')

        CHECK_POINT('项目名称是否正确', texts == expected)
        # if texts == expected:
        #     print('测试通过')
        # else:
        #     print('测试失败')
