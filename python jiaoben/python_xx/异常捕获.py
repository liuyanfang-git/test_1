#python异常处理
#  1、错误
"""
1、python语法错误：书写格式class、缩进
2、代码逻辑错误：python解释器无法编译解释，导致python报错
"""
# 2、异常
"""
处理错误过程被称为异常处理
"""
# 3、try ... except  最简单的异常处理
# try:
#     d = 1 / 0
#     print(d)
# except:
#     print("异常被处理")
# 4、try  ...  except  ...  finally
# try:
#     d = 1 / 0
#     print(d)
# except OverflowError:
#     print("OverflowError异常处理")
# except ZeroDivisionError:
#     print("ZeroDivisionError已处理")
# finally:
#     print('无论是否被处理，都会输出finally下面的代码')
#try ...  except  ... else
# try:
#     d = 1 / 0
#     print(d)
# except OverflowError:
#     print("OverflowError异常处理")
# except ZeroDivisionError:
#     print("ZeroDivisionError已处理")
# else:
#     print("不存在异常处理，执行else下面的代码")
# python  with
#with： 应用场合：主要是操作系统资源、建立连接、python线程、进程的关闭释放
#with ：上下文管理
with open(file="a.txt",mode="r",encoding="utf-8")  as  f :
    print(f.read())




