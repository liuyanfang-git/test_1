# -*- coding: utf-8 -*-
# 指定代码的编码方式
#吧括号里面的内容输出到控制台，让人看到括号里的内容
#print('hello world")
#模拟天猫登录脚本
# name = input("请输入用户名")
# password = input("请输入密码")
# if  name == "刘远方":
#     if  password == "123456":
#           print("登录成功")
#     else:
#         print("密码错误")
# else:
    # print("登录失败")
# num_1 = 11
# num_2 = 20
# t = num_2  ** num_1
# print(t)
#计算机输入任意两个数进行计算，选择计算方式
# number1 = int(input("输入一个数"))
# ys = input("输入运算方式")
# number2 = int(input("输入一个数"))
# if  ys  ==  "+":
#     a = number1 +  number2
#     print(a)
# if  ys  ==  "-":
#     b =  number1  -  number2
#     print(b)
# if  ys  ==  "*":
#     c  =  number1  *  number2
#     print(c)
# if  ys  ==  "/":
#     d  =  number1  /  number2
#     print(d)

# number  =  int(input("输入一个成绩"))输入一个成绩
# if  number>=90:
#     print("优秀")
# if  80<=number  <90:
#     print("良好")
# if   60<=  number  <  80:
#     print("及格")
# if   number <  60:
#     print("不及格")
# """
# a=1
# a%=100
# print(a)
"""
x = 100
y = 50
z = 30
if  x > y  or  z > y:
    print("x")

if   not  y  == 50:
    print("y")
else:
    print("y=50")
"""
# a = int(input("输入最长边"))
# b = int(input("输入第二条边"))
# d = int(input("输入第三条边"))
# if  a>b and  a>d and  b>d:
#     print("a为最长边,b为中间，d为最小")
#     print(a,b,d)
# if  a>b and a>d and d>b:
#     print("a为最长边,d中间，b最小")
#     print(a,d,b)
# if b>a and  b>d and a>d:
#     print("b为最长边,a为中间，d最小")
#     print(b,a,d)
# if b>a and b>d and  a<d:
#     print("d最长边,d为中间，a为最小")
#     print(d,b,a)
# if  d>a and d>b and  a>d:
#
#     print("d为最大边,a为中间边,b最小")
#     print(d,a,b)
# if  d>a and d>b and a<b:
#     print("d最大边,b为中间，a为最小")
#     print(d,b,a)
# if a+b >d  and  a+d >b  and b+d >a:
#     print("这是一个三角形")
#     if  a**2> b**2+d**2:
#         print("这是个钝角")
#     if  a**2< b**2+d**2:
#         print("这是个锐角")
#     if  a**2==b**2+d**2:
#         print("这是个直角")
# else:
#     print("这不是个三角形")
# a = "qwertyu"
# b = "we"
# if  b not in  a:
#     print("b在a")
# a=""
# if  a:
#     print("aa")
# else:
#     print("bb")
# b="2345678743234"
# l = len(b)
# print(l)
# c="hello"
# d="world"
# f=c+d
# print(f)
# print("来阿里\n" *  5)
# print(b[-6])
# s="博文智生1903小朋友"
# print(s[1:8:2])
# a ="hello"
# b = "sss"
# print(a.index(b))
# a="hello world HELLO WORLD"
# print(a.title())
# print(a.upper())
# print(a.swapcase())
# b="1232321323431454343454566543121134345353"
# c="3"
# print(b.count(c))
# print(b.startswith("sdg"))
# print(b.startswith("123"))
# d="0123abc"
# print(max(d))
# print(min(d))
# f="你过来啊"
# h="我就是不来"
# g=f"我不来{f},{h}"
# print(g)
# j="I know I beautiful"
# i=j.split(" ")
# print(i)
# a=input("请输入一段英文")
# c=a.split(" ")
# d=len(c[-1])
# print(d)
# print(j.lstrip("I"))
# print(j.replace("I",""))
# a=","
# b=["20","29","17"]
# print(a.join(b))
# a="\r"
# print(a.isspace())
# s="hello  world"

#九九乘法表
# for  a  in  (range(1,10)):
#     for  b  in  range(1,a+1):
#         c=a*b
#         print(f"{b}*{a}={c}\t",end='')
#     print("\n")


#水仙花数
# for   d  in  range(100,1000):
#         e=d//100
#         f=d//10%10
#         g=d%10
#         n=e**3+f**3+g**3
#         if  d!=n:
#             pass
#         else:
#             print(f"{d}")

#判断回文
# n=input("请输入任一自然数:")
# a=len(n)
# j=0
# for i in range(a):
#     if n[i]==n[-(i+1)]:
#         pass
#     else:
#         j=j+1
# if j==0:
#     print("是回文")
# else:
#     print("no")



