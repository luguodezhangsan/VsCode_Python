# P148
# + 合并   * 复制     支持字符串、列表、元组，不支持字典
# in 和 not in 判断元素是否在其中    支持以上4中格式

a = 'Hello World!'
print(a * 10)
# Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!

# 打印10个中横杠
print('-' * 10)
# ----------

list1 = ['Hello']
print(list1 * 10)
# ['Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello']

# in 和 not in
print('H' in list1)
# False --> 列表每个逗号间隔为一个元素，H 不为元素
print('Hello' in list1)
# True

str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
t1 = (10, 20, 30, 40, 50)
s1 = {10, 20, 30, 40, 50}
dict1 = {'name': 'Tom', 'age': 18}
# len() --> 计算容器中元素个数
print(len(str1), len(list1), len(t1), len(s1), len(dict1))
# 7 5 5 5 2

# del 或 del()
# del str1 == del(str1)
# del list1 == del(list1)
# 可添加下标指定删除某个元素

# max()  返回容器中元素最大值
# min()  返回容器中元素最小值
print(max(str1))
print(min(list1))
# g
# 10

# range(start, end, step)  供 for 循环使用
# 和切片类似，end 不包含结束位，同样 step 也可以省略，则默认步长为 1
for i in range(1, 10, 1):
    print(i, end=' ')
# 1 2 3 4 5 6 7 8 9
print()

for j in range(10):
    print(j, end=' ')
# 0 1 2 3 4 5 6 7 8 9
print()

# enumerate() --> 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和下标，一般用在for循环当中
# 语法： enumerate(可遍历对象, start = 0)
# 注意： start参数用来设置遍历数据的下标的起始值，默认为0，可以省略
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
for i in enumerate(list2):
    print(i)
'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
(5, 'f')'''
# 返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据
for j in enumerate(list2,start=1):
    print(j)
'''
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
(5, 'e')
(6, 'f')'''
# 使得下标的起始值从1开始，输出的数据个数不变

# 容器类型的转换
list1 = [1, 2, 3, 4, 5]
s1 = {1 , 2, 3, 4, 5}
t1 = ('a', 'b', 'c', 'd', 'e')
# tuple() --> 将某个列表转化为元组
print(tuple(list1))
print(tuple(s1))
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)

# list() --> 转化为列表
print(list(t1))
# ['a', 'b', 'c', 'd', 'e']

# set() --> 转化为集合，会去掉重复数据

