name = 'Tom'
age = 18
weight = 75.5

# 我的名字是x，今年x岁了，体重x公斤。
print('我的名字是%s，今年%s岁了，体重%.2f公斤。' % (name, age, weight))  # %s 也可以输出整数和浮点数，功能更为强大
print('我的名字是{}，今年{}岁了，体重{:.2f}公斤。'.format(name, age, weight))  # 方法二：用format输出
print(f'我的名字是{name}，今年{age}岁了，体重{weight:.2f}公斤。')  # 方法三，用f()输出