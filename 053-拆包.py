# 1. 拆包：元组
def return_num():
    return 100, 200
num1, num2 = return_num()
print(num1)
print(num2)
# 100
# 200

# 2. 拆包：字典
dict1 = {'name': 'Tom', 'age': 18}
a, b = dict1  # 默认a, b取字典的键
print(a)
print(b)
# name
# age
print(dict1[a])
print(dict1[b])
# Tom
# 18
