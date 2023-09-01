# 1. 模块定义别名
# import 模块名 as 别名

# 2. 功能定义别名
# from 模块名 import 功能 as 别名

# 改变了名称之后只能使用别名了，不能再使用模块名

# 需求：运行后暂停 2 秒打印 hello
import time as tt  # time --> tt
tt.sleep(2)
# time.sleep(2) --> NameError: name 'time' is not defined --> time 已经被修改了，再次调用会显示未被定义（但 math 库里 time 的名称没有被改，只是在这个 Python 件中被修改了
print('hello')
# hello

from time import sleep as s1
s1(4)
print('hello')
# hello
