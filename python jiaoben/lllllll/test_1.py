"""
pytest  是 python 自动化测试一个工具库
作用：
    1、调整测试用例的运行顺序
    2、对测试用例传入测试数据
    3、对测试用例设置断言
    4、python 与allure生成测试报告
特点：
    灵活、支持的插件丰富
"""
import  pytest
"""
自动化测试用例是什么？
    指的是一个函数，必须以test开头
"""
def test_0():
    """计算100之内的和"""
    n = 0
    for i in  range(101):
        n += i
        #预期结果是5050
        #实际结果是n
        #断言指的是：拿实际结果与预期结果对比的过程
    assert  n == 5050
#执行测试用例
"""
1、pytest  -v  加文件名(test_1.py)
2、py.test  -v  test_1.py






pytest 与allure联用
pytest test_1.py  --alluredir  ./result/
allure generate ./result/ -o ./report/ --clean
allure open -h 127.0.0.1 -p 8083 ./report/
"""
