# 一般定义函数名 get_xx 用来获取私有属性，定义 set_xx 用来修改私有属性
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
        # 定义私有属性
        self.__money = 20

    # 定义函数：获取私有属性值 get_xx
    def get_money(self):
        return self.__money
    
    def set_money(self):
        self.__money = 500

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self) 

class Tusun(Prentice):
    pass

Chris = Tusun()
print(Chris.get_money())
# 20
Chris.set_money()
print(Chris.get_money())
# 500