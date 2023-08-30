# 1. 不包含参数的情况
def add_num():
    result = 1 + 2
    print(result)

add_num()
# 3

# 2. 包含参数的情况
def add_num2(a, b):   # 形参：等待接受的数据
    c = a + b
    print(c)


add_num2(10, 20)   # 实参：实际接受的数据
# 30
add_num2(12, 23) 
# 35
result =  add_num2(10, 20) + add_num2(12, 23)  # 为什么这里一相加就会报错？  # 是不是因为定义的函数直接输出了，并没有给后面的代码返回值，同行同时出现了两个函数引用都直接打印了，不能继续相加
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(result)   

m = eval(input('请你输入第一个数：'))
n = eval(input('请你输入第二个树：'))
add_num2(m, n)
# 形参和实参不能用相同的字符来表达，定义了两个参数，输入一个参数则会报错