# 视频教程未涉及，来源于Python程序设计
# 字典中一般不支持中文的排序，故使用英文
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
a = sorted(dictAreas)
print(a)
# ['Canada', 'China', 'Russia']  默认将键按照字母顺序升序排列，但字典本身的键值不会发生变化
print(dictAreas)
# {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}

# 按照国家名的升序输出三个国家和对应的土地面积：
for country in a:
    print(country,dictAreas[country])
'''
Canada 997.1
China 960.1
Russia 1707.5'''

# 拓展：如何通过国土面积大小输出升序排序？
IsVK = [(v, k) for k,v in dictAreas.items()]  # 将其转化为列表嵌套元组的方式
IsVK.sort()
IsVK = [(k, v) for v,k in IsVK]
print(IsVK)
# [('China', 960.1), ('Canada', 997.1), ('Russia', 1707.5)]

# 字典的合并
# 1. for循环
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
dictOthers = {'Brazil': 854.7, 'America': 936.4}
for k,v in dictOthers.items():
    dictAreas[k] = v
print(dictAreas)
# {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1, 'Brazil': 854.7, 'America': 936.4}

# 2. update()
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
dictOthers = {'Brazil': 854.7, 'America': 936.4}
dictAreas.update(dictOthers)
print(dictAreas)
# {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1, 'Brazil': 854.7, 'America': 936.4}

# 3. dict() 
# 将字典变成列表后合并，再转化为字典
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
dictOthers = {'Brazil': 854.7, 'America': 936.4}
Is = list(dictAreas.items()) + list(dictOthers.items())  # 不加.items()则会报错
dictAreas = dict(Is)
print(dictAreas)
# {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1, 'Brazil': 854.7, 'America': 936.4}

# 4.dict(**)
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
dictOthers = {'Brazil': 854.7, 'America': 936.4}
dictAreas = dict(dictAreas,**dictOthers)
print(dictAreas)
# {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1, 'Brazil': 854.7, 'America': 936.4}

# 案例：合并“国家-面积”和“国家-首都”的两个字典为一个字典
dictAreas = {'Russia': 1707.5, 'Canada': 997.1, 'China': 960.1}
dictCapitals = {'Russia': 'Moscow', 'Canada': 'Ottawa', 'China': 'Beijing'}
dictcountries = {}
for key in dictAreas.keys():
    dictcountries[key] = [dictAreas[key], dictCapitals[key]]
for item in dictcountries.items():
    print(item)
'''
('Russia', [1707.5, 'Moscow'])
('Canada', [997.1, 'Ottawa'])
('China', [960.1, 'Beijing'])'''