# #冒泡（可能不对）
# a=input("输入一段话：")
# b=a.split(" ")
# d=len(b)
# for  i   in  range(0,d):
#     for  j  in  range(0,d-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)
#选择排序
# a=input("输入数字：")
# b=a.split(" ")
# d=len(b)
# for  i  in  range(0,d):
#     for  j  in  range(0,d):
#         if  int(b[i]) < int(b[j]):
#             b[i],b[j]=b[j],b[i]
# print(b)

#阶乘之和
# a=0
# for  b in  range(1,6):
#     c=1
#     for  d in range(1,b+1):
#         c=c*d
#     a=a+c
# print(a)

#质数之和
# a=0
# for  b  in  range(2,101):
#     for  c  in  range(2,b+1):
#         if   b%c==0:
#             break
#
#     if  b==c:
#         a=b+a
# print(a)

# a=[1,2,3,["qwerty",4]]
# b=a[-1]
# print(b[-1])
# a.append("liuyuanf")
# print(f"添加元素之后的a列表{a}")
# ab=a+b
# print(ab)
# print(a*2)
# print(a[::-1])
# c=[1,2,3,4]
# print(max(c))
# str_1="123456"
# print(list(str_1))
# a=input("输入一段话：")
# b=a.split(" ")
# c=len(b)
#
# e=0
# f=0
# for  d  in  range(c):
#     if  b[d].isdigit():
#         e=e+1
#
#     if  b[d].istitle():
#         f=f+1
# print(f)
# a=["a","b","c","e"]
# for  i,j  in  enumerate(a):
#     print(i,j)
# a=input("商品")
# f=int(input("数量"))
# b=["方便面","矿泉水"]
# c=[100,200]
# d=len(b)
# for  i,j  in enumerate(b):
#     if  a==j:
#         d=c[i]*f
#         print(d)
#         break
# else:
#     print("没有")
#
# for  i  in   range(d):
#     if  a==b[i]:
#         print(b[i])
#         print(c[i])
#         print(c[i]*f)
#         break
# else:
#     print("没有")

# def a(x):
#     #写求和的代码
#     b=0
#     for  i  in  range(x):
#         b += i
    # print(b)
    # return  b  #  b 要返回的结果
    # return  #没有返回结果
#一个函数使用return  但是没有返回结果的时候返回none
#一个函数不使用retunrn  返回none（空值）
# a(101)
#如何使用函数
"""
1、函数的名字
"""



# a = "全局变量"
# print(a)
"""
全局变量：定义之后整个脚本都可以用
局部变量：定义之后只能在一定的范围内使用
"""
# def liu():
#     b="局部变量"
#     return b
    #liu()等价于“局部变量”
# print(liu())

#将局部变量转化为全局变量
#使用关键字 global 作用：将局部变量转变成全局变量
# c="全局变量"
# def yuan():
#     global c  #全局变量
#     c = 100
#     print(c)
# yuan()
# print(c)


"""
红点：调试断点
进入调试模式：绿色的小虫子
"""
#pycharm  调试
# def  k(x1,x2):
#     c = x1 + x2
#     print(c)
#     return c
# k(100,200)

"""
函数的作用域：从定义函数的那一行开始一直到retunrn那一行结束
"""
#阶乘之和写函数
# def  f(d):
#     a=0
#     c=1
#     for  b in  range(1,d+1):
#         c=c*b
#         a=a+c
#     print(a)
#     return a
# f(5)
"""
函数的参数分类：
1、必填函数：参数定义之后，在函数被使用的时候，必须传入、赋值的参数
# def  k(x1,x2):
#     c = x1 + x2
#     print(c)
#     return c
# k(100,200)
2、默认参数：在参数被定义的时候，参数有一个默认值，在函数使用的时候，
   对默认参数赋值，则使用赋予值，不对默认参数赋值，就使用默认值
# def  k(x1,x2=5000):          x2默认参数，默认值为5000
#     c = x1 + x2
#     print(c)
#     return c
# k(100,200)
"""
"""
可变长参数：
1、以元组的形式赋值

"""
# # def  a(*args):
#     # x1,x2,x3 = args
#     # print(x1)
#     # print(x2)
#     # print(x3)
#
# # a(1,2,3)
# def a(*cc):
#     c=len(cc)
#     for  i  in  range(0,c):
#         aa=f"s_{i}"
#         print(f"参数是{aa},对应的是{cc[i]}")
# a(1,3,4,"w",5)
#
#
# def d(*cc):
#     e=len(cc)
#     for i in range(0,e):
#         a=f"s_{i}"
#         print(f"参数值是{a}，对应值是{cc[i]}")
# d(1,2,3)
#
# def  k(**kwargs):
#     print(kwargs) #kwargs  字典，关于字典的所有的函数都可以使用
#     values = kwargs.values()
# #参数传递  写法1
# k(a=1,b=2,c=3)
# #写法2:先写成一个字典，**变量名
# n = {"x1":4,"x2":5,"x3":6}
# k(**n)

