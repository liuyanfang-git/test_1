
#        使用python远程操作linux系统         paramiko        下载方法： pip  install  paramiko
#  运维  专业操作linux
import   paramiko

#第一步  连接linux系统
#  建立连接第一步，创造一个sshlien对象
s = paramiko.SSHClient()
#  建立连接第二步，允许信任linux主机，类似xshell第一次连接的保存信息
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#  建立连接的第三步，使用connect（）连接远程linux主机
s.connect(
    hostname="192.168.10.42",
    port=22,
    username="root",
    password="123456"
)
#   然后运行

# 第二步  执行linux命令
#   exec_command(需要执行的命令)：  执行命令发的方法，命令要写成字符串类型
stdin,stdout,stderr = s.exec_command("ls -al")   #stdin  命令， stdout 结果，  stderr   错误
print(stdout.read().decode())       #  读取需要执行命令的结果

#  第三步  文件上传，下载
# 第二种连接方式linux的方式，  使用端口号连接  22
#   套字节编程   ————网络编程
#Transport (参数):  端口号连接linux系统， 参数：包含ip地址，端口号的元组
t = paramiko.Transport(("192.168.10.42",22))
t.connect(username="root",password="123456")
# SFTPtClient.from_transport(t)     sftp客户端方法        参数  指的是一个套字节服务端口   ————t
sftp = paramiko.SFTPClient.from_transport(t)     #   创建一个文件传输通道
x1 = "/home/python.py"    #   linux 远程文件
x2 = r"E:\untitled1\python\a.txt"    #  保存到本地的位置     路径前加  r    关闭转义
#  get(远程文件，本地文件)   ：  下载
sftp.get(x1,x2)

#  put (本地文件，远程文件);   上传

sftp.put(x2,x1)

#  关闭连接，断开连接
t.close()
s.close()



import paramiko
class A(object):
    def __init__(self):
        self.t = paramiko.Transport(('192.168.85.133', 22))
        self.t.connect(username='root', password='123456')
    def Li(self):
        sftp = paramiko.SFTPClient.from_transport( self.t)
        x1 = '/home/huazheng/74'  # linux远程文件
        x2 = r'D:\Users\huazheng\PycharmProjects\untitled/o.txt'  # 保存到本地位置
        sftp.get(x1, x2)

r=A()
r.Li()


