# 函数中如果需要返回结果给用户，需要使用函数返回值 --> return
def buy():
    return '可口可乐'
    # 遇到 return 后负责函数返回值，并退出当前函数，使得下方缩进的所有代码不执行
    print('百事可乐')
# 使用变量保存函数返回值
goods = buy()
print(goods)
# 可口可乐

# 制作一个计算器，计算任意两个数字之和，并保存结果
def sum_num(a, b):             # def add_num2(a, b): 
    return a + b               #     c = a + b
                               #     print(c)
result = sum_num(1, 2)         # add_num2(1,2) 
print(result)
# 3                            # 3
'''区别是：1. print() 所在位置不同
          2. return 返回的值能在后面继续进行计算'''

m = eval(input('请你输入第一个数：'))
n = eval(input('请你输入第二个树：'))
result2 = sum_num(m, n)
print(result2)
