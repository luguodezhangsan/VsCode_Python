# P157
'''
只有：
列表推导式
字典推导式
集合推导式
作用：用一个表达式创建一个有规律的列表或控制一个有规律列表
列表推导式 又称 列表生成式
目标：简化代码'''

# 需求：创建一个 0-10 的列表
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for 循环实现
list2 = []
for i in range(10):
    list2.append(i)
print(list2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式实现
list3 = [i for i in range(10)]
print(list3)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 带 if 的列表推导式
# 创建 0-10 的偶数列表
list4 = [i for i in range(10) if i % 2 == 0]
print(list4)
# [0, 2, 4, 6, 8]

# 多个 for 循环实现列表推导式
# 需求：创建列表如下：
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1： 1 和 2 --> range(1,3)
# 数据2： 0, 1, 2 --> range(3)
list5 = []
for i in range(1, 3):
    for j in range(3):
        list5.append((i, j))
print(list5)
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

list6 = [(i,j) for i in range(1,3) for j in range(3)]  # --> for 的顺序就是从左到右
print(list6)
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 字典推导式
dict1 = {}
for key in range(1, 5):
    dict1[key] = key ** 2
print(dict1)
# {1: 1, 2: 4, 3: 9, 4: 16}

dict2 = {i: i**2 for i in range(1, 5)}
print(dict2)
# {1: 1, 2: 4, 3: 9, 4: 16}

# 快速将两个列表合并为一个字典
list7 = ['name' ,'age', 'gender']
list8 = ['Tom', 20, 'man']
dict3 = {list7[i]: list8[i] for i in range(len(list7))}
print(dict3)
# {'name': 'Tom', 'age': 20, 'gender': 'man'}
# 1. 如果两个列表数据个数相同，len()统计任何一个列表的长度都可以
# 2. 如果两个列表数据个数不同，len()统计数据多的列表数据个数会报错；len()统计数据少的列表数据个数不会报错
dict4 = {}
i = 0
for key in list7:
    dict4[key] = list8[i]
    i += 1
print(dict4)
# {'name': 'Tom', 'age': 20, 'gender': 'man'} --> 自己想的

# 提取字典中的目标数据
counts = {'Mac': 268, 'HP': 125, 'Dell': 201, 'Acer':99, 'Lenovo': 320}
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)
# {'Mac': 268, 'Dell': 201, 'Lenovo': 320}

# 集合推导式（使用机率最低）
list9 = [1, 1, 2, 3]
set9 = {i ** 2 for i in list9}
print(set9)
# {1, 4, 9} --> 自动使用了去重功能