# 多态指的是一类事物有多种形态，（一个抽象类有多个子类，因而多态的概念依赖于继承）。
# 定义：多态是一种使用对象的方式，子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果
# 好处：调用灵活，有了多态，更容易编写出通用的代码，做出通用的编程，以适应需求的不断变化
'''
实现步骤：
1. 定义父类，并提供公共方法
2. 定义子类，并重写父类方法
3. 传递子类对象给调用者，可以看到不同子类执行效果不同'''

# 需求：警务人员和警犬一起工作，警犬分为两种：追击敌人和追查毒品，携带不同的警犬，执行不同的工作
# 1. 定义父类，提供公共方法
class Dog(object):
    def work(self):  # 父类提供统一的方法，哪怕是空方法
        pass

# 2. 定义子类，子类重写父类方法：定义两个类表示不同的警犬
class ArmyDog(Dog):  # 继承 Dog 类
    def work(self):  # 子类重写父类同名方法
        print('追击敌人...')

class DrugDog(Dog):
    def work(self):
        print('追查毒品...')

class Person(object):
    def work_with_dog(self, dog):   # 传入不同的对象，执行不同的代码，即不同的 work 函数
        dog.work()

# 3. 创建对象，调用不同的功能，传入不同的对象，观察执行的结果
dog1 = ArmyDog()
dog2 = DrugDog()

Jack = Person()
Jack.work_with_dog(dog1)
Jack.work_with_dog(dog2)
'''
追击敌人...
追查毒品...'''