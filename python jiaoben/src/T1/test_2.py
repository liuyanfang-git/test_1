import pytest

import yaml
with  open(file=r'D:\python jiaoben\lllllll\a.yaml',mode='r',encoding='utf-8')  as fb:
    data = yaml.load(fb,Loader=yaml.FullLoader)

import time
def test_1(lian):
    lian.find_element_by_id(data['qq']).click()
    time.sleep(20)
    lian.find_element_by_class_name(data['denglu']).click()
    time.sleep(5)
    text = lian.find_element_by_id(data['chenggong']).text
    time.sleep(10)
    assert text == '直播'
def test_2(lian):
    a = lian.find_elements_by_id(data['wode'])
    a[-1].click()
    time.sleep(5)
    a1 = lian.find_element_by_id(data['ting']).text
    time.sleep(5)
    assert a1 == '听余音未了'
from until.huadong import swipe_up
def test_3(lian):
    swipe_up(lian)
    a2 = lian.fand_element_by_id(data['shezhi']).fand_element_by_class_name(data['hua']).text
    time.sleep(10)
    assert a2 == '设置'
def test_4(lian):
    lian.find_element_by_id(data['shezhi']).click()
    time.sleep(5)






























#
# def test_1():
#     a = 1
#     b = 2
#     c = a + b
#     # 实际结果是3，预期结果是2
#     # 设定断言
#     assert c == 2
#
#
# def test_2():
#     str_1 = "hello pytest"
#     str_2 = "python"
#     # 设定断言，判断str_2 在 str_1内
#     assert str_2 in str_1
#
#
# def test_three():
#     n = 10
#     # 设定断言，判断n小于101
#     assert n < 101




