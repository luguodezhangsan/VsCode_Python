'''
lambda 作用就是为了简化代码，如果一个函数只有一个返回值，并且只有一句代码，可以使用 lambda 简化
lambda 语法：
lambda 参数列表 : 函数表达式
注意：
1. lambda 表达式的参数可有可无，函数的参数在 lambda 表达式中完全适用
2. lambda 表达式能接收任何数量的参数但只能返回一个表达式的值'''

# 需求：函数 返回值100
# 1. 函数
def fn1():
    return 100

result = fn1()
print(result)
# 100

# 2. lambda 也称 匿名函数
fn2 = lambda: 100
print(fn2)
# <function <lambda> at 0x0000021AD7806040> 返回的是 lambda 的返回地址

print(fn2())
# 100

# 示例：计算 a + b
# 1. 函数实现
def add(a, b):
    return a + b

result = add(1, 2)
print(result)
# 3

# 2. lambda 的实现
f = lambda a, b : a + b
print(f(1, 2))
# 3