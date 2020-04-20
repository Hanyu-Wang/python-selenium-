*** Settings ***

Library  药品管理.py   WITH NAME  M

Library  药品管理.TestOne   WITH NAME  TestOne



*** Test Cases ***

药品管理

  TestOne.teststeps
