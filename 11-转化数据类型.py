# 将input()接收到的字符串转化为其他数据类型
'''
常用的函数：
int(x[,base])
float(x)
str(x)
eval(str)  将字符串里的数据转化为原本的类型
tuple(s)  转化为元组 numbers1 = (1, 2, 3)
list(s)  转化为列表 number2 = [1, 2, 3]
'''

num = input('请输入数字：')
print(num)
print(type(num))
print(type(int(num)))  # 转化num为整数类型，int()

# float也可以将字符串里的数字转化为浮点型
str = '23'
print(float(str))

str2 = '[1, 2, 3]'
print(type(eval(str2)))

# Python中所有代码都可以在pycharm的python console中运行，即交互式开发环境，能不用print就快速展示其结果，最好只用于写简单的测试