# while的循环嵌套，案例：
m = 0
while m < 3:
    print('媳妇，我错了')
    m += 1
print('刷晚饭的碗')
# 将案例扩展为连续三天都执行该代码：
x = 0
y = 0
while y < 3:
    while x < 3:
        print('媳妇，我错了')
        x += 1
    print('刷晚饭的碗')
    y += 1  # 错误案例，将代码模拟运行就知道顺序错在哪里了

# 正确示范：
a = 0
while a < 3:
    b = 0                      # 20-24行为一套循环
    while b < 3:
        print('媳妇我错了')
        b += 1
    print('刷晚饭的碗')
    a += 1
print('折磨结束了')

# while 循环嵌套的运用（终极目的是打出 9*9 乘法表）
'''
1. 打印1个星星
2. 一行5个星星
3. 打印5行'''

j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*',end= '')
        i += 1
    print()  # 直接 print() 都可以 print('\n')则是换两行了，会多输出一个空行
    j += 1

# 打印三角形的星号
# 思路：每行星星的个数和行数是相同的
j = 0
while j < 5:
    i = 0
    while i <= j:  # 将 i 与 j 发生联动关系
        print('*',end= '')
        i += 1
    print()
    j += 1

# 打印 9*9 乘法表，d与行数是相同的（自己写的，没看标准讲解）
# 每行循环开始都是1，即从i=1开始
j = 1
while j <= 9:
    i = 1
    while i <= j:
        d = j
        o = i * d
        print(f'{i}*{d}={o}',end= ' ')
        i += 1
    print()
    j += 1

# 标准写法：
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end= '\t')  # end='\t' 可以起到对齐的作用
        i += 1
    print()
    j += 1