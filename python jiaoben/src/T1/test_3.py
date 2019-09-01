"""
清理测试环境的一个机制
第一步：在用例执行之前进行环境清理
第二步：在用例执行之后进行环境清理
"""
#脚本级别的清理
#setup_module  用例执行之前的
#teardown_module  用例执行之后
#module 本脚本所有的用例执行之前、之后的操作仅执行一次

import pytest
"""
def setup_module():
    print("所有用例执行之前执行一次")

def test_1():
    print("用例1执行")

def  test_2():
    print("用例2执行")

def  test_3():
    print("用例3执行")

def  teardown_module():
    print("所有用例执行之后执行一次")
    
#setup_function  每个测试用例运行之前都要执行一次
#teardown_function  每个测试用例运行之后都要执行一次
"""

"""
def setup_function():
    print("每个用例执行之前执行一次")


def test_1():
    print("用例1执行")


def test_2():
    print("用例2执行")


def test_3():
    print("用例3执行")


def teardown_function():
    print("每个用例执行之后执行一次")
#setup   teardown   在类的范围内使用
class  TestOne(object):
    def  setup(self):
        print("执行setup")
    def  teardown(self):
        print("执行teardown")

    def test_4(self):
        print("用例4执行")

    def test_5(self):
        print("用例5执行")

    def test_6(self):
        print("用例6执行")
"""
#setup --->每个测试用例运行之前执行一次
#teardown--->每个测试用例运行之后执行一次

#setup_class  ---->类中的所有测试用例运行前执行一次
#teardown_class --->类中的所有测试用例运行后执行一次

"""
class  TestOne(object):
    def  setup_class(self):
        print("执行setup")
    def  teardown_class(self):
        print("执行teardown")

    def test_4(self):
        print("用例4执行")

    def test_5(self):
        print("用例5执行")

    def test_6(self):
        print("用例6执行")
"""

#setup_method  --->每个测试用例运行之前执行一次 方法级别
#teardown_method ---> 每个测试用例运行之后执行一次 方法级别

"""
class  TestOne(object):
    def  setup_method(self):
        print("执行setup_method")
    def  teardown_method(self):
        print("执行teardown_method")

    def test_4(self):
        print("用例4执行")

    def test_5(self):
        print("用例5执行")

    def test_6(self):
        print("用例6执行")

"""
#测试夹具 fixture
# @pytest.fixture()
"""
scope ：装饰器的作用范围
        function  方法级别（函数级别）默认
        class     类级别
        module    脚本级别
        package   目录级别（包级别）
        session   会话级别
"""

# def fixture(scope="function", params=None, autouse=False, ids=None, name=None):
#     """Decorator to mark a fixture factory function.
#
#     This decorator can be used, with or without parameters, to define a
#     fixture function.
#
#     The name of the fixture function can later be referenced to cause its
#     invocation ahead of running tests: test
#     modules or classes can use the ``pytest.mark.usefixtures(fixturename)``
#     marker.
#
#     Test functions can directly use fixture names as input
#     arguments in which case the fixture instance returned from the fixture
#     function will be injected.
#
#     Fixtures can provide their values to test functions using ``return`` or ``yield``
#     statements. When using ``yield`` the code block after the ``yield`` statement is executed
#     as teardown code regardless of the test outcome, and must yield exactly once.
#
#     :arg scope: the scope for which this fixture is shared, one of
#                 ``"function"`` (default), ``"class"``, ``"module"``,
#                 ``"package"`` or ``"session"``.
#
#                 ``"package"`` is considered **experimental** at this time.
#
#     :arg params: an optional list of parameters which will cause multiple
#                 invocations of the fixture function and all of the tests
#                 using it.
#                 The current parameter is available in ``request.param``.
#
#     :arg autouse: if True, the fixture func is activated for all tests that
#                 can see it.  If False (the default) then an explicit
#                 reference is needed to activate the fixture.
#
#     :arg ids: list of string ids each corresponding to the params
#                 so that they are part of the test id. If no ids are provided
#                 they will be generated automatically from the params.
#
#     :arg name: the name of the fixture. This defaults to the name of the
#                 decorated function. If a fixture is used in the same module in
#                 which it is defined, the function name of the fixture will be
#                 shadowed by the function arg that requests the fixture; one way
#                 to resolve this is to name the decorated function
#                 ``fixture_<fixturename>`` and then use
#                 ``@pytest.fixture(name='<fixturename>')``.
#     """
#     if callable(scope) and params is None and autouse is False:
#         # direct decoration
#         return FixtureFunctionMarker("function", params, autouse, name=name)(scope)
#     if params is not None and not isinstance(params, (list, tuple)):
#         params = list(params)
#     return FixtureFunctionMarker(scope, params, autouse, ids=ids, name=name)


import pytest
"""
@pytest.fixture()
def login():
    print("login函数开始执行")

def  test_1(login):
    print("执行用例1")

def  test_2(login):
    print("执行用例2")

def  test_3(login):
    print("执行用例3")

"""
"""
class TestThree(object):
    @pytest.fixture(scope='class')
    def login_1(self):
        print("开始执行login_1方法")

    def test_4(self,login_1):
        print("执行用例4")

    def test_5(self,login_1):
        print("执行用例5")

    def test_6(self,login_1):
        print("执行用例6")
"""

# module  :脚本级别。 所有的测试用例执行之前运行一次，只运行一次
#使用方法： 在测试用例的（放被@pytest.fixtute装饰的函数）
#package  ：目录级别。
#session  ：会话级别。，多个测试用例组合的时候使用

"""
@pytest.fixture(scope='module')

def start():
    print("所有的测试用例执行之前、运行一次")
@pytest.fixture(scope='module')
def close():
    print("所有的测试用例执行之前运行一次")


def test_4(start):
    print("执行用例4")


def test_5(start):
    print("执行用例5")


def test_6(start,close):
    print("执行用例6")
"""



"""
conftest.py : python文件，用来存放公共函数。被不同的测试用例使用
test开头的脚本下，一般只写以test开头的函数、类、方法
注意事项：
        conftest.py必须放在当前测试用例所在的目录下面
        src/T1/test_1py,   conftest.py必须在T1下面 
"""


"""
def test_1():
    print("输入账号")

def test_2(clean):
    print("输入账号")


def test_3(clean):
    print("输入账号")
"""

""""
# 参数化 ---> 向测试用例中传入参数的过程
d = [1,2,3,4,5,6,7]
@pytest.fixture(scope='function',params=d)
def read_data(request):
    #request  : 必须写成这样，固定写法
    #作用：取出参数列表中每一个元素
    #request.param :固定写法
    #作用： 与request结合使用，取出参数
     print(f"当前的传入的参数是{request.param}")
     return request.param
def  test_1(read_data):
    t = read_data  #实际结果
    #预期结果
    assert  t < 6
"""
"""
#传入两个参数
d2 = [(1,2),(2,2),(3,4)]

@pytest.mark.parametrize("y1,y2",d2)
def test_2(y1,y2):
    print(f"y1的值是{y1}")
    print(f"y2的值是{y2}")
    assert   y1 == y2
"""

@pytest.fixture(autouse='true')
def myfix():
    print("每个测试用例都要跑myfix")
"""
@pytest.mark.usefixtures('myfix')  ---->myfix  等价
pytestmark=pytest.mark.usefixtures("myfix")   每个用例都跑一遍
@pytest.fixture(autouse='true')
ids：
name：
pytest  跳过某些用例、失败重跑、统计测试覆盖率等
"""
# pytestmark=pytest.mark.usefixtures("myfix")
def test_1():
    pass
def test_2():
    pass