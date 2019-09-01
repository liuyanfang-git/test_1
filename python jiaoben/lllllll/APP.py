#!/usr/bin/python
#--*-- conding :utf-8 --*--
import time
from appium import webdriver
#python 代码的客户端连接手机时所需要的信息
d = {
    #设备系统类型
  "platformName": "Android",
  "platformVersion": "5.1.1",#移动端平台
  "deviceName": "emulator-5554",#
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true"
}

#步骤一：与手机建立连接
#http://127.0.0.1:4723/wd/hub
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
time.sleep(10)
"""
将手机信息发送到appium服务器，使服务器和手机建立一个session
appium 与python 客户端建立一个连接。
"""
#第二步：执行操作
"""
id不唯一，使用class定位
解决方法：
    向上一级或上上以级查找id唯一或class唯一。
    再使用使用class进行定位
"""
#先找唯一的ID，在找class
#联系人、看点、动态、三个组成的列表【1,2,3】
# s = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
# for  i  in  s:
#     i.click()
#     time.sleep(10)
# #消息的可点击的定位
# dr.find_element_by_id("android:id/tabs").find_element_by_class_name("android.widget.RelativeLayout").click()
# aa = dr.find_element_by_id("android:id/tabs").find_elements_by_id("com.tencent.mobileqq:id/name")
# p = []
# for  i  in  aa:
#     pp = i.text
#     p.append(pp)
# print(p)
l = dr.find_element_by_id("android:id/tabs").find_elements_by_class_name("android.widget.FrameLayout")
l[0].click()
dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").click()
dr.find_element_by_id("com.tencent.mobileqq:id/et_search_keyword").send_keys("2707257180")
l1 = dr.find_element_by_class_name("android.widget.AbsListView").find_elements_by_class_name("android.widget.LinearLayout")
l1[5].click()
dr.find_element_by_id("com.tencent.mobileqq:id/input").send_keys("hello")
dr.find_element_by_id("com.tencent.mobileqq:id/fun_btn").click()
l2 = dr.find_element_by_id("com.tencent.mobileqq:id/rlCommenTitle").find_elements_by_id("com.tencent.mobileqq:id/name")
l2[3].click()
# dr.find_element_by_id("com.tencent.mobileqq:id/btn_cancel_search").click()
# time.sleep(5)
l3 = dr.find_elements_by_class_name("android.widget.Button")
l3[2].click()
dr.find_element_by_id("com.tencent.mobileqq:id/settings").click()
dr.find_element_by_id("com.tencent.mobileqq:id/account_switch").click()
dr.find_element_by_id("com.tencent.mobileqq:id/logoutBtn").click()