# 4.认识不同的数据类型
'''
数值型:
int
float
布尔型:
True
False

str
list
tuple
set
dict
'''

# 如何检测数据的类型？
num1 = 1
num2 = 1.1
print(type(num1))
print(type(num2))
# 必须加print才能输出，否则不会输出
a = 'hello world!'
print(type(a))

# bool -- 布尔型，通常判断使用，布尔型有两个取值True或False.
b = True
print(type(b))

# list -- 列表
c = [1, 2, 3]

# tuple -- 元组
d = (2, 4, 6)

# dict -- 字典
e = {'狗熊', '老虎', '熊猫'}