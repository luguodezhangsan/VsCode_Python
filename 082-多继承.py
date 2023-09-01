# 多继承意思是一个类同时继承了多个父类
# 故事推进：Jack是个爱学习的人，想要学习更多的煎饼果子技术，于是在百度搜索到狗头培训班，并报班学习煎饼果子技术

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

class Prentice(School, Master):  # 想要继承谁，就将谁放在第一位
    pass

Jack = Prentice()
print(Jack.kongfu)
Jack.make_cake()
'''
[狗头煎饼果子配方]
运用[狗头煎饼果子配方]制作煎饼果子'''
# 结论：当拥有多个父类时，默认继承定义类中第一个类的属性与方法