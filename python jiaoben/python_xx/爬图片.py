

import re
import requests
import random
"""
n = random.randint(0, 36)
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

res1 = requests.get('http://desk.zol.com.cn/bizhi/7590_94219_2.html', headers={"User-Agent": user_agent[n]})

html1 = res1.text
s = re.compile('<li class=".*">\s*<a href="(.*?)">')
u = re.findall(s, html1)[0]

xiao_tu_url = 'http://desk.zol.com.cn' + u
print(xiao_tu_url)

res2 =requests.get(xiao_tu_url)
html2 = res2.text
big = re.compile('<a target="_blank" id="1920x1200" href="(.*?)">')
s = re.findall(big, html2)

print(s)

res3 = requests.get("http://desk.zol.com.cn" + s[0])
html3 = res3.text
print(html3)
x = re.compile('<img src="(.*?)">')
g = re.findall(x, html3)
print(g)


res2 = requests.get(g[0])
img = res2.content
# 保存
with open('3.jpg', 'wb') as f:
    f.write(img)
"""
# 爬虫：spider   ,网络蜘蛛
#根据自己制定的规则，模拟浏览器去批量下载网络中的资源
#聚焦爬虫：只针对某一个网站进行的资源爬取
# 搜索爬虫：针对全网络进行的资源爬取（百度搜索引擎）

#可以模拟浏览器的模块：request/  urllib2/   urllib3/   /httpclient
# 筛选数据： re/  bs4/   xpath/

class Douban(object):
    def  print_res(self,c1):
        url =f'https://movie.douban.com/top250?start={c1}&filter='
        head = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13"}
        res = requests.get(url = url,headers=head)
        html = res.content.decode('utf-8')

        return html
    def guolv(self,html):
        title = []
        lianjie = []
        patt = re.compile(r'<div class="hd">(.*?)</span>',re.S)
        items = re.findall(patt,html)
        for i in  items:
            cc = re.compile('<span class="title">(.*)',re.S)
            ww = re.findall(cc,i)
            title.append(ww[0])
        # print(title)
        tupan1 = re.compile('<div class="pic">(.*?)</a>',re.S)
        bbb = tupan1.findall(html)
        for j in bbb:

            tupian = re.compile('src="https://(.*?).jpg',re.S)
            qqq = tupian.findall(j)
            ccc = 'https://'+qqq[0]+'.jpg'
            lianjie.append(ccc)
            # print(lianjie)
        return title,lianjie
    def save(self,ziyuan):
        for k,p in  enumerate(ziyuan[1]):
            res = requests.get(p)
            hhh = res.content
            with open(f'{ziyuan[0][k]}.jpg','wb') as f:
                f.write(hhh)




dou = Douban()
for  i  in range(0,101,25):
# print(dou.print_res())
    htm=dou.print_res(i)
# print(htm)
    ziyuan=dou.guolv(htm)
    dou.save(ziyuan)


