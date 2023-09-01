# 一个父类继承给一个子类的形式称之为单继承
# 故事主线：一个煎饼果子老师傅研发了一套精湛的摊煎饼果子技术，师父要把这套技术传递给唯一的最优秀的弟子

# 1. 师父类，属性和方法
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

# 2. 徒弟类，继承师父类
class Prentice(Master):
    pass

# 3. 创建对象，调用实例属性和方法
Jack = Prentice()
print(Jack.kongfu)
Jack.make_cake()
'''
[古法煎饼果子配方]
运用[古法煎饼果子配方]制作煎饼果子'''