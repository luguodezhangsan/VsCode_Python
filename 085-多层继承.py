# 父类继承给子类，子类再继承给下一个子类，超过两层的继承就是多层继承
# 故事：N年后，Jack老了，想要把技术传递给自己的徒弟 Chris
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
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self) 

# 步骤：1. 创建类 Tusun，用这个类来创建对象；2. 用这个对象调用 Tusun 的父类 Prentice 的属性或方法看能否成功
class Tusun(Prentice):
    pass

Chris = Tusun()
Chris.make_cake()
Chris.make_master_cake()
Chris.make_school_cake()
'''
运用[独创的煎饼果子配方]制作煎饼果子
运用[古法煎饼果子配方]制作煎饼果子
运用[狗头煎饼果子配方]制作煎饼果子'''