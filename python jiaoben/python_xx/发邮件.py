#python  发送电子邮件
#使用模块  smtplib   email

import  smtplib
from email.mime.text import  MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 设置服务所需的信息
#邮件服务器地址
mail_host = "smtp.163.com"
#用户名
mail_user = "l1157517579@163.com"
#客户端授权吗或密码
mail_pass = "l1157517579"
#设置服务器端口号
mail_port = 465
#邮件发送方的地址
sender = "l1157517579@163.com"
#邮件接收方的地址
receivers = ['benkint@sina.com']#可以写多个

#设置邮件主题：
subject = "python测试"
# #设置正文
# content = "这是我使用python发送的"
# #三个参数：第一个为文本内容，第二个  plain  设置文本格式，第三个 Utf-8  设置编码
# message = MIMEText(content,'plain','utf-8')
#发送有件事填写收件人、发件人、主题
#Header():填写邮件头部

# #发送方信息
# message['From'] = Header(sender)
# #接收方信息
# message['To'] = Header(str(";".join(receivers)))
# #主题绑定
# message['Subject'] = Header(subject)

# # #登录并 发邮件
# # #第一步，登录到邮箱
# # #不使用授权吗
# # a = smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# # #输入密码登录邮箱
# # a.login(user=mail_user,password=mail_pass)
# # #发送邮件
# # a.sendmail(sender,receivers,message.as_string())
# # #发送完成后退出邮箱
# # a.quit()
# # print('发送完成')
# # try:
# #     # 第一步，登录到邮箱
# #     # 不使用授权吗
# #     a = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
# #     # 输入密码登录邮箱
# #     a.login(user=mail_user, password=mail_pass)
# #     # 发送邮件
# #     a.sendmail(sender, receivers, message.as_string())
# #     # 发送完成后退出邮箱
# #     a.quit()
# #     print('发送完成')
# # except smtplib.SMTPException as e:
# #     print("接着把")
# class Yj(object):
#
#     host = "smtp.163.com"
#     user = "l1157517579@163.com"
#     password = "l1157517579"
#     port = 465
#     fa = "l1157517579@163.com"
#     shou = ['guohg18991002302@163.com']
#     zhu = "刘远方"
#     zheng = "刘远方来了"
#     a = MIMEText(zheng, 'plain', 'utf-8')
#     def you(self):
#         self.a = MIMEText(self.zheng,'plain','utf-8')
#         self.a['From'] = Header(self.fa)
#         self.a['To'] = Header(str(';'.join(self.shou)))
#         self.a['Zhu'] = Header(self.zhu)
#     def f(self):
#         try:
#             a1 = smtplib.SMTP_SSL(host=self.host, port=self.port)
#             a1.login(user=self.user, password=self.password)
#             a1.sendmail(self.fa, self.shou, self.a.as_string())
#             a1.quit()
#             print("发送完成")
#         except smtplib.SMTPException as e:
#             print("zhe")
# y = Yj()
# y.f()

#添加一个MIMEMultipart类，将正文及附件天剑到邮件里
message = MIMEMultipart()

#发送方信息
message['From'] = Header(sender)
#接收方信息
message['To'] = Header(str(";".join(receivers)))
#主题绑定
message['Subject'] = Header(subject)
#使用HTML格式的正文内容，添加附件
with  open('123.html','r') as f:
    content = f.read()
#设置HTML格式参数
part1 = MIMEText(content,'html','utf-8')
# 附件代码
#添加一个txt文本附件
with open('a.txt','r') as h:
    content2 = h.read()
#设置txt参数
part2 = MIMEText(content2,'plain','utf-8')

# 附件设置内容类型，方便起见，设置为二进制流
part2['Content-Type'] = 'application/octet-stream'
#设置附件头，添加文件名
part2['Content-Disposition'] = 'attachment;filename="123.txt"'
#添加照片
with open('在网页登录.png','rb') as fp:
    picture = MIMEImage(fp.read())
picture['Content-Type'] = 'application/octet-stream'
picture['Content-Disposition'] = 'attachment;filename="在网页登录.png"'
#将内容附加到邮件主体中  attach（添加的内容）
#将html添加邮件
message.attach(part1)
message.attach(part2)
message.attach(picture)
part1= MIMEText(content,'plain','utf-8')
part1['From'] = Header(sender)
part1['To'] = Header(str(';'.join(receivers)))
part1['Zhu'] = Header(message)

try:
    a1 = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
    a1.login(user=mail_user, password=mail_pass)
    a1.sendmail(sender,receivers,part1.as_string())
    a1.quit()
    print("发送完成")
except smtplib.SMTPException as e:
    print("zhe")