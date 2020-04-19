*** Settings ***

Library  客户管理.py   WITH NAME  M

Library  客户管理.TestOne   WITH NAME  TestOne

Library  客户管理.TestTwo   WITH NAME  TestTwo



*** Test Cases ***

第一个测试用例

  TestOne.teststeps


测试添加用户

  TestTwo.teststeps
