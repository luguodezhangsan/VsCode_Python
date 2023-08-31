# 如果子类和父类拥有同名属性和方法，如果用子类创建对象，该对象调用同名属性与方法的时候，会调用到子类中的属性与方法
# 故事：Jack 掌握了师父和培训的技术后，自己潜心专研出自己的独门配方的一套全新煎饼果子技术

class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class School(object):
    def __init__(self):
        self.kongfu = '[狗头煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(School, Master):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

Jack = Prentice()
print(Jack.kongfu)
Jack.make_cake()
'''
[独创的煎饼果子配方]
运用[独创的煎饼果子配方]制作煎饼果子'''
# 结论：如果和子类和父类拥有同名属性与方法，子类创建对象调用属性和方法的时候，调用到的是子类里的同名属性与方法

# 拓展 mro 顺序，了解某类的继承顺序，从底层到顶层
print(Prentice.__mro__)
'''
(<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)'''