from hyrobot.common import STEP, CHECK_POINT, INFO
import time
from selenium import webdriver


class TestOne:
    # 测试用例的名字
    name = '第一个测试用例'

    # 测试用例的执行步骤
    def teststeps(self):

        STEP(1, '登录家培网')

        driver = webdriver.Chrome()
        driver.get('http://www.cfept.com/login.html')
        driver.implicitly_wait(10)
        driver.find_element_by_id('Phone').send_keys('17625528946')
        driver.find_element_by_id('Password').send_keys('666666')
        driver.find_element_by_css_selector('.btn-normal').click()
        time.sleep(5)

        STEP(2, '获取项目名称')

        elements = driver.find_elements_by_css_selector('.col-3-g .teamBg')
        # elements = driver.find_elements_by_xpath("//*[@id='app3']/div[1]/div")
        menutitles = []
        for element in elements:
            # print(element.text)
            menutitles.append(element.text)
        INFO(menutitles)

        STEP(3, '检查是否和预期项目吻合')

        CHECK_POINT(
            '项目名称是否正确', menutitles[:4] == [
                '技术部疫情项目测试', '疫期专项▪家庭教育指导师培训', '广东省家庭教育指导师第五期培训',
                '中陶家庭第一期家庭教育指导骨干教师培训（二）'
            ])

        driver.quit()
