

#
# # class Ms(object):
# #     def __init__(self):
# #         self.connect = pymysql.connect(
# #             host="192.168.10.36",
# #             port=3306,
# #             user="root",
# #             password="123456",
# #             charset="utf8",
# #         )
# #         self.cursor = self.connect.cursor()
# #     def  create(self,m):
# #         sql =  f"create database {m} "
# #         self.cursor.execute(sql)
# #     def  createtable(self,m,n):
# #         sq2=f"use {m}"
# #         sq3=f"create table {n}  ( name char(20),sex  char(4),age int(2),sg char(8),country char(8))"
# #         self.cursor.execute(sq2)
# #         self.cursor.execute(sq3)
# #     def insert(self,m,n,s1):
# #         sq2 = f"use {m}"
# #         c = 1
# #         for i in s1:
# #             q = i[f"s_{c}"]
# #             q.append(i["country"])
# #             w = tuple(q)
# #             print(w)
# #             sq3 = f'insert  into  {n} (name,sex,age,sg,country) values {w}'
# #             self.cursor.execute(sq2)
# #             self.cursor.execute(sq3)
# #             c += 1
# # a=Ms()
# # m="mmm"
# # n="stu11"
# # d = {
# #     "data": {
# #         "msg":
# #         [
# #             {
# #                 "s_1": ["Jim", "n",  19, "175cm"],
# #                 "country": "mg"
# #             },
# #             {
# #                 "s_2": ["Kity", "v",  17, "165cm"],
# #                 "country": "fg"
# #             },
# #             {
# #                 "s_3": ["Tom", "n",  19, "173cm"],
# #                 "country": "mg"
# #             },
# #             {
# #                 "s_4": ["tlsj", "n",  18, "180cm"],
# #                 "country": "els"
# #             },
# #             {
# #                 "s_5": ["akl", "v",  17, "175cm"],
# #                 "country": "wkl"
# #             },
# #             {
# #                 "s_6": ["mydaz", "v",  18, "161cm"],
# #                 "country": "rb"
# #             },
# #             {
# #                 "s_7": ["gtyl", "n",  19, "175cm"],
# #                 "country": "rb"
# #             },
# #             {
# #                 "s_8": ["zs", "n",  20, "180cm"],
# #                 "country": "zg"
# #             },
# #             {
# #                 "s_9": ["lxq", "v",  19, "175cm"],
# #                 "country": "zg"
# #             },
# #             {
# #                 "s_10": ["szj", "v",  19, "175cm"],
# #                 "country": "hg"
# #             },
# #             {
# #                 "s_11": ["jzx", "n",  19, "168cm"],
# #                 "country": "cx"
# #             },
# #             {
# #                 "s_12": ["klsj", "n",  21, "190cm"],
# #                 "country": "els"
# #             },
# #         ]
# #     },
# # }
# # s=d["data"]
# # s1=s["msg"]
# # a.create(m)
# # a.createtable(m,n)
# # a.insert(m,n,s1)
# # der cha(self):
# # #     #写查询sql
# # #     sql = "select  *  from  info"
# # #     #执行查询sql
# # #     a = self.cur.execute(sql)
# # #     #输出查询结果
# # #     b = self.cur.fetchall()#查询执行sql语句获得所有结果
# # #     #fetchall（）返回的是一个元组，包含若干个小元组
# # #     #prin(b)
# # #     #c = self.cur.fetchmany(size=4)#查询指定条
# # #     #c = self.cur.fetchone() 只查询一条
# # # def close(self):
# # #     #与数据库断开连接
# # #     self.connect.close()
#
#
# 郑前进 2019/7/6 16:24:59
# import requests
# import re
# import time
# import hashlib
#
# def get_page(url):
#     print('GET %s' %url)
#     try:
#         response=requests.get(url)
#         if response.status_code == 200:
#             return response.content
#     except Exception:
#         pass
#
# def parse_index(res):
#     obj=re.compile('class="items.*?<a href="(.*?)"',re.S)
#     detail_urls=obj.findall(res.decode('gbk'))
#     for detail_url in detail_urls:
#         if not detail_url.startswith('http'):
#             detail_url='http://www.xiaohuar.com'+detail_url
#         yield detail_url
#
# def parse_detail(res):
#     obj=re.compile('id="media".*?src="(.*?)"',re.S)
#     res=obj.findall(res.decode('gbk'))
#     if len(res) > 0:
#         movie_url=res[0]
#         return movie_url
#
#
# def save(movie_url):
#     response=requests.get(movie_url,stream=False)
#     if response.status_code == 200:
#         m=hashlib.md5()
#         m.update(('%s%s.mp4' %(movie_url,time.time())).encode('utf-8'))
#         filename=m.hexdigest()
#         with open(r'./movies/%s.mp4' %filename,'wb') as f:
#             f.write(response.content)
#             f.flush()
#
#
# def main():
#     index_url='http://www.xiaohuar.com/list-3-{0}.html'
#     for i in range(5):
#         print('*'*50,i)
#         #爬取主页面
#         index_page=get_page(index_url.format(i,))
#         #解析主页面,拿到视频所在的地址列表
#         detail_urls=parse_index(index_page)
#         #循环爬取视频页
#         for detail_url in detail_urls:
#             #爬取视频页
#             detail_page=get_page(detail_url)
#             #拿到视频的url
#             movie_url=parse_detail(detail_page)
#             if movie_url:
#                 #保存视频
#                 save(movie_url)
#
#
# if __name__ == '__main__':
#     main()
#
#
# #并发爬取



