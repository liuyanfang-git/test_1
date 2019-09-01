#!/usr/bin/python
#--*-- conding :utf-8 --*--
import time
from appium import webdriver
#python 代码的客户端连接手机时所需要的信息
d = {
    #设备系统类型
  "platformName": "Android",
  "platformVersion": "5.1.1",#移动端平台
  "deviceName": "emulator-5554",#序列号
  "appPackage": "com.qk.butterfly",#安装包名
  "appActivity": ".main.LauncherActivity",#活动栈
  "noReset": "true"
}

#步骤一：与手机建立连接
#http://127.0.0.1:4723/wd/hub
dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
time.sleep(10)
dr.find_element_by_id("com.qk.butterfly:id/v_login_qq").click()
time.sleep(20)
dr.find_element_by_class_name("android.widget.Button").click()
time.sleep(5)



