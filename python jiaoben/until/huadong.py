from  appium  import  webdriver

#获取手机屏幕的大小

# l = dr.get_window_size()
# #放缩屏幕
# x1 = l['width']  *  0.5
#
# x2 = l['width']  *  0.75
# y1 = l['height'] *  0.25
# y2 = l['height'] *  0.5
#
# #左滑动
# dr.swipe(x2,y1,x1,y1,t
# =500,n =1)

def swipe_left(dr,t=500):
    # 获取手机屏幕的大小
    l = dr.get_window_size()
    # 放缩屏幕
    x1 = l['width'] * 0.5
    x2 = l['width'] * 0.75
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    # 向左滑动
    dr.swipe(x2, y1, x1, y1, duration=t)

def swipe_up(dr,t=500):
    # 获取手机屏幕的大小
    l = dr.get_window_size()
    # 放缩屏幕
    x1 = l['width'] * 0.5
    x2 = l['width'] * 0.75
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    # 向上滑动
    dr.swipe(x1, y2, x1, y1, duration=t)