name_list = ['Tom', 'Lily', 'Rose']

# 列表增加数据操作：
# append(), extennd()   列表末尾增加数据
# insert()  任意位置增加数据

# 1. append()
name_list.append('Jack')
print(name_list)
# 列表为可改的 -- 列表为可变类型
name_list.append([1, 2])
print(name_list)
# 输出：['Tom', 'Lily', 'Rose', 'Jack', [1, 2]]
# 列表追加的数据是一个序列，则追加整个序列到列表

# 2. extend()
# 列表追加数据，若数据单个元素，则会被拆分开，并逐一加入到列表之中
name_list.extend('Xiaoming')
print(name_list)
# 输出：['Tom', 'Lily', 'Rose', 'Jack', [1, 2], 'X', 'i', 'a', 'o', 'm', 'i', 'n', 'g']

name_list.extend(['Xiaoming', 'Honghong'])
print(name_list)
# 输出：['Tom', 'Lily', 'Rose', 'Jack', [1, 2], 'X', 'i', 'a', 'o', 'm', 'i', 'n', 'g', 'Xiaoming', 'Honghong']
# 若追加列表数据，会把列表剥开为一个个元素并加入到原有列表中（具有拆分的效果）

# 3. insert()
# 语法：列表序列.insert(位置下标, 增加数据)
name_list2 = ['Tom', 'Lily', 'Rose']
name_list2.insert(1, 'Mary')
print(name_list2)  # 位置下标，使增加数据变为下标位置
# 输出：['Tom', 'Mary', 'Lily', 'Rose']

# 删除数据
# 1. del 目标数据
# name_list3 = ['Tom', 'Lily', 'Rose']
# del name_list3
# print(name_list3)
# 输出：NameError: name 'name_list3' is not defined
# name_list3已被删除掉，则显示name_list3未被定义
# 可以和索引下标结合删除指定下标的数据
name_list4 = ['Tom', 'Lily', 'Rose']
del name_list4[0]
print(name_list4)

# 2. pop() -- 删除指定下标的数据，如果不指定下标，则默认删除最后一个数据
# 无论是按照下标还是删除最后一个数据pop函数都会返回这个被删除的数据
name_list5 = ['Tom', 'Lily', 'Rose']
del_name_list5 = name_list5.pop(1)
print(name_list5)       # 输出：['Tom', 'Rose']
print(del_name_list5)   # 输出：Lily

# 3.remove(数据)
name_list5.remove('Tom')
print(name_list5)  # 输出：['Rose']

# 4.clear() -- 清空数据
name_list5.clear()
print(name_list5)  # 返回：[]

# 两个列表相结合的简单操作
list_a = [10, 100, 1000]
list_b = [10000, 100000]
list_c = list_a + list_b
print(list_c)