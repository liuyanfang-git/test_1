
"""

#使用python远程操作linux系统
import paramiko
#第一个，连接linux系统

#建立连接第一步，创造一个sshclien对象   ssh协议

s = paramiko.SSHClient()

#建立连接第二步，允许信任Linux 主机，类似xshell第一次连接的保存信息
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#建立连接第三步， 使用connect（）连接远程linux主机
s.connect(hostname="192.168.10.39",port=22,username="root",password="123456")

#第二个，执行linux命令
#exec_command("ls -al")执行命令的方法，命令要写成字符串类型
# stdin,stdout,stderr=s.exec_command("ls -al")
# print(stdout.read().decode())

#第三个：文件上传、下载
#SFTPClient()：sftp 客户端方法  参数：指的是之前建立的连接——>s
#第二种连接Linux方式，使用端口号连接  22
#套字节编程  -->   网络编程
# Transport((参数)): 端口号连接linux系统，参数：包含ip地址，端口号的元组
t=paramiko.Transport(("192.168.10.39",22))
t.connect(username="root",password="123456")
# SFTPClient.from_transport(参数):sftp客户端方法，参数：指的是一个套字节服务端口
sftp = paramiko.SFTPClient.from_transport(t)#创建一个文件传输通道
#r  关闭转义
# x1="/home/1.xx"   #Linux远程文件
# x2="D:\python文件/cc.txt"    #保存到本地的位置
# sftp.get(x1,x2)
#get（"远程文件","本地文件"）：下载
#put（"本地文件","远程文件"）：上传
# sftp.put(x2,x1)
#
# #关闭连接、断开连接
# t.close()
# s.close()

"""
import  paramiko


#python 与系统交互
#系统包括：windows、mac、unix
#python的内置模块-->python自带的模块，安装之后就有的
#os 库
#导入os模块
import os

#获取当前目录，类似于linux：pwd
#os.getcwd()
# a=os.getcwd()
# print(a)

#切换到指定目录：os.chdir(目录名字)
# os.chdir("A")
# b=os.getcwd()
# print(b)

#当前目录：os.curdir代表的是字符串'.'curdir = '.' 当前目录  pardir = '..'上一级目录
# os.chdir(os.curdir)
# c=os.getcwd()
# # print(c)

#上一级目录os.chdir(os.pardir)
# os.chdir(os.pardir)
# c=os.getcwd()
# print(c)

#获取操作系统类型 os.name
#nt代表windows系统，‘posix’
# n=os.name
# print(n)

#创建多级目录
# os.makedirs('aaa/bbb/ccc')

#创建一个目录
# os.mkdir('ddd')

#删除多个目录  删除的是空目录
# os.removedirs()

#删除单个目录
# os.rmdir('ddd')

#查看当前路径下所有的文件、目录、包括隐藏的
# os.listdir(路径名)
# d=os.listdir("d:\python文件")
# print(d)

#对文件、目录进行重命名
# os.rename("D:\python文件/a","D:\python文件/aaa")

#删除文件
# os.remove("D:\python文件\cc.txt")

#执行当前系统命令
# a=os.popen('dir')
# print(a.read())

#目录树
# for root,dirs,files in  os.walk("D:\python文件"):
#     print(dirs)

# os.path类 对文件的操作
#1 返回文件的绝对路径
#abspath(文件名)
# d=os.path.abspath("aaa")
# print(d)
#
# #2 返回文件的上一级目录
# dd=os.path.dirname("D:\python文件")
# print(dd)
#
# #3 返回文件当前的目录
# c=os.path.basename("D:\python文件")
# print(c)
#
# #4 判断文件是否存在 返回布尔值
# cc=os.path.exists("D:\python文件\day3.py")
# print(cc)
#
# #5 判断是否为目录
# ddd=os.path.isdir("aaa")
# print(ddd)

#6 判断是否为文件
# a=os.path.isfile("day3.py")
# print(a)

#7 判断是否为链接文件
# a=os.path.islink("day3.py")
# print(a)

#8 文件路径拼接
# a=os.path.join("aaa","B")
# print(a)

#9 文件路径分离,将最后一个文件、目录和前面进行分割，返回一个元组
# a=os.path.split("D:\python文件\day3.py")
# print(a)

#10 分割文件的后缀名  返回一个元组
# a=os.path.splitext("D:\python文件\day3.py")
# print(a)

#统计当前目录下有多少个文件、目录

# os.chdir(r'D:\python jiaoben')
# d=os.listdir(r'D:\python jiaoben')
# print(d)
import os
# class Wen(object):
#     def a(self):
#         a1 = os.listdir(r'D:\python jiaoben')
#         a2 = 0
#         a3 = 0
#         for i  in  a1:
#             if os.path.isdir(i):
#                 a2 = a2 +1
#             if os.path.isfile(i):
#                 a3 = a3 +1
#         return f"当前目录下有{a2}个目录，{a3}个文件"
#     # print(a2)
# ss = Wen()
# print(ss.a())




#python 对时间的操作
#time
import time
# 1、睡眠 sleep(数)  浮点数、整数   单位秒
# print("睡眠前")
# time.sleep(0.5)
# print("tyu")
#2、cpu运算代码的时间
# print(time.clock())
#3、本地当前时间时间
# print(time.ctime())
#4、输出时间的详细信息
# print(time.localtime())
#5、格式化输出时间
# print(type(time.strftime("%A %d %B %H:%M:%S")))
#6、根据格式解析表示时间的字符串
# print(time.strptime("30  Nov  00","%d  %b  %y"))
#7、距离计算机元年到现在有多少秒
# print(time.time())

#python 对日期的操作
#detetime
# import datetime
from datetime import *
#1、获取当前时间、日期
print(datetime.now())
#2、获取指定的时间日期
print(datetime(1994,11,9,12,1,1))
#3、字符串时间转日期
t = datetime.strptime("1994-11-09 12:01:01","%Y-%m-%d  %H:%M:%S")
print(t)
#4、日期转字符串
s = datetime.now().strftime('%A %d %B %H:%M:%S')
print(s)
#5、datetime  日期的加减
now = datetime.now()
q = now + timedelta(days=5)#days:天  hours：小时
print(q)
# 6、获取当前时间
print(date.today())
#7、对日期进行加减
f = date.today() - timedelta(days=1)
print(f)









































