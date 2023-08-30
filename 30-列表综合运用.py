# 有三个办公室，8位老师，将8位老师随机分配到3个办公室
# 1. 准备数据
teacher = ['Tom', 'Jack', 'Rose', 'Lily', 'Chris', 'Holland', 'Edi', 'Rick']
room = [[], [],[]]

# 2. 随机分配老师到办公室(append(), extend(), insert())
#    extend() 会拆开增加，不要使用，所以使用append()
from random import *   # == import random
for i in teacher:
    num = randint(0, 2)
    room[num].append(i)
print(room)

m = 1
# 3. 验证是否分配成功
for j in room:
    # 打印每个办公室的人数
    print(f'办公室{m}的人数是：{len(j)}，老师的名字分别是：')
    # 打印老师们的名字
    # print(f'老师分别是：{j}')
    m += 1
    for i in j:
        print(i)

# 列表生成式
# 列表 = [循环变量相关表达式 for 循环变量 in range()函数]
list = [i ** 2 for i in range(1, 5)]
print(list)
# 返回：[1, 4, 9, 16]