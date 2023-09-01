'''
语法：
try:
    可能发生错误的代码
except 异常类型:
    如果捕获到该异常则执行改代码'''

# print(num)
''' 
NameError: name 'num' is not defined
NameError: 异常类型
后面的部分为异常信息'''

# print(1/0)
''' 
除数不能为0
ZeroDivisionError: division by zero'''

'''
try:
    print(num)
except NameError:
    print('num未被定义')
'''
# num未被定义

try:
    print(1/0)
except ZeroDivisionError:
    print('0 不能做除数')
# 0 不能做除数

try:
    print(2/0)
except NameError:
    print('0 不能做除数')
# ZeroDivisionError: division by zero  捕获的异常类型与执行代码异常不一致,会报错异常代码的解释器,非 except 则 try 
'''
1. 如果尝试执行的代码的异常和要捕获的异常类型不一样，则无法捕获异常
2. 一般 try 下方只放一行尝试执行的代码'''
# except 的作用更像是捕获 try 中出现的问题，然后进行输出 except 后面的内容