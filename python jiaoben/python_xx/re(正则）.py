#python 正则
# 正则模块  re
#正则只能匹配字符串
import re
"""
re.I  不区分大小写
s = "https://www.baidu.com"
# .代表除了\n 以外的所有字符，一个点 .  代表一个字符
#re.S 给 . 加功能，让.可以匹配到包括换行符在内的任意字符
# * 匹配*前面的字符0次或多次
x1 = re.compile('ab*')
# + 匹配+前面的字符1次或多次
x2 = re.compile('abc+')
# ? 匹配？前面的字符0次或1次
x3 = re.compile('abc+')
# ^ 匹配字符串以某个字符开头
x4 = re.compile('^a')
# $ 匹配字符串以某个字符结尾
x5 = re.compile('bc$')
# {m] 匹配花括号前面字符出现的指定次数  m  = 1
x6 = re.compile('ab{1}')
#{m,n} 匹配花括号前面字符出现的指定次数,最少m次，最多n次
x6 = re.compile('ab{1,2}')
#[] 匹配括号内的任意一个字符,每个字符只匹配一次，
x7 = re.compile('a[bc]')
"""
"""
[a-z]  26个小写字母
[A-Z]  26个大写字母
[0-9]  数字
"""
"""
# | 匹配 |  左右的表达式
x8 = re.compile('ab|ac')
# \D  匹配任何非十进制数字的字符 0-9
x9 = re.compile('\D')
# \d 匹配任何十进制数字的字符 0-9
x10 = re.compile('\d')
#\s 匹配空白字符 空格  \t   \n  \f  \v
x11 = re.compile('\s')
# \S 匹配非空白字符的任意字符
#() 匹配括号里的字符
x12 = re.compile("https://www.(.....).com")
# group():获取匹配到的内容
#编译正则表达式  re.compile()
x = re.compile('.')
# 匹配正则 match(编译过得正则表达式，字符串）
#匹配不成功返回none
res = re.match(x12,s)
print(res)
print(res.group())
"""

#re.search (正则表达式，要匹配字符串）
#从左到右对整个字符串进行搜索匹配，匹配不到返回none，匹配到第一个就停止匹配
a2 = "https://www.baidu.com https://www.baidu.com"
a = re.compile('w')
a1 = re.search(a,a2)
# print(a1)
#re.findall(正则表达式，要匹配字符串)
#从左到右对整个字符串进行搜索匹配，匹配到的内容放到列表里
#使用（）时，仅仅匹配括号里的内容
a3 = re.compile(r'www.(.*).com')
a4 = re.findall(a3,a2)
# print(a4)
#贪婪 模式  ：  .*   尽可能多的匹配字符
# 非贪婪模式：.*?    匹配到字符就停止
#re.sub(正则表达式，要替换的字符，要匹配的字符串）    替换
# g = 'hello world'
# k = re.sub('l','kk',g)
# print(k)

f = '1234567890'
# g = '1,234,567,890'
# k = re.sub(f,g,g)
# print(k)
f1 = re.compile('1234567(.*)')
f2 = re.findall(f1,f)
print(f2)
f3 = f2[0]
f4 =  ','+ f3
print(f4)
f5 = re.compile('1234(.*)890')
f6 = re.findall(f5,f)
f7 = f6[0]
f8 = ',' + f7
print(f8)
f9 = re.compile('1(.*)567890')
f10 = re.findall(f9,f)
f11 = f10[0]
f12 = ',' + f11
print(f12)
f13 = '1' + f12 + f8 + f4
print(f13)


#爬虫：有目的的获取互联网中的资源
#爬虫框架：scrapy

import json
json.loads("想转的内容") #作用：将json转为python字典

json.dumps("想转的内容")#将json.dumps("将python字典转成json字符串")
