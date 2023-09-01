a = 10
b = 20

# 方法一：
# 借助第三变量存储数据：
c = 0
c = a
a = b
b = c
print(a)
print(b)
# 20
# 10

# 方法二：
# 交换写法
a, b = 1, 2
a ,b = b, a
print(a)
print(b)
# 2
# 1