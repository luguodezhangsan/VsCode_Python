# 字典的添加操作
dictAreas = {}
dictAreas['俄罗斯'] = 1707.5
dictAreas['加拿大'] = 991.7
dictAreas['中国'] = 960.1
print(dictAreas)
# 输出：{'俄罗斯': 1707.5, '加拿大': 991.7, '中国': 960.1}

# 字典的修改操作
dictAreas['中国'] = 1
print(dictAreas)
# {'俄罗斯': 1707.5, '加拿大': 991.7, '中国': 1}
# 字典名[键] = 值 --> 是一个双重操作，当键值在字典中不存在则执行的是添加操作，当键值存在时则执行的是修改操作

# 字典的删除操作
# 1. del 字典名[键]
del dictAreas['中国']
print(dictAreas)
# {'俄罗斯': 1707.5, '加拿大': 991.7}
# del dictAreas == del(dictAreas) --> 直接删除整个字典
# print(dictAreas) --> 直接删除了整个字典会报错
# NameError: name 'dictAreas' is not defined

# 2. 字典名.pop(键, 默认值)
area = dictAreas.pop('加拿大')
print(area)
# 991.7
# pop删除会返回键所对应的值，故需要将值赋予相应的变量(area)
# 若不确定键在字典之中是否存在，需要给出 默认值 ，否则删除不确定键时系统会报错，给出 默认值 后会返回 默认值，不会报错
area1 = dictAreas.pop('美国', '找不到要删除的条目')
print(area1)
# 找不到要删除的条目

# 3. 字典名.popitem()
# 该方法为随机删除并返回某个完整的条目，并将删除的条目返回为元组
dict1 = {'name': 'Tom', 'age': 20 ,'gender': '男'}
item = dict1.popitem()
print(item)        # ('gender', '男')
print(type(item))  # <class 'tuple'>
print(dict1)       # {'name': 'Tom', 'age': 20}

# 4. 字典名.clear()
# 直接清空字典里所用键值对，但仍然保留空字典与格式dict，不需要赋值
dict1.clear()
print(dict1)
# {}

# 字典的查找操作
#  1. 键 in 字典
dict1 = {'name': 'Tom', 'age': 20 ,'gender': '男'}
i = 'name' in dict1
print(i)
# True

# 2. 字典名.get(键, 默认值)
print(dict1.get('name'))
# Tom
m = dict1.get('id', 'id未能成功查找！')
print(m)
# id未能成功查找！ --> 由于字典中不存在该键，所以系统返回了设定的默认值：id未能成功查找！
n = dict1.get('color')
print(n)
# None --> 未设定默认值则返回 None\

# 3. 字典名.keys() --> 查找字典中所有的 key， 返回可迭代的对象（即可以被遍历的对象）
print(dict1.keys())
# dict_keys(['name', 'age', 'gender'])

# 4. 字典名.values() --> 查找字典中所有的 value， 返回可迭代的对象（即可以被遍历的对象）
print(dict1.values())
# dict_values(['Tom', 20, '男'])

# 5. 字典名.items() --> 返回可迭代的列表，将键值变为元组

print(dict1.items())
# dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])

