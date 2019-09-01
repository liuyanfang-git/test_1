import time
from appium import webdriver
import  pytest
@pytest.fixture(scope='module')
def lian():

    # python 代码的客户端连接手机时所需要的信息
    d = {
        # 设备系统类型
        "platformName": "Android",
        "platformVersion": "5.1.1",  # 移动端平台
        "deviceName": "emulator-5554",  # 序列号
        "appPackage": "com.qk.butterfly",  # 安装包名
        "appActivity": ".main.LauncherActivity",  # 活动栈
        "noReset": "true"
    }
    dr = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=d)
    time.sleep(10)
    return dr
