# P127
# 元组：存储多个不可修改的数据
t = (1, 2 ,3)
print(t)
print(type(t))
# 用于存些身份证号等严肃的，不可修改的数据

# 多个数据元组
t1 = (10, 20, 30)
# 单个数据元组
t2 = (10,)       # 加单个逗号才能变为元组
t3 = (10)
t4 = ('aaa')
print(type(t2))  # <class 'tuple'>
print(type(t3))  # <class 'int'>
print(type(t4))  # <class 'str'>