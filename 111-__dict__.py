# 1. 定义类
class A(object):
    a = 0  # 类属性

    def __init__(self):
        self.b = 1  # 实例属性

# 2. 创建对象
aa = A()

# 3. 调用__dict__
print(A.__dict__)
# 返回类内部所有属性和方法对应的字典

print(aa.__dict__)
# 返回实例属性和值组成的字典
'''
{'__module__': '__main__', 'a': 0, '__init__': <function A.__init__ at 0x00000234A6C70EE0>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{'b': 1}'''
# 返回的都是字典