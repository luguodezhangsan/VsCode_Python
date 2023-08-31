# 类方法需要用装饰器 @classmothod 来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以 cls 作为第一个参数
'''
类方法的使用场景：
1. 当方法中需要使用类对象（如访问私有类属性等）时，定义类方法
2. 类方法一般和类属性配合使用
'''

# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth
    
# 2. 创建对象，调用类方法
dog1 = Dog()
result = dog1.get_tooth()
print(result)
# 10