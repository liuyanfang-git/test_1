# class Student(object):
#     height = 190
#     weight = 87
#     def name(self,x):
#
#         print(f"有一个人是{x},身高{self.height}cm,体重是{self.weight}kg")
# a = Student()
# a.name("傻逼")
# class  Hello(object):
#     b = "234567"
#     c = "1234567"
#     def xt(self):
#         print(f"账户是{self.b},密码是{self.c}")
# d = Hello()
# d.xt()
# class  Score(object):
#     i = "语文"
#
#     def students(self,id,score):
#         print(f"{id}的{self.i}成绩是{score}")
# f = Score()
# f.students("傻子","99")
# class A(object):
#     #类的属性
#     banji = "1"
#     __a = "234"
#     def __init__(self,name,age): #类的构造方法  如果定义了init方法在创造对象的时候，必须传入参数
#         #对象的属性
#         self.name = name
#         self.age = age
#         self.__g = "qwer"
#     def show(self):
#         print("类的普通 方法")
#     @staticmethod
#     def foo():  #静态方法   -->   类似于函数
#         print("类的静态方法")
#     @classmethod
#     def koo(cls):   #类方法  cls和self的作用一致，只不过换了个名字
#         print("类的方法")
#     def __siyou(self):
#         print("类中的私有方法")
#     def yu(self):
#         #在类的方法中使用其他方法的方式
#         #self.方法名[所有的方法名]
#         self.__siyou()
# #类的方法可以被哪些使用
# # A.show() 报错
# a = A("张三",12)
# a.yu()
# a.show()#对象名.普通方法名  ——>   使用普通方法
# a.foo()#对象名.静态方法名  ——>   使用静态方法
# a.koo()#对象名.类方法名    ——>   使用类方法
# # a.__siyou() 私有方法不可以在类的外部使用
# A.koo() #类名.类方法名、类名.静态方法名；可以使用类方法、静态方法
# """
# 1、类中的普通方法不能被类名.方法名的方式使用
# 2、对象名.普通方法名  ——>   使用普通方法
# 3、对象名.静态方法名  ——>   使用静态方法
# 4、对象名.类方法名    ——>   使用类方法
# 5、私有方法不可以在类的外部使用
# 6、类名.类方法名、类名.静态方法名；可以使用类方法、静态方法
# """
# """
# @  ——>  python的语法糖
# @staticmethod 将普通方法转变为静态方法的装饰器
# @classmethod  将普通方法转变为类方法的装饰器
# """
# z = A("liu",12)# 这个是创造对象的过程
# z.show()# 对象使用类的方法，类的方法只有类的对象才能用

#继承
# class B(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def say(self):
#         print(f"B类中的普通方法")
#         return self.name,self.age
# # (类名) ——>  继承于xx类，只要被继承类有的，继承的类都可以直接使用
# class C(B):
#     def talk(self):
#         # res = self.say()
#         res = super().say()
#         print(res)
#         #多态 ——> 重写方法
#     def say(self):
#         print("C类里的方法")
#
# c1 = C("张三",99)
# c1.talk()
# c1.say()
"""
多态：
1、继承类对被继承类的方法重写【方法名一样，语句块不一样】
2、如何在多态之后使用被继承类的方法，使用super（）.被继承的方法
"""
"""
pip是python的第三方包下载工具
作用：
下载python的第三方包
什么是python的包？
对python脚本文件的汇总集合被称为包
pip命令
1、pip install  包名 ——>下载
2、pip  list ——>查找pip下载过得所有包
"""

