# Python 模块（Module）是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和 Python 语句
# 模块能定义函数、类和变量，模块中也能包含可执行的代码

# Python 自带库，运用 import 引入的函数等，也就是模块，例如 random 函数其实是个 Python 文件，也是个模块

# 1. import
'''
语法：
1. 导入模块
import 模块名
import 模块名1, 模块名2...

2. 调用功能
模块名. 功能名()'''

# 需求：math 模块下 sqrt() 开平方计算
# 1.1 import 模块名
import math          # 导入数学模块
print(math.sqrt(9))  # 开平方功能 sqrt()
# 3.0

# 1.2 from...import...
'''
语法：
from 模块 import 功能1, 功能2, 功能3'''
from math import sqrt
print(sqrt(16))     # 可以省略功能名
# 4.0


# 1.3 from...import *
'''
语法：
from 模块名 import *'''
from math import *  # * 有点类似于 基类 的感觉，包括所有 math 里的 函数（自己的理解）
print(sqrt(25))
# 5.0
