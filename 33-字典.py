# P132
# 字典以键值对形式出现，字典顺序和数据顺序没有关系，即字典不支持下标，无论后期数据如何变化，找到对应的键就能找到所对应的值
'''
字典的特点：
1. 符号为大括号
2. 数据为键值对的形式出现
3. 各个键值对之间用逗号隔开'''

# 1. 有数据的字典
# 直接创建字典
dict1 = {'name': 'Tom', 'age': 20 ,'gender': '男'}
print(dict1)
print(type(dict1))
dict2 = {}
print(dict2)

# 使用内置函数dict()创建字典
dict3 = dict()
print(dict3)

items = [('俄罗斯', 1707.5), ('加拿大', 997.1), ('中国', 960.1)]
dict4 = dict(items)
print(dict4)
# 输出：{'俄罗斯': 1707.5, '加拿大': 997.1, '中国': 960.1}

# 字典的键具有唯一性，不允许出现相同的键，键还是不可变的类型，一般是字符串，数字或元组，不可以用列表等可变数据作为键，否则会报错
# 如果键由多个数据组成则可以将键写成元组的形式

# 访问字典
print(dict4['俄罗斯'])
# 返回：1707.5
# 如果用键访问字典中不存在的键则会报错