import  pymysql
"""
#第一步连接数据库
connect = pymysql.connect(
    host = "192.168.10.24",  #数据库所在的主机ip地址/域名【云服务器--mysql数据库】
    port = 3306,#mysql 的端口号
    user = "root",# mysql 的用户名
    password = "123456",# mysql的密码
    charset = "utf8", # mysql数据的编码方式
    # database = "库名"  #指定数据库，不写这个参数，默认使用所有的数据库
)
cur = connect.cursor()#游标：类似于mysql  > 命令行模式
sql = "create database stu1903"
a = "show databases"
#执行sql语句
cur.execute(a)
"""
# class A(object):
#     def __init__(self,host,port,user,password,charset):
#         self.host = host
#         self.port = port
#         self.user = user
#         self.password = password
#         self.charset = charset
#     def create_database(self):
#         cur = self.connect.cursor()
#         sql = "create database liu1903"
#         cur.execute(sql)
# a = A("192.168.10.24",3306,"root","123456","utf8")
# a.create_database()
class Mysql(object):
    def __init__(self,connect):
        self.connect = pymysql.connect(
            host = "192.168.10.33",
            port = 3306,
            user = "root",
            password = "123456",
            charset = "utf8",
            database = "yuan1903"
        )
        self.cur = self.connect.cursor()
    def create_database(self):
        sql = "create database yuan1903 default charset utf8 collate utf8_general_ci"
        self.cur.execute(sql)
    def create_table(self):
        d = "create table ydyb(name char(20),sex char(10),age int(20),lenght char(50),country char (50))"
        self.cur.execute(d)
    def  insert_into(self):
        i = self.connect.cursor()
        d = {
            "data": {
                "msg":
                    [
                        {
                            "s_1": ["Jim", "男", 19, "175cm"],
                            "country": "美国"
                        },
                        {
                            "s_2": ["Kity", "女", 17, "165cm"],
                            "country": "法国"
                        },
                        {
                            "s_3": ["Tom", "男", 19, "173cm"],
                            "country": "美国"
                        },
                        {
                            "s_4": ["拖拉斯基", "男", 18, "180cm"],
                            "country": "俄罗斯"
                        },
                        {
                            "s_5": ["阿卡丽", "女", 17, "175cm"],
                            "country": "乌克兰"
                        },
                        {
                            "s_6": ["牙买稻子", "女", 18, "161cm"],
                            "country": "日本"
                        },
                        {
                            "s_7": ["龟田一郎", "男", 19, "175cm"],
                            "country": "日本"
                        },
                        {
                            "s_8": ["张三", "男", 20, "180cm"],
                            "country": "中国"
                        },
                        {
                            "s_9": ["李秀琴", "女", 19, "175cm"],
                            "country": "中国"
                        },
                        {
                            "s_10": ["宋仲基", "女", 19, "175cm"],
                            "country": "韩国"
                        },
                        {
                            "s_11": ["金正鞋", "男", 19, "168cm"],
                            "country": "朝鲜"
                        },
                        {
                            "s_12": ["卡列夫斯基", "男", 21, "190cm"],
                            "country": "俄罗斯"
                        },
                    ]
            },
        }
        a = d["data"]["msg"]
        # print(a)
        # for i in a:
        #     print(i["country"])
        for j in range(1, 13):
            b = f"s_{j}"
            bb = a[(j - 1)][b]
            # print(bb)
            aa = a[j - 1]["country"]
            bb.append(aa)
            # print(bb)
            cc = tuple(bb)
            print(cc)

            j = f"insert into ydyb values {cc}"

            self.cur.execute(j)
# 保存数据到数据库
        self.connect.commit()
    def cha(self):
        s1 = "select * from ydyb"
        s2 = self.cur.execute(s1)
        s3 = self.cur.fetchall()
        # s4 = self.cur.fetchmany(size=6)
        # s5 = self.cur.fetchone()
        print(s3)




# my = Mysql("wert")
# # my.create_database()
# # my.create_table()
# # my.insert_into()
# my.cha()

class Txt(Mysql):
    def write(self):
        f = open(file="liu.txt",mode='w',encoding="utf-8")
        q1 = []
        q2 = len(self.cha())
        for a in  range(q2-1):
            q1.append(a)
        return a

        shuju = a
        for  i  in shuju:
            for j  in i:
                f.write(f'{str(j)} '"\t")
                f.write("\n")
s1 = Txt("wer")
s1.write()



# f = open(file="wen.txt",mode='w',encoding="utf-8")
# shuju = my.cha()
# f.write("数据")