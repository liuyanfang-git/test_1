#python 爬虫
# 使用到的库：requests  re
#爬虫：有目的的获取网络中的资源
import requests
import re
"""
# d ={"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
# #1、发送URL请求
# req = requests.get('https://www.fpzw.com/xiaoshuo/88/88413/',headers=d)
#接收html文本，

res = req.content.decode('gbk')
# print(res)
s3 = re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
urls = re.findall(s3,res)
k={

}
for i  in urls:
    url = f'https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}.html'
    mu = i[1]
    k[mu] = url
print(k)
k[]
#获取小说文本的内容
# s1 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp(.*?)</p></div>')
# s2 = re.compile('<h2>(.*?)</h2>')
# biaoti = re.findall(s2,res)
# print(biaoti)
# neirong = re.findall(s1,res)
# print(neirong)

# s1 = re.compile('<title>\s*(.*?)\s*</title>')
# a = re.findall(s1,res)
# print(a)
"""
import requests
import re
# dd={"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
# #发送url请求
# req=requests.get("https://www.fpzw.com/xiaoshuo/88/88413",headers=dd)
# #接收html文本
# res=req.content.decode("gbk")
# #
# # s1=re.compile("<title>\s*(.*)\s*</title>")
# # a=re.findall(s1,res)
# # print(a)
# #获取小说文本的内容
# # print(res)
# s3=re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
# urls=re.findall(s3,res)
# for i in urls:
#     url=f'https://www.fpzw.com/xiaoshuo/88/88413/{i[0]}.html'
#     req=requests.get(url,headers=dd)
#     #接收html文本
#     res=req.content.decode("gbk")
#     s1=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
#     # s2=re.compile("<h2>(.*?)</h2>")
#     # mulu=re.findall(s2,res)
#     neirong=re.findall(s1,res)
#     print(neirong)
#     # n=neirong[0]
#     # n=n.replace("<br /><br />","\n")
#     # n=n.replace("&nbsp;&nbsp;&nbsp;&nbsp;"," ")
#     # with open(file="b.txt",mode="a",encoding="utf8") as  f:
#     #     f.write(f"{i[1]}\n")
#     #     f.write(f"{n}")
#     #     f.write("\n")

# 获取图片
import re
import requests
import random
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]
n= random.randint(0,36)
class Zol(object):
    #请求Url  11个小图的url
    def get_url(self):
        res = requests.get("http://desk.zol.com.cn/bizhi/7590_94219_2.html",headers={"User-Agent":user_agent[n]})
        #获取htlm文本
        html = res.text
        # print(html)
        a = re.compile('<li class=".*?">\s*<a href="(.*?)">')
        b = re.findall(a,html)
        # print(b)
        c = []
        for i  in b:
            a1 = "http://desk.zol.com.cn" + i
            c.append(a1)
        # print(c)
        return c
    def get_url1(self):
        s = self.get_url()
        # print(s)
        c1 = []
        for i in s:
            res1 = requests.get(i)
            html1 = res1.text
            a2 = re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
            b1 = re.findall(a2,html1)
            # print(b1)
            if len(b1):
                d = "http://desk.zol.com.cn" + b1[0]
                c1.append(d)
        # print(c1)
        return c1
    def get_url2(self):
        s1 = self.get_url1()
        c2 = []
        for i  in s1:
            res2 = requests.get(i)
            html2 = res2.text
            a3 = re.compile('<img src="(.*?)">')
            b2 = re.findall(a3,html2)
            # print(b2)
            c2.append(b2)
        # print(c2)
        return c2
    def get_url3(self):

        s2 = self.get_url2()
        l = 0
        l1= 0
        for i in s2:

            res3 = requests.get(i[0])
            q = res3.content

            with open(f"{l}.jpg","wb") as  f:
                f.write(q)
            l = l +1


z =Zol()
z.get_url3()

        # s = re.compile('<li class=".*?">\s*<a href="(.*?)">')
        # u = re.findall(s,html)
        # print(u)
        # u2 = []
        # for i in u:
        #     u1 = "http://desk.zol.com.cn" + i
        #     print(u1)
        #     u2.append(u1)
        # return u2

    # # 从小图里拿大图？
    # def get_big_img_url(self):
    #     a = self.get_url()
    #     for i in a:
    #         res1 = requests.get(i,headers={"User-Agent":user_agent[n]})
    #         html = res1.text
    #         big = re.compile('<a target="_blank" id=".*" href="(.*?)">')

#从文本中获取我们想要的资源
#     def  res(self):
#         a = self.get_url()   #html文本
#         print(a)
#         #匹配大图的正则
#         big = re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
#         big_msg = "http://desk.zol.com.cn" + re.findall(big,a)[0]
#         print(big_msg)
#         s = re.compile('<li class=".*?">\s*<a href="(.*?)">')
#         u = re.findall(s,a)
#         print(u)
#         for i  in u:
#             u1 = "http://desk.zol.com.cn" + i
#             print(u1)
#
#
#
#     def get_big_img(self):
#         res = requests.get('http://desk.zol.com.cn/showpic/1920x1200_94219_248.html',headers={"User-Agent":user_agent[n]})
#         html = res.content.decode('gb2312')
#         # http: // desk.zol.com.cn / showpic / 1920
#         # x1200_94219_248.html
#         s = re.compile('<img src="(.*?)">')
#         img_url = re.findall(s,html)
#         print(img_url)
#         #下载图片
#         res2 = requests.get(img_url[0],headers={"User-Agent":user_agent[n]})
#         img = res2.content
#         #保存
#         with open('2.jpg','wb') as f:
#             f.write(img)
#
# z = Zol()
# # z.res()
# z.get_big_img()


