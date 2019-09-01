#客户端
import  socket
#指定客户端IP，端口号
ip_port = ('127.0.0.1',6666)
#创建一个套接字，目的是接收服务器发送的数据
c = socket.socket()
#连接服务器
c.connect(ip_port)

# t = input("输入发送的信息")
# #发送
# c.sendall(t.encode())

while True:
    # 发送数据到服务器、接收服务器数据
    t = input("输入发送的信息")
    #设置一个条件跳出死循环
    if t == '1':
        break
    else:
        #发送信息到服务器
        print(f'客户端向服务器发送的信息')
        c.sendall(t.encode())
    #处理服务器已经发送到客户端上的信息
    s_data = c.recv(1024).decode(encoding='utf-8')
    print(s_data)
#关闭连接
c.close()


