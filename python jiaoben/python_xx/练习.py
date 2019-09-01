import xlrd
import xlwt
# from xlutils.copy import copy
# class A(object):
#     def __init__(self,name,num):
#         self.d = xlrd.open_workbook(filename=name)
#         self.t = table = self.d.sheet_by_index(num)
#     def a(self):
#         a1 = []
#         a2 = []
#         s1 = self.t.row_values(0,0)
#         print(s1)
#         s2 = s1[1]
#         s3 = s1[2]
#         s4 = "test"
#         s5 = s4 + s2
#         s6 = s4 + s3
#         a1.append(s5)
#         a2.append(s6)
#         print(a1,a2)
#         q1 = copy(self.d)
#         q2 = q1.get_sheet(0)
#         q2.write(2,1,a1)
#         q2.write(2,2,a2)
#         q1.save("73.xls")
#
#         # self.d.self.t.write(1,1,a1)
#         # # self.d.self.t.write(1,2,a2)
#         # # self.d.self.t.save()
#
# aa = A("73.xls",0)
# aa.a()



#d.save("73.xls")
# class Excel(object):
#     def __init__(self,name,num):
#         #第一步  打开文件
#         self.d = xlrd.open_workbook(filename=name)
#         #使用某一张表
#         self.t = table = self.d.sheet_by_index(num)#d.sheets()[0]
#     #data 方法的作用，获取一张表中的所有数据
#     def data(self):
#         #将所有数据装到一个列表中
#         r = []
#         n = self.t.nrows
#         for  i  in  range(n):
#             # print(self.t.row_values(i))
#             r.append(self.t.row_values(i))
#         return r
#
# # dui = Excel("刘远方.xlsx",0)
# # print(dui.data())
# import xlwt
# class A(Excel):
#     def __init__(self,name,num,s1):
#         Excel.__init__(self,name,num)
#         self.s1 = s1
#     def q1(self):
#         d = xlwt.Workbook()
#         table = d.add_sheet("表1")
#         s2 = len(self.s1)
#         for  i  in range(s2):
#             s3 = len(self.s1[i])
#             for  j  in range(s3):
#                 table.write(i,j,self.s1[i][j])
#         d.save("80.xls")
# s5 = Excel("刘远方.xlsx",0)
#
#
#
# s4 = A("刘远方.xlsx",0,s5.data())
# s4.q1()


# import xlwt
# d = xlwt.Workbook()
# table = d.add_sheet("表1")
# s1 = [['序号', '名字', '年龄', '性别'], [1.0, '张三', 20.0, '男'], [2.0, '李四', 19.0, '男'], [3.0, '王五', 18.0, '女'], [4.0, '赵信', 16.0, '女']]
# s2 = len(s1)
# for i in range(s2):
#     s3 = len(s1[i])
#     for j in range(s3):
#         table.write(i,j,s1[i][j])
# d.save("234.xls")
#九九
# class Jj(object):
#     def __init__(self,s1,s2):
#         self.s2 = s2
#         self.s1 = s1
#     def a1(self):
#         b = xlwt.Workbook()
#         b1 = b.add_sheet(self.s1)
#         for i in range(1,10):
#             for j in range(1,i+1):
#                 c = i * j
#                 b1.write(i-1,j-1,f"{j}*{i}={c}")
#         b.save(self.s2)
# ss = Jj("表","00.xls")
# ss.a1()

"""
class Txt(object):
    def __init__(self,f1):
        self.f1 = f1
        self.f = open(file="b.txt",mode="w",encoding="utf-8")
    def aa(self):
        for i in range(1,self.f1):
            for j in range(1,i+1):
                self.f.write(f"{j}*{i}={i*j}" '\t')
            self.f.write("\n")
sss = Txt(10)
sss.aa()
"""
# import  pymysql
# class A(object):
#     def a(self):
#         c = pymysql.connect(
#             host = "192.168.0.10",
#             port = 3306,
#             user = "root",
#             password = '123456',
#             charset = 'utf8',
#             database = 'liu'
#
#         )
#         s = c.cursor()
#         return s
#     def v(self):
#         sql = 'create  table  test_tab(a  char(20),b  char(20),c  char(20),d  int(20))'
#         self.a().execute(sql)
#         with open(file='a.txt',mode='r',encoding='utf-8') as f:
#             d = f.read()
#         sql1 = 'insert  into test_tab  valuses(d)'
#         self.a().execute(sql1)
# ss = A()
# ss.v()
#
#
# import  socket
# #客户端
# ip_port = ('127.0.0.1',6666)
# c = socket.socket()
# c.connect(ip_port)
# t = input("输入发送的信息")
# c.sendall(t.encode())
# #服务器
# ip = ('127.0.0.1',9999)
# s = socket.socket()
# s.bind(ip)
# s.listen(5)
# print('启动socket服务')
# b,c=s.accept()
# a = b.recv(1024).decode('utf-8')
# print(a)





# import re
# import requests
# import xlwt
# class B(object):
#     def qq(self):
#         url = 'https://www.qiushibaike.com/'
#         heards = {'User-Agent':'浏览器 头部'}
#         q = requests.get(url,heards)
#         q1 = q.text
#         q2 = re.compile('使用正则过滤')
#         q3 = re.findall(q2,q1)
#         return  q3
#     def qqq(self):
#         q4 = self.qq()
#         with open(file='a.txt',mode='w',encoding='utf-8') as f:
#             f.write(q4)
# bb = B()
# bb.qqq()

# class A(object):
#     x = 1
# class B(A):
#     pass
# class C(A):
#     pass
# print(A.x,B.x,C.x)
# B.x = 2
# print(A.x,B.x,C.x)
# A.x = 3
# print(A.x,B.x,C.x)
# import selenium
# import time
# from  selenium  import webdriver
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://127.0.0.1")
# time.sleep(3)
# # driver.quit()
