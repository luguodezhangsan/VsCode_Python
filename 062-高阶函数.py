# 把函数作为参数传入，这样的函数称为高阶函数，目的是为了化简函数
print(abs(-10))
print(round(1.2))
print(round(1.9))
'''
10
1
2
'''

# 需求：任意两个数字，按照指定要求整理后再进行求和计算
# 方法1：
def add_num(a, b):
    return abs(a) + abs(b)

print(add_num(3, -1))
# 4


# 方法2：
def sum_num(a, b, f):
    return f(a) + f(b)

result = sum_num(3, -1, abs)  # abs 为函数名，这就是高阶函数，和 方法1 相比更加简洁了
print(result)
# 4
result2 = sum_num(1.1, 1.9, round)
print(result2)
# 3

# 内置高阶函数
# 1. map(func, lst) --> 将传入的函数变量 func 作用到 lst 变量的每一个元素中，并将结果组成新的列表 (Python2) 或迭代器 (Python3) 返回
list1 = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result1 = map(func, list1)
print(result1)  # map 函数的地址
print(list(result1))  # 输出结果
# <map object at 0x00000276572C6FA0>
# [1, 4, 9, 16, 25]

# 2. reduce(func, lst) --> 其中 func 必须有两个参数。每次 func 计算的结果继续和序列下一个元素做累积计算
# 需求：计算 list2 中所有数据累加和
import functools

list2 = [1, 2, 3, 4, 5]
def func(a, b):
    return a + b  # 这里改为 * 以后，结果就是所有数据相乘，最后结果为 120

result2 = functools.reduce(func, list2)
print(result2)
# 15

# 3. filter(func, lst) --> 函数用于过滤序列，过滤掉不符合条件的元素，返回一个 filter 对象。如果要转化为列表，可以用 list() 来转换
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x % 2 == 0

result3 = filter(func, list3)
print(result3)
print(list(result3))
# <filter object at 0x000002DCEFA18DF0>
# [2, 4, 6, 8, 10] --> 过滤掉了不符合条件的元素

# 没有使用函数，纯循环
list4 = []

for x in list3:
    if x % 2 == 0:
        list4.append(x)

print(list4)
# [2, 4, 6, 8, 10]
