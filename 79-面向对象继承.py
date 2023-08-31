# P292

# Python 面向对象的继承是指多个类之间的所属关系，即子类默认继承父类的所有属性和方法
# 继承的好处：1. 节省代码量

# 父类A
class A(object):
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(self.num)

# 子类B
class B(A): 
    pass

# 创建对象，验证结论
result = B()
result.print_info()
# 1
# 所有类默认继承 object 类，object 类是顶级类或基类，其他子类称之为派生类