import pytest


def test_1():
    a = 1
    b = 2
    c = a + b
    # 实际结果是3，预期结果是2
    # 设定断言
    assert c == 2


def test_2():
    str_1 = "hello pytest"
    str_2 = "python"
    # 设定断言，判断str_2 在 str_1内
    assert str_2 in str_1
"""
pytest:
查找当前目录下，所有文件或目录，找包含test目录或文件
如果找到test目录，类似于cd，执行所有包含test开头的文件
搜索test开头的所有的函数

整个当前目录下没有包含test开头的文件和目录：
_____ERROR collecting test session ____
"""
# -v  使输出的信息更加详细
# -q  简化输出信息

# -k  执行包含“关键字”的用例
# -s  输出测试用例中print内的信息
#脚本名：：用例名   --->运行执行脚本中的具体用例