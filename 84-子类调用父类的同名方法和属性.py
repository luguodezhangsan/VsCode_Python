# 故事：很多顾客都希望也能迟到古法和狗头的技术的煎饼果子

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
        self.__init__()  # 加自己初始化的原因，如果不加这个自己的初始化，kongfu 属性值会是上一次调用的 init 内的 kongfu 属性值；同时子类里拥有和父类相同的属性和方法，故该 self.__init__() 调用的是子类里面的  self.kongfu = '[独创的煎饼果子配方]'
        print(f'运用{self.kongfu}制作煎饼果子')

    # 子类去调用父类的同名属性和方法：把父类的同名属性和方法再次封装
    def make_master_cake(self):
        # 父类类名，函数()
        # 再次强调初始化的原因：这里想要调用父类的同名属性和方法，属性在 init 初始化位置，所以需要再次调用 init
        Master.__init__(self)     # [古法煎饼果子配方]
        # 如果缺少这步初始化，self.kongfu = '[独创的煎饼果子配方]'，输出结果也会是：运用[独创的煎饼果子配方]制作煎饼果子
        Master.make_cake(self)    # 运用[古法煎饼果子配方]制作煎饼果子

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)     

Jack = Prentice()
Jack.make_cake()
Jack.make_master_cake()
Jack.make_school_cake()
Jack.make_cake()
'''
运用[独创的煎饼果子配方]制作煎饼果子
运用[古法煎饼果子配方]制作煎饼果子
运用[狗头煎饼果子配方]制作煎饼果子
运用[独创的煎饼果子配方]制作煎饼果子'''