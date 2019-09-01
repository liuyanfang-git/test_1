# python 套接字  使用的模块 socket
#作用：实现两个应用或多个应用的数据传输

#服务端
import socket
#指定服务器的ip地址和监听端口号
ip_port = ('127.0.0.1',6666)
#建立一个套接字，为了服务器与客户端传输信息
s = socket.socket()
# 绑定服务地址和端口号
s.bind(ip_port)
#设置最大连接数
s.listen(5)
# 提示服务端已经开启的信息，
print('启动socket服务，等待客户端连接...')
# socket会自动处理拥塞控制  accept(),持续开启服务，一直到手动关闭为止
conn, address = s.accept()

#处理客户端发来的数据


#第一步接收客户端的发送的数据
# s_data = conn.recv(1024).decode('utf-8')
# print(s_data)
# print(address)
# t = input("输入发送的信息")
# #发送
# s.sendall(t.encode())
while True:
    #第一步接收客户端发送的数据
    c_date = conn.recv(1024).decode('utf-8')
    print(f'服务器向客户端发送的内容是：{c_date}')
    t = input("输入发送到客户端的信息")
    if t == '1':
        print('关闭服务器')
        break
    else:
        #发送信息给客户端
        """
        1、先找到客户端
        2、使用sendall
        """
        conn.sendall(t.encode())





#关闭连接
s.close()