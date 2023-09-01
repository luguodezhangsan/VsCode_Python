# P304
# Python 中可以为实例属性和方法设置私有权限，即设置某个实例属性或实例方法步继承给子类
# 故事：Jack 把技术传承给徒弟的同时，不想把自己的钱 20 亿继承给徒弟 Chris，这个时候需要为这个 钱 这个实例设置私有权限

# 设置私有权限的方法：在属性名和方法名前面加上两个下划线__
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
        # 定义公有属性
        self.money = 10
        # 定义私有属性
        self.__money = 20

    # 打印私有方法
    def __print_info():
        print('这是私有方法！')

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

print(Chris.money)
# 10

print(Chris.__money)
# 输出对象里代码的格式
# AttributeError: 'Tusun' object has no attribute '__money'

Chris.__print_info()
# 引用某个对象的格式
# AttributeError: 'Tusun' object has no attribute '__print_info'