# a=input("输入一段话：")
# b=a.split(" ")
# d=len(b)
# for  i   in  range(0,d):
#     for  j  in  range(0,d-1):
#         if int(b[j]) > int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)
# a = input("sss")
# b=a.split("")
# print(b)
# def f(a):
#     b=a.split(",")
#     c=len(b)
#     for i in range(0,c):
#         for  j  in  range(0,c-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1]  =  b[j+1],b[j]
#     return b
# print (f("1,2,8,-1,-100,2333"))
# def f(a,l):
#     b = a.split(",")
#     p = l.split(",")
#
#     if len(b) < len(p):
#         c=len(b)
#     else:
#         c=len(p)
#     e=[]
#     j=[]
#     for i in range(0,c):
#         d=len(b[i])
#         g=len(p[i])
#         if 5 <= d <= 8:
#             if 6<= g <= 9:
#                 e.append(b[i])
#                 j.append(p[i])
#
#     return e,j
#
# print(f("2345345,234,1234567,wqerty,qwertyuiyuytr,wer,45678","1234567,12345671234,3456789,2345678,2344,qwertyu,wrjkyiutr"))



# a={"m":20,"n":10}
# a["j"] = 30
# # print(a["j"])
# value=a.get("j")
# print(value)
# c=a.keys()
# print(c)
# d=a.values()
# print(d)
# e=a.keys()
# b=a.copy()
# print(b)
# print(a.pop("m"))
# print(a)
# a.popitem()
# print(a)
# b=len(a)
# print(b)
# seq = [1,2,"3"]
# c=dict.fromkeys(seq,"tryui")
# print(c)
# b=a.items()
# print(b)
# for  i,j  in  b:
#     print(i,j)
# b={1:2,3:4,}
# c=a.update(b)
# print(a)
# print(b)
# a.setdefault("c",[20])
# print(a)
# a=("c","b")
# # print(a*1)
# a = ['红茶','阔落','芬达']
# b = [5,7,9]
# c = [200,300,400]
# m = 1000
# while True:
#     import time
#     print('编号',"\t","\t",'商品',"\t","\t",'单价',"\t","\t","库存")
#     for i1,i2 in enumerate(a):
#         print(i1+1,"\t","\t",i2,"\t","\t",b[i1],"\t","\t",c[i1])
#     s = int(input('请输入购买的商品编号'))
#     n = int(input('输入购买的数量'))
#     q = int(input("会员输入1,没有会员输入0"))
#     if q == 1:
#         name=input("输入会员名")
#         password=input("输入会员密码")
#         if name == '刘远方':
#             if password == "666666":
#                 print(f"尊敬的会员,您的账户余额:{m}")
#             else:
#                 print(f"密码错误")
#             for i,j in enumerate(a):
#                 if int(c[i]) <= 0:
#                    continue
#                 if i+1==s:
#                     v =b[i]*n*0.9
#                     m-=v
#                     str(c)
#                     c[i]-=n
#                     print(f"支付:{v},账户余额:{m}")
#     else:
#         for i,j in enumerate(a):
#             if int(c[i]) <= 0:
#                 continue
#             if i+1 == s:
#                 w = b[i]*n
#                 m-=w
#                 str(c)
#                 c[i]-=n
#                 print(f"支付:{w},账户余额:{m}")
#     p = input("X结束购买,x继续操作")
#     if p.find("X") != -1:
#         break
# def foo():
#     x = 100
#     def k():
#         c = x * 10
#         return c
#     return k
# print(foo())

# a = [ i  for  i  in  range(1,11)]
# print(a)
# a  = [ lambda  n :n+i for i  in range(1,10) ]
# b=a[::-1]
#
# print(b[0](10))
# a=[1,2],[3,4],[5,6]
# b=a[0]
# c=a[1]
# d=a[2]
# e=b+c+d
# print(e)
# b=[a.s]
# a = open("a.txt",mode='w',encoding="utf-8")
# a.write("hello world")
# a.close()
# b=["a","b","c"]
# a = open("a.txt",encoding="utf-8")
# # for  i  in b:
# a.write(f"{b[0]}\n{b[1]}\n{b[2]}\n")
# a.close()
# d = a.readlines(2)
# c=[]
# for i in d:
#     c.append(i.strip())
# print(c)
# a.close
def  b(x):
    a = open(x,mode="r", encoding="utf-8")
    print(a.read())
    a.close()
    return
b("a.txt")
