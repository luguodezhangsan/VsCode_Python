# 1. 无参数
fn1 = lambda: 100
print(fn1())
# 100

# 2. 一个参数
fn3 = lambda a: a
print(fn3('hello world'))
# hello world

# 3. 默认参数 (缺省参数) --> 如果对默认参数传值，则会修改默认值，若不修改默认值，则自动使用默认值
fn2 = lambda a, b, c= 100: a + b + c
print(fn2(10, 20))
# 130

# 4.可变参数：*args
fn4 = lambda *args: args
print(fn4(10, 20, 30))
# (10, 20, 30)  返回的是元组
print(fn4(1, 2, 3, 4, 5))
# (1, 2, 3, 4, 5)

# 5. 可变参数：**kwargs
fn5 = lambda **kwargs: kwargs
print(fn5(name = 'Tom', age = 20, tel = 114514))
# {'name': 'Tom', 'age': 20, 'tel': 114514}  返回的是字典
print(fn5(tel = 112134, name = 'Jack', age = 18))
# {'tel': 112134, 'name': 'Jack', 'age': 18}