# python  操作Excel表格
"""
下载xlrd      cmd里输入：pip  install xlrd
打开Excel文件
open_workbook(filename="文件名")
"""

import xlrd
d = xlrd.open_workbook(filename="刘远方.xlsx")
#获取Excel表，返回的是包含所有Excel的列表
#假设文件中存在两个Excel表，那么列表中["sheet1","sheet2"]
table = d.sheets()[0]
#获取表中的数据  row_values():获取整行数据，必须指定获取的行号
x = table.row_values(0,0)
print(x)
#获取某个单元格的值  先通过row（）获取某一行——>返回一个列表——>在通过列表的索引获取元素——>在 .value 获取具体的值
dan = table.row(0)[0].value
print(dan)
#取某一列  先通过rcol（）获取某一行——>返回一个列表——>在通过列表的索引获取元素——>在 .value 获取具体的值
a = table.col(0)[1].value
print(a)
#获取某个单元格的值  先通过cell（）获取某一行某一列，在 .value 获取具体的值
b = table.cell(0,0).value
print(b)
#获取行数
c = table.nrows
print(c)
#获取列数
f = table.ncols
print(f)
#通过行数获取所有数据
for i in range(c):
    print(table.row_values(i))
#通过列数获取所有数据
e = table.col_values(1)#获取某一列数据
print(e)
for i  in  range(f):
    print(table.col_values(i))
#打印/输出excel表的名字
#d ：打开Excel文件   sheet_names():找出文件中所有表的名字
print(d.sheet_names())
#通过索引获取表
#假设一个文件中存在两个表sheet1、sheet2
#sheet_by_index():0 ——> 打开的就是sheet1
table = d.sheet_by_index(0)
print(table)

"""
import xlrd
class Excel(object):
    def __init__(self,name,num):
        #第一步  打开文件
        self.d = xlrd.open_workbook(filename=name)
        #使用某一张表
        self.t = table = self.d.sheet_by_index(num)#d.sheets()[0]
    #data 方法的作用，获取一张表中的所有数据
    def data(self):
        #将所有数据装到一个列表中
        r = []
        n = self.t.nrows
        for  i  in  range(n):
            # print(self.t.row_values(i))
            r.append(self.t.row_values(i))
        return r

dui = Excel("刘远方.xlsx",0)
print(dui.data())


f = open(file="wen.txt",mode='w',encoding="utf-8")
# shuju = dui.data()
# # for  i  in  shuju:
# #     print(i)
# #     for  j  in i:
# #         f.write(str(j) + "\t")
# #     f.write("\n")
# #     print()
# for  i  in shuju:
#     print(i)
#     for  j  in i :
#         f.write(f'{str(j)} '"\t")
#     f.write("\n")

class Txt(Excel):
    def write_date(self):
        f = open(file="wen.txt", mode='w', encoding="utf-8")
        shuju = self.data()
        for i in shuju:
            print(i)
            for j in i:
                f.write(f'{str(j)} '"\t")
            f.write("\n")
t1 = Txt("刘远方.xlsx",0)
t1.write_date()
# python  向Excel文件中写入数据 pip install  xlwt
import xlwt
#新建一个Excel文件
d = xlwt.Workbook()
#新建Excel表  add_sheet(表名）  必填
table = d.add_sheet("表1")
#写入数据到Excel表中
#一次写入一个单元格
table.write(0,0,"张三")
#保存文件
d.save("73.xls")#ctrl  +  s
"""