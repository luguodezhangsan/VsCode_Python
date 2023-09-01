dict1 = {'name': 'Tom', 'age': 20 ,'gender': '男'}
# 遍历键
for key in dict1.keys():
    print(key)
'''
name
age
gender'''

# 遍历值
for value in dict1.values():
    print(value)
'''
Tom
20
男'''

# 遍历键值 items() --> 键值对
for item in dict1.items():
    print(item)
'''
('name', 'Tom')
('age', 20)
('gender', '男')'''
dict2 = {'俄罗斯': 1707.5, '加拿大': 997.1, '中国': 960.1}
for i,j in dict2.items():   # 键值对的拆包
    print(f'{i}的面积是{j}万平方千米')
'''
俄罗斯的面积是1707.5万平方千米
加拿大的面积是997.1万平方千米
中国的面积是960.1万平方千米'''