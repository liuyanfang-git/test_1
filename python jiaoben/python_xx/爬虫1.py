import re
import requests
import re
import xlwt
import xlrd
# class DouBan(object):
#     def Tou(self):
#       url = 'https://book.douban.com/latest?icn=index-latestbook-all'
#       heards = {'User-agent':'mozilla/5.0 (Windows NT 10.0: WOW64)'
#                    }
#       a=requests.get(url,heards)
#       s=a.content.decode('utf-8')
#       i=re.compile(r'><img src="(.*?)"/></a',re.S)
#       j=i.findall(s)
#       w=re.compile(r'<a href="https://book.douban.com/subject/.*?/">(.*?)</a>',re.S)
#       q=w.findall(s)
#       #c=zip(j,q)
#       #print(j)
#       for x,y in zip(j,q):
#           #print(x)
#           ss=requests.get(x)
#           aa=ss.content
#           with open(r'd:/aa/{}.jpg'.format(y),'wb') as f:
#               f.write(aa)
# Picture=DouBan()
# Picture.Tou()
class Zl(object):
    def get(self):
        url = r"https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.97367611&x-zp-page-request-id=e3ce6b8e335943f1a928310dab8b93bc-1562659128753-22218&x-zp-client-id=fac80a41-ebc2-4e4b-8593-ee8339b0c857"
        heards = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        a = requests.get(url,heards)
        s = a.content.decode('utf-8')#可以写成 a.text
        print(s)
        i = re.compile(r'jobName":"(.*?)".*?company":{"name":"(.*?)".*?display":"(.*?)".*?salary":"(.*?)".*?eduLevel":{"name":"(.*?)".*?workingExp":{"name":"(.*?)"',re.S)
        j = re.findall(i,s)
        # print(j)
        return j
    def biao(self):
        s1 = self.get()
        q1 = xlwt.Workbook()
        q2 = q1.add_sheet("biao")
        print(s1)
        for  j in range(len(s1)):
            # print(j)
            for i in range(len(s1[j])):

                q2.write(j,i,s1[j][i])
        q1.save('zhilian1.xls')
z = Zl()
# z.get()
z.biao()
