# 302
# super() 调用父类的方法：调用该子类的上一个父类
# 分为有参数和无参数的情况，无参数会自动寻找上一个父类，有参数则寻找参数里的父类

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

        # 2.1 super() 带参数写法
        # super(School, self).__init__()
        # super(School, self).make_cake()
        # 方法2.2 super(). 函数()
        super().__init__()
        super().make_cake()

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

    # 一次性调用 Master 和 School 两个父类的同名属性与方法
    def make_old_cake(self):
        # 方法一：代码冗余，父类类名如果变化，这里的代码需要频繁修改，如果对象多，则代码量会很多，冗余
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self) 

        # 方法二：super()
        # 方法2.1 super(当前类名, self). 函数()
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()
        # 方法2.2 super(). 函数()
        super().__init__()   # 转到 13 行
        super().make_cake()  # 转到 15 行

Jack = Prentice()
Jack.make_old_cake()
'''
方法一：
运用[古法煎饼果子配方]制作煎饼果子
运用[狗头煎饼果子配方]制作煎饼果子'''
'''
方法二：
运用[狗头煎饼果子配方]制作煎饼果子
运用[古法煎饼果子配方]制作煎饼果子'''