import requests
import re
dd={"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}
#发送url请求
req=requests.get("https://www.fpzw.com/xiaoshuo/88/88413",headers=dd)
#接收html文本
res=req.content.decode("gbk")
#
# s1=re.compile("<title>\s*(.*)\s*</title>")
# a=re.findall(s1,res)
# print(a)
#获取小说文本的内容
# print(res)
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
    # n=neirong[0]
    # n=n.replace("<br /><br />","\n")
    # n=n.replace("&nbsp;&nbsp;&nbsp;&nbsp;"," ")
    # with open(file="b.txt",mode="a",encoding="utf8") as  f:
    #     f.write(f"{i[1]}\n")
    #     f.write(f"{n}")
    #     f.write("\n")

# lyf 2019/7/9 17:00:44
# jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S
#
# 对方取消在线传输，转为发送离线文件“%}p{lni[s`8.jpeg”(793.34KB)。
#
# 郑前进 2019/7/30 11:00:48
#
#
# 郑前进 2019/8/2 19:10:27
# D:\Youdao
#
# 郑前进 2019/8/2 19:10:33
# import requests
# import re
# import time
# import hashlib
#
# def get_page(url):
#     print('GET %s' %url)
#     try:
#         response=requests.get(url)
#         if response.status_code == 200:
#             return response.content
#     except Exception:
#         pass
#
# def parse_index(res):
#     obj=re.compile('class="items.*?<a href="(.*?)"',re.S)
#     detail_urls=obj.findall(res.decode('gbk'))
#     for detail_url in detail_urls:
#         if not detail_url.startswith('http'):
#             detail_url='http://www.xiaohuar.com'+detail_url
#         yield detail_url
#
# def parse_detail(res):
#     obj=re.compile('id="media".*?src="(.*?)"',re.S)
#     res=obj.findall(res.decode('gbk'))
#     if len(res) > 0:
#         movie_url=res[0]
#         return movie_url
#
#
# def save(movie_url):
#     response=requests.get(movie_url,stream=False)
#     if response.status_code == 200:
#         m=hashlib.md5()
#         m.update(('%s%s.mp4' %(movie_url,time.time())).encode('utf-8'))
#         filename=m.hexdigest()
#         with open(r'./movies/%s.mp4' %filename,'wb') as f:
#             f.write(response.content)
#             f.flush()
#
#
# def main():
#     index_url='http://www.xiaohuar.com/list-3-{0}.html'
#     for i in range(5):
#         print('*'*50,i)
#         #爬取主页面
#         index_page=get_page(index_url.format(i,))
#         #解析主页面,拿到视频所在的地址列表
#         detail_urls=parse_index(index_page)
#         #循环爬取视频页
#         for detail_url in detail_urls:
#             #爬取视频页
#             detail_page=get_page(detail_url)
#             #拿到视频的url
#             movie_url=parse_detail(detail_page)
#             if movie_url:
#                 #保存视频
#                 save(movie_url)
#
#
# if __name__ == '__main__':
#     main()


#并发爬取
from concurrent.futures import ThreadPoolExecutor
import queue
import requests
import re
import time
import hashlib
from threading import current_thread

p=ThreadPoolExecutor(50)

def get_page(url):
    print('%s GET %s' %(current_thread().getName(),url))
    try:
        response=requests.get(url)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(e)

def parse_index(res):
    print('%s parse index ' %current_thread().getName())
    res=res.result()
    obj=re.compile('class="items.*?<a href="(.*?)"',re.S)
    detail_urls=obj.findall(res.decode('gbk'))
    for detail_url in detail_urls:
        if not detail_url.startswith('http'):
            detail_url='http://www.xiaohuar.com'+detail_url
        p.submit(get_page,detail_url).add_done_callback(parse_detail)

def parse_detail(res):
    print('%s parse detail ' %current_thread().getName())
    res=res.result()
    obj=re.compile('id="media".*?src="(.*?)"',re.S)
    res=obj.findall(res.decode('gbk'))
    if len(res) > 0:
        movie_url=res[0]
        print('MOVIE_URL: ',movie_url)
        with open('db.txt','a') as f:
            f.write('%s\n' %movie_url)
        # save(movie_url)
        p.submit(save,movie_url)
        print('%s下载任务已经提交' %movie_url)
def save(movie_url):
    print('%s SAVE: %s' %(current_thread().getName(),movie_url))
    try:
        response=requests.get(movie_url,stream=False)
        if response.status_code == 200:
            m=hashlib.md5()
            m.update(('%s%s.mp4' %(movie_url,time.time())).encode('utf-8'))
            filename=m.hexdigest()
            with open(r'./%s.mp4' %filename,'wb') as f:
                f.write(response.content)
                f.flush()
    except Exception as e:
        print(e)

def main():
    index_url='http://www.xiaohuar.com/list-3-{0}.html'
    for i in range(5):
        p.submit(get_page,index_url.format(i,)).add_done_callback(parse_index)


if __name__ == '__main__':
    main()

# 爬取校花网视频
