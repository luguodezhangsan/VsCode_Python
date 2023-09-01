# 案例一：
# 1. 打印一条横线
def print_line():
    print('-' * 20)

print_line()
# --------------------

# 2. 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1

print_lines(5)
'''
--------------------
--------------------
--------------------
--------------------
--------------------
'''

# 旧的方法
j = 0
while j < 5:
    print('-' * 10)
    j += 1

# 案例二：
# 3. 求三个数之和
def sum_num(a, b, c):
    return a + b + c

result = sum_num(1, 2, 3)
print(result)
# 6

# 4. 求三个数平均值
def average_num(a, b, c):
    sumResult = sum_num(a, b, c)  # 这里是调用了 3 当中的 sum_num(a, b, c) 
                                  # == sumResult = a + b + c
    return sumResult / 3

result2 = average_num(1, 2, 3)
print(result2)