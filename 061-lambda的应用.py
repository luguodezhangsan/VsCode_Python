# 1. 带判断的 lambda
fn1 = lambda a, b: a if a > b else b
print(fn1(10, 50))
# 50

# 2. 列表数据按字典 key 值进行排序
students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Mary', 'age': 18}, 
    {'name': 'Jack', 'age': 19}
]

# sort(key = lambda ..., reverse = bool)
# 1. name key 对应的值进行升降排序
students.sort(key = lambda x: x['name'])
print(students)
# [{'name': 'Jack', 'age': 19}, {'name': 'Mary', 'age': 18}, {'name': 'Tom', 'age': 20}]

# 2. name key 对应的值进行降序排序
students.sort(key = lambda x: x['name'], reverse = True)
print(students)
# [{'name': 'Tom', 'age': 20}, {'name': 'Mary', 'age': 18}, {'name': 'Jack', 'age': 19}]

# 3. 使用 sorted(字典名, key = lambda ..., reserse = bool) 进行排序
print(sorted(students, key= lambda x: x['name'], reverse= True))
# [{'name': 'Tom', 'age': 20}, {'name': 'Mary', 'age': 18}, {'name': 'Jack', 'age': 19}]